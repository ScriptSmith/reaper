import os
import tempfile
import unittest
from unittest import mock

from components.globals import _calc_path


class CalcPathTests(unittest.TestCase):
    def test_returns_project_root_when_layout_markers_exist(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            project_root = os.path.join(temp_dir, "reaper-master")
            components_dir = os.path.join(project_root, "components")
            ui_dir = os.path.join(project_root, "ui")

            os.makedirs(components_dir)
            os.makedirs(ui_dir)

            self.assertEqual(_calc_path(components_dir), project_root)

    def test_returns_start_path_when_project_root_not_found(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            nested = os.path.join(temp_dir, "a", "b", "c")
            os.makedirs(nested)

            self.assertEqual(_calc_path(nested), os.path.abspath(nested))

    def test_stops_when_split_returns_same_path(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            start = os.path.abspath(temp_dir)

            with mock.patch(
                "components.globals.os.path.split",
                side_effect=lambda p: (p, ""),
            ):
                self.assertEqual(_calc_path(start), start)


if __name__ == "__main__":
    unittest.main()
