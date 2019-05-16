import webbrowser

from PyQt5.QtWidgets import QDialog

from package.ENV import ENV
from ui.AboutMe import Ui_about_me
from ui.License import Ui_License
from ui.OssUsed import Ui_Oss_Used


class AboutMe(Ui_about_me):
    """Adds triggers and other fun stuff based on the code generated by the Designer"""

    def setup_signals(self):
        """Define what would happen when user press the buttons"""
        # User clicks "OSS Used" -> show a list of wonderful open-sauce apps and libs used in this software
        self.pushButton_software.clicked.connect(self.show_oss_used)
        # User clicks "License" -> show the license of the app
        self.pushButton_license.clicked.connect(self.show_license)
        # User clicks "View on GitHub" -> show the GitHub project page
        self.pushButton_github.clicked.connect(self.launch_github_page)

    @staticmethod
    def show_oss_used():
        """Shows a list of open-sauce software used in this app"""
        oss_used = QDialog()
        ui = Ui_Oss_Used()
        ui.setupUi(oss_used)
        oss_used.exec()

    @staticmethod
    def show_license():
        """Shows the license used by the software"""
        license_page = QDialog()
        ui = Ui_License()
        ui.setupUi(license_page)
        license_page.exec()

    @staticmethod
    def launch_github_page():
        """Launches the project page on GitHub"""
        webbrowser.open(ENV.github_project_page, 2)
