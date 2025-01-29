import sys

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtSql import QSqlTableModel, QSqlDatabase
from PyQt6.QtWidgets import QMainWindow

from addEditCoffeeForm_ui import Ui_Form

class Ui_MainWindow(QMainWindow):
    def __init__(self, child, con):
        super(Ui_MainWindow, self).__init__()
        self.childForm = child
        self.con = con
        self.setWindowTitle("MainWindow")
        self.resize(800, 459)
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 19, 761, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(parent=self.verticalLayoutWidget)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.showdata = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.showdata.setObjectName("showdata")
        self.horizontalLayout.addWidget(self.showdata)
        self.adddata = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.adddata.setObjectName("adddata")
        self.horizontalLayout.addWidget(self.adddata)
        self.editdata = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.editdata.setObjectName("editdata")
        self.horizontalLayout.addWidget(self.editdata)
        self.exit = QtWidgets.QPushButton(parent=self.verticalLayoutWidget)
        self.exit.setObjectName("exit")
        self.horizontalLayout.addWidget(self.exit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.setCentralWidget(self.centralwidget)

        self.showdata.clicked.connect(self.onShowdata)
        self.adddata.clicked.connect(self.onAdddata)
        self.editdata.clicked.connect(self.onEditdata)
        self.exit.clicked.connect(self.onExit)
        self.setWindowTitle("Главное окно")
        self.showdata.setText("Показать данные")
        self.adddata.setText("Создать запись")
        self.editdata.setText("Редактировать запись")
        self.exit.setText("Выход")

    def onShowdata(self):
        self.con.open()
        self.model = QSqlTableModel(self, self.con)
        self.model.setTable('cofee')
        self.model.select()
        self.con.close()
        self.tableView.setModel(self.model)
        self.update()

    def onAdddata(self):
        self.frame = self.childForm
        self.frame.flag = 'add'
        self.frame.show()

    def onEditdata(self):
        self.frame = self.childForm
        self.frame.flag = 'edit'
        index = (self.tableView.selectionModel().currentIndex())
        self.frame.id.setText(str(index.sibling(index.row(), 0).data()))
        self.frame.name.setText(index.sibling(index.row(), 1).data())
        self.frame.stepen.setText(index.sibling(index.row(), 2).data())
        self.frame.zerno.setCurrentText(index.sibling(index.row(), 3).data())
        self.frame.vkus.setText(index.sibling(index.row(), 4).data())
        self.frame.price.setText(str(index.sibling(index.row(), 5).data()))
        self.frame.objem.setText(str(index.sibling(index.row(), 6).data()))
        self.frame.show()

    def onExit(self):
        sys.exit()