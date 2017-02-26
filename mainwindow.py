# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1333, 807)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.stackedWidget.setObjectName("stackedWidget")
        self.introduction = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.introduction.sizePolicy().hasHeightForWidth())
        self.introduction.setSizePolicy(sizePolicy)
        self.introduction.setObjectName("introduction")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.introduction)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.label_121 = QtWidgets.QLabel(self.introduction)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_121.setFont(font)
        self.label_121.setObjectName("label_121")
        self.horizontalLayout_11.addWidget(self.label_121)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_11)
        self.label_123 = QtWidgets.QLabel(self.introduction)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_123.sizePolicy().hasHeightForWidth())
        self.label_123.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_123.setFont(font)
        self.label_123.setWordWrap(True)
        self.label_123.setObjectName("label_123")
        self.verticalLayout_10.addWidget(self.label_123)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_124 = QtWidgets.QLabel(self.introduction)
        self.label_124.setObjectName("label_124")
        self.verticalLayout_11.addWidget(self.label_124)
        self.label_125 = QtWidgets.QLabel(self.introduction)
        self.label_125.setOpenExternalLinks(True)
        self.label_125.setObjectName("label_125")
        self.verticalLayout_11.addWidget(self.label_125)
        self.horizontalLayout_13.addLayout(self.verticalLayout_11)
        self.verticalLayout_10.addLayout(self.horizontalLayout_13)
        self.introductionContinue = QtWidgets.QPushButton(self.introduction)
        self.introductionContinue.setObjectName("introductionContinue")
        self.verticalLayout_10.addWidget(self.introductionContinue)
        self.stackedWidget.addWidget(self.introduction)
        self.authentication = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.authentication.sizePolicy().hasHeightForWidth())
        self.authentication.setSizePolicy(sizePolicy)
        self.authentication.setObjectName("authentication")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.authentication)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tabWidget = QtWidgets.QTabWidget(self.authentication)
        self.tabWidget.setObjectName("tabWidget")
        self.facebookAuthTab = QtWidgets.QWidget()
        self.facebookAuthTab.setObjectName("facebookAuthTab")
        self.formLayout = QtWidgets.QFormLayout(self.facebookAuthTab)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.facebookAuthTab)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.facebookApiKeyInput = QtWidgets.QLineEdit(self.facebookAuthTab)
        self.facebookApiKeyInput.setObjectName("facebookApiKeyInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.facebookApiKeyInput)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem3)
        self.tabWidget.addTab(self.facebookAuthTab, "")
        self.twitterAuthTab = QtWidgets.QWidget()
        self.twitterAuthTab.setObjectName("twitterAuthTab")
        self.formLayout_3 = QtWidgets.QFormLayout(self.twitterAuthTab)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_5 = QtWidgets.QLabel(self.twitterAuthTab)
        self.label_5.setObjectName("label_5")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.twitterAppKeyInput = QtWidgets.QLineEdit(self.twitterAuthTab)
        self.twitterAppKeyInput.setObjectName("twitterAppKeyInput")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.twitterAppKeyInput)
        self.label_6 = QtWidgets.QLabel(self.twitterAuthTab)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.twitterAppSecretInput = QtWidgets.QLineEdit(self.twitterAuthTab)
        self.twitterAppSecretInput.setObjectName("twitterAppSecretInput")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.twitterAppSecretInput)
        self.label_7 = QtWidgets.QLabel(self.twitterAuthTab)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.twitterOauthTokenInput = QtWidgets.QLineEdit(self.twitterAuthTab)
        self.twitterOauthTokenInput.setObjectName("twitterOauthTokenInput")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.twitterOauthTokenInput)
        self.label_8 = QtWidgets.QLabel(self.twitterAuthTab)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.twitterOauthTokenSecretInput = QtWidgets.QLineEdit(self.twitterAuthTab)
        self.twitterOauthTokenSecretInput.setObjectName("twitterOauthTokenSecretInput")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.twitterOauthTokenSecretInput)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_3.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.tabWidget.addTab(self.twitterAuthTab, "")
        self.redditAuthTab = QtWidgets.QWidget()
        self.redditAuthTab.setObjectName("redditAuthTab")
        self.formLayout_4 = QtWidgets.QFormLayout(self.redditAuthTab)
        self.formLayout_4.setContentsMargins(0, 0, 0, 0)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_9 = QtWidgets.QLabel(self.redditAuthTab)
        self.label_9.setObjectName("label_9")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.redditApplicationIdInput = QtWidgets.QLineEdit(self.redditAuthTab)
        self.redditApplicationIdInput.setObjectName("redditApplicationIdInput")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.redditApplicationIdInput)
        self.label_10 = QtWidgets.QLabel(self.redditAuthTab)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.redditApplicationSecretInput = QtWidgets.QLineEdit(self.redditAuthTab)
        self.redditApplicationSecretInput.setObjectName("redditApplicationSecretInput")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.redditApplicationSecretInput)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_4.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem5)
        self.tabWidget.addTab(self.redditAuthTab, "")
        self.youtubeAuthTab = QtWidgets.QWidget()
        self.youtubeAuthTab.setObjectName("youtubeAuthTab")
        self.formLayout_2 = QtWidgets.QFormLayout(self.youtubeAuthTab)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_11 = QtWidgets.QLabel(self.youtubeAuthTab)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.youtubeApiKeyInput = QtWidgets.QLineEdit(self.youtubeAuthTab)
        self.youtubeApiKeyInput.setObjectName("youtubeApiKeyInput")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.youtubeApiKeyInput)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout_2.setItem(0, QtWidgets.QFormLayout.FieldRole, spacerItem6)
        self.tabWidget.addTab(self.youtubeAuthTab, "")
        self.gridLayout_3.addWidget(self.tabWidget, 3, 0, 1, 1)
        self.authenticationDone = QtWidgets.QPushButton(self.authentication)
        self.authenticationDone.setProperty("int", 2)
        self.authenticationDone.setObjectName("authenticationDone")
        self.gridLayout_3.addWidget(self.authenticationDone, 4, 0, 1, 1)
        self.label_122 = QtWidgets.QLabel(self.authentication)
        self.label_122.setOpenExternalLinks(True)
        self.label_122.setObjectName("label_122")
        self.gridLayout_3.addWidget(self.label_122, 2, 0, 1, 1)
        self.label_127 = QtWidgets.QLabel(self.authentication)
        self.label_127.setObjectName("label_127")
        self.gridLayout_3.addWidget(self.label_127, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.authentication)
        self.input = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input.sizePolicy().hasHeightForWidth())
        self.input.setSizePolicy(sizePolicy)
        self.input.setObjectName("input")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.input)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.inputTab = QtWidgets.QTabWidget(self.input)
        self.inputTab.setObjectName("inputTab")
        self.facebookTab = QtWidgets.QWidget()
        self.facebookTab.setObjectName("facebookTab")
        self.gridLayout = QtWidgets.QGridLayout(self.facebookTab)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.facebookTab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.f_functions = QtWidgets.QListWidget(self.facebookTab)
        self.f_functions.setObjectName("f_functions")
        item = QtWidgets.QListWidgetItem()
        self.f_functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.f_functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.f_functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.f_functions.addItem(item)
        self.gridLayout.addWidget(self.f_functions, 1, 0, 1, 1)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.facebookTab)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        self.f1_postIds = QtWidgets.QPlainTextEdit(self.page)
        self.f1_postIds.setObjectName("f1_postIds")
        self.verticalLayout_5.addWidget(self.f1_postIds)
        self.stackedWidget_2.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.formLayout_6 = QtWidgets.QFormLayout(self.page_2)
        self.formLayout_6.setContentsMargins(0, 0, 0, 0)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_13 = QtWidgets.QLabel(self.page_2)
        self.label_13.setObjectName("label_13")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.f2_commentType = QtWidgets.QListWidget(self.page_2)
        self.f2_commentType.setObjectName("f2_commentType")
        item = QtWidgets.QListWidgetItem()
        self.f2_commentType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.f2_commentType.addItem(item)
        self.formLayout_6.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.f2_commentType)
        self.label_14 = QtWidgets.QLabel(self.page_2)
        self.label_14.setObjectName("label_14")
        self.formLayout_6.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.f2_commentOrder = QtWidgets.QListWidget(self.page_2)
        self.f2_commentOrder.setObjectName("f2_commentOrder")
        item = QtWidgets.QListWidgetItem()
        self.f2_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.f2_commentOrder.addItem(item)
        self.formLayout_6.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.f2_commentOrder)
        self.label_12 = QtWidgets.QLabel(self.page_2)
        self.label_12.setObjectName("label_12")
        self.formLayout_6.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.f2_numComments = QtWidgets.QSpinBox(self.page_2)
        self.f2_numComments.setMinimum(0)
        self.f2_numComments.setMaximum(999999999)
        self.f2_numComments.setProperty("value", 50)
        self.f2_numComments.setObjectName("f2_numComments")
        self.formLayout_6.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.f2_numComments)
        self.f2_postId = QtWidgets.QLineEdit(self.page_2)
        self.f2_postId.setObjectName("f2_postId")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.f2_postId)
        self.stackedWidget_2.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.formLayout_7 = QtWidgets.QFormLayout(self.page_3)
        self.formLayout_7.setContentsMargins(0, 0, 0, 0)
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_15 = QtWidgets.QLabel(self.page_3)
        self.label_15.setObjectName("label_15")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.label_16 = QtWidgets.QLabel(self.page_3)
        self.label_16.setObjectName("label_16")
        self.formLayout_7.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.f3_includeHidden = QtWidgets.QCheckBox(self.page_3)
        self.f3_includeHidden.setObjectName("f3_includeHidden")
        self.formLayout_7.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.f3_includeHidden)
        self.label_17 = QtWidgets.QLabel(self.page_3)
        self.label_17.setObjectName("label_17")
        self.formLayout_7.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.f3_numPosts = QtWidgets.QSpinBox(self.page_3)
        self.f3_numPosts.setMinimum(0)
        self.f3_numPosts.setMaximum(999999999)
        self.f3_numPosts.setProperty("value", 200)
        self.f3_numPosts.setObjectName("f3_numPosts")
        self.formLayout_7.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.f3_numPosts)
        self.f3_pageId = QtWidgets.QLineEdit(self.page_3)
        self.f3_pageId.setObjectName("f3_pageId")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.f3_pageId)
        self.f3_postType = QtWidgets.QListWidget(self.page_3)
        self.f3_postType.setObjectName("f3_postType")
        item = QtWidgets.QListWidgetItem()
        self.f3_postType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.f3_postType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.f3_postType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.f3_postType.addItem(item)
        self.formLayout_7.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.f3_postType)
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.page_4)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout_8 = QtWidgets.QFormLayout()
        self.formLayout_8.setObjectName("formLayout_8")
        self.f4_numPosts = QtWidgets.QSpinBox(self.page_4)
        self.f4_numPosts.setMinimum(0)
        self.f4_numPosts.setMaximum(999999999)
        self.f4_numPosts.setProperty("value", 50)
        self.f4_numPosts.setObjectName("f4_numPosts")
        self.formLayout_8.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.f4_numPosts)
        self.label_20 = QtWidgets.QLabel(self.page_4)
        self.label_20.setObjectName("label_20")
        self.formLayout_8.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.label_19 = QtWidgets.QLabel(self.page_4)
        self.label_19.setObjectName("label_19")
        self.formLayout_8.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.f4_includeHIdden = QtWidgets.QCheckBox(self.page_4)
        self.f4_includeHIdden.setObjectName("f4_includeHIdden")
        self.formLayout_8.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.f4_includeHIdden)
        self.label_18 = QtWidgets.QLabel(self.page_4)
        self.label_18.setObjectName("label_18")
        self.formLayout_8.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.f4_pageId = QtWidgets.QLineEdit(self.page_4)
        self.f4_pageId.setObjectName("f4_pageId")
        self.formLayout_8.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.f4_pageId)
        self.f4_postType = QtWidgets.QListWidget(self.page_4)
        self.f4_postType.setObjectName("f4_postType")
        item = QtWidgets.QListWidgetItem()
        self.f4_postType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.f4_postType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.f4_postType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.f4_postType.addItem(item)
        self.formLayout_8.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.f4_postType)
        self.horizontalLayout_2.addLayout(self.formLayout_8)
        self.formLayout_9 = QtWidgets.QFormLayout()
        self.formLayout_9.setObjectName("formLayout_9")
        self.f4_numComments = QtWidgets.QSpinBox(self.page_4)
        self.f4_numComments.setMinimum(0)
        self.f4_numComments.setMaximum(999999999)
        self.f4_numComments.setProperty("value", 50)
        self.f4_numComments.setObjectName("f4_numComments")
        self.formLayout_9.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.f4_numComments)
        self.label_21 = QtWidgets.QLabel(self.page_4)
        self.label_21.setObjectName("label_21")
        self.formLayout_9.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.label_23 = QtWidgets.QLabel(self.page_4)
        self.label_23.setObjectName("label_23")
        self.formLayout_9.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.label_22 = QtWidgets.QLabel(self.page_4)
        self.label_22.setObjectName("label_22")
        self.formLayout_9.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.f4_commentOrder = QtWidgets.QListWidget(self.page_4)
        self.f4_commentOrder.setObjectName("f4_commentOrder")
        item = QtWidgets.QListWidgetItem()
        self.f4_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.f4_commentOrder.addItem(item)
        self.formLayout_9.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.f4_commentOrder)
        self.f4_commentType = QtWidgets.QListWidget(self.page_4)
        self.f4_commentType.setObjectName("f4_commentType")
        item = QtWidgets.QListWidgetItem()
        self.f4_commentType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.f4_commentType.addItem(item)
        self.formLayout_9.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.f4_commentType)
        self.horizontalLayout_2.addLayout(self.formLayout_9)
        self.stackedWidget_2.addWidget(self.page_4)
        self.gridLayout.addWidget(self.stackedWidget_2, 2, 0, 1, 1)
        self.inputTab.addTab(self.facebookTab, "")
        self.twitterTab = QtWidgets.QWidget()
        self.twitterTab.setObjectName("twitterTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.twitterTab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_24 = QtWidgets.QLabel(self.twitterTab)
        self.label_24.setObjectName("label_24")
        self.verticalLayout_2.addWidget(self.label_24)
        self.t_functions = QtWidgets.QListWidget(self.twitterTab)
        self.t_functions.setObjectName("t_functions")
        item = QtWidgets.QListWidgetItem()
        self.t_functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.t_functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.t_functions.addItem(item)
        self.verticalLayout_2.addWidget(self.t_functions)
        self.stackedWidget_3 = QtWidgets.QStackedWidget(self.twitterTab)
        self.stackedWidget_3.setObjectName("stackedWidget_3")
        self.page_11 = QtWidgets.QWidget()
        self.page_11.setObjectName("page_11")
        self.formLayout_10 = QtWidgets.QFormLayout(self.page_11)
        self.formLayout_10.setContentsMargins(0, 0, 0, 0)
        self.formLayout_10.setObjectName("formLayout_10")
        self.label_25 = QtWidgets.QLabel(self.page_11)
        self.label_25.setObjectName("label_25")
        self.formLayout_10.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.t1_searchQuery = QtWidgets.QLineEdit(self.page_11)
        self.t1_searchQuery.setObjectName("t1_searchQuery")
        self.formLayout_10.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.t1_searchQuery)
        self.label_26 = QtWidgets.QLabel(self.page_11)
        self.label_26.setObjectName("label_26")
        self.formLayout_10.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.t1_includeEntities = QtWidgets.QCheckBox(self.page_11)
        self.t1_includeEntities.setObjectName("t1_includeEntities")
        self.formLayout_10.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.t1_includeEntities)
        self.label_27 = QtWidgets.QLabel(self.page_11)
        self.label_27.setObjectName("label_27")
        self.formLayout_10.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.t1_resultType = QtWidgets.QListWidget(self.page_11)
        self.t1_resultType.setObjectName("t1_resultType")
        item = QtWidgets.QListWidgetItem()
        self.t1_resultType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.t1_resultType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.t1_resultType.addItem(item)
        self.formLayout_10.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.t1_resultType)
        self.label_119 = QtWidgets.QLabel(self.page_11)
        self.label_119.setObjectName("label_119")
        self.formLayout_10.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_119)
        self.t1_numTweets = QtWidgets.QSpinBox(self.page_11)
        self.t1_numTweets.setMinimum(0)
        self.t1_numTweets.setMaximum(999999999)
        self.t1_numTweets.setProperty("value", 300)
        self.t1_numTweets.setObjectName("t1_numTweets")
        self.formLayout_10.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.t1_numTweets)
        self.t1_maxId = QtWidgets.QLineEdit(self.page_11)
        self.t1_maxId.setObjectName("t1_maxId")
        self.formLayout_10.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.t1_maxId)
        self.stackedWidget_3.addWidget(self.page_11)
        self.page_12 = QtWidgets.QWidget()
        self.page_12.setObjectName("page_12")
        self.formLayout_11 = QtWidgets.QFormLayout(self.page_12)
        self.formLayout_11.setContentsMargins(0, 0, 0, 0)
        self.formLayout_11.setObjectName("formLayout_11")
        self.label_28 = QtWidgets.QLabel(self.page_12)
        self.label_28.setObjectName("label_28")
        self.formLayout_11.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.label_30 = QtWidgets.QLabel(self.page_12)
        self.label_30.setObjectName("label_30")
        self.formLayout_11.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_30)
        self.t2_includeEntities = QtWidgets.QCheckBox(self.page_12)
        self.t2_includeEntities.setObjectName("t2_includeEntities")
        self.formLayout_11.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.t2_includeEntities)
        self.label_29 = QtWidgets.QLabel(self.page_12)
        self.label_29.setObjectName("label_29")
        self.formLayout_11.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.t2_hashtag = QtWidgets.QLineEdit(self.page_12)
        self.t2_hashtag.setText("")
        self.t2_hashtag.setObjectName("t2_hashtag")
        self.formLayout_11.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.t2_hashtag)
        self.t2_resultType = QtWidgets.QListWidget(self.page_12)
        self.t2_resultType.setObjectName("t2_resultType")
        item = QtWidgets.QListWidgetItem()
        self.t2_resultType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.t2_resultType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.t2_resultType.addItem(item)
        self.formLayout_11.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.t2_resultType)
        self.label_120 = QtWidgets.QLabel(self.page_12)
        self.label_120.setObjectName("label_120")
        self.formLayout_11.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_120)
        self.t2_numTweets = QtWidgets.QSpinBox(self.page_12)
        self.t2_numTweets.setMinimum(0)
        self.t2_numTweets.setMaximum(999999999)
        self.t2_numTweets.setProperty("value", 300)
        self.t2_numTweets.setObjectName("t2_numTweets")
        self.formLayout_11.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.t2_numTweets)
        self.t2_maxId = QtWidgets.QLineEdit(self.page_12)
        self.t2_maxId.setObjectName("t2_maxId")
        self.formLayout_11.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.t2_maxId)
        self.stackedWidget_3.addWidget(self.page_12)
        self.page_13 = QtWidgets.QWidget()
        self.page_13.setObjectName("page_13")
        self.formLayout_12 = QtWidgets.QFormLayout(self.page_13)
        self.formLayout_12.setContentsMargins(0, 0, 0, 0)
        self.formLayout_12.setObjectName("formLayout_12")
        self.label_31 = QtWidgets.QLabel(self.page_13)
        self.label_31.setObjectName("label_31")
        self.formLayout_12.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.t3_excludeReplies = QtWidgets.QCheckBox(self.page_13)
        self.t3_excludeReplies.setObjectName("t3_excludeReplies")
        self.formLayout_12.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.t3_excludeReplies)
        self.t3_includeRetweets = QtWidgets.QCheckBox(self.page_13)
        self.t3_includeRetweets.setObjectName("t3_includeRetweets")
        self.formLayout_12.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.t3_includeRetweets)
        self.label_32 = QtWidgets.QLabel(self.page_13)
        self.label_32.setObjectName("label_32")
        self.formLayout_12.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_32)
        self.t3_numTweets = QtWidgets.QSpinBox(self.page_13)
        self.t3_numTweets.setMinimum(0)
        self.t3_numTweets.setMaximum(3200)
        self.t3_numTweets.setProperty("value", 3200)
        self.t3_numTweets.setObjectName("t3_numTweets")
        self.formLayout_12.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.t3_numTweets)
        self.t3_username = QtWidgets.QLineEdit(self.page_13)
        self.t3_username.setText("")
        self.t3_username.setObjectName("t3_username")
        self.formLayout_12.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.t3_username)
        self.stackedWidget_3.addWidget(self.page_13)
        self.verticalLayout_2.addWidget(self.stackedWidget_3)
        self.inputTab.addTab(self.twitterTab, "")
        self.redditTab = QtWidgets.QWidget()
        self.redditTab.setObjectName("redditTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.redditTab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_33 = QtWidgets.QLabel(self.redditTab)
        self.label_33.setObjectName("label_33")
        self.verticalLayout_3.addWidget(self.label_33)
        self.r_functions = QtWidgets.QListWidget(self.redditTab)
        self.r_functions.setObjectName("r_functions")
        item = QtWidgets.QListWidgetItem()
        self.r_functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r_functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r_functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r_functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r_functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r_functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r_functions.addItem(item)
        self.verticalLayout_3.addWidget(self.r_functions)
        self.stackedWidget_4 = QtWidgets.QStackedWidget(self.redditTab)
        self.stackedWidget_4.setObjectName("stackedWidget_4")
        self.page_14 = QtWidgets.QWidget()
        self.page_14.setObjectName("page_14")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.page_14)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_34 = QtWidgets.QLabel(self.page_14)
        self.label_34.setObjectName("label_34")
        self.verticalLayout_4.addWidget(self.label_34)
        self.r1_threadIds = QtWidgets.QPlainTextEdit(self.page_14)
        self.r1_threadIds.setObjectName("r1_threadIds")
        self.verticalLayout_4.addWidget(self.r1_threadIds)
        self.horizontalLayout_8.addLayout(self.verticalLayout_4)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_118 = QtWidgets.QLabel(self.page_14)
        self.label_118.setObjectName("label_118")
        self.verticalLayout_8.addWidget(self.label_118)
        self.r1_subredditNames = QtWidgets.QPlainTextEdit(self.page_14)
        self.r1_subredditNames.setObjectName("r1_subredditNames")
        self.verticalLayout_8.addWidget(self.r1_subredditNames)
        self.horizontalLayout_8.addLayout(self.verticalLayout_8)
        self.stackedWidget_4.addWidget(self.page_14)
        self.page_15 = QtWidgets.QWidget()
        self.page_15.setObjectName("page_15")
        self.formLayout_13 = QtWidgets.QFormLayout(self.page_15)
        self.formLayout_13.setContentsMargins(0, 0, 0, 0)
        self.formLayout_13.setObjectName("formLayout_13")
        self.label_35 = QtWidgets.QLabel(self.page_15)
        self.label_35.setObjectName("label_35")
        self.formLayout_13.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_35)
        self.r2_threadId = QtWidgets.QLineEdit(self.page_15)
        self.r2_threadId.setObjectName("r2_threadId")
        self.formLayout_13.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.r2_threadId)
        self.label_36 = QtWidgets.QLabel(self.page_15)
        self.label_36.setObjectName("label_36")
        self.formLayout_13.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.label_36)
        self.r2_subreddit = QtWidgets.QLineEdit(self.page_15)
        self.r2_subreddit.setObjectName("r2_subreddit")
        self.formLayout_13.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.r2_subreddit)
        self.label_38 = QtWidgets.QLabel(self.page_15)
        self.label_38.setObjectName("label_38")
        self.formLayout_13.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_38)
        self.label_37 = QtWidgets.QLabel(self.page_15)
        self.label_37.setObjectName("label_37")
        self.formLayout_13.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_37)
        self.r2_numComments = QtWidgets.QSpinBox(self.page_15)
        self.r2_numComments.setMinimum(0)
        self.r2_numComments.setMaximum(999999999)
        self.r2_numComments.setProperty("value", 500)
        self.r2_numComments.setObjectName("r2_numComments")
        self.formLayout_13.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.r2_numComments)
        self.r2_commentOrder = QtWidgets.QListWidget(self.page_15)
        self.r2_commentOrder.setObjectName("r2_commentOrder")
        item = QtWidgets.QListWidgetItem()
        self.r2_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r2_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r2_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r2_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r2_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r2_commentOrder.addItem(item)
        self.formLayout_13.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.r2_commentOrder)
        self.stackedWidget_4.addWidget(self.page_15)
        self.page_16 = QtWidgets.QWidget()
        self.page_16.setObjectName("page_16")
        self.formLayout_15 = QtWidgets.QFormLayout(self.page_16)
        self.formLayout_15.setContentsMargins(0, 0, 0, 0)
        self.formLayout_15.setObjectName("formLayout_15")
        self.label_39 = QtWidgets.QLabel(self.page_16)
        self.label_39.setObjectName("label_39")
        self.formLayout_15.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_39)
        self.label_41 = QtWidgets.QLabel(self.page_16)
        self.label_41.setObjectName("label_41")
        self.formLayout_15.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_41)
        self.label_40 = QtWidgets.QLabel(self.page_16)
        self.label_40.setObjectName("label_40")
        self.formLayout_15.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_40)
        self.r3_numThreads = QtWidgets.QSpinBox(self.page_16)
        self.r3_numThreads.setMinimum(0)
        self.r3_numThreads.setMaximum(999999999)
        self.r3_numThreads.setProperty("value", 100)
        self.r3_numThreads.setObjectName("r3_numThreads")
        self.formLayout_15.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.r3_numThreads)
        self.r3_query = QtWidgets.QLineEdit(self.page_16)
        self.r3_query.setObjectName("r3_query")
        self.formLayout_15.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.r3_query)
        self.r3_resultOrder = QtWidgets.QListWidget(self.page_16)
        self.r3_resultOrder.setObjectName("r3_resultOrder")
        item = QtWidgets.QListWidgetItem()
        self.r3_resultOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r3_resultOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r3_resultOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r3_resultOrder.addItem(item)
        self.formLayout_15.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.r3_resultOrder)
        self.label_42 = QtWidgets.QLabel(self.page_16)
        self.label_42.setObjectName("label_42")
        self.formLayout_15.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_42)
        self.r3_timePeriod = QtWidgets.QListWidget(self.page_16)
        self.r3_timePeriod.setObjectName("r3_timePeriod")
        item = QtWidgets.QListWidgetItem()
        self.r3_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r3_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r3_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r3_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r3_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r3_timePeriod.addItem(item)
        self.formLayout_15.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.r3_timePeriod)
        self.stackedWidget_4.addWidget(self.page_16)
        self.page_17 = QtWidgets.QWidget()
        self.page_17.setObjectName("page_17")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_17)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_43 = QtWidgets.QLabel(self.page_17)
        self.label_43.setObjectName("label_43")
        self.formLayout_5.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_43)
        self.label_46 = QtWidgets.QLabel(self.page_17)
        self.label_46.setObjectName("label_46")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_46)
        self.label_44 = QtWidgets.QLabel(self.page_17)
        self.label_44.setObjectName("label_44")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_44)
        self.label_45 = QtWidgets.QLabel(self.page_17)
        self.label_45.setObjectName("label_45")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_45)
        self.r4_numThreads = QtWidgets.QSpinBox(self.page_17)
        self.r4_numThreads.setMinimum(0)
        self.r4_numThreads.setMaximum(999999999)
        self.r4_numThreads.setProperty("value", 50)
        self.r4_numThreads.setObjectName("r4_numThreads")
        self.formLayout_5.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.r4_numThreads)
        self.r4_query = QtWidgets.QLineEdit(self.page_17)
        self.r4_query.setObjectName("r4_query")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.r4_query)
        self.r4_resultOrder = QtWidgets.QListWidget(self.page_17)
        self.r4_resultOrder.setObjectName("r4_resultOrder")
        item = QtWidgets.QListWidgetItem()
        self.r4_resultOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r4_resultOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r4_resultOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r4_resultOrder.addItem(item)
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.r4_resultOrder)
        self.r4_timePeriod = QtWidgets.QListWidget(self.page_17)
        self.r4_timePeriod.setObjectName("r4_timePeriod")
        item = QtWidgets.QListWidgetItem()
        self.r4_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r4_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r4_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r4_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r4_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r4_timePeriod.addItem(item)
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.r4_timePeriod)
        self.horizontalLayout_3.addLayout(self.formLayout_5)
        self.formLayout_14 = QtWidgets.QFormLayout()
        self.formLayout_14.setObjectName("formLayout_14")
        self.label_48 = QtWidgets.QLabel(self.page_17)
        self.label_48.setObjectName("label_48")
        self.formLayout_14.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_48)
        self.label_47 = QtWidgets.QLabel(self.page_17)
        self.label_47.setObjectName("label_47")
        self.formLayout_14.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_47)
        self.r4_numComments = QtWidgets.QSpinBox(self.page_17)
        self.r4_numComments.setMinimum(0)
        self.r4_numComments.setMaximum(999999999)
        self.r4_numComments.setProperty("value", 500)
        self.r4_numComments.setObjectName("r4_numComments")
        self.formLayout_14.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.r4_numComments)
        self.r4_commentOrder = QtWidgets.QListWidget(self.page_17)
        self.r4_commentOrder.setObjectName("r4_commentOrder")
        item = QtWidgets.QListWidgetItem()
        self.r4_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r4_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r4_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r4_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r4_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r4_commentOrder.addItem(item)
        self.formLayout_14.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.r4_commentOrder)
        self.horizontalLayout_3.addLayout(self.formLayout_14)
        self.stackedWidget_4.addWidget(self.page_17)
        self.page_18 = QtWidgets.QWidget()
        self.page_18.setObjectName("page_18")
        self.formLayout_16 = QtWidgets.QFormLayout(self.page_18)
        self.formLayout_16.setContentsMargins(0, 0, 0, 0)
        self.formLayout_16.setObjectName("formLayout_16")
        self.label_52 = QtWidgets.QLabel(self.page_18)
        self.label_52.setObjectName("label_52")
        self.formLayout_16.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_52)
        self.r5_subreddit = QtWidgets.QLineEdit(self.page_18)
        self.r5_subreddit.setObjectName("r5_subreddit")
        self.formLayout_16.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.r5_subreddit)
        self.label_50 = QtWidgets.QLabel(self.page_18)
        self.label_50.setObjectName("label_50")
        self.formLayout_16.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_50)
        self.label_51 = QtWidgets.QLabel(self.page_18)
        self.label_51.setObjectName("label_51")
        self.formLayout_16.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_51)
        self.r5_timePeriod = QtWidgets.QListWidget(self.page_18)
        self.r5_timePeriod.setObjectName("r5_timePeriod")
        item = QtWidgets.QListWidgetItem()
        self.r5_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r5_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r5_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r5_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r5_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r5_timePeriod.addItem(item)
        self.formLayout_16.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.r5_timePeriod)
        self.label_49 = QtWidgets.QLabel(self.page_18)
        self.label_49.setObjectName("label_49")
        self.formLayout_16.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_49)
        self.r5_numThreads = QtWidgets.QSpinBox(self.page_18)
        self.r5_numThreads.setMinimum(0)
        self.r5_numThreads.setMaximum(999999999)
        self.r5_numThreads.setProperty("value", 200)
        self.r5_numThreads.setObjectName("r5_numThreads")
        self.formLayout_16.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.r5_numThreads)
        self.r5_resultOrder = QtWidgets.QListWidget(self.page_18)
        self.r5_resultOrder.setObjectName("r5_resultOrder")
        item = QtWidgets.QListWidgetItem()
        self.r5_resultOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r5_resultOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r5_resultOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r5_resultOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r5_resultOrder.addItem(item)
        self.formLayout_16.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.r5_resultOrder)
        self.stackedWidget_4.addWidget(self.page_18)
        self.page_19 = QtWidgets.QWidget()
        self.page_19.setObjectName("page_19")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_19)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.formLayout_17 = QtWidgets.QFormLayout()
        self.formLayout_17.setObjectName("formLayout_17")
        self.label_54 = QtWidgets.QLabel(self.page_19)
        self.label_54.setObjectName("label_54")
        self.formLayout_17.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_54)
        self.r6_subreddit = QtWidgets.QLineEdit(self.page_19)
        self.r6_subreddit.setObjectName("r6_subreddit")
        self.formLayout_17.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.r6_subreddit)
        self.label_55 = QtWidgets.QLabel(self.page_19)
        self.label_55.setObjectName("label_55")
        self.formLayout_17.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_55)
        self.label_56 = QtWidgets.QLabel(self.page_19)
        self.label_56.setObjectName("label_56")
        self.formLayout_17.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_56)
        self.r6_timePeriod = QtWidgets.QListWidget(self.page_19)
        self.r6_timePeriod.setObjectName("r6_timePeriod")
        item = QtWidgets.QListWidgetItem()
        self.r6_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r6_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r6_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r6_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r6_timePeriod.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r6_timePeriod.addItem(item)
        self.formLayout_17.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.r6_timePeriod)
        self.label_53 = QtWidgets.QLabel(self.page_19)
        self.label_53.setObjectName("label_53")
        self.formLayout_17.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_53)
        self.r6_numThreads = QtWidgets.QSpinBox(self.page_19)
        self.r6_numThreads.setMinimum(0)
        self.r6_numThreads.setMaximum(999999999)
        self.r6_numThreads.setProperty("value", 200)
        self.r6_numThreads.setObjectName("r6_numThreads")
        self.formLayout_17.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.r6_numThreads)
        self.r6_resultOrder = QtWidgets.QListWidget(self.page_19)
        self.r6_resultOrder.setObjectName("r6_resultOrder")
        item = QtWidgets.QListWidgetItem()
        self.r6_resultOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r6_resultOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r6_resultOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r6_resultOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r6_resultOrder.addItem(item)
        self.formLayout_17.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.r6_resultOrder)
        self.horizontalLayout_4.addLayout(self.formLayout_17)
        self.formLayout_18 = QtWidgets.QFormLayout()
        self.formLayout_18.setObjectName("formLayout_18")
        self.label_57 = QtWidgets.QLabel(self.page_19)
        self.label_57.setObjectName("label_57")
        self.formLayout_18.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_57)
        self.r6_commentOrder = QtWidgets.QListWidget(self.page_19)
        self.r6_commentOrder.setObjectName("r6_commentOrder")
        item = QtWidgets.QListWidgetItem()
        self.r6_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r6_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r6_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r6_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r6_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r6_commentOrder.addItem(item)
        self.formLayout_18.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.r6_commentOrder)
        self.label_58 = QtWidgets.QLabel(self.page_19)
        self.label_58.setObjectName("label_58")
        self.formLayout_18.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_58)
        self.r6_numComments = QtWidgets.QSpinBox(self.page_19)
        self.r6_numComments.setMinimum(0)
        self.r6_numComments.setMaximum(999999999)
        self.r6_numComments.setProperty("value", 500)
        self.r6_numComments.setObjectName("r6_numComments")
        self.formLayout_18.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.r6_numComments)
        self.horizontalLayout_4.addLayout(self.formLayout_18)
        self.stackedWidget_4.addWidget(self.page_19)
        self.page_20 = QtWidgets.QWidget()
        self.page_20.setObjectName("page_20")
        self.formLayout_19 = QtWidgets.QFormLayout(self.page_20)
        self.formLayout_19.setContentsMargins(0, 0, 0, 0)
        self.formLayout_19.setObjectName("formLayout_19")
        self.label_59 = QtWidgets.QLabel(self.page_20)
        self.label_59.setObjectName("label_59")
        self.formLayout_19.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_59)
        self.r7_username = QtWidgets.QLineEdit(self.page_20)
        self.r7_username.setObjectName("r7_username")
        self.formLayout_19.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.r7_username)
        self.label_61 = QtWidgets.QLabel(self.page_20)
        self.label_61.setObjectName("label_61")
        self.formLayout_19.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_61)
        self.label_62 = QtWidgets.QLabel(self.page_20)
        self.label_62.setObjectName("label_62")
        self.formLayout_19.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_62)
        self.label_60 = QtWidgets.QLabel(self.page_20)
        self.label_60.setObjectName("label_60")
        self.formLayout_19.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_60)
        self.r7_numResults = QtWidgets.QSpinBox(self.page_20)
        self.r7_numResults.setMinimum(0)
        self.r7_numResults.setMaximum(999999999)
        self.r7_numResults.setProperty("value", 500)
        self.r7_numResults.setObjectName("r7_numResults")
        self.formLayout_19.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.r7_numResults)
        self.r7_resultOrder = QtWidgets.QListWidget(self.page_20)
        self.r7_resultOrder.setObjectName("r7_resultOrder")
        item = QtWidgets.QListWidgetItem()
        self.r7_resultOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r7_resultOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r7_resultOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r7_resultOrder.addItem(item)
        self.formLayout_19.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.r7_resultOrder)
        self.r7_resultType = QtWidgets.QListWidget(self.page_20)
        self.r7_resultType.setObjectName("r7_resultType")
        item = QtWidgets.QListWidgetItem()
        self.r7_resultType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r7_resultType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r7_resultType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.r7_resultType.addItem(item)
        self.formLayout_19.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.r7_resultType)
        self.stackedWidget_4.addWidget(self.page_20)
        self.verticalLayout_3.addWidget(self.stackedWidget_4)
        self.inputTab.addTab(self.redditTab, "")
        self.youtubeTab = QtWidgets.QWidget()
        self.youtubeTab.setObjectName("youtubeTab")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.youtubeTab)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.youtubeQueryLabel = QtWidgets.QLabel(self.youtubeTab)
        self.youtubeQueryLabel.setObjectName("youtubeQueryLabel")
        self.verticalLayout_7.addWidget(self.youtubeQueryLabel)
        self.y_functions = QtWidgets.QListWidget(self.youtubeTab)
        self.y_functions.setObjectName("y_functions")
        item = QtWidgets.QListWidgetItem()
        self.y_functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y_functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y_functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y_functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y_functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y_functions.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y_functions.addItem(item)
        self.verticalLayout_7.addWidget(self.y_functions)
        self.stackedWidget_5 = QtWidgets.QStackedWidget(self.youtubeTab)
        self.stackedWidget_5.setObjectName("stackedWidget_5")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.page_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_63 = QtWidgets.QLabel(self.page_5)
        self.label_63.setObjectName("label_63")
        self.verticalLayout_6.addWidget(self.label_63)
        self.y1_videoIds = QtWidgets.QPlainTextEdit(self.page_5)
        self.y1_videoIds.setObjectName("y1_videoIds")
        self.verticalLayout_6.addWidget(self.y1_videoIds)
        self.stackedWidget_5.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.formLayout_20 = QtWidgets.QFormLayout(self.page_6)
        self.formLayout_20.setContentsMargins(0, 0, 0, 0)
        self.formLayout_20.setObjectName("formLayout_20")
        self.label_64 = QtWidgets.QLabel(self.page_6)
        self.label_64.setObjectName("label_64")
        self.formLayout_20.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_64)
        self.y2_videoId = QtWidgets.QLineEdit(self.page_6)
        self.y2_videoId.setObjectName("y2_videoId")
        self.formLayout_20.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.y2_videoId)
        self.label_66 = QtWidgets.QLabel(self.page_6)
        self.label_66.setObjectName("label_66")
        self.formLayout_20.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_66)
        self.y2_order = QtWidgets.QListWidget(self.page_6)
        self.y2_order.setObjectName("y2_order")
        item = QtWidgets.QListWidgetItem()
        self.y2_order.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y2_order.addItem(item)
        self.formLayout_20.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.y2_order)
        self.label_67 = QtWidgets.QLabel(self.page_6)
        self.label_67.setObjectName("label_67")
        self.formLayout_20.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_67)
        self.y2_searchTerm = QtWidgets.QLineEdit(self.page_6)
        self.y2_searchTerm.setObjectName("y2_searchTerm")
        self.formLayout_20.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.y2_searchTerm)
        self.label_68 = QtWidgets.QLabel(self.page_6)
        self.label_68.setObjectName("label_68")
        self.formLayout_20.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_68)
        self.y2_format = QtWidgets.QListWidget(self.page_6)
        self.y2_format.setObjectName("y2_format")
        item = QtWidgets.QListWidgetItem()
        self.y2_format.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y2_format.addItem(item)
        self.formLayout_20.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.y2_format)
        self.label_65 = QtWidgets.QLabel(self.page_6)
        self.label_65.setObjectName("label_65")
        self.formLayout_20.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_65)
        self.y2_numComments = QtWidgets.QSpinBox(self.page_6)
        self.y2_numComments.setMinimum(0)
        self.y2_numComments.setMaximum(999999999)
        self.y2_numComments.setProperty("value", 100)
        self.y2_numComments.setObjectName("y2_numComments")
        self.formLayout_20.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.y2_numComments)
        self.stackedWidget_5.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.formLayout_21 = QtWidgets.QFormLayout()
        self.formLayout_21.setObjectName("formLayout_21")
        self.label_69 = QtWidgets.QLabel(self.page_7)
        self.label_69.setObjectName("label_69")
        self.formLayout_21.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_69)
        self.label_70 = QtWidgets.QLabel(self.page_7)
        self.label_70.setObjectName("label_70")
        self.formLayout_21.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_70)
        self.label_71 = QtWidgets.QLabel(self.page_7)
        self.label_71.setObjectName("label_71")
        self.formLayout_21.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_71)
        self.label_72 = QtWidgets.QLabel(self.page_7)
        self.label_72.setObjectName("label_72")
        self.formLayout_21.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_72)
        self.label_73 = QtWidgets.QLabel(self.page_7)
        self.label_73.setObjectName("label_73")
        self.formLayout_21.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_73)
        self.label_74 = QtWidgets.QLabel(self.page_7)
        self.label_74.setObjectName("label_74")
        self.formLayout_21.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_74)
        self.y3_query = QtWidgets.QLineEdit(self.page_7)
        self.y3_query.setObjectName("y3_query")
        self.formLayout_21.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.y3_query)
        self.y3_order = QtWidgets.QListWidget(self.page_7)
        self.y3_order.setObjectName("y3_order")
        item = QtWidgets.QListWidgetItem()
        self.y3_order.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_order.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_order.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_order.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_order.addItem(item)
        self.formLayout_21.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.y3_order)
        self.y3_channelId = QtWidgets.QLineEdit(self.page_7)
        self.y3_channelId.setObjectName("y3_channelId")
        self.formLayout_21.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.y3_channelId)
        self.y3_eventType = QtWidgets.QListWidget(self.page_7)
        self.y3_eventType.setEnabled(False)
        self.y3_eventType.setObjectName("y3_eventType")
        item = QtWidgets.QListWidgetItem()
        self.y3_eventType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_eventType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_eventType.addItem(item)
        self.formLayout_21.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.y3_eventType)
        self.y3_location = QtWidgets.QLineEdit(self.page_7)
        self.y3_location.setObjectName("y3_location")
        self.formLayout_21.setWidget(10, QtWidgets.QFormLayout.SpanningRole, self.y3_location)
        self.y3_radius = QtWidgets.QLineEdit(self.page_7)
        self.y3_radius.setEnabled(True)
        self.y3_radius.setClearButtonEnabled(False)
        self.y3_radius.setObjectName("y3_radius")
        self.formLayout_21.setWidget(12, QtWidgets.QFormLayout.SpanningRole, self.y3_radius)
        self.y3_liveEvent = QtWidgets.QCheckBox(self.page_7)
        self.y3_liveEvent.setObjectName("y3_liveEvent")
        self.formLayout_21.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.y3_liveEvent)
        self.horizontalLayout_5.addLayout(self.formLayout_21)
        self.formLayout_24 = QtWidgets.QFormLayout()
        self.formLayout_24.setObjectName("formLayout_24")
        self.y3_pubAfterCheck = QtWidgets.QCheckBox(self.page_7)
        self.y3_pubAfterCheck.setEnabled(False)
        self.y3_pubAfterCheck.setObjectName("y3_pubAfterCheck")
        self.formLayout_24.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.y3_pubAfterCheck)
        self.y3_pubAfter = QtWidgets.QDateTimeEdit(self.page_7)
        self.y3_pubAfter.setEnabled(False)
        self.y3_pubAfter.setObjectName("y3_pubAfter")
        self.formLayout_24.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.y3_pubAfter)
        self.y3_pubBeforeCheck = QtWidgets.QCheckBox(self.page_7)
        self.y3_pubBeforeCheck.setEnabled(False)
        self.y3_pubBeforeCheck.setObjectName("y3_pubBeforeCheck")
        self.formLayout_24.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.y3_pubBeforeCheck)
        self.y3_pubBefore = QtWidgets.QDateTimeEdit(self.page_7)
        self.y3_pubBefore.setEnabled(False)
        self.y3_pubBefore.setObjectName("y3_pubBefore")
        self.formLayout_24.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.y3_pubBefore)
        self.label_75 = QtWidgets.QLabel(self.page_7)
        self.label_75.setObjectName("label_75")
        self.formLayout_24.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_75)
        self.label_78 = QtWidgets.QLabel(self.page_7)
        self.label_78.setObjectName("label_78")
        self.formLayout_24.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_78)
        self.label_79 = QtWidgets.QLabel(self.page_7)
        self.label_79.setObjectName("label_79")
        self.formLayout_24.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_79)
        self.label_80 = QtWidgets.QLabel(self.page_7)
        self.label_80.setObjectName("label_80")
        self.formLayout_24.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_80)
        self.label_81 = QtWidgets.QLabel(self.page_7)
        self.label_81.setObjectName("label_81")
        self.formLayout_24.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_81)
        self.y3_regionCode = QtWidgets.QLineEdit(self.page_7)
        self.y3_regionCode.setObjectName("y3_regionCode")
        self.formLayout_24.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.y3_regionCode)
        self.y3_relevanceLanguage = QtWidgets.QLineEdit(self.page_7)
        self.y3_relevanceLanguage.setObjectName("y3_relevanceLanguage")
        self.formLayout_24.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.y3_relevanceLanguage)
        self.y3_safeSearch = QtWidgets.QListWidget(self.page_7)
        self.y3_safeSearch.setObjectName("y3_safeSearch")
        item = QtWidgets.QListWidgetItem()
        self.y3_safeSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_safeSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_safeSearch.addItem(item)
        self.formLayout_24.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.y3_safeSearch)
        self.y3_topicId = QtWidgets.QLineEdit(self.page_7)
        self.y3_topicId.setObjectName("y3_topicId")
        self.formLayout_24.setWidget(11, QtWidgets.QFormLayout.SpanningRole, self.y3_topicId)
        self.y3_captioning = QtWidgets.QListWidget(self.page_7)
        self.y3_captioning.setObjectName("y3_captioning")
        item = QtWidgets.QListWidgetItem()
        self.y3_captioning.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_captioning.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_captioning.addItem(item)
        self.formLayout_24.setWidget(13, QtWidgets.QFormLayout.SpanningRole, self.y3_captioning)
        self.horizontalLayout_5.addLayout(self.formLayout_24)
        self.formLayout_25 = QtWidgets.QFormLayout()
        self.formLayout_25.setObjectName("formLayout_25")
        self.label_82 = QtWidgets.QLabel(self.page_7)
        self.label_82.setObjectName("label_82")
        self.formLayout_25.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_82)
        self.label_83 = QtWidgets.QLabel(self.page_7)
        self.label_83.setObjectName("label_83")
        self.formLayout_25.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_83)
        self.label_84 = QtWidgets.QLabel(self.page_7)
        self.label_84.setObjectName("label_84")
        self.formLayout_25.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_84)
        self.y3_embeddable = QtWidgets.QCheckBox(self.page_7)
        self.y3_embeddable.setObjectName("y3_embeddable")
        self.formLayout_25.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.y3_embeddable)
        self.label_85 = QtWidgets.QLabel(self.page_7)
        self.label_85.setObjectName("label_85")
        self.formLayout_25.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_85)
        self.y3_categoryId = QtWidgets.QLineEdit(self.page_7)
        self.y3_categoryId.setObjectName("y3_categoryId")
        self.formLayout_25.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.y3_categoryId)
        self.y3_definition = QtWidgets.QListWidget(self.page_7)
        self.y3_definition.setObjectName("y3_definition")
        item = QtWidgets.QListWidgetItem()
        self.y3_definition.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_definition.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_definition.addItem(item)
        self.formLayout_25.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.y3_definition)
        self.y3_duration = QtWidgets.QListWidget(self.page_7)
        self.y3_duration.setObjectName("y3_duration")
        item = QtWidgets.QListWidgetItem()
        self.y3_duration.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_duration.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_duration.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_duration.addItem(item)
        self.formLayout_25.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.y3_duration)
        self.y3_license = QtWidgets.QListWidget(self.page_7)
        self.y3_license.setObjectName("y3_license")
        item = QtWidgets.QListWidgetItem()
        self.y3_license.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_license.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_license.addItem(item)
        self.formLayout_25.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.y3_license)
        self.horizontalLayout_5.addLayout(self.formLayout_25)
        self.formLayout_27 = QtWidgets.QFormLayout()
        self.formLayout_27.setObjectName("formLayout_27")
        self.y3_externally = QtWidgets.QCheckBox(self.page_7)
        self.y3_externally.setObjectName("y3_externally")
        self.formLayout_27.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.y3_externally)
        self.label_86 = QtWidgets.QLabel(self.page_7)
        self.label_86.setObjectName("label_86")
        self.formLayout_27.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_86)
        self.y3_type = QtWidgets.QListWidget(self.page_7)
        self.y3_type.setObjectName("y3_type")
        item = QtWidgets.QListWidgetItem()
        self.y3_type.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_type.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y3_type.addItem(item)
        self.formLayout_27.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.y3_type)
        self.label_88 = QtWidgets.QLabel(self.page_7)
        self.label_88.setObjectName("label_88")
        self.formLayout_27.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_88)
        self.y3_numVideos = QtWidgets.QSpinBox(self.page_7)
        self.y3_numVideos.setMinimum(0)
        self.y3_numVideos.setMaximum(999999999)
        self.y3_numVideos.setProperty("value", 100)
        self.y3_numVideos.setObjectName("y3_numVideos")
        self.formLayout_27.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.y3_numVideos)
        self.horizontalLayout_5.addLayout(self.formLayout_27)
        self.stackedWidget_5.addWidget(self.page_7)
        self.page_10 = QtWidgets.QWidget()
        self.page_10.setObjectName("page_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.page_10)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.formLayout_26 = QtWidgets.QFormLayout()
        self.formLayout_26.setObjectName("formLayout_26")
        self.label_89 = QtWidgets.QLabel(self.page_10)
        self.label_89.setObjectName("label_89")
        self.formLayout_26.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_89)
        self.label_90 = QtWidgets.QLabel(self.page_10)
        self.label_90.setObjectName("label_90")
        self.formLayout_26.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_90)
        self.label_91 = QtWidgets.QLabel(self.page_10)
        self.label_91.setObjectName("label_91")
        self.formLayout_26.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_91)
        self.label_92 = QtWidgets.QLabel(self.page_10)
        self.label_92.setObjectName("label_92")
        self.formLayout_26.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_92)
        self.label_93 = QtWidgets.QLabel(self.page_10)
        self.label_93.setObjectName("label_93")
        self.formLayout_26.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_93)
        self.label_94 = QtWidgets.QLabel(self.page_10)
        self.label_94.setObjectName("label_94")
        self.formLayout_26.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_94)
        self.y4_query = QtWidgets.QLineEdit(self.page_10)
        self.y4_query.setObjectName("y4_query")
        self.formLayout_26.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.y4_query)
        self.y4_order = QtWidgets.QListWidget(self.page_10)
        self.y4_order.setObjectName("y4_order")
        item = QtWidgets.QListWidgetItem()
        self.y4_order.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_order.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_order.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_order.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_order.addItem(item)
        self.formLayout_26.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.y4_order)
        self.y4_channelId = QtWidgets.QLineEdit(self.page_10)
        self.y4_channelId.setObjectName("y4_channelId")
        self.formLayout_26.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.y4_channelId)
        self.y4_eventType = QtWidgets.QListWidget(self.page_10)
        self.y4_eventType.setEnabled(False)
        self.y4_eventType.setObjectName("y4_eventType")
        item = QtWidgets.QListWidgetItem()
        self.y4_eventType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_eventType.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_eventType.addItem(item)
        self.formLayout_26.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.y4_eventType)
        self.y4_location = QtWidgets.QLineEdit(self.page_10)
        self.y4_location.setInputMask("")
        self.y4_location.setObjectName("y4_location")
        self.formLayout_26.setWidget(10, QtWidgets.QFormLayout.SpanningRole, self.y4_location)
        self.y4_radius = QtWidgets.QLineEdit(self.page_10)
        self.y4_radius.setEnabled(True)
        self.y4_radius.setClearButtonEnabled(False)
        self.y4_radius.setObjectName("y4_radius")
        self.formLayout_26.setWidget(12, QtWidgets.QFormLayout.SpanningRole, self.y4_radius)
        self.y4_liveEvent = QtWidgets.QCheckBox(self.page_10)
        self.y4_liveEvent.setObjectName("y4_liveEvent")
        self.formLayout_26.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.y4_liveEvent)
        self.horizontalLayout_6.addLayout(self.formLayout_26)
        self.formLayout_30 = QtWidgets.QFormLayout()
        self.formLayout_30.setObjectName("formLayout_30")
        self.y4_pubAfterCheck = QtWidgets.QCheckBox(self.page_10)
        self.y4_pubAfterCheck.setEnabled(False)
        self.y4_pubAfterCheck.setObjectName("y4_pubAfterCheck")
        self.formLayout_30.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.y4_pubAfterCheck)
        self.y4_pubAfter = QtWidgets.QDateTimeEdit(self.page_10)
        self.y4_pubAfter.setEnabled(False)
        self.y4_pubAfter.setObjectName("y4_pubAfter")
        self.formLayout_30.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.y4_pubAfter)
        self.y4_pubBeforeCheck = QtWidgets.QCheckBox(self.page_10)
        self.y4_pubBeforeCheck.setEnabled(False)
        self.y4_pubBeforeCheck.setObjectName("y4_pubBeforeCheck")
        self.formLayout_30.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.y4_pubBeforeCheck)
        self.y4_pubBefore = QtWidgets.QDateTimeEdit(self.page_10)
        self.y4_pubBefore.setEnabled(False)
        self.y4_pubBefore.setObjectName("y4_pubBefore")
        self.formLayout_30.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.y4_pubBefore)
        self.label_101 = QtWidgets.QLabel(self.page_10)
        self.label_101.setObjectName("label_101")
        self.formLayout_30.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_101)
        self.label_102 = QtWidgets.QLabel(self.page_10)
        self.label_102.setObjectName("label_102")
        self.formLayout_30.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_102)
        self.label_103 = QtWidgets.QLabel(self.page_10)
        self.label_103.setObjectName("label_103")
        self.formLayout_30.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_103)
        self.label_104 = QtWidgets.QLabel(self.page_10)
        self.label_104.setObjectName("label_104")
        self.formLayout_30.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_104)
        self.label_105 = QtWidgets.QLabel(self.page_10)
        self.label_105.setObjectName("label_105")
        self.formLayout_30.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_105)
        self.y4_regionCode = QtWidgets.QLineEdit(self.page_10)
        self.y4_regionCode.setObjectName("y4_regionCode")
        self.formLayout_30.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.y4_regionCode)
        self.y4_relevanceLanguage = QtWidgets.QLineEdit(self.page_10)
        self.y4_relevanceLanguage.setObjectName("y4_relevanceLanguage")
        self.formLayout_30.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.y4_relevanceLanguage)
        self.y4_safeSearch = QtWidgets.QListWidget(self.page_10)
        self.y4_safeSearch.setObjectName("y4_safeSearch")
        item = QtWidgets.QListWidgetItem()
        self.y4_safeSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_safeSearch.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_safeSearch.addItem(item)
        self.formLayout_30.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.y4_safeSearch)
        self.y4_topicId = QtWidgets.QLineEdit(self.page_10)
        self.y4_topicId.setObjectName("y4_topicId")
        self.formLayout_30.setWidget(11, QtWidgets.QFormLayout.SpanningRole, self.y4_topicId)
        self.y4_captioning = QtWidgets.QListWidget(self.page_10)
        self.y4_captioning.setObjectName("y4_captioning")
        item = QtWidgets.QListWidgetItem()
        self.y4_captioning.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_captioning.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_captioning.addItem(item)
        self.formLayout_30.setWidget(13, QtWidgets.QFormLayout.SpanningRole, self.y4_captioning)
        self.horizontalLayout_6.addLayout(self.formLayout_30)
        self.formLayout_29 = QtWidgets.QFormLayout()
        self.formLayout_29.setObjectName("formLayout_29")
        self.label_97 = QtWidgets.QLabel(self.page_10)
        self.label_97.setObjectName("label_97")
        self.formLayout_29.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_97)
        self.label_98 = QtWidgets.QLabel(self.page_10)
        self.label_98.setObjectName("label_98")
        self.formLayout_29.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_98)
        self.label_99 = QtWidgets.QLabel(self.page_10)
        self.label_99.setObjectName("label_99")
        self.formLayout_29.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_99)
        self.y4_embeddable = QtWidgets.QCheckBox(self.page_10)
        self.y4_embeddable.setObjectName("y4_embeddable")
        self.formLayout_29.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.y4_embeddable)
        self.label_100 = QtWidgets.QLabel(self.page_10)
        self.label_100.setObjectName("label_100")
        self.formLayout_29.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_100)
        self.y4_categoryId = QtWidgets.QLineEdit(self.page_10)
        self.y4_categoryId.setObjectName("y4_categoryId")
        self.formLayout_29.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.y4_categoryId)
        self.y4_definition = QtWidgets.QListWidget(self.page_10)
        self.y4_definition.setObjectName("y4_definition")
        item = QtWidgets.QListWidgetItem()
        self.y4_definition.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_definition.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_definition.addItem(item)
        self.formLayout_29.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.y4_definition)
        self.y4_duration = QtWidgets.QListWidget(self.page_10)
        self.y4_duration.setObjectName("y4_duration")
        item = QtWidgets.QListWidgetItem()
        self.y4_duration.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_duration.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_duration.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_duration.addItem(item)
        self.formLayout_29.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.y4_duration)
        self.y4_license = QtWidgets.QListWidget(self.page_10)
        self.y4_license.setObjectName("y4_license")
        item = QtWidgets.QListWidgetItem()
        self.y4_license.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_license.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_license.addItem(item)
        self.formLayout_29.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.y4_license)
        self.horizontalLayout_6.addLayout(self.formLayout_29)
        self.formLayout_28 = QtWidgets.QFormLayout()
        self.formLayout_28.setObjectName("formLayout_28")
        self.y4_externally = QtWidgets.QCheckBox(self.page_10)
        self.y4_externally.setObjectName("y4_externally")
        self.formLayout_28.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.y4_externally)
        self.label_95 = QtWidgets.QLabel(self.page_10)
        self.label_95.setObjectName("label_95")
        self.formLayout_28.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_95)
        self.y4_type = QtWidgets.QListWidget(self.page_10)
        self.y4_type.setObjectName("y4_type")
        item = QtWidgets.QListWidgetItem()
        self.y4_type.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_type.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_type.addItem(item)
        self.formLayout_28.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.y4_type)
        self.label_96 = QtWidgets.QLabel(self.page_10)
        self.label_96.setObjectName("label_96")
        self.formLayout_28.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_96)
        self.y4_numVideos = QtWidgets.QSpinBox(self.page_10)
        self.y4_numVideos.setMinimum(0)
        self.y4_numVideos.setMaximum(999999999)
        self.y4_numVideos.setProperty("value", 100)
        self.y4_numVideos.setObjectName("y4_numVideos")
        self.formLayout_28.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.y4_numVideos)
        self.label_106 = QtWidgets.QLabel(self.page_10)
        self.label_106.setObjectName("label_106")
        self.formLayout_28.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_106)
        self.label_107 = QtWidgets.QLabel(self.page_10)
        self.label_107.setObjectName("label_107")
        self.formLayout_28.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_107)
        self.label_108 = QtWidgets.QLabel(self.page_10)
        self.label_108.setObjectName("label_108")
        self.formLayout_28.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_108)
        self.label_109 = QtWidgets.QLabel(self.page_10)
        self.label_109.setObjectName("label_109")
        self.formLayout_28.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_109)
        self.y4_numComments = QtWidgets.QSpinBox(self.page_10)
        self.y4_numComments.setMinimum(0)
        self.y4_numComments.setMaximum(999999999)
        self.y4_numComments.setProperty("value", 50)
        self.y4_numComments.setObjectName("y4_numComments")
        self.formLayout_28.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.y4_numComments)
        self.y4_commentOrder = QtWidgets.QListWidget(self.page_10)
        self.y4_commentOrder.setObjectName("y4_commentOrder")
        item = QtWidgets.QListWidgetItem()
        self.y4_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_commentOrder.addItem(item)
        self.formLayout_28.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.y4_commentOrder)
        self.y4_commentText = QtWidgets.QLineEdit(self.page_10)
        self.y4_commentText.setObjectName("y4_commentText")
        self.formLayout_28.setWidget(8, QtWidgets.QFormLayout.SpanningRole, self.y4_commentText)
        self.y4_commentFormat = QtWidgets.QListWidget(self.page_10)
        self.y4_commentFormat.setObjectName("y4_commentFormat")
        item = QtWidgets.QListWidgetItem()
        self.y4_commentFormat.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y4_commentFormat.addItem(item)
        self.formLayout_28.setWidget(10, QtWidgets.QFormLayout.SpanningRole, self.y4_commentFormat)
        self.horizontalLayout_6.addLayout(self.formLayout_28)
        self.stackedWidget_5.addWidget(self.page_10)
        self.page_9 = QtWidgets.QWidget()
        self.page_9.setObjectName("page_9")
        self.formLayout_33 = QtWidgets.QFormLayout(self.page_9)
        self.formLayout_33.setContentsMargins(0, 0, 0, 0)
        self.formLayout_33.setObjectName("formLayout_33")
        self.label_111 = QtWidgets.QLabel(self.page_9)
        self.label_111.setObjectName("label_111")
        self.formLayout_33.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_111)
        self.label_110 = QtWidgets.QLabel(self.page_9)
        self.label_110.setObjectName("label_110")
        self.formLayout_33.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_110)
        self.label_112 = QtWidgets.QLabel(self.page_9)
        self.label_112.setObjectName("label_112")
        self.formLayout_33.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_112)
        self.y5_numVideos = QtWidgets.QSpinBox(self.page_9)
        self.y5_numVideos.setMinimum(0)
        self.y5_numVideos.setMaximum(999999999)
        self.y5_numVideos.setProperty("value", 100)
        self.y5_numVideos.setObjectName("y5_numVideos")
        self.formLayout_33.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.y5_numVideos)
        self.y5_channelId = QtWidgets.QLineEdit(self.page_9)
        self.y5_channelId.setObjectName("y5_channelId")
        self.formLayout_33.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.y5_channelId)
        self.y5_order = QtWidgets.QListWidget(self.page_9)
        self.y5_order.setObjectName("y5_order")
        item = QtWidgets.QListWidgetItem()
        self.y5_order.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y5_order.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y5_order.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y5_order.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y5_order.addItem(item)
        self.formLayout_33.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.y5_order)
        self.stackedWidget_5.addWidget(self.page_9)
        self.page_8 = QtWidgets.QWidget()
        self.page_8.setObjectName("page_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.page_8)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.formLayout_31 = QtWidgets.QFormLayout()
        self.formLayout_31.setObjectName("formLayout_31")
        self.label_76 = QtWidgets.QLabel(self.page_8)
        self.label_76.setObjectName("label_76")
        self.formLayout_31.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_76)
        self.label_87 = QtWidgets.QLabel(self.page_8)
        self.label_87.setObjectName("label_87")
        self.formLayout_31.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_87)
        self.label_77 = QtWidgets.QLabel(self.page_8)
        self.label_77.setObjectName("label_77")
        self.formLayout_31.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_77)
        self.y6_numVideos = QtWidgets.QSpinBox(self.page_8)
        self.y6_numVideos.setMinimum(0)
        self.y6_numVideos.setMaximum(999999999)
        self.y6_numVideos.setProperty("value", 20)
        self.y6_numVideos.setObjectName("y6_numVideos")
        self.formLayout_31.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.y6_numVideos)
        self.y6_channelId = QtWidgets.QLineEdit(self.page_8)
        self.y6_channelId.setObjectName("y6_channelId")
        self.formLayout_31.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.y6_channelId)
        self.y6_order = QtWidgets.QListWidget(self.page_8)
        self.y6_order.setObjectName("y6_order")
        item = QtWidgets.QListWidgetItem()
        self.y6_order.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y6_order.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y6_order.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y6_order.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y6_order.addItem(item)
        self.formLayout_31.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.y6_order)
        self.horizontalLayout_7.addLayout(self.formLayout_31)
        self.formLayout_23 = QtWidgets.QFormLayout()
        self.formLayout_23.setObjectName("formLayout_23")
        self.label_114 = QtWidgets.QLabel(self.page_8)
        self.label_114.setObjectName("label_114")
        self.formLayout_23.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_114)
        self.label_113 = QtWidgets.QLabel(self.page_8)
        self.label_113.setObjectName("label_113")
        self.formLayout_23.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_113)
        self.label_116 = QtWidgets.QLabel(self.page_8)
        self.label_116.setObjectName("label_116")
        self.formLayout_23.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_116)
        self.label_115 = QtWidgets.QLabel(self.page_8)
        self.label_115.setObjectName("label_115")
        self.formLayout_23.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_115)
        self.y6_numComments = QtWidgets.QSpinBox(self.page_8)
        self.y6_numComments.setMinimum(0)
        self.y6_numComments.setMaximum(999999999)
        self.y6_numComments.setProperty("value", 100)
        self.y6_numComments.setObjectName("y6_numComments")
        self.formLayout_23.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.y6_numComments)
        self.y6_commentOrder = QtWidgets.QListWidget(self.page_8)
        self.y6_commentOrder.setObjectName("y6_commentOrder")
        item = QtWidgets.QListWidgetItem()
        self.y6_commentOrder.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y6_commentOrder.addItem(item)
        self.formLayout_23.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.y6_commentOrder)
        self.y6_commentText = QtWidgets.QLineEdit(self.page_8)
        self.y6_commentText.setObjectName("y6_commentText")
        self.formLayout_23.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.y6_commentText)
        self.y6_commentFormat = QtWidgets.QListWidget(self.page_8)
        self.y6_commentFormat.setObjectName("y6_commentFormat")
        item = QtWidgets.QListWidgetItem()
        self.y6_commentFormat.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.y6_commentFormat.addItem(item)
        self.formLayout_23.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.y6_commentFormat)
        self.horizontalLayout_7.addLayout(self.formLayout_23)
        self.stackedWidget_5.addWidget(self.page_8)
        self.page_21 = QtWidgets.QWidget()
        self.page_21.setObjectName("page_21")
        self.formLayout_32 = QtWidgets.QFormLayout(self.page_21)
        self.formLayout_32.setContentsMargins(0, 0, 0, 0)
        self.formLayout_32.setObjectName("formLayout_32")
        self.label_117 = QtWidgets.QLabel(self.page_21)
        self.label_117.setObjectName("label_117")
        self.formLayout_32.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_117)
        self.y7_channelName = QtWidgets.QLineEdit(self.page_21)
        self.y7_channelName.setObjectName("y7_channelName")
        self.formLayout_32.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.y7_channelName)
        self.stackedWidget_5.addWidget(self.page_21)
        self.verticalLayout_7.addWidget(self.stackedWidget_5)
        self.inputTab.addTab(self.youtubeTab, "")
        self.gridLayout_4.addWidget(self.inputTab, 1, 0, 1, 1)
        self.inputDownload = QtWidgets.QPushButton(self.input)
        self.inputDownload.setObjectName("inputDownload")
        self.gridLayout_4.addWidget(self.inputDownload, 2, 0, 1, 1)
        self.inputLabel = QtWidgets.QLabel(self.input)
        self.inputLabel.setObjectName("inputLabel")
        self.gridLayout_4.addWidget(self.inputLabel, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.input)
        self.progress = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progress.sizePolicy().hasHeightForWidth())
        self.progress.setSizePolicy(sizePolicy)
        self.progress.setObjectName("progress")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.progress)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressDone = QtWidgets.QPushButton(self.progress)
        self.progressDone.setObjectName("progressDone")
        self.horizontalLayout.addWidget(self.progressDone)
        self.displayResultsButton = QtWidgets.QPushButton(self.progress)
        self.displayResultsButton.setEnabled(False)
        self.displayResultsButton.setObjectName("displayResultsButton")
        self.horizontalLayout.addWidget(self.displayResultsButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.saveCSV = QtWidgets.QPushButton(self.progress)
        self.saveCSV.setObjectName("saveCSV")
        self.horizontalLayout.addWidget(self.saveCSV)
        self.saveJSON = QtWidgets.QPushButton(self.progress)
        self.saveJSON.setObjectName("saveJSON")
        self.horizontalLayout.addWidget(self.saveJSON)
        self.gridLayout_8.addLayout(self.horizontalLayout, 8, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.progressBar = QtWidgets.QProgressBar(self.progress)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_9.addWidget(self.progressBar)
        self.pauseButton = QtWidgets.QPushButton(self.progress)
        self.pauseButton.setObjectName("pauseButton")
        self.horizontalLayout_9.addWidget(self.pauseButton)
        self.gridLayout_8.addLayout(self.horizontalLayout_9, 3, 0, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.progress)
        self.tableWidget.setDragEnabled(True)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 3, item)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.gridLayout_8.addWidget(self.tableWidget, 7, 0, 1, 1)
        self.textOut = QtWidgets.QTextEdit(self.progress)
        self.textOut.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textOut.setReadOnly(True)
        self.textOut.setAcceptRichText(True)
        self.textOut.setObjectName("textOut")
        self.gridLayout_8.addWidget(self.textOut, 1, 0, 1, 1)
        self.label_126 = QtWidgets.QLabel(self.progress)
        self.label_126.setObjectName("label_126")
        self.gridLayout_8.addWidget(self.label_126, 0, 0, 1, 1)
        self.label_128 = QtWidgets.QLabel(self.progress)
        self.label_128.setObjectName("label_128")
        self.gridLayout_8.addWidget(self.label_128, 2, 0, 1, 1)
        self.stackedWidget.addWidget(self.progress)
        self.preferences = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preferences.sizePolicy().hasHeightForWidth())
        self.preferences.setSizePolicy(sizePolicy)
        self.preferences.setObjectName("preferences")
        self.formLayout_35 = QtWidgets.QFormLayout(self.preferences)
        self.formLayout_35.setContentsMargins(0, 0, 0, 0)
        self.formLayout_35.setObjectName("formLayout_35")
        self.checkBox = QtWidgets.QCheckBox(self.preferences)
        self.checkBox.setEnabled(False)
        self.checkBox.setCheckable(True)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.formLayout_35.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.preferences)
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout_35.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkBox_2)
        self.preferencesDone = QtWidgets.QPushButton(self.preferences)
        self.preferencesDone.setObjectName("preferencesDone")
        self.formLayout_35.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.preferencesDone)
        self.preferencesLabel = QtWidgets.QLabel(self.preferences)
        self.preferencesLabel.setObjectName("preferencesLabel")
        self.formLayout_35.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.preferencesLabel)
        self.stackedWidget.addWidget(self.preferences)
        self.updates = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.updates.sizePolicy().hasHeightForWidth())
        self.updates.setSizePolicy(sizePolicy)
        self.updates.setObjectName("updates")
        self.formLayout_34 = QtWidgets.QFormLayout(self.updates)
        self.formLayout_34.setContentsMargins(0, 0, 0, 0)
        self.formLayout_34.setObjectName("formLayout_34")
        self.checkUpdatesButton = QtWidgets.QPushButton(self.updates)
        self.checkUpdatesButton.setObjectName("checkUpdatesButton")
        self.formLayout_34.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkUpdatesButton)
        self.updateStatusLabel = QtWidgets.QLabel(self.updates)
        self.updateStatusLabel.setOpenExternalLinks(True)
        self.updateStatusLabel.setObjectName("updateStatusLabel")
        self.formLayout_34.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.updateStatusLabel)
        self.updatesDone = QtWidgets.QPushButton(self.updates)
        self.updatesDone.setObjectName("updatesDone")
        self.formLayout_34.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.updatesDone)
        self.updatesLabel = QtWidgets.QLabel(self.updates)
        self.updatesLabel.setObjectName("updatesLabel")
        self.formLayout_34.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.updatesLabel)
        self.stackedWidget.addWidget(self.updates)
        self.licenses = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.licenses.sizePolicy().hasHeightForWidth())
        self.licenses.setSizePolicy(sizePolicy)
        self.licenses.setObjectName("licenses")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.licenses)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.licensesLabel = QtWidgets.QLabel(self.licenses)
        self.licensesLabel.setObjectName("licensesLabel")
        self.verticalLayout_9.addWidget(self.licensesLabel)
        self.textEdit = QtWidgets.QTextEdit(self.licenses)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_9.addWidget(self.textEdit)
        self.licencesDone = QtWidgets.QPushButton(self.licenses)
        self.licencesDone.setObjectName("licencesDone")
        self.verticalLayout_9.addWidget(self.licencesDone)
        self.stackedWidget.addWidget(self.licenses)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1333, 33))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionAuthentication = QtWidgets.QAction(MainWindow)
        self.actionAuthentication.setObjectName("actionAuthentication")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLicences = QtWidgets.QAction(MainWindow)
        self.actionLicences.setObjectName("actionLicences")
        self.actionCheck_for_Updates = QtWidgets.QAction(MainWindow)
        self.actionCheck_for_Updates.setObjectName("actionCheck_for_Updates")
        self.menuFile.addAction(self.actionQuit)
        self.menuSettings.addAction(self.actionPreferences)
        self.menuSettings.addAction(self.actionAuthentication)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuHelp.addAction(self.actionLicences)
        self.menuHelp.addAction(self.actionCheck_for_Updates)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.inputTab.setCurrentIndex(0)
        self.f_functions.setCurrentRow(0)
        self.stackedWidget_2.setCurrentIndex(0)
        self.f2_commentType.setCurrentRow(0)
        self.f2_commentOrder.setCurrentRow(0)
        self.f3_postType.setCurrentRow(0)
        self.f4_postType.setCurrentRow(0)
        self.f4_commentOrder.setCurrentRow(0)
        self.f4_commentType.setCurrentRow(0)
        self.t_functions.setCurrentRow(0)
        self.stackedWidget_3.setCurrentIndex(0)
        self.t1_resultType.setCurrentRow(0)
        self.t2_resultType.setCurrentRow(0)
        self.r_functions.setCurrentRow(0)
        self.stackedWidget_4.setCurrentIndex(0)
        self.r2_commentOrder.setCurrentRow(0)
        self.r3_resultOrder.setCurrentRow(0)
        self.r3_timePeriod.setCurrentRow(0)
        self.r4_resultOrder.setCurrentRow(0)
        self.r4_timePeriod.setCurrentRow(0)
        self.r4_commentOrder.setCurrentRow(0)
        self.r5_timePeriod.setCurrentRow(0)
        self.r5_resultOrder.setCurrentRow(0)
        self.r6_timePeriod.setCurrentRow(0)
        self.r6_resultOrder.setCurrentRow(0)
        self.r6_commentOrder.setCurrentRow(0)
        self.r7_resultOrder.setCurrentRow(0)
        self.r7_resultType.setCurrentRow(0)
        self.y_functions.setCurrentRow(0)
        self.stackedWidget_5.setCurrentIndex(0)
        self.y2_order.setCurrentRow(0)
        self.y2_format.setCurrentRow(0)
        self.y3_order.setCurrentRow(0)
        self.y3_eventType.setCurrentRow(0)
        self.y3_safeSearch.setCurrentRow(0)
        self.y3_captioning.setCurrentRow(0)
        self.y3_definition.setCurrentRow(0)
        self.y3_duration.setCurrentRow(0)
        self.y3_license.setCurrentRow(0)
        self.y3_type.setCurrentRow(0)
        self.y4_order.setCurrentRow(0)
        self.y4_eventType.setCurrentRow(0)
        self.y4_safeSearch.setCurrentRow(0)
        self.y4_captioning.setCurrentRow(0)
        self.y4_definition.setCurrentRow(0)
        self.y4_duration.setCurrentRow(0)
        self.y4_license.setCurrentRow(0)
        self.y4_type.setCurrentRow(0)
        self.y4_commentOrder.setCurrentRow(0)
        self.y4_commentFormat.setCurrentRow(0)
        self.y5_order.setCurrentRow(0)
        self.y6_order.setCurrentRow(0)
        self.y6_commentOrder.setCurrentRow(0)
        self.y6_commentFormat.setCurrentRow(0)
        self.f_functions.currentRowChanged['int'].connect(self.stackedWidget_2.setCurrentIndex)
        self.r_functions.currentRowChanged['int'].connect(self.stackedWidget_4.setCurrentIndex)
        self.t_functions.currentRowChanged['int'].connect(self.stackedWidget_3.setCurrentIndex)
        self.y_functions.currentRowChanged['int'].connect(self.stackedWidget_5.setCurrentIndex)
        self.y4_pubBeforeCheck.toggled['bool'].connect(self.y4_pubBefore.setEnabled)
        self.y3_pubAfterCheck.toggled['bool'].connect(self.y3_pubAfter.setEnabled)
        self.y4_pubAfterCheck.toggled['bool'].connect(self.y4_pubAfter.setEnabled)
        self.y3_pubBeforeCheck.toggled['bool'].connect(self.y3_pubBefore.setEnabled)
        self.y4_liveEvent.toggled['bool'].connect(self.y4_eventType.setEnabled)
        self.y3_liveEvent.toggled['bool'].connect(self.y3_eventType.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Reaper"))
        self.label_121.setText(_translate("MainWindow", "Welcome to Reaper"))
        self.label_123.setText(_translate("MainWindow", "\n"
"Reaper is a graphical tool that interacts with social media APIs using the socialreaper python package. \n"
"\n"
"Reaper currently supports scraping Facebook, Twitter, Reddit and Youtube. By using this software, you are agreeing to these platform\'s privacy policies and terms of use \n"
"\n"
"To get started, you must provide Reaper with authentication "))
        self.label_124.setText(_translate("MainWindow", "Reaper is licensed under the GPL 3.0 \n"
"\n"
"© Adam Smith, 2017\n"
""))
        self.label_125.setText(_translate("MainWindow", "<a href=\"https://github.com/scriptsmith/reaper\">https://github.com/scriptsmith/reaper</a>"))
        self.introductionContinue.setText(_translate("MainWindow", "Continue"))
        self.label.setText(_translate("MainWindow", "API key"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.facebookAuthTab), _translate("MainWindow", "Facebook"))
        self.label_5.setText(_translate("MainWindow", "App key"))
        self.label_6.setText(_translate("MainWindow", "App secret"))
        self.label_7.setText(_translate("MainWindow", "OAuth token"))
        self.label_8.setText(_translate("MainWindow", "OAuth token secret"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.twitterAuthTab), _translate("MainWindow", "Twitter"))
        self.label_9.setText(_translate("MainWindow", "Application id"))
        self.label_10.setText(_translate("MainWindow", "Application secret"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.redditAuthTab), _translate("MainWindow", "Reddit"))
        self.label_11.setText(_translate("MainWindow", "API key"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.youtubeAuthTab), _translate("MainWindow", "Youtube"))
        self.authenticationDone.setText(_translate("MainWindow", "Done"))
        self.label_122.setText(_translate("MainWindow", "<a href=\"https://reaper.readthedocs.io\">Help</a>"))
        self.label_127.setText(_translate("MainWindow", "Authentication"))
        self.inputTab.setToolTip(_translate("MainWindow", "Reddit query type"))
        self.facebookTab.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Function"))
        __sortingEnabled = self.f_functions.isSortingEnabled()
        self.f_functions.setSortingEnabled(False)
        item = self.f_functions.item(0)
        item.setText(_translate("MainWindow", "Posts from post ids"))
        item = self.f_functions.item(1)
        item.setText(_translate("MainWindow", "Comments from post"))
        item = self.f_functions.item(2)
        item.setText(_translate("MainWindow", "Posts from page"))
        item = self.f_functions.item(3)
        item.setText(_translate("MainWindow", "Comments from page\'s posts"))
        self.f_functions.setSortingEnabled(__sortingEnabled)
        self.label_3.setText(_translate("MainWindow", "Comma-seperated list of post ids"))
        self.f1_postIds.setPlaceholderText(_translate("MainWindow", "179866158722992_1312328855476711, 179866158722992_1314779625231634"))
        self.label_4.setText(_translate("MainWindow", "Post id"))
        self.label_13.setText(_translate("MainWindow", "Comment type"))
        __sortingEnabled = self.f2_commentType.isSortingEnabled()
        self.f2_commentType.setSortingEnabled(False)
        item = self.f2_commentType.item(0)
        item.setText(_translate("MainWindow", "stream"))
        item = self.f2_commentType.item(1)
        item.setText(_translate("MainWindow", "toplevel"))
        self.f2_commentType.setSortingEnabled(__sortingEnabled)
        self.label_14.setText(_translate("MainWindow", "Comment order"))
        __sortingEnabled = self.f2_commentOrder.isSortingEnabled()
        self.f2_commentOrder.setSortingEnabled(False)
        item = self.f2_commentOrder.item(0)
        item.setText(_translate("MainWindow", "chronological"))
        item = self.f2_commentOrder.item(1)
        item.setText(_translate("MainWindow", "reverse_chronological"))
        self.f2_commentOrder.setSortingEnabled(__sortingEnabled)
        self.label_12.setText(_translate("MainWindow", "Number of comments"))
        self.f2_postId.setPlaceholderText(_translate("MainWindow", "179866158722992_1312328855476711"))
        self.label_15.setText(_translate("MainWindow", "Page id"))
        self.label_16.setText(_translate("MainWindow", "Post type"))
        self.f3_includeHidden.setText(_translate("MainWindow", "Include hidden posts"))
        self.label_17.setText(_translate("MainWindow", "Number of posts"))
        self.f3_pageId.setPlaceholderText(_translate("MainWindow", "Wikipedia"))
        __sortingEnabled = self.f3_postType.isSortingEnabled()
        self.f3_postType.setSortingEnabled(False)
        item = self.f3_postType.item(0)
        item.setText(_translate("MainWindow", "posts"))
        item = self.f3_postType.item(1)
        item.setText(_translate("MainWindow", "feed"))
        item = self.f3_postType.item(2)
        item.setText(_translate("MainWindow", "tagged"))
        item = self.f3_postType.item(3)
        item.setText(_translate("MainWindow", "promotable_posts"))
        self.f3_postType.setSortingEnabled(__sortingEnabled)
        self.label_20.setText(_translate("MainWindow", "Page id"))
        self.label_19.setText(_translate("MainWindow", "Post type"))
        self.f4_includeHIdden.setText(_translate("MainWindow", "Include hidden posts"))
        self.label_18.setText(_translate("MainWindow", "Number of posts"))
        self.f4_pageId.setPlaceholderText(_translate("MainWindow", "TrolleyProblemMemes"))
        __sortingEnabled = self.f4_postType.isSortingEnabled()
        self.f4_postType.setSortingEnabled(False)
        item = self.f4_postType.item(0)
        item.setText(_translate("MainWindow", "posts"))
        item = self.f4_postType.item(1)
        item.setText(_translate("MainWindow", "feed"))
        item = self.f4_postType.item(2)
        item.setText(_translate("MainWindow", "tagged"))
        item = self.f4_postType.item(3)
        item.setText(_translate("MainWindow", "promotable_posts"))
        self.f4_postType.setSortingEnabled(__sortingEnabled)
        self.label_21.setText(_translate("MainWindow", "Comment type"))
        self.label_23.setText(_translate("MainWindow", "Comment order"))
        self.label_22.setText(_translate("MainWindow", "Number of comments per post"))
        __sortingEnabled = self.f4_commentOrder.isSortingEnabled()
        self.f4_commentOrder.setSortingEnabled(False)
        item = self.f4_commentOrder.item(0)
        item.setText(_translate("MainWindow", "chronological"))
        item = self.f4_commentOrder.item(1)
        item.setText(_translate("MainWindow", "reverse_chronological"))
        self.f4_commentOrder.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.f4_commentType.isSortingEnabled()
        self.f4_commentType.setSortingEnabled(False)
        item = self.f4_commentType.item(0)
        item.setText(_translate("MainWindow", "stream"))
        item = self.f4_commentType.item(1)
        item.setText(_translate("MainWindow", "toplevel"))
        self.f4_commentType.setSortingEnabled(__sortingEnabled)
        self.inputTab.setTabText(self.inputTab.indexOf(self.facebookTab), _translate("MainWindow", "Facebook"))
        self.label_24.setText(_translate("MainWindow", "Function"))
        __sortingEnabled = self.t_functions.isSortingEnabled()
        self.t_functions.setSortingEnabled(False)
        item = self.t_functions.item(0)
        item.setText(_translate("MainWindow", "Search"))
        item = self.t_functions.item(1)
        item.setText(_translate("MainWindow", "Hashtag"))
        item = self.t_functions.item(2)
        item.setText(_translate("MainWindow", "User"))
        self.t_functions.setSortingEnabled(__sortingEnabled)
        self.label_25.setText(_translate("MainWindow", "Search query"))
        self.t1_searchQuery.setPlaceholderText(_translate("MainWindow", "travel"))
        self.label_26.setText(_translate("MainWindow", "Result type"))
        self.t1_includeEntities.setText(_translate("MainWindow", "Include entities"))
        self.label_27.setText(_translate("MainWindow", "Max id"))
        __sortingEnabled = self.t1_resultType.isSortingEnabled()
        self.t1_resultType.setSortingEnabled(False)
        item = self.t1_resultType.item(0)
        item.setText(_translate("MainWindow", "mixed"))
        item = self.t1_resultType.item(1)
        item.setText(_translate("MainWindow", "recent"))
        item = self.t1_resultType.item(2)
        item.setText(_translate("MainWindow", "popular"))
        self.t1_resultType.setSortingEnabled(__sortingEnabled)
        self.label_119.setText(_translate("MainWindow", "Number of tweets"))
        self.t1_maxId.setPlaceholderText(_translate("MainWindow", "796351336178655232"))
        self.label_28.setText(_translate("MainWindow", "Hashtag"))
        self.label_30.setText(_translate("MainWindow", "Result type"))
        self.t2_includeEntities.setText(_translate("MainWindow", "Include entities"))
        self.label_29.setText(_translate("MainWindow", "Max id"))
        self.t2_hashtag.setPlaceholderText(_translate("MainWindow", "#news"))
        __sortingEnabled = self.t2_resultType.isSortingEnabled()
        self.t2_resultType.setSortingEnabled(False)
        item = self.t2_resultType.item(0)
        item.setText(_translate("MainWindow", "mixed"))
        item = self.t2_resultType.item(1)
        item.setText(_translate("MainWindow", "recent"))
        item = self.t2_resultType.item(2)
        item.setText(_translate("MainWindow", "popular"))
        self.t2_resultType.setSortingEnabled(__sortingEnabled)
        self.label_120.setText(_translate("MainWindow", "Number of tweets"))
        self.t2_maxId.setPlaceholderText(_translate("MainWindow", "796351336178655232"))
        self.label_31.setText(_translate("MainWindow", "Username"))
        self.t3_excludeReplies.setText(_translate("MainWindow", "Exclude replies"))
        self.t3_includeRetweets.setText(_translate("MainWindow", "Include retweets"))
        self.label_32.setText(_translate("MainWindow", "Number of tweets"))
        self.t3_username.setPlaceholderText(_translate("MainWindow", "@jack"))
        self.inputTab.setTabText(self.inputTab.indexOf(self.twitterTab), _translate("MainWindow", "Twitter"))
        self.label_33.setText(_translate("MainWindow", "Function"))
        __sortingEnabled = self.r_functions.isSortingEnabled()
        self.r_functions.setSortingEnabled(False)
        item = self.r_functions.item(0)
        item.setText(_translate("MainWindow", "Threads from thread ids"))
        item = self.r_functions.item(1)
        item.setText(_translate("MainWindow", "Thread\'s comments"))
        item = self.r_functions.item(2)
        item.setText(_translate("MainWindow", "Search\'s threads"))
        item = self.r_functions.item(3)
        item.setText(_translate("MainWindow", "Search\'s threads\' comments"))
        item = self.r_functions.item(4)
        item.setText(_translate("MainWindow", "Subreddit\'s threads"))
        item = self.r_functions.item(5)
        item.setText(_translate("MainWindow", "Subreddit\'s threads\' comments"))
        item = self.r_functions.item(6)
        item.setText(_translate("MainWindow", "User\'s posts"))
        self.r_functions.setSortingEnabled(__sortingEnabled)
        self.label_34.setText(_translate("MainWindow", "Comma-seperated list of thread ids"))
        self.r1_threadIds.setPlaceholderText(_translate("MainWindow", "5jrlw1, 488gjl"))
        self.label_118.setText(_translate("MainWindow", "Comma seperated list of subreddit names"))
        self.r1_subredditNames.setPlaceholderText(_translate("MainWindow", "gifs, movies"))
        self.label_35.setText(_translate("MainWindow", "Thread id"))
        self.r2_threadId.setPlaceholderText(_translate("MainWindow", "488gjl"))
        self.label_36.setText(_translate("MainWindow", "Subreddit"))
        self.r2_subreddit.setPlaceholderText(_translate("MainWindow", "movies"))
        self.label_38.setText(_translate("MainWindow", "Comment order"))
        self.label_37.setText(_translate("MainWindow", "Number of comments"))
        __sortingEnabled = self.r2_commentOrder.isSortingEnabled()
        self.r2_commentOrder.setSortingEnabled(False)
        item = self.r2_commentOrder.item(0)
        item.setText(_translate("MainWindow", "top"))
        item = self.r2_commentOrder.item(1)
        item.setText(_translate("MainWindow", "new"))
        item = self.r2_commentOrder.item(2)
        item.setText(_translate("MainWindow", "best"))
        item = self.r2_commentOrder.item(3)
        item.setText(_translate("MainWindow", "controversial"))
        item = self.r2_commentOrder.item(4)
        item.setText(_translate("MainWindow", "old"))
        item = self.r2_commentOrder.item(5)
        item.setText(_translate("MainWindow", "q&a"))
        self.r2_commentOrder.setSortingEnabled(__sortingEnabled)
        self.label_39.setText(_translate("MainWindow", "Query"))
        self.label_41.setText(_translate("MainWindow", "Result order"))
        self.label_40.setText(_translate("MainWindow", "Number of threads"))
        self.r3_query.setPlaceholderText(_translate("MainWindow", "puppy"))
        __sortingEnabled = self.r3_resultOrder.isSortingEnabled()
        self.r3_resultOrder.setSortingEnabled(False)
        item = self.r3_resultOrder.item(0)
        item.setText(_translate("MainWindow", "top"))
        item = self.r3_resultOrder.item(1)
        item.setText(_translate("MainWindow", "new"))
        item = self.r3_resultOrder.item(2)
        item.setText(_translate("MainWindow", "relevance"))
        item = self.r3_resultOrder.item(3)
        item.setText(_translate("MainWindow", "comments"))
        self.r3_resultOrder.setSortingEnabled(__sortingEnabled)
        self.label_42.setText(_translate("MainWindow", "Time period"))
        __sortingEnabled = self.r3_timePeriod.isSortingEnabled()
        self.r3_timePeriod.setSortingEnabled(False)
        item = self.r3_timePeriod.item(0)
        item.setText(_translate("MainWindow", "all"))
        item = self.r3_timePeriod.item(1)
        item.setText(_translate("MainWindow", "year"))
        item = self.r3_timePeriod.item(2)
        item.setText(_translate("MainWindow", "month"))
        item = self.r3_timePeriod.item(3)
        item.setText(_translate("MainWindow", "week"))
        item = self.r3_timePeriod.item(4)
        item.setText(_translate("MainWindow", "today"))
        item = self.r3_timePeriod.item(5)
        item.setText(_translate("MainWindow", "hour"))
        self.r3_timePeriod.setSortingEnabled(__sortingEnabled)
        self.label_43.setText(_translate("MainWindow", "Number of threads"))
        self.label_46.setText(_translate("MainWindow", "Query"))
        self.label_44.setText(_translate("MainWindow", "Result order"))
        self.label_45.setText(_translate("MainWindow", "Result time period"))
        self.r4_query.setPlaceholderText(_translate("MainWindow", "puppy"))
        __sortingEnabled = self.r4_resultOrder.isSortingEnabled()
        self.r4_resultOrder.setSortingEnabled(False)
        item = self.r4_resultOrder.item(0)
        item.setText(_translate("MainWindow", "top"))
        item = self.r4_resultOrder.item(1)
        item.setText(_translate("MainWindow", "new"))
        item = self.r4_resultOrder.item(2)
        item.setText(_translate("MainWindow", "relevance"))
        item = self.r4_resultOrder.item(3)
        item.setText(_translate("MainWindow", "comments"))
        self.r4_resultOrder.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.r4_timePeriod.isSortingEnabled()
        self.r4_timePeriod.setSortingEnabled(False)
        item = self.r4_timePeriod.item(0)
        item.setText(_translate("MainWindow", "all"))
        item = self.r4_timePeriod.item(1)
        item.setText(_translate("MainWindow", "year"))
        item = self.r4_timePeriod.item(2)
        item.setText(_translate("MainWindow", "month"))
        item = self.r4_timePeriod.item(3)
        item.setText(_translate("MainWindow", "week"))
        item = self.r4_timePeriod.item(4)
        item.setText(_translate("MainWindow", "today"))
        item = self.r4_timePeriod.item(5)
        item.setText(_translate("MainWindow", "hour"))
        self.r4_timePeriod.setSortingEnabled(__sortingEnabled)
        self.label_48.setText(_translate("MainWindow", "Comment order"))
        self.label_47.setText(_translate("MainWindow", "Number of comments per thread"))
        __sortingEnabled = self.r4_commentOrder.isSortingEnabled()
        self.r4_commentOrder.setSortingEnabled(False)
        item = self.r4_commentOrder.item(0)
        item.setText(_translate("MainWindow", "top"))
        item = self.r4_commentOrder.item(1)
        item.setText(_translate("MainWindow", "new"))
        item = self.r4_commentOrder.item(2)
        item.setText(_translate("MainWindow", "best"))
        item = self.r4_commentOrder.item(3)
        item.setText(_translate("MainWindow", "controversial"))
        item = self.r4_commentOrder.item(4)
        item.setText(_translate("MainWindow", "old"))
        item = self.r4_commentOrder.item(5)
        item.setText(_translate("MainWindow", "q&a"))
        self.r4_commentOrder.setSortingEnabled(__sortingEnabled)
        self.label_52.setText(_translate("MainWindow", "Subreddit"))
        self.r5_subreddit.setPlaceholderText(_translate("MainWindow", "all"))
        self.label_50.setText(_translate("MainWindow", "Result category"))
        self.label_51.setText(_translate("MainWindow", "Time period"))
        __sortingEnabled = self.r5_timePeriod.isSortingEnabled()
        self.r5_timePeriod.setSortingEnabled(False)
        item = self.r5_timePeriod.item(0)
        item.setText(_translate("MainWindow", "all"))
        item = self.r5_timePeriod.item(1)
        item.setText(_translate("MainWindow", "year"))
        item = self.r5_timePeriod.item(2)
        item.setText(_translate("MainWindow", "month"))
        item = self.r5_timePeriod.item(3)
        item.setText(_translate("MainWindow", "week"))
        item = self.r5_timePeriod.item(4)
        item.setText(_translate("MainWindow", "today"))
        item = self.r5_timePeriod.item(5)
        item.setText(_translate("MainWindow", "hour"))
        self.r5_timePeriod.setSortingEnabled(__sortingEnabled)
        self.label_49.setText(_translate("MainWindow", "Number of threads"))
        __sortingEnabled = self.r5_resultOrder.isSortingEnabled()
        self.r5_resultOrder.setSortingEnabled(False)
        item = self.r5_resultOrder.item(0)
        item.setText(_translate("MainWindow", "top"))
        item = self.r5_resultOrder.item(1)
        item.setText(_translate("MainWindow", "hot"))
        item = self.r5_resultOrder.item(2)
        item.setText(_translate("MainWindow", "new"))
        item = self.r5_resultOrder.item(3)
        item.setText(_translate("MainWindow", "rising"))
        item = self.r5_resultOrder.item(4)
        item.setText(_translate("MainWindow", "controversial"))
        self.r5_resultOrder.setSortingEnabled(__sortingEnabled)
        self.label_54.setText(_translate("MainWindow", "Subreddit"))
        self.r6_subreddit.setPlaceholderText(_translate("MainWindow", "all"))
        self.label_55.setText(_translate("MainWindow", "Result category"))
        self.label_56.setText(_translate("MainWindow", "Result time period"))
        __sortingEnabled = self.r6_timePeriod.isSortingEnabled()
        self.r6_timePeriod.setSortingEnabled(False)
        item = self.r6_timePeriod.item(0)
        item.setText(_translate("MainWindow", "all"))
        item = self.r6_timePeriod.item(1)
        item.setText(_translate("MainWindow", "year"))
        item = self.r6_timePeriod.item(2)
        item.setText(_translate("MainWindow", "month"))
        item = self.r6_timePeriod.item(3)
        item.setText(_translate("MainWindow", "week"))
        item = self.r6_timePeriod.item(4)
        item.setText(_translate("MainWindow", "today"))
        item = self.r6_timePeriod.item(5)
        item.setText(_translate("MainWindow", "hour"))
        self.r6_timePeriod.setSortingEnabled(__sortingEnabled)
        self.label_53.setText(_translate("MainWindow", "Number of threads"))
        __sortingEnabled = self.r6_resultOrder.isSortingEnabled()
        self.r6_resultOrder.setSortingEnabled(False)
        item = self.r6_resultOrder.item(0)
        item.setText(_translate("MainWindow", "top"))
        item = self.r6_resultOrder.item(1)
        item.setText(_translate("MainWindow", "hot"))
        item = self.r6_resultOrder.item(2)
        item.setText(_translate("MainWindow", "new"))
        item = self.r6_resultOrder.item(3)
        item.setText(_translate("MainWindow", "rising"))
        item = self.r6_resultOrder.item(4)
        item.setText(_translate("MainWindow", "controversial"))
        self.r6_resultOrder.setSortingEnabled(__sortingEnabled)
        self.label_57.setText(_translate("MainWindow", "Comment order"))
        __sortingEnabled = self.r6_commentOrder.isSortingEnabled()
        self.r6_commentOrder.setSortingEnabled(False)
        item = self.r6_commentOrder.item(0)
        item.setText(_translate("MainWindow", "top"))
        item = self.r6_commentOrder.item(1)
        item.setText(_translate("MainWindow", "new"))
        item = self.r6_commentOrder.item(2)
        item.setText(_translate("MainWindow", "best"))
        item = self.r6_commentOrder.item(3)
        item.setText(_translate("MainWindow", "controversial"))
        item = self.r6_commentOrder.item(4)
        item.setText(_translate("MainWindow", "old"))
        item = self.r6_commentOrder.item(5)
        item.setText(_translate("MainWindow", "q&a"))
        self.r6_commentOrder.setSortingEnabled(__sortingEnabled)
        self.label_58.setText(_translate("MainWindow", "Number of comments per thread"))
        self.label_59.setText(_translate("MainWindow", "Username"))
        self.r7_username.setPlaceholderText(_translate("MainWindow", "warlizard"))
        self.label_61.setText(_translate("MainWindow", "Result order"))
        self.label_62.setText(_translate("MainWindow", "Result type"))
        self.label_60.setText(_translate("MainWindow", "Number of results"))
        __sortingEnabled = self.r7_resultOrder.isSortingEnabled()
        self.r7_resultOrder.setSortingEnabled(False)
        item = self.r7_resultOrder.item(0)
        item.setText(_translate("MainWindow", "new"))
        item = self.r7_resultOrder.item(1)
        item.setText(_translate("MainWindow", "hot"))
        item = self.r7_resultOrder.item(2)
        item.setText(_translate("MainWindow", "top"))
        item = self.r7_resultOrder.item(3)
        item.setText(_translate("MainWindow", "controversial"))
        self.r7_resultOrder.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.r7_resultType.isSortingEnabled()
        self.r7_resultType.setSortingEnabled(False)
        item = self.r7_resultType.item(0)
        item.setText(_translate("MainWindow", "overview"))
        item = self.r7_resultType.item(1)
        item.setText(_translate("MainWindow", "submitted"))
        item = self.r7_resultType.item(2)
        item.setText(_translate("MainWindow", "comments"))
        item = self.r7_resultType.item(3)
        item.setText(_translate("MainWindow", "gilded"))
        self.r7_resultType.setSortingEnabled(__sortingEnabled)
        self.inputTab.setTabText(self.inputTab.indexOf(self.redditTab), _translate("MainWindow", "Reddit"))
        self.youtubeQueryLabel.setText(_translate("MainWindow", "Function"))
        self.y_functions.setToolTip(_translate("MainWindow", "Youtube query type"))
        __sortingEnabled = self.y_functions.isSortingEnabled()
        self.y_functions.setSortingEnabled(False)
        item = self.y_functions.item(0)
        item.setText(_translate("MainWindow", "Videos from video ids"))
        item = self.y_functions.item(1)
        item.setText(_translate("MainWindow", "Video\'s comments"))
        item = self.y_functions.item(2)
        item.setText(_translate("MainWindow", "Search\'s videos"))
        item = self.y_functions.item(3)
        item.setText(_translate("MainWindow", "Search\'s videos\' comments"))
        item = self.y_functions.item(4)
        item.setText(_translate("MainWindow", "Channel\'s videos"))
        item = self.y_functions.item(5)
        item.setText(_translate("MainWindow", "Channel\'s videos\' comments"))
        item = self.y_functions.item(6)
        item.setText(_translate("MainWindow", "Guess channel id"))
        self.y_functions.setSortingEnabled(__sortingEnabled)
        self.label_63.setText(_translate("MainWindow", "Comma-seperated list of video ids"))
        self.y1_videoIds.setPlaceholderText(_translate("MainWindow", "jNQXAC9IVRw, _GuOjXYl5ew"))
        self.label_64.setText(_translate("MainWindow", "Video id"))
        self.y2_videoId.setPlaceholderText(_translate("MainWindow", "jNQXAC9IVRw"))
        self.label_66.setText(_translate("MainWindow", "Order"))
        __sortingEnabled = self.y2_order.isSortingEnabled()
        self.y2_order.setSortingEnabled(False)
        item = self.y2_order.item(0)
        item.setText(_translate("MainWindow", "time"))
        item = self.y2_order.item(1)
        item.setText(_translate("MainWindow", "relevance"))
        self.y2_order.setSortingEnabled(__sortingEnabled)
        self.label_67.setText(_translate("MainWindow", "Containing the text"))
        self.label_68.setText(_translate("MainWindow", "Comment format"))
        __sortingEnabled = self.y2_format.isSortingEnabled()
        self.y2_format.setSortingEnabled(False)
        item = self.y2_format.item(0)
        item.setText(_translate("MainWindow", "html"))
        item = self.y2_format.item(1)
        item.setText(_translate("MainWindow", "plaintext"))
        self.y2_format.setSortingEnabled(__sortingEnabled)
        self.label_65.setText(_translate("MainWindow", "Number of comments"))
        self.label_69.setText(_translate("MainWindow", "Query"))
        self.label_70.setText(_translate("MainWindow", "Order"))
        self.label_71.setText(_translate("MainWindow", "Channel id"))
        self.label_72.setText(_translate("MainWindow", "Event type"))
        self.label_73.setText(_translate("MainWindow", "Latitude,Longitude"))
        self.label_74.setText(_translate("MainWindow", "Location radius"))
        self.y3_query.setPlaceholderText(_translate("MainWindow", "vlog"))
        __sortingEnabled = self.y3_order.isSortingEnabled()
        self.y3_order.setSortingEnabled(False)
        item = self.y3_order.item(0)
        item.setText(_translate("MainWindow", "date"))
        item = self.y3_order.item(1)
        item.setText(_translate("MainWindow", "rating"))
        item = self.y3_order.item(2)
        item.setText(_translate("MainWindow", "relevance"))
        item = self.y3_order.item(3)
        item.setText(_translate("MainWindow", "reviewCount"))
        item = self.y3_order.item(4)
        item.setText(_translate("MainWindow", "title"))
        self.y3_order.setSortingEnabled(__sortingEnabled)
        self.y3_channelId.setPlaceholderText(_translate("MainWindow", "UCtinbF-Q-fVthA0qrFQTgXQ"))
        __sortingEnabled = self.y3_eventType.isSortingEnabled()
        self.y3_eventType.setSortingEnabled(False)
        item = self.y3_eventType.item(0)
        item.setText(_translate("MainWindow", "completed"))
        item = self.y3_eventType.item(1)
        item.setText(_translate("MainWindow", "live"))
        item = self.y3_eventType.item(2)
        item.setText(_translate("MainWindow", "upcoming"))
        self.y3_eventType.setSortingEnabled(__sortingEnabled)
        self.y3_location.setPlaceholderText(_translate("MainWindow", "40.765867,-73.977513"))
        self.y3_radius.setPlaceholderText(_translate("MainWindow", "10km"))
        self.y3_liveEvent.setText(_translate("MainWindow", "Live Event"))
        self.y3_pubAfterCheck.setText(_translate("MainWindow", "Published after"))
        self.y3_pubBeforeCheck.setText(_translate("MainWindow", "Published before"))
        self.label_75.setText(_translate("MainWindow", "Region code"))
        self.label_78.setText(_translate("MainWindow", "Relevance language"))
        self.label_79.setText(_translate("MainWindow", "Safe search"))
        self.label_80.setText(_translate("MainWindow", "Topic id"))
        self.label_81.setText(_translate("MainWindow", "Captioning"))
        self.y3_regionCode.setPlaceholderText(_translate("MainWindow", "GB"))
        self.y3_relevanceLanguage.setPlaceholderText(_translate("MainWindow", "en"))
        __sortingEnabled = self.y3_safeSearch.isSortingEnabled()
        self.y3_safeSearch.setSortingEnabled(False)
        item = self.y3_safeSearch.item(0)
        item.setText(_translate("MainWindow", "none"))
        item = self.y3_safeSearch.item(1)
        item.setText(_translate("MainWindow", "moderate"))
        item = self.y3_safeSearch.item(2)
        item.setText(_translate("MainWindow", "strict"))
        self.y3_safeSearch.setSortingEnabled(__sortingEnabled)
        self.y3_topicId.setPlaceholderText(_translate("MainWindow", "/m/019_rr"))
        __sortingEnabled = self.y3_captioning.isSortingEnabled()
        self.y3_captioning.setSortingEnabled(False)
        item = self.y3_captioning.item(0)
        item.setText(_translate("MainWindow", "any"))
        item = self.y3_captioning.item(1)
        item.setText(_translate("MainWindow", "closedCaption"))
        item = self.y3_captioning.item(2)
        item.setText(_translate("MainWindow", "none"))
        self.y3_captioning.setSortingEnabled(__sortingEnabled)
        self.label_82.setText(_translate("MainWindow", "Category id"))
        self.label_83.setText(_translate("MainWindow", "Definition"))
        self.label_84.setText(_translate("MainWindow", "Duration"))
        self.y3_embeddable.setText(_translate("MainWindow", "Only embeddable"))
        self.label_85.setText(_translate("MainWindow", "License"))
        self.y3_categoryId.setPlaceholderText(_translate("MainWindow", "18"))
        __sortingEnabled = self.y3_definition.isSortingEnabled()
        self.y3_definition.setSortingEnabled(False)
        item = self.y3_definition.item(0)
        item.setText(_translate("MainWindow", "any"))
        item = self.y3_definition.item(1)
        item.setText(_translate("MainWindow", "high"))
        item = self.y3_definition.item(2)
        item.setText(_translate("MainWindow", "standard"))
        self.y3_definition.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.y3_duration.isSortingEnabled()
        self.y3_duration.setSortingEnabled(False)
        item = self.y3_duration.item(0)
        item.setText(_translate("MainWindow", "any"))
        item = self.y3_duration.item(1)
        item.setText(_translate("MainWindow", "long"))
        item = self.y3_duration.item(2)
        item.setText(_translate("MainWindow", "medium"))
        item = self.y3_duration.item(3)
        item.setText(_translate("MainWindow", "short"))
        self.y3_duration.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.y3_license.isSortingEnabled()
        self.y3_license.setSortingEnabled(False)
        item = self.y3_license.item(0)
        item.setText(_translate("MainWindow", "any"))
        item = self.y3_license.item(1)
        item.setText(_translate("MainWindow", "youtube"))
        item = self.y3_license.item(2)
        item.setText(_translate("MainWindow", "creativeCommon"))
        self.y3_license.setSortingEnabled(__sortingEnabled)
        self.y3_externally.setText(_translate("MainWindow", "Only externally playable"))
        self.label_86.setText(_translate("MainWindow", "Type"))
        __sortingEnabled = self.y3_type.isSortingEnabled()
        self.y3_type.setSortingEnabled(False)
        item = self.y3_type.item(0)
        item.setText(_translate("MainWindow", "any"))
        item = self.y3_type.item(1)
        item.setText(_translate("MainWindow", "episode"))
        item = self.y3_type.item(2)
        item.setText(_translate("MainWindow", "movie"))
        self.y3_type.setSortingEnabled(__sortingEnabled)
        self.label_88.setText(_translate("MainWindow", "Number of videos"))
        self.label_89.setText(_translate("MainWindow", "Query"))
        self.label_90.setText(_translate("MainWindow", "Order"))
        self.label_91.setText(_translate("MainWindow", "Channel id"))
        self.label_92.setText(_translate("MainWindow", "Event type"))
        self.label_93.setText(_translate("MainWindow", "Latitude,Longitude"))
        self.label_94.setText(_translate("MainWindow", "Location radius"))
        self.y4_query.setPlaceholderText(_translate("MainWindow", "vlog"))
        __sortingEnabled = self.y4_order.isSortingEnabled()
        self.y4_order.setSortingEnabled(False)
        item = self.y4_order.item(0)
        item.setText(_translate("MainWindow", "date"))
        item = self.y4_order.item(1)
        item.setText(_translate("MainWindow", "rating"))
        item = self.y4_order.item(2)
        item.setText(_translate("MainWindow", "relevance"))
        item = self.y4_order.item(3)
        item.setText(_translate("MainWindow", "reviewCount"))
        item = self.y4_order.item(4)
        item.setText(_translate("MainWindow", "title"))
        self.y4_order.setSortingEnabled(__sortingEnabled)
        self.y4_channelId.setPlaceholderText(_translate("MainWindow", "UCtinbF-Q-fVthA0qrFQTgXQ"))
        __sortingEnabled = self.y4_eventType.isSortingEnabled()
        self.y4_eventType.setSortingEnabled(False)
        item = self.y4_eventType.item(0)
        item.setText(_translate("MainWindow", "completed"))
        item = self.y4_eventType.item(1)
        item.setText(_translate("MainWindow", "live"))
        item = self.y4_eventType.item(2)
        item.setText(_translate("MainWindow", "upcoming"))
        self.y4_eventType.setSortingEnabled(__sortingEnabled)
        self.y4_location.setPlaceholderText(_translate("MainWindow", "40.765867,-73.977513"))
        self.y4_radius.setPlaceholderText(_translate("MainWindow", "10km"))
        self.y4_liveEvent.setText(_translate("MainWindow", "Live event"))
        self.y4_pubAfterCheck.setText(_translate("MainWindow", "Published after"))
        self.y4_pubBeforeCheck.setText(_translate("MainWindow", "Published before"))
        self.label_101.setText(_translate("MainWindow", "Region code"))
        self.label_102.setText(_translate("MainWindow", "Relevance language"))
        self.label_103.setText(_translate("MainWindow", "Safe search"))
        self.label_104.setText(_translate("MainWindow", "Topic id"))
        self.label_105.setText(_translate("MainWindow", "Captioning"))
        self.y4_regionCode.setPlaceholderText(_translate("MainWindow", "GB"))
        self.y4_relevanceLanguage.setPlaceholderText(_translate("MainWindow", "en"))
        __sortingEnabled = self.y4_safeSearch.isSortingEnabled()
        self.y4_safeSearch.setSortingEnabled(False)
        item = self.y4_safeSearch.item(0)
        item.setText(_translate("MainWindow", "none"))
        item = self.y4_safeSearch.item(1)
        item.setText(_translate("MainWindow", "moderate"))
        item = self.y4_safeSearch.item(2)
        item.setText(_translate("MainWindow", "strict"))
        self.y4_safeSearch.setSortingEnabled(__sortingEnabled)
        self.y4_topicId.setPlaceholderText(_translate("MainWindow", "/m/019_rr"))
        __sortingEnabled = self.y4_captioning.isSortingEnabled()
        self.y4_captioning.setSortingEnabled(False)
        item = self.y4_captioning.item(0)
        item.setText(_translate("MainWindow", "any"))
        item = self.y4_captioning.item(1)
        item.setText(_translate("MainWindow", "closedCaption"))
        item = self.y4_captioning.item(2)
        item.setText(_translate("MainWindow", "none"))
        self.y4_captioning.setSortingEnabled(__sortingEnabled)
        self.label_97.setText(_translate("MainWindow", "Category id"))
        self.label_98.setText(_translate("MainWindow", "Definition"))
        self.label_99.setText(_translate("MainWindow", "Duration"))
        self.y4_embeddable.setText(_translate("MainWindow", "Only embeddable"))
        self.label_100.setText(_translate("MainWindow", "License"))
        self.y4_categoryId.setPlaceholderText(_translate("MainWindow", "18"))
        __sortingEnabled = self.y4_definition.isSortingEnabled()
        self.y4_definition.setSortingEnabled(False)
        item = self.y4_definition.item(0)
        item.setText(_translate("MainWindow", "any"))
        item = self.y4_definition.item(1)
        item.setText(_translate("MainWindow", "high"))
        item = self.y4_definition.item(2)
        item.setText(_translate("MainWindow", "standard"))
        self.y4_definition.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.y4_duration.isSortingEnabled()
        self.y4_duration.setSortingEnabled(False)
        item = self.y4_duration.item(0)
        item.setText(_translate("MainWindow", "any"))
        item = self.y4_duration.item(1)
        item.setText(_translate("MainWindow", "long"))
        item = self.y4_duration.item(2)
        item.setText(_translate("MainWindow", "medium"))
        item = self.y4_duration.item(3)
        item.setText(_translate("MainWindow", "short"))
        self.y4_duration.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.y4_license.isSortingEnabled()
        self.y4_license.setSortingEnabled(False)
        item = self.y4_license.item(0)
        item.setText(_translate("MainWindow", "any"))
        item = self.y4_license.item(1)
        item.setText(_translate("MainWindow", "youtube"))
        item = self.y4_license.item(2)
        item.setText(_translate("MainWindow", "creativeCommon"))
        self.y4_license.setSortingEnabled(__sortingEnabled)
        self.y4_externally.setText(_translate("MainWindow", "Only externally playable"))
        self.label_95.setText(_translate("MainWindow", "Type"))
        __sortingEnabled = self.y4_type.isSortingEnabled()
        self.y4_type.setSortingEnabled(False)
        item = self.y4_type.item(0)
        item.setText(_translate("MainWindow", "any"))
        item = self.y4_type.item(1)
        item.setText(_translate("MainWindow", "episode"))
        item = self.y4_type.item(2)
        item.setText(_translate("MainWindow", "movie"))
        self.y4_type.setSortingEnabled(__sortingEnabled)
        self.label_96.setText(_translate("MainWindow", "Number of videos"))
        self.label_106.setText(_translate("MainWindow", "Comment order"))
        self.label_107.setText(_translate("MainWindow", "Comments containing text:"))
        self.label_108.setText(_translate("MainWindow", "Comment format"))
        self.label_109.setText(_translate("MainWindow", "Number of comments"))
        __sortingEnabled = self.y4_commentOrder.isSortingEnabled()
        self.y4_commentOrder.setSortingEnabled(False)
        item = self.y4_commentOrder.item(0)
        item.setText(_translate("MainWindow", "time"))
        item = self.y4_commentOrder.item(1)
        item.setText(_translate("MainWindow", "relevance"))
        self.y4_commentOrder.setSortingEnabled(__sortingEnabled)
        self.y4_commentText.setPlaceholderText(_translate("MainWindow", "camera,casey"))
        __sortingEnabled = self.y4_commentFormat.isSortingEnabled()
        self.y4_commentFormat.setSortingEnabled(False)
        item = self.y4_commentFormat.item(0)
        item.setText(_translate("MainWindow", "html"))
        item = self.y4_commentFormat.item(1)
        item.setText(_translate("MainWindow", "plaintext"))
        self.y4_commentFormat.setSortingEnabled(__sortingEnabled)
        self.label_111.setText(_translate("MainWindow", "Channel id"))
        self.label_110.setText(_translate("MainWindow", "Video order"))
        self.label_112.setText(_translate("MainWindow", "Number of videos"))
        self.y5_channelId.setPlaceholderText(_translate("MainWindow", "UC3LqW4ijMoENQ2Wv17ZrFJA"))
        __sortingEnabled = self.y5_order.isSortingEnabled()
        self.y5_order.setSortingEnabled(False)
        item = self.y5_order.item(0)
        item.setText(_translate("MainWindow", "date"))
        item = self.y5_order.item(1)
        item.setText(_translate("MainWindow", "rating"))
        item = self.y5_order.item(2)
        item.setText(_translate("MainWindow", "relevance"))
        item = self.y5_order.item(3)
        item.setText(_translate("MainWindow", "title"))
        item = self.y5_order.item(4)
        item.setText(_translate("MainWindow", "viewCount"))
        self.y5_order.setSortingEnabled(__sortingEnabled)
        self.label_76.setText(_translate("MainWindow", "Channel id"))
        self.label_87.setText(_translate("MainWindow", "Video order"))
        self.label_77.setText(_translate("MainWindow", "Number of videos"))
        self.y6_channelId.setPlaceholderText(_translate("MainWindow", "UC3LqW4ijMoENQ2Wv17ZrFJA"))
        __sortingEnabled = self.y6_order.isSortingEnabled()
        self.y6_order.setSortingEnabled(False)
        item = self.y6_order.item(0)
        item.setText(_translate("MainWindow", "date"))
        item = self.y6_order.item(1)
        item.setText(_translate("MainWindow", "rating"))
        item = self.y6_order.item(2)
        item.setText(_translate("MainWindow", "relevance"))
        item = self.y6_order.item(3)
        item.setText(_translate("MainWindow", "title"))
        item = self.y6_order.item(4)
        item.setText(_translate("MainWindow", "viewCount"))
        self.y6_order.setSortingEnabled(__sortingEnabled)
        self.label_114.setText(_translate("MainWindow", "Comment order"))
        self.label_113.setText(_translate("MainWindow", "Comments containing text:"))
        self.label_116.setText(_translate("MainWindow", "Comment format"))
        self.label_115.setText(_translate("MainWindow", "Number of comments"))
        __sortingEnabled = self.y6_commentOrder.isSortingEnabled()
        self.y6_commentOrder.setSortingEnabled(False)
        item = self.y6_commentOrder.item(0)
        item.setText(_translate("MainWindow", "time"))
        item = self.y6_commentOrder.item(1)
        item.setText(_translate("MainWindow", "relevance"))
        self.y6_commentOrder.setSortingEnabled(__sortingEnabled)
        self.y6_commentText.setPlaceholderText(_translate("MainWindow", "internet,idea"))
        __sortingEnabled = self.y6_commentFormat.isSortingEnabled()
        self.y6_commentFormat.setSortingEnabled(False)
        item = self.y6_commentFormat.item(0)
        item.setText(_translate("MainWindow", "html"))
        item = self.y6_commentFormat.item(1)
        item.setText(_translate("MainWindow", "plaintext"))
        self.y6_commentFormat.setSortingEnabled(__sortingEnabled)
        self.label_117.setText(_translate("MainWindow", "Channel name"))
        self.y7_channelName.setPlaceholderText(_translate("MainWindow", "vsauce"))
        self.inputTab.setTabText(self.inputTab.indexOf(self.youtubeTab), _translate("MainWindow", "Youtube"))
        self.inputDownload.setText(_translate("MainWindow", "Download"))
        self.inputLabel.setText(_translate("MainWindow", "Input"))
        self.progressDone.setText(_translate("MainWindow", "Done"))
        self.displayResultsButton.setText(_translate("MainWindow", "Display Results"))
        self.saveCSV.setText(_translate("MainWindow", "Save as CSV"))
        self.saveJSON.setText(_translate("MainWindow", "Save as JSON"))
        self.pauseButton.setText(_translate("MainWindow", "Pause"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Score"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Text"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "Foobar"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "3534523"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("MainWindow", "14"))
        item = self.tableWidget.item(0, 3)
        item.setText(_translate("MainWindow", " Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas velit neque, consequat id arcu quis, viverra porttitor est. Donec non risus ut magna sodales sodales efficitur nec diam. Nam ac rhoncus erat. Suspendisse hendrerit rhoncus mattis. Donec ac semper nulla. Etiam sagittis, diam ac facilisis efficitur, justo ligula fermentum ligula, nec porttitor ligula eros sed sem. In at augue neque. Curabitur rutrum vestibulum metus, in tempor diam pulvinar sit amet. Morbi non ornare nibh. Morbi pellentesque augue in lorem tristique, nec dictum ex euismod. Etiam id nisi ut felis varius suscipit id et mauris. Integer eu posuere mi. Mauris sit amet sem enim. Suspendisse potenti. Maecenas faucibus posuere finibus. Morbi augue metus, lacinia ut tincidunt tempus, laoreet eget leo. "))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "BarFoo"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "8734957"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("MainWindow", "742"))
        item = self.tableWidget.item(1, 3)
        item.setText(_translate("MainWindow", "Maecenas vel tempor libero, nec porttitor odio. In tellus eros, gravida eget leo sed, varius lobortis orci. Cras feugiat sodales sapien, non convallis neque luctus sed. Suspendisse euismod gravida pulvinar. Morbi molestie nibh risus. In nec ipsum vel leo fermentum sagittis. Nunc pulvinar risus ligula, in varius elit blandit non. Suspendisse euismod varius elit, sit amet aliquet sem dictum quis. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Proin posuere finibus nibh in pellentesque. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec et elementum enim, et laoreet tortor. Quisque convallis lacinia massa eu ultricies. Sed imperdiet odio vitae justo tincidunt eleifend. "))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "BooFar"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "9238432"))
        item = self.tableWidget.item(2, 2)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget.item(2, 3)
        item.setText(_translate("MainWindow", "Nam laoreet porta massa non lobortis. Pellentesque tristique quam nec velit tristique, tincidunt facilisis felis faucibus. Maecenas viverra, dui at scelerisque lobortis, orci quam malesuada nulla, sit amet efficitur orci libero nec metus. Ut efficitur, massa ut ornare luctus, mauris leo cursus enim, vel fermentum justo augue eu velit. In suscipit dapibus rhoncus. Vestibulum eu ipsum scelerisque, dignissim leo id, dapibus mi. Aenean cursus, ante sed tempus consectetur, turpis nibh egestas odio, vel suscipit lectus massa nec nisi. Nam lacinia venenatis odio, at aliquam ipsum consectetur a. Praesent a lorem et dui accumsan faucibus a id ipsum. Donec id eleifend ex, ut blandit eros. Donec volutpat nec augue in consequat. Donec vel auctor nisi. Pellentesque non ante libero. "))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.textOut.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_126.setText(_translate("MainWindow", "Error Log"))
        self.label_128.setText(_translate("MainWindow", "Progress"))
        self.checkBox.setText(_translate("MainWindow", "Display results in table"))
        self.checkBox_2.setText(_translate("MainWindow", "Remember authentication keys"))
        self.preferencesDone.setText(_translate("MainWindow", "Done"))
        self.preferencesLabel.setText(_translate("MainWindow", "Preferences"))
        self.checkUpdatesButton.setText(_translate("MainWindow", "Check for updates"))
        self.updateStatusLabel.setText(_translate("MainWindow", "Reaper is up to date"))
        self.updatesDone.setText(_translate("MainWindow", "Done"))
        self.updatesLabel.setText(_translate("MainWindow", "Updates"))
        self.licensesLabel.setText(_translate("MainWindow", "Licenses"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'DejaVu Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Reaper</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                    GNU GENERAL PUBLIC LICENSE</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                       Version 3, 29 June 2007</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Copyright (C) 2007 Free Software Foundation, Inc. &lt;http://fsf.org/&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Everyone is permitted to copy and distribute verbatim copies</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> of this license document, but changing it is not allowed.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                            Preamble</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The GNU General Public License is a free, copyleft license for</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">software and other kinds of works.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The licenses for most software and other practical works are designed</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">to take away your freedom to share and change the works.  By contrast,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the GNU General Public License is intended to guarantee your freedom to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">share and change all versions of a program--to make sure it remains free</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">software for all its users.  We, the Free Software Foundation, use the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GNU General Public License for most of our software; it applies also to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">any other work released this way by its authors.  You can apply it to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">your programs, too.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  When we speak of free software, we are referring to freedom, not</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">price.  Our General Public Licenses are designed to make sure that you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">have the freedom to distribute copies of free software (and charge for</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">them if you wish), that you receive source code or can get it if you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">want it, that you can change the software or use pieces of it in new</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">free programs, and that you know you can do these things.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  To protect your rights, we need to prevent others from denying you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">these rights or asking you to surrender the rights.  Therefore, you have</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">certain responsibilities if you distribute copies of the software, or if</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">you modify it: responsibilities to respect the freedom of others.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  For example, if you distribute copies of such a program, whether</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gratis or for a fee, you must pass on to the recipients the same</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">freedoms that you received.  You must make sure that they, too, receive</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">or can get the source code.  And you must show them these terms so they</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">know their rights.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Developers that use the GNU GPL protect your rights with two steps:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(1) assert copyright on the software, and (2) offer you this License</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">giving you legal permission to copy, distribute and/or modify it.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  For the developers\' and authors\' protection, the GPL clearly explains</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">that there is no warranty for this free software.  For both users\' and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">authors\' sake, the GPL requires that modified versions be marked as</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">changed, so that their problems will not be attributed erroneously to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">authors of previous versions.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Some devices are designed to deny users access to install or run</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">modified versions of the software inside them, although the manufacturer</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">can do so.  This is fundamentally incompatible with the aim of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">protecting users\' freedom to change the software.  The systematic</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">pattern of such abuse occurs in the area of products for individuals to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">use, which is precisely where it is most unacceptable.  Therefore, we</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">have designed this version of the GPL to prohibit the practice for those</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">products.  If such problems arise substantially in other domains, we</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">stand ready to extend this provision to those domains in future versions</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">of the GPL, as needed to protect the freedom of users.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Finally, every program is threatened constantly by software patents.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">States should not allow patents to restrict development and use of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">software on general-purpose computers, but in those that do, we wish to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">avoid the special danger that patents applied to a free program could</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">make it effectively proprietary.  To prevent this, the GPL assures that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">patents cannot be used to render the program non-free.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The precise terms and conditions for copying, distribution and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">modification follow.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                       TERMS AND CONDITIONS</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  0. Definitions.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  &quot;This License&quot; refers to version 3 of the GNU General Public License.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  &quot;Copyright&quot; also means copyright-like laws that apply to other kinds of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">works, such as semiconductor masks.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  &quot;The Program&quot; refers to any copyrightable work licensed under this</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License.  Each licensee is addressed as &quot;you&quot;.  &quot;Licensees&quot; and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&quot;recipients&quot; may be individuals or organizations.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  To &quot;modify&quot; a work means to copy from or adapt all or part of the work</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in a fashion requiring copyright permission, other than the making of an</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">exact copy.  The resulting work is called a &quot;modified version&quot; of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">earlier work or a work &quot;based on&quot; the earlier work.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  A &quot;covered work&quot; means either the unmodified Program or a work based</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">on the Program.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  To &quot;propagate&quot; a work means to do anything with it that, without</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">permission, would make you directly or secondarily liable for</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">infringement under applicable copyright law, except executing it on a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">computer or modifying a private copy.  Propagation includes copying,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">distribution (with or without modification), making available to the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">public, and in some countries other activities as well.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  To &quot;convey&quot; a work means any kind of propagation that enables other</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">parties to make or receive copies.  Mere interaction with a user through</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a computer network, with no transfer of a copy, is not conveying.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  An interactive user interface displays &quot;Appropriate Legal Notices&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">to the extent that it includes a convenient and prominently visible</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">feature that (1) displays an appropriate copyright notice, and (2)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">tells the user that there is no warranty for the work (except to the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">extent that warranties are provided), that licensees may convey the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">work under this License, and how to view a copy of this License.  If</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the interface presents a list of user commands or options, such as a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">menu, a prominent item in the list meets this criterion.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  1. Source Code.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The &quot;source code&quot; for a work means the preferred form of the work</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">for making modifications to it.  &quot;Object code&quot; means any non-source</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">form of a work.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  A &quot;Standard Interface&quot; means an interface that either is an official</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">standard defined by a recognized standards body, or, in the case of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">interfaces specified for a particular programming language, one that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">is widely used among developers working in that language.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The &quot;System Libraries&quot; of an executable work include anything, other</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">than the work as a whole, that (a) is included in the normal form of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">packaging a Major Component, but which is not part of that Major</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Component, and (b) serves only to enable use of the work with that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Major Component, or to implement a Standard Interface for which an</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">implementation is available to the public in source code form.  A</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&quot;Major Component&quot;, in this context, means a major essential component</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(kernel, window system, and so on) of the specific operating system</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(if any) on which the executable work runs, or a compiler used to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">produce the work, or an object code interpreter used to run it.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The &quot;Corresponding Source&quot; for a work in object code form means all</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the source code needed to generate, install, and (for an executable</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">work) run the object code and to modify the work, including scripts to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">control those activities.  However, it does not include the work\'s</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">System Libraries, or general-purpose tools or generally available free</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">programs which are used unmodified in performing those activities but</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">which are not part of the work.  For example, Corresponding Source</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">includes interface definition files associated with source files for</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the work, and the source code for shared libraries and dynamically</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">linked subprograms that the work is specifically designed to require,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">such as by intimate data communication or control flow between those</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">subprograms and other parts of the work.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The Corresponding Source need not include anything that users</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">can regenerate automatically from other parts of the Corresponding</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Source.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The Corresponding Source for a work in source code form is that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">same work.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  2. Basic Permissions.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  All rights granted under this License are granted for the term of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">copyright on the Program, and are irrevocable provided the stated</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">conditions are met.  This License explicitly affirms your unlimited</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">permission to run the unmodified Program.  The output from running a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">covered work is covered by this License only if the output, given its</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">content, constitutes a covered work.  This License acknowledges your</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">rights of fair use or other equivalent, as provided by copyright law.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You may make, run and propagate covered works that you do not</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">convey, without conditions so long as your license otherwise remains</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in force.  You may convey covered works to others for the sole purpose</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">of having them make modifications exclusively for you, or provide you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">with facilities for running those works, provided that you comply with</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the terms of this License in conveying all material for which you do</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">not control copyright.  Those thus making or running the covered works</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">for you must do so exclusively on your behalf, under your direction</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">and control, on terms that prohibit them from making any copies of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">your copyrighted material outside their relationship with you.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Conveying under any other circumstances is permitted solely under</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the conditions stated below.  Sublicensing is not allowed; section 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">makes it unnecessary.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  3. Protecting Users\' Legal Rights From Anti-Circumvention Law.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  No covered work shall be deemed part of an effective technological</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">measure under any applicable law fulfilling obligations under article</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 of the WIPO copyright treaty adopted on 20 December 1996, or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">similar laws prohibiting or restricting circumvention of such</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">measures.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  When you convey a covered work, you waive any legal power to forbid</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">circumvention of technological measures to the extent such circumvention</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">is effected by exercising rights under this License with respect to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the covered work, and you disclaim any intention to limit operation or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">modification of the work as a means of enforcing, against the work\'s</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">users, your or third parties\' legal rights to forbid circumvention of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">technological measures.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  4. Conveying Verbatim Copies.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You may convey verbatim copies of the Program\'s source code as you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">receive it, in any medium, provided that you conspicuously and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">appropriately publish on each copy an appropriate copyright notice;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">keep intact all notices stating that this License and any</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">non-permissive terms added in accord with section 7 apply to the code;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">keep intact all notices of the absence of any warranty; and give all</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">recipients a copy of this License along with the Program.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You may charge any price or no price for each copy that you convey,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">and you may offer support or warranty protection for a fee.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  5. Conveying Modified Source Versions.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You may convey a work based on the Program, or the modifications to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">produce it from the Program, in the form of source code under the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">terms of section 4, provided that you also meet all of these conditions:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    a) The work must carry prominent notices stating that you modified</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    it, and giving a relevant date.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    b) The work must carry prominent notices stating that it is</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    released under this License and any conditions added under section</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    7.  This requirement modifies the requirement in section 4 to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &quot;keep intact all notices&quot;.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    c) You must license the entire work, as a whole, under this</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    License to anyone who comes into possession of a copy.  This</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    License will therefore apply, along with any applicable section 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    additional terms, to the whole of the work, and all its parts,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    regardless of how they are packaged.  This License gives no</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    permission to license the work in any other way, but it does not</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    invalidate such permission if you have separately received it.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    d) If the work has interactive user interfaces, each must display</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Appropriate Legal Notices; however, if the Program has interactive</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    interfaces that do not display Appropriate Legal Notices, your</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    work need not make them do so.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  A compilation of a covered work with other separate and independent</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">works, which are not by their nature extensions of the covered work,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">and which are not combined with it such as to form a larger program,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in or on a volume of a storage or distribution medium, is called an</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&quot;aggregate&quot; if the compilation and its resulting copyright are not</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">used to limit the access or legal rights of the compilation\'s users</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">beyond what the individual works permit.  Inclusion of a covered work</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in an aggregate does not cause this License to apply to the other</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">parts of the aggregate.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  6. Conveying Non-Source Forms.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You may convey a covered work in object code form under the terms</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">of sections 4 and 5, provided that you also convey the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">machine-readable Corresponding Source under the terms of this License,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in one of these ways:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    a) Convey the object code in, or embodied in, a physical product</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    (including a physical distribution medium), accompanied by the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Corresponding Source fixed on a durable physical medium</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    customarily used for software interchange.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    b) Convey the object code in, or embodied in, a physical product</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    (including a physical distribution medium), accompanied by a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    written offer, valid for at least three years and valid for as</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    long as you offer spare parts or customer support for that product</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    model, to give anyone who possesses the object code either (1) a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    copy of the Corresponding Source for all the software in the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    product that is covered by this License, on a durable physical</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    medium customarily used for software interchange, for a price no</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    more than your reasonable cost of physically performing this</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    conveying of source, or (2) access to copy the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Corresponding Source from a network server at no charge.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    c) Convey individual copies of the object code with a copy of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    written offer to provide the Corresponding Source.  This</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    alternative is allowed only occasionally and noncommercially, and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    only if you received the object code with such an offer, in accord</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    with subsection 6b.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    d) Convey the object code by offering access from a designated</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    place (gratis or for a charge), and offer equivalent access to the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Corresponding Source in the same way through the same place at no</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    further charge.  You need not require recipients to copy the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Corresponding Source along with the object code.  If the place to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    copy the object code is a network server, the Corresponding Source</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    may be on a different server (operated by you or a third party)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    that supports equivalent copying facilities, provided you maintain</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    clear directions next to the object code saying where to find the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Corresponding Source.  Regardless of what server hosts the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Corresponding Source, you remain obligated to ensure that it is</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    available for as long as needed to satisfy these requirements.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    e) Convey the object code using peer-to-peer transmission, provided</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    you inform other peers where the object code and Corresponding</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Source of the work are being offered to the general public at no</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    charge under subsection 6d.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  A separable portion of the object code, whose source code is excluded</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">from the Corresponding Source as a System Library, need not be</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">included in conveying the object code work.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  A &quot;User Product&quot; is either (1) a &quot;consumer product&quot;, which means any</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">tangible personal property which is normally used for personal, family,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">or household purposes, or (2) anything designed or sold for incorporation</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">into a dwelling.  In determining whether a product is a consumer product,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">doubtful cases shall be resolved in favor of coverage.  For a particular</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">product received by a particular user, &quot;normally used&quot; refers to a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">typical or common use of that class of product, regardless of the status</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">of the particular user or of the way in which the particular user</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">actually uses, or expects or is expected to use, the product.  A product</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">is a consumer product regardless of whether the product has substantial</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">commercial, industrial or non-consumer uses, unless such uses represent</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the only significant mode of use of the product.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  &quot;Installation Information&quot; for a User Product means any methods,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">procedures, authorization keys, or other information required to install</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">and execute modified versions of a covered work in that User Product from</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a modified version of its Corresponding Source.  The information must</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">suffice to ensure that the continued functioning of the modified object</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">code is in no case prevented or interfered with solely because</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">modification has been made.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  If you convey an object code work under this section in, or with, or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">specifically for use in, a User Product, and the conveying occurs as</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">part of a transaction in which the right of possession and use of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">User Product is transferred to the recipient in perpetuity or for a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">fixed term (regardless of how the transaction is characterized), the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Corresponding Source conveyed under this section must be accompanied</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">by the Installation Information.  But this requirement does not apply</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">if neither you nor any third party retains the ability to install</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">modified object code on the User Product (for example, the work has</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">been installed in ROM).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The requirement to provide Installation Information does not include a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">requirement to continue to provide support service, warranty, or updates</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">for a work that has been modified or installed by the recipient, or for</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the User Product in which it has been modified or installed.  Access to a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">network may be denied when the modification itself materially and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">adversely affects the operation of the network or violates the rules and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">protocols for communication across the network.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Corresponding Source conveyed, and Installation Information provided,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in accord with this section must be in a format that is publicly</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">documented (and with an implementation available to the public in</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">source code form), and must require no special password or key for</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">unpacking, reading or copying.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  7. Additional Terms.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  &quot;Additional permissions&quot; are terms that supplement the terms of this</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License by making exceptions from one or more of its conditions.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Additional permissions that are applicable to the entire Program shall</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">be treated as though they were included in this License, to the extent</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">that they are valid under applicable law.  If additional permissions</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">apply only to part of the Program, that part may be used separately</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">under those permissions, but the entire Program remains governed by</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">this License without regard to the additional permissions.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  When you convey a copy of a covered work, you may at your option</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">remove any additional permissions from that copy, or from any part of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">it.  (Additional permissions may be written to require their own</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">removal in certain cases when you modify the work.)  You may place</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">additional permissions on material, added by you to a covered work,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">for which you have or can give appropriate copyright permission.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Notwithstanding any other provision of this License, for material you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">add to a covered work, you may (if authorized by the copyright holders of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">that material) supplement the terms of this License with terms:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    a) Disclaiming warranty or limiting liability differently from the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    terms of sections 15 and 16 of this License; or</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    b) Requiring preservation of specified reasonable legal notices or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    author attributions in that material or in the Appropriate Legal</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Notices displayed by works containing it; or</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    c) Prohibiting misrepresentation of the origin of that material, or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    requiring that modified versions of such material be marked in</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    reasonable ways as different from the original version; or</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    d) Limiting the use for publicity purposes of names of licensors or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    authors of the material; or</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    e) Declining to grant rights under trademark law for use of some</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    trade names, trademarks, or service marks; or</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    f) Requiring indemnification of licensors and authors of that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    material by anyone who conveys the material (or modified versions of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    it) with contractual assumptions of liability to the recipient, for</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    any liability that these contractual assumptions directly impose on</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    those licensors and authors.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  All other non-permissive additional terms are considered &quot;further</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">restrictions&quot; within the meaning of section 10.  If the Program as you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">received it, or any part of it, contains a notice stating that it is</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">governed by this License along with a term that is a further</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">restriction, you may remove that term.  If a license document contains</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a further restriction but permits relicensing or conveying under this</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License, you may add to a covered work material governed by the terms</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">of that license document, provided that the further restriction does</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">not survive such relicensing or conveying.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  If you add terms to a covered work in accord with this section, you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">must place, in the relevant source files, a statement of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">additional terms that apply to those files, or a notice indicating</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">where to find the applicable terms.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Additional terms, permissive or non-permissive, may be stated in the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">form of a separately written license, or stated as exceptions;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the above requirements apply either way.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  8. Termination.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You may not propagate or modify a covered work except as expressly</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">provided under this License.  Any attempt otherwise to propagate or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">modify it is void, and will automatically terminate your rights under</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">this License (including any patent licenses granted under the third</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">paragraph of section 11).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  However, if you cease all violation of this License, then your</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">license from a particular copyright holder is reinstated (a)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">provisionally, unless and until the copyright holder explicitly and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">finally terminates your license, and (b) permanently, if the copyright</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">holder fails to notify you of the violation by some reasonable means</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">prior to 60 days after the cessation.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Moreover, your license from a particular copyright holder is</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">reinstated permanently if the copyright holder notifies you of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">violation by some reasonable means, this is the first time you have</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">received notice of violation of this License (for any work) from that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">copyright holder, and you cure the violation prior to 30 days after</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">your receipt of the notice.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Termination of your rights under this section does not terminate the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">licenses of parties who have received copies or rights from you under</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">this License.  If your rights have been terminated and not permanently</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">reinstated, you do not qualify to receive new licenses for the same</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">material under section 10.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  9. Acceptance Not Required for Having Copies.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You are not required to accept this License in order to receive or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">run a copy of the Program.  Ancillary propagation of a covered work</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">occurring solely as a consequence of using peer-to-peer transmission</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">to receive a copy likewise does not require acceptance.  However,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">nothing other than this License grants you permission to propagate or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">modify any covered work.  These actions infringe copyright if you do</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">not accept this License.  Therefore, by modifying or propagating a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">covered work, you indicate your acceptance of this License to do so.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  10. Automatic Licensing of Downstream Recipients.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Each time you convey a covered work, the recipient automatically</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">receives a license from the original licensors, to run, modify and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">propagate that work, subject to this License.  You are not responsible</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">for enforcing compliance by third parties with this License.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  An &quot;entity transaction&quot; is a transaction transferring control of an</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">organization, or substantially all assets of one, or subdividing an</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">organization, or merging organizations.  If propagation of a covered</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">work results from an entity transaction, each party to that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">transaction who receives a copy of the work also receives whatever</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">licenses to the work the party\'s predecessor in interest had or could</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">give under the previous paragraph, plus a right to possession of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Corresponding Source of the work from the predecessor in interest, if</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the predecessor has it or can get it with reasonable efforts.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You may not impose any further restrictions on the exercise of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">rights granted or affirmed under this License.  For example, you may</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">not impose a license fee, royalty, or other charge for exercise of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">rights granted under this License, and you may not initiate litigation</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(including a cross-claim or counterclaim in a lawsuit) alleging that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">any patent claim is infringed by making, using, selling, offering for</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sale, or importing the Program or any portion of it.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  11. Patents.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  A &quot;contributor&quot; is a copyright holder who authorizes use under this</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License of the Program or a work on which the Program is based.  The</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">work thus licensed is called the contributor\'s &quot;contributor version&quot;.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  A contributor\'s &quot;essential patent claims&quot; are all patent claims</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">owned or controlled by the contributor, whether already acquired or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">hereafter acquired, that would be infringed by some manner, permitted</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">by this License, of making, using, or selling its contributor version,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">but do not include claims that would be infringed only as a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">consequence of further modification of the contributor version.  For</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">purposes of this definition, &quot;control&quot; includes the right to grant</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">patent sublicenses in a manner consistent with the requirements of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">this License.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Each contributor grants you a non-exclusive, worldwide, royalty-free</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">patent license under the contributor\'s essential patent claims, to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">make, use, sell, offer for sale, import and otherwise run, modify and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">propagate the contents of its contributor version.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  In the following three paragraphs, a &quot;patent license&quot; is any express</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">agreement or commitment, however denominated, not to enforce a patent</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(such as an express permission to practice a patent or covenant not to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sue for patent infringement).  To &quot;grant&quot; such a patent license to a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">party means to make such an agreement or commitment not to enforce a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">patent against the party.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  If you convey a covered work, knowingly relying on a patent license,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">and the Corresponding Source of the work is not available for anyone</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">to copy, free of charge and under the terms of this License, through a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">publicly available network server or other readily accessible means,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">then you must either (1) cause the Corresponding Source to be so</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">available, or (2) arrange to deprive yourself of the benefit of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">patent license for this particular work, or (3) arrange, in a manner</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">consistent with the requirements of this License, to extend the patent</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">license to downstream recipients.  &quot;Knowingly relying&quot; means you have</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">actual knowledge that, but for the patent license, your conveying the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">covered work in a country, or your recipient\'s use of the covered work</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in a country, would infringe one or more identifiable patents in that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">country that you have reason to believe are valid.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  If, pursuant to or in connection with a single transaction or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">arrangement, you convey, or propagate by procuring conveyance of, a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">covered work, and grant a patent license to some of the parties</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">receiving the covered work authorizing them to use, propagate, modify</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">or convey a specific copy of the covered work, then the patent license</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">you grant is automatically extended to all recipients of the covered</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">work and works based on it.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  A patent license is &quot;discriminatory&quot; if it does not include within</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the scope of its coverage, prohibits the exercise of, or is</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">conditioned on the non-exercise of one or more of the rights that are</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">specifically granted under this License.  You may not convey a covered</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">work if you are a party to an arrangement with a third party that is</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in the business of distributing software, under which you make payment</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">to the third party based on the extent of your activity of conveying</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the work, and under which the third party grants, to any of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">parties who would receive the covered work from you, a discriminatory</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">patent license (a) in connection with copies of the covered work</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">conveyed by you (or copies made from those copies), or (b) primarily</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">for and in connection with specific products or compilations that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">contain the covered work, unless you entered into that arrangement,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">or that patent license was granted, prior to 28 March 2007.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Nothing in this License shall be construed as excluding or limiting</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">any implied license or other defenses to infringement that may</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">otherwise be available to you under applicable patent law.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  12. No Surrender of Others\' Freedom.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  If conditions are imposed on you (whether by court order, agreement or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">otherwise) that contradict the conditions of this License, they do not</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">excuse you from the conditions of this License.  If you cannot convey a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">covered work so as to satisfy simultaneously your obligations under this</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License and any other pertinent obligations, then as a consequence you may</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">not convey it at all.  For example, if you agree to terms that obligate you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">to collect a royalty for further conveying from those to whom you convey</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the Program, the only way you could satisfy both those terms and this</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License would be to refrain entirely from conveying the Program.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  13. Use with the GNU Affero General Public License.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Notwithstanding any other provision of this License, you have</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">permission to link or combine any covered work with a work licensed</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">under version 3 of the GNU Affero General Public License into a single</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">combined work, and to convey the resulting work.  The terms of this</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License will continue to apply to the part which is the covered work,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">but the special requirements of the GNU Affero General Public License,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">section 13, concerning interaction through a network will apply to the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">combination as such.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  14. Revised Versions of this License.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The Free Software Foundation may publish revised and/or new versions of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the GNU General Public License from time to time.  Such new versions will</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">be similar in spirit to the present version, but may differ in detail to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">address new problems or concerns.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Each version is given a distinguishing version number.  If the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Program specifies that a certain numbered version of the GNU General</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Public License &quot;or any later version&quot; applies to it, you have the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">option of following the terms and conditions either of that numbered</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">version or of any later version published by the Free Software</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Foundation.  If the Program does not specify a version number of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GNU General Public License, you may choose any version ever published</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">by the Free Software Foundation.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  If the Program specifies that a proxy can decide which future</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">versions of the GNU General Public License can be used, that proxy\'s</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">public statement of acceptance of a version permanently authorizes you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">to choose that version for the Program.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Later license versions may give you additional or different</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">permissions.  However, no additional obligations are imposed on any</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">author or copyright holder as a result of your choosing to follow a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">later version.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  15. Disclaimer of Warranty.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM &quot;AS IS&quot; WITHOUT WARRANTY</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ALL NECESSARY SERVICING, REPAIR OR CORRECTION.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  16. Limitation of Liability.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SUCH DAMAGES.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  17. Interpretation of Sections 15 and 16.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  If the disclaimer of warranty and limitation of liability provided</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">above cannot be given local legal effect according to their terms,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">reviewing courts shall apply local law that most closely approximates</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">an absolute waiver of all civil liability in connection with the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Program, unless a warranty or assumption of liability accompanies a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">copy of the Program in return for a fee.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                     END OF TERMS AND CONDITIONS</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            How to Apply These Terms to Your New Programs</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  If you develop a new program, and you want it to be of the greatest</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">possible use to the public, the best way to achieve this is to make it</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">free software which everyone can redistribute and change under these terms.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  To do so, attach the following notices to the program.  It is safest</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">to attach them to the start of each source file to most effectively</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">state the exclusion of warranty; and each file should have at least</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the &quot;copyright&quot; line and a pointer to where the full notice is found.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;one line to give the program\'s name and a brief idea of what it does.&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Copyright (C) &lt;year&gt;  &lt;name of author&gt;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    This program is free software: you can redistribute it and/or modify</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    it under the terms of the GNU General Public License as published by</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    the Free Software Foundation, either version 3 of the License, or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    (at your option) any later version.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    This program is distributed in the hope that it will be useful,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    but WITHOUT ANY WARRANTY; without even the implied warranty of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    GNU General Public License for more details.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    You should have received a copy of the GNU General Public License</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    along with this program.  If not, see &lt;http://www.gnu.org/licenses/&gt;.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Also add information on how to contact you by electronic and paper mail.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  If the program does terminal interaction, make it output a short</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">notice like this when it starts in an interactive mode:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;program&gt;  Copyright (C) &lt;year&gt;  &lt;name of author&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w\'.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    This is free software, and you are welcome to redistribute it</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    under certain conditions; type `show c\' for details.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The hypothetical commands `show w\' and `show c\' should show the appropriate</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">parts of the General Public License.  Of course, your program\'s commands</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">might be different; for a GUI interface, you would use an &quot;about box&quot;.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You should also get your employer (if you work as a programmer) or school,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">if any, to sign a &quot;copyright disclaimer&quot; for the program, if necessary.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For more information on this, and how to apply and follow the GNU GPL, see</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;http://www.gnu.org/licenses/&gt;.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The GNU General Public License does not permit incorporating your program</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">into proprietary programs.  If your program is a subroutine library, you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">may consider it more useful to permit linking proprietary applications with</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the library.  If this is what you want to do, use the GNU Lesser General</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Public License instead of this License.  But first, please read</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;http://www.gnu.org/philosophy/why-not-lgpl.html&gt;.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">SocialReaper</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:20pt; font-weight:600;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copyright 2016 Adam Smith</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the &quot;Software&quot;), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions: </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software. </p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">THE SOFTWARE IS PROVIDED &quot;AS IS&quot;, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">PyQt</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                    GNU GENERAL PUBLIC LICENSE</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                       Version 3, 29 June 2007</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Copyright (C) 2007 Free Software Foundation, Inc. &lt;http://fsf.org/&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> Everyone is permitted to copy and distribute verbatim copies</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> of this license document, but changing it is not allowed.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                            Preamble</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The GNU General Public License is a free, copyleft license for</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">software and other kinds of works.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The licenses for most software and other practical works are designed</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">to take away your freedom to share and change the works.  By contrast,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the GNU General Public License is intended to guarantee your freedom to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">share and change all versions of a program--to make sure it remains free</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">software for all its users.  We, the Free Software Foundation, use the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GNU General Public License for most of our software; it applies also to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">any other work released this way by its authors.  You can apply it to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">your programs, too.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  When we speak of free software, we are referring to freedom, not</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">price.  Our General Public Licenses are designed to make sure that you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">have the freedom to distribute copies of free software (and charge for</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">them if you wish), that you receive source code or can get it if you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">want it, that you can change the software or use pieces of it in new</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">free programs, and that you know you can do these things.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  To protect your rights, we need to prevent others from denying you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">these rights or asking you to surrender the rights.  Therefore, you have</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">certain responsibilities if you distribute copies of the software, or if</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">you modify it: responsibilities to respect the freedom of others.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  For example, if you distribute copies of such a program, whether</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gratis or for a fee, you must pass on to the recipients the same</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">freedoms that you received.  You must make sure that they, too, receive</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">or can get the source code.  And you must show them these terms so they</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">know their rights.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Developers that use the GNU GPL protect your rights with two steps:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(1) assert copyright on the software, and (2) offer you this License</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">giving you legal permission to copy, distribute and/or modify it.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  For the developers\' and authors\' protection, the GPL clearly explains</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">that there is no warranty for this free software.  For both users\' and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">authors\' sake, the GPL requires that modified versions be marked as</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">changed, so that their problems will not be attributed erroneously to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">authors of previous versions.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Some devices are designed to deny users access to install or run</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">modified versions of the software inside them, although the manufacturer</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">can do so.  This is fundamentally incompatible with the aim of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">protecting users\' freedom to change the software.  The systematic</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">pattern of such abuse occurs in the area of products for individuals to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">use, which is precisely where it is most unacceptable.  Therefore, we</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">have designed this version of the GPL to prohibit the practice for those</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">products.  If such problems arise substantially in other domains, we</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">stand ready to extend this provision to those domains in future versions</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">of the GPL, as needed to protect the freedom of users.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Finally, every program is threatened constantly by software patents.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">States should not allow patents to restrict development and use of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">software on general-purpose computers, but in those that do, we wish to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">avoid the special danger that patents applied to a free program could</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">make it effectively proprietary.  To prevent this, the GPL assures that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">patents cannot be used to render the program non-free.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The precise terms and conditions for copying, distribution and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">modification follow.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                       TERMS AND CONDITIONS</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  0. Definitions.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  &quot;This License&quot; refers to version 3 of the GNU General Public License.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  &quot;Copyright&quot; also means copyright-like laws that apply to other kinds of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">works, such as semiconductor masks.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  &quot;The Program&quot; refers to any copyrightable work licensed under this</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License.  Each licensee is addressed as &quot;you&quot;.  &quot;Licensees&quot; and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&quot;recipients&quot; may be individuals or organizations.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  To &quot;modify&quot; a work means to copy from or adapt all or part of the work</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in a fashion requiring copyright permission, other than the making of an</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">exact copy.  The resulting work is called a &quot;modified version&quot; of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">earlier work or a work &quot;based on&quot; the earlier work.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  A &quot;covered work&quot; means either the unmodified Program or a work based</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">on the Program.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  To &quot;propagate&quot; a work means to do anything with it that, without</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">permission, would make you directly or secondarily liable for</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">infringement under applicable copyright law, except executing it on a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">computer or modifying a private copy.  Propagation includes copying,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">distribution (with or without modification), making available to the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">public, and in some countries other activities as well.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  To &quot;convey&quot; a work means any kind of propagation that enables other</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">parties to make or receive copies.  Mere interaction with a user through</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a computer network, with no transfer of a copy, is not conveying.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  An interactive user interface displays &quot;Appropriate Legal Notices&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">to the extent that it includes a convenient and prominently visible</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">feature that (1) displays an appropriate copyright notice, and (2)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">tells the user that there is no warranty for the work (except to the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">extent that warranties are provided), that licensees may convey the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">work under this License, and how to view a copy of this License.  If</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the interface presents a list of user commands or options, such as a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">menu, a prominent item in the list meets this criterion.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  1. Source Code.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The &quot;source code&quot; for a work means the preferred form of the work</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">for making modifications to it.  &quot;Object code&quot; means any non-source</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">form of a work.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  A &quot;Standard Interface&quot; means an interface that either is an official</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">standard defined by a recognized standards body, or, in the case of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">interfaces specified for a particular programming language, one that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">is widely used among developers working in that language.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The &quot;System Libraries&quot; of an executable work include anything, other</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">than the work as a whole, that (a) is included in the normal form of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">packaging a Major Component, but which is not part of that Major</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Component, and (b) serves only to enable use of the work with that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Major Component, or to implement a Standard Interface for which an</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">implementation is available to the public in source code form.  A</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&quot;Major Component&quot;, in this context, means a major essential component</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(kernel, window system, and so on) of the specific operating system</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(if any) on which the executable work runs, or a compiler used to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">produce the work, or an object code interpreter used to run it.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The &quot;Corresponding Source&quot; for a work in object code form means all</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the source code needed to generate, install, and (for an executable</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">work) run the object code and to modify the work, including scripts to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">control those activities.  However, it does not include the work\'s</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">System Libraries, or general-purpose tools or generally available free</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">programs which are used unmodified in performing those activities but</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">which are not part of the work.  For example, Corresponding Source</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">includes interface definition files associated with source files for</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the work, and the source code for shared libraries and dynamically</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">linked subprograms that the work is specifically designed to require,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">such as by intimate data communication or control flow between those</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">subprograms and other parts of the work.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The Corresponding Source need not include anything that users</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">can regenerate automatically from other parts of the Corresponding</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Source.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The Corresponding Source for a work in source code form is that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">same work.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  2. Basic Permissions.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  All rights granted under this License are granted for the term of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">copyright on the Program, and are irrevocable provided the stated</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">conditions are met.  This License explicitly affirms your unlimited</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">permission to run the unmodified Program.  The output from running a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">covered work is covered by this License only if the output, given its</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">content, constitutes a covered work.  This License acknowledges your</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">rights of fair use or other equivalent, as provided by copyright law.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You may make, run and propagate covered works that you do not</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">convey, without conditions so long as your license otherwise remains</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in force.  You may convey covered works to others for the sole purpose</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">of having them make modifications exclusively for you, or provide you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">with facilities for running those works, provided that you comply with</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the terms of this License in conveying all material for which you do</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">not control copyright.  Those thus making or running the covered works</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">for you must do so exclusively on your behalf, under your direction</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">and control, on terms that prohibit them from making any copies of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">your copyrighted material outside their relationship with you.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Conveying under any other circumstances is permitted solely under</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the conditions stated below.  Sublicensing is not allowed; section 10</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">makes it unnecessary.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  3. Protecting Users\' Legal Rights From Anti-Circumvention Law.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  No covered work shall be deemed part of an effective technological</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">measure under any applicable law fulfilling obligations under article</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">11 of the WIPO copyright treaty adopted on 20 December 1996, or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">similar laws prohibiting or restricting circumvention of such</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">measures.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  When you convey a covered work, you waive any legal power to forbid</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">circumvention of technological measures to the extent such circumvention</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">is effected by exercising rights under this License with respect to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the covered work, and you disclaim any intention to limit operation or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">modification of the work as a means of enforcing, against the work\'s</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">users, your or third parties\' legal rights to forbid circumvention of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">technological measures.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  4. Conveying Verbatim Copies.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You may convey verbatim copies of the Program\'s source code as you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">receive it, in any medium, provided that you conspicuously and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">appropriately publish on each copy an appropriate copyright notice;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">keep intact all notices stating that this License and any</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">non-permissive terms added in accord with section 7 apply to the code;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">keep intact all notices of the absence of any warranty; and give all</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">recipients a copy of this License along with the Program.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You may charge any price or no price for each copy that you convey,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">and you may offer support or warranty protection for a fee.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  5. Conveying Modified Source Versions.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You may convey a work based on the Program, or the modifications to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">produce it from the Program, in the form of source code under the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">terms of section 4, provided that you also meet all of these conditions:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    a) The work must carry prominent notices stating that you modified</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    it, and giving a relevant date.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    b) The work must carry prominent notices stating that it is</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    released under this License and any conditions added under section</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    7.  This requirement modifies the requirement in section 4 to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &quot;keep intact all notices&quot;.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    c) You must license the entire work, as a whole, under this</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    License to anyone who comes into possession of a copy.  This</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    License will therefore apply, along with any applicable section 7</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    additional terms, to the whole of the work, and all its parts,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    regardless of how they are packaged.  This License gives no</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    permission to license the work in any other way, but it does not</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    invalidate such permission if you have separately received it.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    d) If the work has interactive user interfaces, each must display</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Appropriate Legal Notices; however, if the Program has interactive</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    interfaces that do not display Appropriate Legal Notices, your</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    work need not make them do so.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  A compilation of a covered work with other separate and independent</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">works, which are not by their nature extensions of the covered work,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">and which are not combined with it such as to form a larger program,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in or on a volume of a storage or distribution medium, is called an</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&quot;aggregate&quot; if the compilation and its resulting copyright are not</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">used to limit the access or legal rights of the compilation\'s users</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">beyond what the individual works permit.  Inclusion of a covered work</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in an aggregate does not cause this License to apply to the other</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">parts of the aggregate.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  6. Conveying Non-Source Forms.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You may convey a covered work in object code form under the terms</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">of sections 4 and 5, provided that you also convey the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">machine-readable Corresponding Source under the terms of this License,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in one of these ways:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    a) Convey the object code in, or embodied in, a physical product</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    (including a physical distribution medium), accompanied by the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Corresponding Source fixed on a durable physical medium</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    customarily used for software interchange.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    b) Convey the object code in, or embodied in, a physical product</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    (including a physical distribution medium), accompanied by a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    written offer, valid for at least three years and valid for as</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    long as you offer spare parts or customer support for that product</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    model, to give anyone who possesses the object code either (1) a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    copy of the Corresponding Source for all the software in the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    product that is covered by this License, on a durable physical</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    medium customarily used for software interchange, for a price no</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    more than your reasonable cost of physically performing this</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    conveying of source, or (2) access to copy the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Corresponding Source from a network server at no charge.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    c) Convey individual copies of the object code with a copy of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    written offer to provide the Corresponding Source.  This</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    alternative is allowed only occasionally and noncommercially, and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    only if you received the object code with such an offer, in accord</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    with subsection 6b.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    d) Convey the object code by offering access from a designated</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    place (gratis or for a charge), and offer equivalent access to the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Corresponding Source in the same way through the same place at no</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    further charge.  You need not require recipients to copy the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Corresponding Source along with the object code.  If the place to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    copy the object code is a network server, the Corresponding Source</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    may be on a different server (operated by you or a third party)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    that supports equivalent copying facilities, provided you maintain</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    clear directions next to the object code saying where to find the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Corresponding Source.  Regardless of what server hosts the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Corresponding Source, you remain obligated to ensure that it is</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    available for as long as needed to satisfy these requirements.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    e) Convey the object code using peer-to-peer transmission, provided</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    you inform other peers where the object code and Corresponding</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Source of the work are being offered to the general public at no</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    charge under subsection 6d.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  A separable portion of the object code, whose source code is excluded</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">from the Corresponding Source as a System Library, need not be</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">included in conveying the object code work.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  A &quot;User Product&quot; is either (1) a &quot;consumer product&quot;, which means any</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">tangible personal property which is normally used for personal, family,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">or household purposes, or (2) anything designed or sold for incorporation</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">into a dwelling.  In determining whether a product is a consumer product,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">doubtful cases shall be resolved in favor of coverage.  For a particular</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">product received by a particular user, &quot;normally used&quot; refers to a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">typical or common use of that class of product, regardless of the status</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">of the particular user or of the way in which the particular user</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">actually uses, or expects or is expected to use, the product.  A product</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">is a consumer product regardless of whether the product has substantial</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">commercial, industrial or non-consumer uses, unless such uses represent</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the only significant mode of use of the product.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  &quot;Installation Information&quot; for a User Product means any methods,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">procedures, authorization keys, or other information required to install</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">and execute modified versions of a covered work in that User Product from</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a modified version of its Corresponding Source.  The information must</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">suffice to ensure that the continued functioning of the modified object</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">code is in no case prevented or interfered with solely because</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">modification has been made.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  If you convey an object code work under this section in, or with, or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">specifically for use in, a User Product, and the conveying occurs as</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">part of a transaction in which the right of possession and use of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">User Product is transferred to the recipient in perpetuity or for a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">fixed term (regardless of how the transaction is characterized), the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Corresponding Source conveyed under this section must be accompanied</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">by the Installation Information.  But this requirement does not apply</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">if neither you nor any third party retains the ability to install</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">modified object code on the User Product (for example, the work has</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">been installed in ROM).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The requirement to provide Installation Information does not include a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">requirement to continue to provide support service, warranty, or updates</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">for a work that has been modified or installed by the recipient, or for</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the User Product in which it has been modified or installed.  Access to a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">network may be denied when the modification itself materially and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">adversely affects the operation of the network or violates the rules and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">protocols for communication across the network.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Corresponding Source conveyed, and Installation Information provided,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in accord with this section must be in a format that is publicly</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">documented (and with an implementation available to the public in</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">source code form), and must require no special password or key for</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">unpacking, reading or copying.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  7. Additional Terms.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  &quot;Additional permissions&quot; are terms that supplement the terms of this</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License by making exceptions from one or more of its conditions.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Additional permissions that are applicable to the entire Program shall</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">be treated as though they were included in this License, to the extent</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">that they are valid under applicable law.  If additional permissions</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">apply only to part of the Program, that part may be used separately</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">under those permissions, but the entire Program remains governed by</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">this License without regard to the additional permissions.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  When you convey a copy of a covered work, you may at your option</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">remove any additional permissions from that copy, or from any part of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">it.  (Additional permissions may be written to require their own</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">removal in certain cases when you modify the work.)  You may place</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">additional permissions on material, added by you to a covered work,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">for which you have or can give appropriate copyright permission.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Notwithstanding any other provision of this License, for material you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">add to a covered work, you may (if authorized by the copyright holders of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">that material) supplement the terms of this License with terms:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    a) Disclaiming warranty or limiting liability differently from the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    terms of sections 15 and 16 of this License; or</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    b) Requiring preservation of specified reasonable legal notices or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    author attributions in that material or in the Appropriate Legal</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Notices displayed by works containing it; or</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    c) Prohibiting misrepresentation of the origin of that material, or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    requiring that modified versions of such material be marked in</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    reasonable ways as different from the original version; or</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    d) Limiting the use for publicity purposes of names of licensors or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    authors of the material; or</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    e) Declining to grant rights under trademark law for use of some</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    trade names, trademarks, or service marks; or</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    f) Requiring indemnification of licensors and authors of that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    material by anyone who conveys the material (or modified versions of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    it) with contractual assumptions of liability to the recipient, for</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    any liability that these contractual assumptions directly impose on</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    those licensors and authors.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  All other non-permissive additional terms are considered &quot;further</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">restrictions&quot; within the meaning of section 10.  If the Program as you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">received it, or any part of it, contains a notice stating that it is</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">governed by this License along with a term that is a further</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">restriction, you may remove that term.  If a license document contains</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">a further restriction but permits relicensing or conveying under this</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License, you may add to a covered work material governed by the terms</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">of that license document, provided that the further restriction does</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">not survive such relicensing or conveying.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  If you add terms to a covered work in accord with this section, you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">must place, in the relevant source files, a statement of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">additional terms that apply to those files, or a notice indicating</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">where to find the applicable terms.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Additional terms, permissive or non-permissive, may be stated in the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">form of a separately written license, or stated as exceptions;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the above requirements apply either way.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  8. Termination.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You may not propagate or modify a covered work except as expressly</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">provided under this License.  Any attempt otherwise to propagate or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">modify it is void, and will automatically terminate your rights under</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">this License (including any patent licenses granted under the third</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">paragraph of section 11).</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  However, if you cease all violation of this License, then your</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">license from a particular copyright holder is reinstated (a)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">provisionally, unless and until the copyright holder explicitly and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">finally terminates your license, and (b) permanently, if the copyright</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">holder fails to notify you of the violation by some reasonable means</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">prior to 60 days after the cessation.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Moreover, your license from a particular copyright holder is</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">reinstated permanently if the copyright holder notifies you of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">violation by some reasonable means, this is the first time you have</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">received notice of violation of this License (for any work) from that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">copyright holder, and you cure the violation prior to 30 days after</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">your receipt of the notice.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Termination of your rights under this section does not terminate the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">licenses of parties who have received copies or rights from you under</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">this License.  If your rights have been terminated and not permanently</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">reinstated, you do not qualify to receive new licenses for the same</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">material under section 10.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  9. Acceptance Not Required for Having Copies.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You are not required to accept this License in order to receive or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">run a copy of the Program.  Ancillary propagation of a covered work</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">occurring solely as a consequence of using peer-to-peer transmission</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">to receive a copy likewise does not require acceptance.  However,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">nothing other than this License grants you permission to propagate or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">modify any covered work.  These actions infringe copyright if you do</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">not accept this License.  Therefore, by modifying or propagating a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">covered work, you indicate your acceptance of this License to do so.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  10. Automatic Licensing of Downstream Recipients.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Each time you convey a covered work, the recipient automatically</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">receives a license from the original licensors, to run, modify and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">propagate that work, subject to this License.  You are not responsible</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">for enforcing compliance by third parties with this License.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  An &quot;entity transaction&quot; is a transaction transferring control of an</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">organization, or substantially all assets of one, or subdividing an</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">organization, or merging organizations.  If propagation of a covered</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">work results from an entity transaction, each party to that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">transaction who receives a copy of the work also receives whatever</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">licenses to the work the party\'s predecessor in interest had or could</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">give under the previous paragraph, plus a right to possession of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Corresponding Source of the work from the predecessor in interest, if</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the predecessor has it or can get it with reasonable efforts.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You may not impose any further restrictions on the exercise of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">rights granted or affirmed under this License.  For example, you may</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">not impose a license fee, royalty, or other charge for exercise of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">rights granted under this License, and you may not initiate litigation</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(including a cross-claim or counterclaim in a lawsuit) alleging that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">any patent claim is infringed by making, using, selling, offering for</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sale, or importing the Program or any portion of it.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  11. Patents.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  A &quot;contributor&quot; is a copyright holder who authorizes use under this</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License of the Program or a work on which the Program is based.  The</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">work thus licensed is called the contributor\'s &quot;contributor version&quot;.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  A contributor\'s &quot;essential patent claims&quot; are all patent claims</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">owned or controlled by the contributor, whether already acquired or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">hereafter acquired, that would be infringed by some manner, permitted</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">by this License, of making, using, or selling its contributor version,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">but do not include claims that would be infringed only as a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">consequence of further modification of the contributor version.  For</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">purposes of this definition, &quot;control&quot; includes the right to grant</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">patent sublicenses in a manner consistent with the requirements of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">this License.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Each contributor grants you a non-exclusive, worldwide, royalty-free</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">patent license under the contributor\'s essential patent claims, to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">make, use, sell, offer for sale, import and otherwise run, modify and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">propagate the contents of its contributor version.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  In the following three paragraphs, a &quot;patent license&quot; is any express</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">agreement or commitment, however denominated, not to enforce a patent</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(such as an express permission to practice a patent or covenant not to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sue for patent infringement).  To &quot;grant&quot; such a patent license to a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">party means to make such an agreement or commitment not to enforce a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">patent against the party.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  If you convey a covered work, knowingly relying on a patent license,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">and the Corresponding Source of the work is not available for anyone</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">to copy, free of charge and under the terms of this License, through a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">publicly available network server or other readily accessible means,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">then you must either (1) cause the Corresponding Source to be so</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">available, or (2) arrange to deprive yourself of the benefit of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">patent license for this particular work, or (3) arrange, in a manner</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">consistent with the requirements of this License, to extend the patent</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">license to downstream recipients.  &quot;Knowingly relying&quot; means you have</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">actual knowledge that, but for the patent license, your conveying the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">covered work in a country, or your recipient\'s use of the covered work</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in a country, would infringe one or more identifiable patents in that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">country that you have reason to believe are valid.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  If, pursuant to or in connection with a single transaction or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">arrangement, you convey, or propagate by procuring conveyance of, a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">covered work, and grant a patent license to some of the parties</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">receiving the covered work authorizing them to use, propagate, modify</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">or convey a specific copy of the covered work, then the patent license</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">you grant is automatically extended to all recipients of the covered</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">work and works based on it.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  A patent license is &quot;discriminatory&quot; if it does not include within</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the scope of its coverage, prohibits the exercise of, or is</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">conditioned on the non-exercise of one or more of the rights that are</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">specifically granted under this License.  You may not convey a covered</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">work if you are a party to an arrangement with a third party that is</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">in the business of distributing software, under which you make payment</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">to the third party based on the extent of your activity of conveying</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the work, and under which the third party grants, to any of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">parties who would receive the covered work from you, a discriminatory</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">patent license (a) in connection with copies of the covered work</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">conveyed by you (or copies made from those copies), or (b) primarily</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">for and in connection with specific products or compilations that</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">contain the covered work, unless you entered into that arrangement,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">or that patent license was granted, prior to 28 March 2007.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Nothing in this License shall be construed as excluding or limiting</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">any implied license or other defenses to infringement that may</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">otherwise be available to you under applicable patent law.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  12. No Surrender of Others\' Freedom.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  If conditions are imposed on you (whether by court order, agreement or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">otherwise) that contradict the conditions of this License, they do not</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">excuse you from the conditions of this License.  If you cannot convey a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">covered work so as to satisfy simultaneously your obligations under this</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License and any other pertinent obligations, then as a consequence you may</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">not convey it at all.  For example, if you agree to terms that obligate you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">to collect a royalty for further conveying from those to whom you convey</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the Program, the only way you could satisfy both those terms and this</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License would be to refrain entirely from conveying the Program.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  13. Use with the GNU Affero General Public License.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Notwithstanding any other provision of this License, you have</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">permission to link or combine any covered work with a work licensed</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">under version 3 of the GNU Affero General Public License into a single</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">combined work, and to convey the resulting work.  The terms of this</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">License will continue to apply to the part which is the covered work,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">but the special requirements of the GNU Affero General Public License,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">section 13, concerning interaction through a network will apply to the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">combination as such.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  14. Revised Versions of this License.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The Free Software Foundation may publish revised and/or new versions of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the GNU General Public License from time to time.  Such new versions will</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">be similar in spirit to the present version, but may differ in detail to</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">address new problems or concerns.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Each version is given a distinguishing version number.  If the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Program specifies that a certain numbered version of the GNU General</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Public License &quot;or any later version&quot; applies to it, you have the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">option of following the terms and conditions either of that numbered</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">version or of any later version published by the Free Software</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Foundation.  If the Program does not specify a version number of the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GNU General Public License, you may choose any version ever published</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">by the Free Software Foundation.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  If the Program specifies that a proxy can decide which future</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">versions of the GNU General Public License can be used, that proxy\'s</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">public statement of acceptance of a version permanently authorizes you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">to choose that version for the Program.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  Later license versions may give you additional or different</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">permissions.  However, no additional obligations are imposed on any</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">author or copyright holder as a result of your choosing to follow a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">later version.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  15. Disclaimer of Warranty.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM &quot;AS IS&quot; WITHOUT WARRANTY</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ALL NECESSARY SERVICING, REPAIR OR CORRECTION.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  16. Limitation of Liability.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SUCH DAMAGES.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  17. Interpretation of Sections 15 and 16.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  If the disclaimer of warranty and limitation of liability provided</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">above cannot be given local legal effect according to their terms,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">reviewing courts shall apply local law that most closely approximates</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">an absolute waiver of all civil liability in connection with the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Program, unless a warranty or assumption of liability accompanies a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">copy of the Program in return for a fee.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">                     END OF TERMS AND CONDITIONS</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">            How to Apply These Terms to Your New Programs</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  If you develop a new program, and you want it to be of the greatest</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">possible use to the public, the best way to achieve this is to make it</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">free software which everyone can redistribute and change under these terms.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  To do so, attach the following notices to the program.  It is safest</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">to attach them to the start of each source file to most effectively</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">state the exclusion of warranty; and each file should have at least</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the &quot;copyright&quot; line and a pointer to where the full notice is found.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;one line to give the program\'s name and a brief idea of what it does.&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Copyright (C) &lt;year&gt;  &lt;name of author&gt;</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    This program is free software: you can redistribute it and/or modify</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    it under the terms of the GNU General Public License as published by</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    the Free Software Foundation, either version 3 of the License, or</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    (at your option) any later version.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    This program is distributed in the hope that it will be useful,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    but WITHOUT ANY WARRANTY; without even the implied warranty of</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    GNU General Public License for more details.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    You should have received a copy of the GNU General Public License</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    along with this program.  If not, see &lt;http://www.gnu.org/licenses/&gt;.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Also add information on how to contact you by electronic and paper mail.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  If the program does terminal interaction, make it output a short</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">notice like this when it starts in an interactive mode:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    &lt;program&gt;  Copyright (C) &lt;year&gt;  &lt;name of author&gt;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w\'.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    This is free software, and you are welcome to redistribute it</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    under certain conditions; type `show c\' for details.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The hypothetical commands `show w\' and `show c\' should show the appropriate</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">parts of the General Public License.  Of course, your program\'s commands</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">might be different; for a GUI interface, you would use an &quot;about box&quot;.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  You should also get your employer (if you work as a programmer) or school,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">if any, to sign a &quot;copyright disclaimer&quot; for the program, if necessary.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">For more information on this, and how to apply and follow the GNU GPL, see</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;http://www.gnu.org/licenses/&gt;.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">  The GNU General Public License does not permit incorporating your program</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">into proprietary programs.  If your program is a subroutine library, you</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">may consider it more useful to permit linking proprietary applications with</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">the library.  If this is what you want to do, use the GNU Lesser General</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Public License instead of this License.  But first, please read</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&lt;http://www.gnu.org/philosophy/why-not-lgpl.html&gt;.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Python Requests</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copyright 2016 Kenneth Reitz</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   Licensed under the Apache License, Version 2.0 (the &quot;License&quot;);</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   you may not use this file except in compliance with the License.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   You may obtain a copy of the License at</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">       http://www.apache.org/licenses/LICENSE-2.0</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   Unless required by applicable law or agreed to in writing, software</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   distributed under the License is distributed on an &quot;AS IS&quot; BASIS,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">   See the License for the specific language governing permissions and</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">limitations under the License.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Requests oauthlib</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ISC License</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copyright (c) 2014 Kenneth Reitz.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Permission to use, copy, modify, and/or distribute this software for any</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">purpose with or without fee is hereby granted, provided that the above</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">copyright notice and this permission notice appear in all copies.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">THE SOFTWARE IS PROVIDED &quot;AS IS&quot; AND THE AUTHOR DISCLAIMS ALL WARRANTIES</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600;\">Oauthlib</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copyright (c) 2011 Idan Gazit and contributors</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">All rights reserved.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Redistribution and use in source and binary forms, with or without</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">modification, are permitted provided that the following conditions are met:</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    1. Redistributions of source code must retain the above copyright notice,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">       this list of conditions and the following disclaimer.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    2. Redistributions in binary form must reproduce the above copyright</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">       notice, this list of conditions and the following disclaimer in the</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">       documentation and/or other materials provided with the distribution.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    3. Neither the name of this project nor the names of its contributors may</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">       be used to endorse or promote products derived from this software without</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">       specific prior written permission.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS &quot;AS IS&quot;</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.licencesDone.setText(_translate("MainWindow", "Done"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionAuthentication.setText(_translate("MainWindow", "Authentication"))
        self.actionAuthentication.setShortcut(_translate("MainWindow", "Ctrl+Shift+A"))
        self.actionPreferences.setText(_translate("MainWindow", "Preferences"))
        self.actionPreferences.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionLicences.setText(_translate("MainWindow", "Licences"))
        self.actionCheck_for_Updates.setText(_translate("MainWindow", "Check for updates"))
        self.actionCheck_for_Updates.setShortcut(_translate("MainWindow", "Ctrl+U"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

