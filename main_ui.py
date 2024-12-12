# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TodoListWindow(object):
    def setupUi(self, TodoListWindow):
        TodoListWindow.setObjectName("TodoListWindow")
        TodoListWindow.resize(800, 600)
        self.mainLayout = QtWidgets.QHBoxLayout(TodoListWindow)
        self.mainLayout.setObjectName("mainLayout")
        self.leftColumnLayout = QtWidgets.QVBoxLayout()
        self.leftColumnLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.leftColumnLayout.setSpacing(10)
        self.leftColumnLayout.setObjectName("leftColumnLayout")
        self.addTaskButton = QtWidgets.QPushButton(TodoListWindow)
        self.addTaskButton.setObjectName("addTaskButton")
        self.leftColumnLayout.addWidget(self.addTaskButton)
        self.deleteTaskButton = QtWidgets.QPushButton(TodoListWindow)
        self.deleteTaskButton.setObjectName("deleteTaskButton")
        self.leftColumnLayout.addWidget(self.deleteTaskButton)
        self.clearAllButton = QtWidgets.QPushButton(TodoListWindow)
        self.clearAllButton.setObjectName("clearAllButton")
        self.leftColumnLayout.addWidget(self.clearAllButton)
        self.mainLayout.addLayout(self.leftColumnLayout)
        self.rightColumnLayout = QtWidgets.QVBoxLayout()
        self.rightColumnLayout.setSpacing(10)
        self.rightColumnLayout.setObjectName("rightColumnLayout")
        self.taskListLabel = QtWidgets.QLabel(TodoListWindow)
        self.taskListLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.taskListLabel.setObjectName("taskListLabel")
        self.rightColumnLayout.addWidget(self.taskListLabel)
        self.taskListWidget = QtWidgets.QListWidget(TodoListWindow)
        self.taskListWidget.setObjectName("taskListWidget")
        self.rightColumnLayout.addWidget(self.taskListWidget)
        self.mainLayout.addLayout(self.rightColumnLayout)

        self.retranslateUi(TodoListWindow)
        QtCore.QMetaObject.connectSlotsByName(TodoListWindow)

    def retranslateUi(self, TodoListWindow):
        _translate = QtCore.QCoreApplication.translate
        TodoListWindow.setWindowTitle(_translate("TodoListWindow", "Todo List"))
        self.addTaskButton.setText(_translate("TodoListWindow", "Add Task"))
        self.deleteTaskButton.setText(_translate("TodoListWindow", "Delete Task"))
        self.clearAllButton.setText(_translate("TodoListWindow", "Clear All"))
        self.taskListLabel.setText(_translate("TodoListWindow", "Task List"))