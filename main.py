from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlRecord, QSqlQuery
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView, QWidget, QPushButton, QDialog, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6 import uic
import sys

from main_ui import Ui_MainWindow
from addEditCoffeeForm_ui import Ui_Form

CON = QSqlDatabase.addDatabase('QSQLITE')
CON.setDatabaseName('.\data\coffee.sqlite')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Ui_MainWindow(Ui_Form(CON), CON)
    ex.show()
    sys.exit(app.exec())