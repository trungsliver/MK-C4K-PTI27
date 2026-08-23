import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6 import uic
import oop 

# xử lý
app = QApplication(sys.argv)

# Khởi tạo database
db = oop.UserDatabase('data.json')
db.convert_to_object()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('list.ui', self)
        # Lấy dữ liệu từ database
        users = db.get_all_users()
        # Hiển thị user lên list widget
        self.listWidget.addItems(users)

def msg_box(title, content):
    msg = QtWidgets.QMessageBox()
    msg.setStyleSheet("QLabel{min-width: 200px;}"
                          "QLabel{max-width: 200px;}"
                          "QMessageBox{background-color:rgba(35,36,40,255);}"
                          "QPushButton{background-color:rgb(30,95,181);}"
                          "QLabel{color:rgb(255,255,255);}"
                          "QPushButton{color:rgb(255,255,255);}")
    msg.setWindowTitle(title)
    msg.setInformativeText(content)
    msg.exec()

# Run app
window = MainWindow()
window.show()
sys.exit(app.exec())