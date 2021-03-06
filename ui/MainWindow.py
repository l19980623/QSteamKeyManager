# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\kilve\PycharmProjects\QSteamKeyManager\ui\MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(800, 600)
        self.widget_master = QtWidgets.QWidget(main_window)
        self.widget_master.setObjectName("widget_master")
        self.layout_main = QtWidgets.QVBoxLayout(self.widget_master)
        self.layout_main.setObjectName("layout_main")
        self.layout_search = QtWidgets.QHBoxLayout()
        self.layout_search.setObjectName("layout_search")
        self.lineEdit_search = QtWidgets.QLineEdit(self.widget_master)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_search.sizePolicy().hasHeightForWidth())
        self.lineEdit_search.setSizePolicy(sizePolicy)
        self.lineEdit_search.setMinimumSize(QtCore.QSize(0, 24))
        self.lineEdit_search.setMouseTracking(False)
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.layout_search.addWidget(self.lineEdit_search)
        self.pushButton_clear = QtWidgets.QPushButton(self.widget_master)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_clear.sizePolicy().hasHeightForWidth())
        self.pushButton_clear.setSizePolicy(sizePolicy)
        self.pushButton_clear.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.layout_search.addWidget(self.pushButton_clear)
        self.layout_main.addLayout(self.layout_search)
        self.table_view_content = QtWidgets.QTableView(self.widget_master)
        self.table_view_content.setSortingEnabled(True)
        self.table_view_content.setObjectName("table_view_content")
        self.table_view_content.horizontalHeader().setSortIndicatorShown(True)
        self.table_view_content.horizontalHeader().setStretchLastSection(True)
        self.table_view_content.verticalHeader().setVisible(False)
        self.layout_main.addWidget(self.table_view_content)
        self.layout_add = QtWidgets.QHBoxLayout()
        self.layout_add.setObjectName("layout_add")
        self.lineEdit_game = QtWidgets.QLineEdit(self.widget_master)
        self.lineEdit_game.setMinimumSize(QtCore.QSize(248, 25))
        self.lineEdit_game.setObjectName("lineEdit_game")
        self.layout_add.addWidget(self.lineEdit_game)
        self.lineEdit_key = QtWidgets.QLineEdit(self.widget_master)
        self.lineEdit_key.setMinimumSize(QtCore.QSize(244, 25))
        self.lineEdit_key.setObjectName("lineEdit_key")
        self.layout_add.addWidget(self.lineEdit_key)
        self.lineEdit_notes = QtWidgets.QLineEdit(self.widget_master)
        self.lineEdit_notes.setMinimumSize(QtCore.QSize(0, 25))
        self.lineEdit_notes.setObjectName("lineEdit_notes")
        self.layout_add.addWidget(self.lineEdit_notes)
        self.pushButton_add = QtWidgets.QPushButton(self.widget_master)
        self.pushButton_add.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_add.setObjectName("pushButton_add")
        self.layout_add.addWidget(self.pushButton_add)
        self.layout_main.addLayout(self.layout_add)
        main_window.setCentralWidget(self.widget_master)
        self.menuBar = QtWidgets.QMenuBar(main_window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu_file = QtWidgets.QMenu(self.menuBar)
        self.menu_file.setObjectName("menu_file")
        self.menu_options = QtWidgets.QMenu(self.menuBar)
        self.menu_options.setObjectName("menu_options")
        self.menu_language = QtWidgets.QMenu(self.menu_options)
        self.menu_language.setObjectName("menu_language")
        self.menu_help = QtWidgets.QMenu(self.menuBar)
        self.menu_help.setObjectName("menu_help")
        main_window.setMenuBar(self.menuBar)
        self.action_open_collection = QtWidgets.QAction(main_window)
        self.action_open_collection.setObjectName("action_open_collection")
        self.action_save_changes = QtWidgets.QAction(main_window)
        self.action_save_changes.setObjectName("action_save_changes")
        self.action_export = QtWidgets.QAction(main_window)
        self.action_export.setObjectName("action_export")
        self.action_english = QtWidgets.QAction(main_window)
        self.action_english.setCheckable(True)
        self.action_english.setObjectName("action_english")
        self.action_chinese_simplified = QtWidgets.QAction(main_window)
        self.action_chinese_simplified.setCheckable(True)
        self.action_chinese_simplified.setObjectName("action_chinese_simplified")
        self.action_japanese = QtWidgets.QAction(main_window)
        self.action_japanese.setCheckable(True)
        self.action_japanese.setObjectName("action_japanese")
        self.action_about_qskm = QtWidgets.QAction(main_window)
        self.action_about_qskm.setMenuRole(QtWidgets.QAction.AboutRole)
        self.action_about_qskm.setObjectName("action_about_qskm")
        self.action_check_for_updates = QtWidgets.QAction(main_window)
        self.action_check_for_updates.setObjectName("action_check_for_updates")
        self.action_exit = QtWidgets.QAction(main_window)
        self.action_exit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.action_exit.setObjectName("action_exit")
        self.action_import_from_file = QtWidgets.QAction(main_window)
        self.action_import_from_file.setObjectName("action_import_from_file")
        self.menu_file.addAction(self.action_open_collection)
        self.menu_file.addAction(self.action_import_from_file)
        self.menu_file.addAction(self.action_save_changes)
        self.menu_file.addAction(self.action_export)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menu_language.addAction(self.action_english)
        self.menu_language.addAction(self.action_chinese_simplified)
        self.menu_language.addAction(self.action_japanese)
        self.menu_options.addAction(self.menu_language.menuAction())
        self.menu_help.addAction(self.action_about_qskm)
        self.menu_help.addAction(self.action_check_for_updates)
        self.menuBar.addAction(self.menu_file.menuAction())
        self.menuBar.addAction(self.menu_options.menuAction())
        self.menuBar.addAction(self.menu_help.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "QSteamKeyManager"))
        self.lineEdit_search.setPlaceholderText(_translate("main_window", "Type here to search for anything..."))
        self.pushButton_clear.setText(_translate("main_window", "Clear"))
        self.lineEdit_game.setPlaceholderText(_translate("main_window", "Game"))
        self.lineEdit_key.setPlaceholderText(_translate("main_window", "Key/URL"))
        self.lineEdit_notes.setPlaceholderText(_translate("main_window", "Notes"))
        self.pushButton_add.setText(_translate("main_window", "Add"))
        self.menu_file.setTitle(_translate("main_window", "File"))
        self.menu_options.setTitle(_translate("main_window", "Options"))
        self.menu_language.setTitle(_translate("main_window", "Language"))
        self.menu_help.setTitle(_translate("main_window", "Help"))
        self.action_open_collection.setText(_translate("main_window", "Open Collection..."))
        self.action_save_changes.setText(_translate("main_window", "Save Changes"))
        self.action_export.setText(_translate("main_window", "Export As..."))
        self.action_english.setText(_translate("main_window", "English"))
        self.action_chinese_simplified.setText(_translate("main_window", "Chinese Simplified/简体中文"))
        self.action_japanese.setText(_translate("main_window", "Japanese/日本語"))
        self.action_about_qskm.setText(_translate("main_window", "About QSteamKeyManager..."))
        self.action_check_for_updates.setText(_translate("main_window", "Check for Updates..."))
        self.action_exit.setText(_translate("main_window", "Exit"))
        self.action_import_from_file.setText(_translate("main_window", "Import From File..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_main_window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())
