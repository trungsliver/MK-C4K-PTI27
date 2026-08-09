import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6 import uic
import oop, data_io

# xử lý
app = QApplication(sys.argv)
dtb = oop.UserDatabase("users.json")

class Signup(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui//signup.ui", self)
        self.pushButton_signup.clicked.connect(self.check_signup)

    # Phương thức check signup
    def check_signup(self):
        # Lấy dữ liệu từ các trường
        username = self.lineEdit_username.text().strip()
        email = self.lineEdit_email.text().strip()
        password = self.lineEdit_password.text().strip()
        confirm = self.lineEdit_confirm.text().strip()
        checkB = self.checkBox.isChecked()
        # Biến kiểm tra đăng ký
        check = True

        # Thiếu Thông tin
        if username == '' or email == '' or password == '' or confirm == '' or checkB != True:
            check = False
            msg_box('Signup fail', 'Missing information!')
        # Password và confirm không khớp
        elif password != confirm:
            check = False
            msg_box('Signup fail', 'Password and confirm not match!')
        # Password ít nhất 6 ký tự
        elif len(password) < 6:
            check = False
            msg_box('Signup fail', 'Password must be at least 6 characters!')
        # Email sai định dạng
        elif '@' not in email:
            check = False
            msg_box('Signup fail', 'Email is incorrect!')
        # Đã tồn tại email trong danh sách users
        else:
            check_user = dtb.find_user_by_email(email)
            if check_user == True:
                check = False
                msg_box('Signup fail', 'Email already exists!')
        # Kiểm tra xem có đang ký thành công không
        if check == True:
            # Add tài khoản mới vào danh sách users
            dtb.add_user(email, password)
            msg_box('Signup success', 'Signup success!')
            # Chuyển trang
            switch_window(Login())

class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui//login.ui", self)
        self.pushButton_login.clicked.connect(self.check_login)

    def check_login(self):
        check = False
        # Khai báo thuộc tính sẽ sử dụng
        email = self.lineEdit_email.text().strip()
        password = self.lineEdit_password.text().strip()
        # Kiểm tra 
        check = dtb.check_login(email, password)
        
        if check == True:
            msg_box('Login success', 'Welcome to my app !!!')
            switch_window(Signup())
        else:
            msg_box('Login fail', 'Email or password is incorrect!')

# Hàm hiển thị thông báo
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

# Chuyển cửa sổ giao diện
def switch_window(classw):
    global window
    window = classw
    window.show()

# Run app
window = Signup()
window.show()
sys.exit(app.exec())