from os.path import expanduser

from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog, QInputDialog, QDialog

from package.AboutMe import AboutMe
from package.ENV import ENV


class Prompts(QWidget):
    """A collection of prompts used in QSKM."""

    def __init__(self):
        super().__init__()

    @staticmethod
    def show_db_chooser():
        """A file chooser prompt that asks for a database file."""
        db_chooser = QFileDialog()
        db_chooser.setWindowTitle('Open a QSKM Collection...')
        # User may only select the files that exists in the hdd
        db_chooser.setFileMode(QFileDialog.ExistingFile)
        db_chooser.setNameFilter('Database File (*.db)')
        db_chooser.setDirectory(expanduser(ENV.default_db_folder_path))

        # Return the full path to file back to main window if the execution was successful
        if db_chooser.exec():
            return db_chooser.selectedFiles()[0]

    @staticmethod
    def show_about_me():
        """Shows a 'About QSKM' page along with other nice stuff"""
        about_me = QDialog()
        ui = AboutMe()
        ui.setupUi(about_me)
        ui.setup_signals()
        about_me.exec()

    @staticmethod
    def show_file_open():
        """A file chooser prompt that asks for a (text) file to import."""
        file_chooser = QFileDialog()
        file_chooser.setWindowTitle('Open a File...')
        # User may only select the files that exists in the hdd
        file_chooser.setFileMode(QFileDialog.ExistingFile)
        # Will use the file's MIME type to determine autodetect
        filters = ['Auto Detect (*)',
                   'Text File (*.txt)',
                   'Excel File (*.xlsx)',
                   'Database File (*.db)']

        file_chooser.setNameFilters(filters)
        file_chooser.setDirectory(expanduser(ENV.default_db_folder_path))

        # Return the full path to file back to main window if the execution was successful
        if file_chooser.exec():
            return file_chooser.selectedFiles()[0]

    @staticmethod
    def show_file_save():
        """A file chooser prompt allows user to save the collection."""
        file_chooser = QFileDialog()
        file_chooser.setFileMode(QFileDialog.AnyFile)
        file_chooser.setWindowTitle('Save New Collection...')
        file_chooser.setNameFilter('Database File (*.db)')
        file_chooser.setDefaultSuffix('db')
        file_chooser.setDirectory(expanduser(ENV.default_db_folder_path))

        # Return the full path to file back to main window if the execution was successful
        if file_chooser.exec():
            return file_chooser.selectedFiles()[0]

    @staticmethod
    def show_lines_parsed(num_lines):
        """A prompt showing how many lines were parsed and imported from the file"""
        lines_prompt = QMessageBox()
        lines_prompt.setIcon(QMessageBox.Information)
        lines_prompt.setWindowTitle('File Parsed')
        lines_prompt.setText('QSKM has parsed the file and added {} entries to the collection.'.format(num_lines))
        lines_prompt.exec()

    @staticmethod
    def ask_for_col():
        """When the parser is unable to determine which column is the key on, ask user for input"""
        col, ok = QInputDialog().getInt(None, 'Enter the column where key is on',
                                        'QSKM was unable to auto detect the key column.<br>'
                                        'Please enter it below.',
                                        min=0)
        if ok:
            return col
        else:
            return -1

    @staticmethod
    def ask_for_delimiter():
        """Prompt user for the delimiter used in the text file"""
        delimiter, ok = QInputDialog().getText(None, 'Enter the delimiter',
                                               'You have selected a text file.<br>'
                                               'Please enter the delimiter separating the elements (default ;).')
        if ok and delimiter:
            return delimiter
        else:
            return ';'

    @staticmethod
    def show_exit_conf():
        """A prompt asking for confirmation on exit."""
        exit_conf = QMessageBox()
        exit_conf.setIcon(QMessageBox.Question)
        exit_conf.setWindowTitle('Confirm Exit')
        exit_conf.setText('Do you want to exit?<br>'
                          'All changes have been saved automatically.')
        exit_conf.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        exit_conf.setDefaultButton(QMessageBox.Yes)
        user_choice = exit_conf.exec()

        if user_choice == QMessageBox.Yes:
            exit(0)

    @staticmethod
    def show_exit_conf_unsaved():
        """A prompt asking for confirmation on exit (users have unsaved changed)."""
        exit_conf = QMessageBox()
        exit_conf.setIcon(QMessageBox.Question)
        exit_conf.setWindowTitle('Confirm Exit')
        exit_conf.setText('<b>You have unsaved changes.</b><br><br>'
                          'Exit without saving will discard these changes.<br>'
                          'Do you want to save the changes?')
        exit_conf.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        exit_conf.setDefaultButton(QMessageBox.Save)
        user_choice = exit_conf.exec()

        if user_choice == QMessageBox.Discard:
            exit(0)
        elif user_choice == QMessageBox.Save:
            return 1
