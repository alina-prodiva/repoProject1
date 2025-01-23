from PyQt6.QtSql import QSqlDatabase, QSqlTableModel, QSqlRecord, QSqlQuery
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView, QWidget, QPushButton, QDialog, QMessageBox
from PyQt6.QtCore import Qt
from PyQt6 import uic
import sys


def neNone(n):
    if len(n) == 0:
        return ''
    else:
        return str(n)


class AddEditWidget(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.stepen = None
        self.name = None
        self.price = None
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.con = QSqlDatabase.addDatabase('QSQLITE')
        self.con.setDatabaseName('coffee.sqlite')
        self.flag = ''
        self.id.setEnabled(False)
        self.zerno.addItems(['молотый', 'в зернах'])
        self.save.clicked.connect(self.onSave)
        self.cancel.clicked.connect(self.onCancel)

    def onSave(self):
        if self.flag == 'add':
            self.con.open()
            cur = QSqlQuery()
            cur.exec(f"""insert into cofee (name, stepen, zerno, vkus, price, objem) 
                        values ('{self.name.text()}', '{self.stepen.text()}', '{self.zerno.currentText()}', 
                        '{self.vkus.text()}', '{float(self.price.text())}', '{self.objem.text()}')""")
            self.con.close()
            self.parent.show()
            self.parent.onShowdata()
            self.destroy()
        else:

            self.name.text()
            self.con.open()
            cur = QSqlQuery()
            cur.exec(f"""update cofee set name = '{self.name.text()}', stepen = '{self.stepen.text()}', 
                        zerno = '{self.zerno.currentText()}', vkus = '{self.vkus.text()}', price = '{float(self.price.text())}', 
                        objem = '{self.objem.text()}'
                        where id = '{int(self.id.text())}'""")
            self.con.close()
            self.parent.show()
            self.parent.onShowdata()
            self.destroy()

    def onCancel(self):
        self.parent.show()
        self.destroy()


class MyWidget(QMainWindow):
    def __init__(self):
        super(MyWidget, self).__init__()
        uic.loadUi('main.ui', self)
        self.con = QSqlDatabase.addDatabase('QSQLITE')
        self.con.setDatabaseName('coffee.sqlite')
        self.showdata.clicked.connect(self.onShowdata)
        self.adddata.clicked.connect(self.onAdddata)
        self.editdata.clicked.connect(self.onEditdata)
        self.exit.clicked.connect(self.onExit)

    def onShowdata(self):
        self.con.open()
        self.model = QSqlTableModel(self, self.con)
        self.model.setTable('cofee')
        self.model.select()
        self.con.close()
        self.tableView.setModel(self.model)
        ex.update()

    def onAdddata(self):
        self.frame = AddEditWidget(self)
        self.frame.flag = 'add'
        self.frame.show()

    def onEditdata(self):
        self.frame = AddEditWidget(self)
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
        sys.exit(app.exec())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())