#!/usr/bin/env python3

# Copyright (C) 2017 Adam Smith

# This file is part of Reaper

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pickle
import sys
import logging
import tempfile
import os

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QSizePolicy
from PyQt5.QtCore import QThread, pyqtSignal, QUrl
from PyQt5.QtGui import QDesktopServices, QTextCursor, QIcon

import socialreaper
import requests
from mainwindow import Ui_MainWindow

logfile = tempfile.gettempdir() + os.sep + 'reaper.log'
logging.basicConfig(filename=logfile, level=logging.DEBUG)
logger = logging.getLogger("reaper")


def log_handler(ex_type, value, traceback):
    logger.debug(traceback)
    logger.exception("Uncaught exception", exc_info=(ex_type, value, traceback))
    sys.exit()


class GenerateData(QThread):
    item_generated = pyqtSignal(dict)
    progress_changed = pyqtSignal(int)
    api_error = pyqtSignal(Exception)
    write_console = pyqtSignal(str)
    show_status = pyqtSignal(str, int)

    def __init__(self, source, generator, count):
        super().__init__()
        self.source = source
        self.generator = generator
        self.count = count
        self.quit_bool = False
        self.paused = False

        chunk_size = int(count / 1000)
        self.chunk_size = 10 if chunk_size == 0 else chunk_size

    def run(self):
        downloaded_count = 0

        for item in self.generator:
            if self.quit_bool:
                self.source.force_stop = True
                self.quit_bool = False
                return

            while self.paused:
                self.msleep(500)

            if isinstance(item, Exception):
                self.api_error.emit(item)
            else:
                self.item_generated.emit(item)

            self.progress_changed.emit(int(100 * downloaded_count /
                                           self.count))

            if downloaded_count % self.chunk_size == 0:
                self.show_status.emit("Estimated {}/{} rows complete".format(
                    downloaded_count, self.count), 10000)

            downloaded_count += 1
        self.progress_changed.emit(100)
        self.show_status.emit("Query complete", 2000)

    def write(self, text):
        self.write_console.emit(str(text))

    def toggle_pause(self):
        self.paused = not self.paused


class Reaper(Ui_MainWindow):
    def __init__(self, window, show=True):
        super().__init__()

        self.version = "v0.1.0"

        self.auth_keys = {}
        self.download_details = {}

        self.data = []
        self.existing_field_names = []
        self.table_thread = None
        self.table_max_cols = 30

        self.generator_thread = GenerateData({}, (), 0)
        self.generator_thread.start()

        self.window = window
        self.window.setWindowIcon(QIcon('ui/icon.png'))

        self.setupUi(window)
        self.updateStatusLabel.setText("Reaper {} is up to date".format(
            self.version))
        self.stack_introduction()
        self.load_auth_keys()
        self.add_actions()

        if show:
            window.show()

    def stack_jump(self, index):
        self.stackedWidget.setCurrentIndex(index)

    def change_priority(self, page):
        page.setSizePolicy(QSizePolicy(
            QSizePolicy.Preferred, QSizePolicy.Preferred))
        self.window.resize(self.window.minimumSizeHint())

        pages = [
            self.introduction,
            self.authentication,
            self.input,
            self.progress,
            self.preferences,
            self.updates,
            self.licenses
        ]

        pages.remove(page)

        for page in pages:
            page.setSizePolicy(QSizePolicy(
                QSizePolicy.Ignored, QSizePolicy.Ignored))

    def stack_introduction(self):
        self.stack_jump(0)
        self.change_priority(self.introduction)

    def stack_auth(self):
        self.stack_jump(1)
        self.change_priority(self.authentication)

    def stack_input(self):
        self.stack_jump(2)
        self.change_priority(self.input)

    def stack_progress(self):
        self.stack_jump(3)
        self.change_priority(self.progress)

    def stack_preferences(self):
        self.stack_jump(4)
        self.change_priority(self.preferences)

    def stack_updates(self):
        self.stack_jump(5)
        self.change_priority(self.updates)

    def stack_licenses(self):
        self.stack_jump(6)
        self.change_priority(self.licenses)

    def exit_generator(self):
        self.generator_thread.paused = False
        self.generator_thread.quit_bool = True
        self.generator_thread.quit()

    def new_input(self):
        self.data = []
        self.existing_field_names = []
        self.inputDownload.setEnabled(True)
        self.textOut.clear()
        self.exit_generator()
        self.tableWidget.clear()
        self.disable_display_results()
        self.stack_input()

    def choose_save_dir(self):
        try:
            if os.name == 'posix' and not os.environ.get('developing'):
                directory = os.path.expanduser("~") + "/.config/reaper"
            else:
                directory = "."
            if not os.path.exists(directory):
                os.makedirs(directory)
            os.chdir(directory)
        except Exception as e:
            self.error_message(e)

    def load_auth_keys(self):
        self.choose_save_dir()
        try:
            self.auth_keys = pickle.load(open('reaper_keys.p', 'rb'))

            self.facebookApiKeyInput.setText(self.auth_keys.get(
                'facebook_api_key', ''))
            self.twitterAppKeyInput.setText(self.auth_keys.get(
                'twitter_app_key', ''))
            self.twitterAppSecretInput.setText(self.auth_keys.get(
                'twitter_app_secret', ''))
            self.twitterOauthTokenInput.setText(self.auth_keys.get(
                'twitter_oauth_token', ''))
            self.twitterOauthTokenSecretInput.setText(self.auth_keys.get(
                'twitter_oauth_token_secret', ''))
            self.youtubeApiKeyInput.setText(self.auth_keys.get(
                'youtube_api_key', ''))
            self.redditApplicationIdInput.setText(self.auth_keys.get(
                'reddit_application_id', ''))
            self.redditApplicationSecretInput.setText(self.auth_keys.get(
                'reddit_application_secret', ''))

            if self.auth_keys != {}:
                self.stack_input()

        except FileNotFoundError:
            pass

    def save_auth_keys(self):
        self.choose_save_dir()
        self.auth_keys['facebook_api_key'] = self.facebookApiKeyInput.text()
        self.auth_keys['twitter_app_key'] = self.twitterAppKeyInput.text()
        self.auth_keys['twitter_app_secret'] = self.twitterAppSecretInput.text()
        self.auth_keys['twitter_oauth_token'] = \
            self.twitterOauthTokenInput.text()
        self.auth_keys['twitter_oauth_token_secret'] = \
            self.twitterOauthTokenSecretInput.text()
        self.auth_keys['youtube_api_key'] = self.youtubeApiKeyInput.text()
        self.auth_keys['reddit_application_id'] = \
            self.redditApplicationIdInput.text()
        self.auth_keys['reddit_application_secret'] = \
            self.redditApplicationSecretInput.text()

        pickle.dump(self.auth_keys, open('reaper_keys.p', 'wb'))

        self.stack_input()

    @staticmethod
    def error_message(exception):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("An error occurred when processing your request")
        msg.setWindowTitle("Error")
        msg.setDetailedText(str(exception))
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    @staticmethod
    def project_url():
        url = QUrl('https://github.com/ScriptSmith/reaper')
        QDesktopServices.openUrl(url)

    @staticmethod
    def help_url():
        url = QUrl('https://reaper.readthedocs.io')
        QDesktopServices.openUrl(url)

    def write_console(self, text):
        self.textOut.append(str(text))
        self.textOut.moveCursor(QTextCursor.End)

    def set_status(self, text, time):
        self.statusbar.showMessage(text, time)

    def pause_thread(self):
        text = self.pauseButton.text()
        text = "Pause" if text == "Resume" else "Resume"
        self.pauseButton.setText(text)
        self.generator_thread.toggle_pause()

    def enable_display_results(self):
        self.displayResultsButton.setEnabled(True)

    def disable_display_results(self):
        self.displayResultsButton.setEnabled(False)

    def table_fill(self, table_data, field_names):
        for row_count, row in enumerate(table_data):
            for col_count, col in enumerate(field_names):
                value = row[col]
                if isinstance(value, list):
                    value = str(value)

                self.tableWidget.setItem(row_count, col_count,
                                         QtWidgets.QTableWidgetItem(
                                             value))

    def display_results(self):
        self.disable_display_results()
        self.tableWidget.clear()

        data = self.data
        data = [socialreaper.tools.flatten(datum) for datum in data]
        field_names, data = socialreaper.tools.fill_gaps(data)

        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(len(data[0]))

        self.table_fill(data, field_names)

        self.tableWidget.setHorizontalHeaderLabels(field_names)
        self.tableWidget.horizontalHeader().show()

    def table_append(self, item, force=False):
        self.data.append(item)
        item = socialreaper.tools.flatten(item)

        if len(item) > self.table_max_cols and not force:
            self.tableWidget.setRowCount(1)
            self.tableWidget.setColumnCount(1)
            err_text = "Too many table fields to display"
            self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(err_text))
            return

        field_names, item = socialreaper.tools.fill_gaps(
            [item, dict.fromkeys(self.existing_field_names)])

        item = item[0]
        field_names.sort()
        self.tableWidget.setColumnCount(len(field_names))

        if field_names != self.existing_field_names:
            table_data = [socialreaper.tools.flatten(datum) for datum in
                          self.data]
            field_names, table_data = socialreaper.tools.fill_gaps(table_data)
            field_names.sort()

            self.tableWidget.setRowCount(len(table_data))
            self.tableWidget.setColumnCount(len(field_names))

            self.table_fill(table_data, field_names)
        else:
            row_count = self.tableWidget.rowCount()+1
            self.tableWidget.setRowCount(row_count)

            for col_count, col in enumerate(field_names):
                value = item[col]
                if isinstance(value, list):
                    value = str(value)

                self.tableWidget.setItem(row_count-1, col_count,
                                         QtWidgets.QTableWidgetItem(
                                             value))

        row_height = self.tableWidget.rowHeight(0)
        table_height = self.tableWidget.height()

        num_rows = int(table_height / row_height) - 1
        max = self.tableWidget.rowCount() - num_rows if \
            self.tableWidget.rowCount() - num_rows > 0 else 0

        for i in range(max):
            self.tableWidget.removeRow(i)

        self.existing_field_names = field_names
        self.tableWidget.setHorizontalHeaderLabels(field_names)
        vertical_labels = (
            str(label + 1) for label in range(len(self.data) -
                                              self.tableWidget.rowCount(),
                                              len(self.data)))

        self.tableWidget.setVerticalHeaderLabels(vertical_labels)
        self.tableWidget.horizontalHeader().show()

    def initiate_download(self):
        index = self.inputTab.currentIndex()
        self.exit_generator()
        self.inputDownload.setEnabled(False)
        if not self.generator_thread.isFinished():
            self.generator_thread.finished.connect(self.stack_progress)
        else:
            self.stack_progress()

        self.progressBar.setValue(0)
        self.tableWidget.clear()
        self.textOut.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.progressBar.setValue(0)

        self.statusbar.showMessage("Running query", 10000)
        self.pauseButton.setText("Pause")
        self.generator_thread.paused = False

        generator = count = None

        if index == 0:  # Facebook
            source = socialreaper.Facebook(
                self.auth_keys['facebook_api_key'],
                log_function=self.generator_thread.write
            )
            function_id = self.f_functions.currentIndex().row() + 1

            if function_id == 1:
                posts = self.f1_postIds.toPlainText()
                posts = posts.replace(" ", "").split(",")

                generator = source.posts(posts)
                count = len(posts)

            elif function_id == 2:
                post_id = self.f2_postId.text()
                comment_type = self.f2_commentType.currentItem().text()
                comment_order = self.f2_commentOrder.currentItem().text()
                num_comments = self.f2_numComments.value()

                generator = source.post_comments(post_id, count=num_comments,
                                                 category=comment_type,
                                                 order=comment_order)
                count = num_comments

            elif function_id == 3:
                page_id = self.f3_pageId.text()
                post_type = self.f3_postType.currentItem().text()
                include_hidden = self.f3_includeHidden.isChecked()
                num_posts = self.f3_numPosts.value()

                generator = source.page_posts(page_id, count=num_posts,
                                              post_type=post_type,
                                              include_hidden=include_hidden)
                count = num_posts

            elif function_id == 4:
                page_id = self.f4_pageId.text()
                post_type = self.f4_postType.currentItem().text()
                include_hidden = self.f4_includeHIdden.isChecked()
                num_posts = self.f4_numPosts.value()
                comment_type = self.f4_commentType.currentItem().text()
                comment_order = self.f4_commentOrder.currentItem().text()
                num_comments = self.f4_numComments.value()

                generator = source.page_posts_comments(page_id,
                                                       post_count=num_posts,
                                                       post_type=post_type,
                                                       include_hidden_posts=
                                                       include_hidden,
                                                       comment_count=
                                                       num_comments,
                                                       comment_category=
                                                       comment_type,
                                                       comment_order=
                                                       comment_order
                                                       )
                count = num_posts * num_comments

        elif index == 1:  # Twitter
            source = socialreaper.Twitter(
                self.auth_keys['twitter_app_key'],
                self.auth_keys['twitter_app_secret'],
                self.auth_keys['twitter_oauth_token'],
                self.auth_keys['twitter_oauth_token_secret'],
                log_function=self.generator_thread.write
            )
            function_id = self.t_functions.currentIndex().row() + 1

            if function_id == 1:
                search_term = self.t1_searchQuery.text()
                result_type = self.t1_resultType.currentItem().text()
                include_entities = self.t1_includeEntities.isChecked()
                max_id = self.t1_maxId.text()
                num_tweets = self.t1_numTweets.value()

                generator = source.search(search_term, count=num_tweets,
                                          result_type=result_type,
                                          include_entities=include_entities,
                                          max_id=max_id)
                count = num_tweets

            elif function_id == 2:
                hashtag = self.t2_hashtag.text()
                result_type = self.t2_resultType.currentItem().text()
                include_entities = self.t2_includeEntities.isChecked()
                max_id = self.t2_maxId.text()
                num_tweets = self.t2_numTweets.value()

                generator = source.search(hashtag, count=num_tweets,
                                          result_type=result_type,
                                          include_entities=include_entities,
                                          max_id=max_id)
                count = num_tweets

            elif function_id == 3:
                username = self.t3_username.text()
                if isinstance(username, str) and username[0] == '@':
                    username = username[1:]
                exclude_replies = self.t3_excludeReplies.isChecked()
                include_retweets = self.t3_includeRetweets.isChecked()
                num_tweets = self.t3_numTweets.value()

                generator = source.user(username, count=num_tweets,
                                        exclude_replies=exclude_replies,
                                        include_retweets=include_retweets)
                count = num_tweets

        elif index == 2:  # Reddit
            source = socialreaper.Reddit(
                self.auth_keys['reddit_application_id'],
                self.auth_keys['reddit_application_secret'],
                log_function=self.generator_thread.write
            )
            function_id = self.r_functions.currentIndex().row() + 1

            if function_id == 1:
                thread_ids = self.r1_threadIds.toPlainText()
                thread_ids = thread_ids.replace(" ", "").split(",")

                reddit_names = self.r1_subredditNames.toPlainText()
                reddit_names = reddit_names.replace(" ", "").split(",")

                id_sub_list = list(zip(thread_ids, reddit_names))

                generator = source.threads(id_sub_list)
                count = len(id_sub_list)

            elif function_id == 2:
                thread_id = self.r2_threadId.text()
                subreddit = self.r2_subreddit.text()
                comment_order = self.r2_commentOrder.currentItem().text()
                num_comments = self.r2_numComments.value()

                generator = source.thread_comments(thread_id, subreddit,
                                                   count=num_comments,
                                                   order=comment_order)
                count = num_comments

            elif function_id == 3:
                query = self.r3_query.text()
                thread_order = self.r3_resultOrder.currentItem().text()
                time_period = self.r3_timePeriod.currentItem().text()
                num_threads = self.r3_numThreads.value()

                generator = source.search(query, count=num_threads,
                                          order=thread_order, time_period=
                                          time_period)
                count = num_threads

            elif function_id == 4:
                query = self.r4_query.text()
                thread_order = self.r4_resultOrder.currentItem().text()
                time_period = self.r4_timePeriod.currentItem().text()
                num_threads = self.r4_numThreads.value()
                comment_order = self.r4_commentOrder.currentItem().text()
                num_comments = self.r4_numComments.value()

                generator = source.search_thread_comments(query,
                                                          thread_count=
                                                          num_threads,
                                                          search_order=
                                                          thread_order,
                                                          search_time_period=
                                                          time_period,
                                                          comment_order=
                                                          comment_order,
                                                          comment_count=
                                                          num_comments)
                count = num_threads * num_comments

            elif function_id == 5:
                subreddit = self.r5_subreddit.text()
                thread_order = self.r5_resultOrder.currentItem().text()
                time_period = self.r5_timePeriod.currentItem().text()
                num_threads = self.r5_numThreads.value()

                generator = source.subreddit(subreddit, count=num_threads,
                                             category=thread_order,
                                             time_period=time_period)
                count = num_threads

            elif function_id == 6:
                subreddit = self.r6_subreddit.text()
                thread_order = self.r6_resultOrder.currentItem().text()
                time_period = self.r6_timePeriod.currentItem().text()
                num_threads = self.r6_numThreads.value()
                comment_order = self.r6_commentOrder.currentItem().text()
                num_comments = self.r6_numComments.value()

                generator = source.subreddit_thread_comments(subreddit,
                                                             thread_count=
                                                             num_threads,
                                                             order=thread_order,
                                                             time_period=
                                                             time_period,
                                                             comment_order=
                                                             comment_order,
                                                             comment_count=
                                                             num_comments)
                count = num_threads * num_comments

            elif function_id == 7:
                username = self.r7_username.text()
                result_order = self.r7_resultOrder.currentItem().text()
                result_type = self.r7_resultType.currentItem().text()
                num_results = self.r7_numResults.value()

                generator = source.user(username, count=num_results,
                                        order=result_order,
                                        result_type=result_type)
                count = num_results

        elif index == 3:  # Youtube
            source = socialreaper.Youtube(
                self.auth_keys['youtube_api_key'],
                log_function=self.generator_thread.write)
            function_id = self.y_functions.currentIndex().row() + 1

            if function_id == 1:
                video_ids = self.y1_videoIds.toPlainText()
                video_ids = video_ids.replace(" ", "").split(",")

                generator = source.videos(video_ids)
                count = len(video_ids)

            elif function_id == 2:
                video_id = self.y2_videoId.text()
                order = self.y2_order.currentItem().text()
                search_term = self.y2_searchTerm.text()
                comment_format = self.y2_format.currentItem().text()
                num_comments = self.y2_numComments

                generator = source.video_comments(video_id,
                                                  count=num_comments,
                                                  order=order,
                                                  search_term=search_term,
                                                  comment_format=comment_format)
                count = num_comments

            elif function_id == 3:
                query = self.y3_query.text()
                order = self.y3_order.currentItem().text()
                channel_id = self.y3_channelId.text()
                channel_id = channel_id if channel_id else None
                if self.y3_liveEvent.isChecked():
                    event_type = self.y3_eventType.currentItem().text()
                else:
                    event_type = None
                location = self.y3_location.text()
                location = location if location else None
                radius = self.y3_radius.text()
                radius = radius if radius else None
                if self.y3_pubAfterCheck.isChecked():
                    pub_after = self.y3_pubAfter.dateTime()
                else:
                    pub_after = None
                if self.y3_pubBeforeCheck.isChecked():
                    pub_before = self.y3_pubBefore.dateTime()
                else:
                    pub_before = None
                region_code = self.y3_regionCode.text()
                region_code = region_code if region_code else None
                region_code = region_code if region_code else None
                relevance_language = self.y3_relevanceLanguage.text()
                relevance_language = relevance_language if relevance_language \
                    else None
                safe_search = self.y3_safeSearch.currentItem().text()
                topic_id = self.y3_topicId.text()
                topic_id = topic_id if topic_id else None
                captioning = self.y3_captioning.currentItem().text()
                category_id = self.y3_categoryId.text()
                category_id = category_id if category_id else None
                definition = self.y3_definition.currentItem().text()
                duration = self.y3_duration.currentItem().text()
                embed = "true" if self.y3_embeddable.isChecked() else "any"
                video_license = self.y3_license.currentItem().text()
                externally = "true" if self.y3_externally.isChecked() else "any"
                video_type = self.y3_type.currentItem().text()
                num_videos = self.y3_numVideos.value()

                generator = source.search(query=query,
                                          order=order,
                                          channel_id=channel_id,
                                          event_type=event_type,
                                          location=location,
                                          location_radius=radius,
                                          published_after=pub_after,
                                          published_before=pub_before,
                                          region_code=region_code,
                                          relevance_language=relevance_language,
                                          safe_search=safe_search,
                                          topic_id=topic_id,
                                          video_caption=captioning,
                                          video_category_id=category_id,
                                          video_definition=definition,
                                          video_duration=duration,
                                          video_embeddable=embed,
                                          video_license=video_license,
                                          video_syndicated=externally,
                                          video_type=video_type,
                                          count=num_videos)
                count = num_videos

            elif function_id == 4:
                query = self.y4_query.text()
                order = self.y4_order.currentItem().text()
                channel_id = self.y4_channelId.text()
                channel_id = channel_id if channel_id else None
                if self.y4_liveEvent.isChecked():
                    event_type = self.y4_eventType.currentItem().text()
                else:
                    event_type = None
                location = self.y4_location.text()
                location = location if location else None
                radius = self.y4_radius.text()
                radius = radius if radius else None
                if self.y4_pubAfterCheck.isChecked():
                    pub_after = self.y4_pubAfter.dateTime()
                else:
                    pub_after = None
                if self.y4_pubBeforeCheck.isChecked():
                    pub_before = self.y4_pubBefore.dateTime()
                else:
                    pub_before = None
                region_code = self.y4_regionCode.text()
                region_code = region_code if region_code else None
                region_code = region_code if region_code else None
                relevance_language = self.y4_relevanceLanguage.text()
                relevance_language = relevance_language if relevance_language \
                    else None
                safe_search = self.y4_safeSearch.currentItem().text()
                topic_id = self.y4_topicId.text()
                topic_id = topic_id if topic_id else None
                captioning = self.y4_captioning.currentItem().text()
                category_id = self.y4_categoryId.text()
                category_id = category_id if category_id else None
                definition = self.y4_definition.currentItem().text()
                duration = self.y4_duration.currentItem().text()
                embed = "true" if self.y4_embeddable.isChecked() else "any"
                video_license = self.y4_license.currentItem().text()
                externally = "true" if self.y4_externally.isChecked() else "any"
                video_type = self.y4_type.currentItem().text()
                num_videos = self.y4_numVideos.value()
                comment_order = self.y4_commentOrder.currentItem().text()
                comment_text = self.y4_commentText.text()
                comment_text = comment_text.replace(" ","").split(",")
                comment_format = self.y4_commentFormat.currentItem().text()
                num_comments = self.y4_numComments.value()

                generator = source.search_video_comments(query=query,
                                                         video_order=order,
                                                         channel_id=channel_id,
                                                         event_type=event_type,
                                                         location=location,
                                                         location_radius=
                                                         radius,
                                                         published_after=
                                                         pub_after,
                                                         published_before=
                                                         pub_before,
                                                         region_code=
                                                         region_code,
                                                         relevance_language=
                                                         relevance_language,
                                                         safe_search=
                                                         safe_search,
                                                         topic_id=topic_id,
                                                         video_caption=
                                                         captioning,
                                                         video_category_id=
                                                         category_id,
                                                         video_definition=
                                                         definition,
                                                         video_duration=
                                                         duration,
                                                         video_embeddable=
                                                         embed,
                                                         video_license=
                                                         video_license,
                                                         video_syndicated=
                                                         externally,
                                                         video_type=video_type,
                                                         video_count=num_videos,
                                                         comment_count=
                                                         num_comments,
                                                         comment_order=
                                                         comment_order,
                                                         comment_search_terms=
                                                         comment_text,
                                                         comment_format=
                                                         comment_format
                                                         )
                count = num_videos * num_comments

            elif function_id == 5:
                channel_id = self.y5_channelId.text()
                video_order = self.y5_order.currentItem().text()
                num_videos = self.y5_numVideos.value()

                generator = source.channel(channel_id, order=video_order,
                                           count=num_videos)
                count = num_videos

            elif function_id == 6:
                channel_id = self.y6_channelId.text()
                video_order = self.y6_order.currentItem().text()
                num_videos = self.y6_numVideos.value()
                comment_order = self.y6_commentOrder.currentItem().text()
                comment_text = self.y6_commentText.text()
                comment_format = self.y6_commentFormat.currentItem().text()
                num_comments = self.y6_numComments.value()

                generator = source.channel_video_comments(channel_id,
                                                          video_order=
                                                          video_order,
                                                          video_count=
                                                          num_videos,
                                                          comment_order=
                                                          comment_order,
                                                          search_term=
                                                          comment_text,
                                                          comment_format=
                                                          comment_format,
                                                          comment_count=
                                                          num_comments)
                count = num_videos * num_comments

            elif function_id == 7:
                channel_name = self.y7_channelName.text()

                generator = source.guess_channel_id(channel_name)
                count = 1

        if generator and count:
            self.generator_thread = GenerateData(source, generator, count)
            self.generator_thread.start()
            self.generator_thread.item_generated.connect(self.table_append)
            self.generator_thread.progress_changed.connect(
                self.progressBar.setValue)
            self.generator_thread.api_error.connect(self.error_message)
            self.generator_thread.write_console.connect(self.write_console)
            self.generator_thread.show_status.connect(self.set_status)

            self.generator_thread.finished.connect(self.enable_display_results)
            self.displayResultsButton.clicked.connect(self.display_results)

    def save(self, file_type="csv"):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_name, _ = QtWidgets.QFileDialog.getSaveFileName(
            caption="Save", directory="",
            filter="{} Files (*.{});;All Files (*)".format(
                file_type.upper(), file_type),
            options=options)

        if file_name:
            if '.' not in file_name and file_name[-4:] != '.' + file_type:
                file_name += '.' + file_type

            if file_type == "csv":
                socialreaper.tools.to_csv(self.data, filename=file_name)
            elif file_type == "json":
                socialreaper.tools.to_json(self.data, filename=file_name)

    def save_csv(self):
        self.save("csv")

    def save_json(self):
        self.save("json")

    def add_actions(self):
        self.actionQuit.triggered.connect(QtWidgets.qApp.quit)
        self.introductionContinue.clicked.connect(self.stack_auth)
        self.actionAuthentication.triggered.connect(self.stack_auth)
        self.actionLicences.triggered.connect(self.stack_licenses)
        self.actionCheck_for_Updates.triggered.connect(self.stack_updates)
        self.actionPreferences.triggered.connect(self.stack_preferences)

        self.actionHelp.triggered.connect(self.help_url)
        self.actionAbout.triggered.connect(self.project_url)

        self.checkUpdatesButton.clicked.connect(self.check_updates)

        self.authenticationDone.clicked.connect(self.save_auth_keys)
        self.progressDone.clicked.connect(self.new_input)
        self.licencesDone.clicked.connect(self.new_input)
        self.updatesDone.clicked.connect(self.new_input)
        self.preferencesDone.clicked.connect(self.new_input)
        self.inputDownload.clicked.connect(self.initiate_download)
        self.saveCSV.clicked.connect(self.save_csv)
        self.saveJSON.clicked.connect(self.save_json)

        self.pauseButton.clicked.connect(self.pause_thread)

    def check_updates(self):
        self.checkUpdatesButton.setEnabled(False)
        try:
            req = requests.get(
                "https://api.github.com/repos/scriptsmith/reaper/releases")
        except requests.RequestException as e:
            self.error_message(e)

        self.checkUpdatesButton.setEnabled(True)
        req = req.json()

        if isinstance(req, dict) and req.get('message'):
            self.error_message(Exception("Could not get updates:" + req[
                'message']))
            return

        if req[0]['tag_name'] != self.version:
            new_text = "<a href='{}'>Download latest version</a>".format(
                "http://github.com/ScriptSmith/reaper/releases")
            self.updateStatusLabel.setText(new_text)


if __name__ == "__main__":
    sys.excepthook = log_handler
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Reaper(main_window)
    sys.exit(app.exec_())
