import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6 import QtCore, QtWidgets
from PyQt6 import uic

# xử lý
app = QApplication(sys.argv)
arr = ["Đức Anh", 'Vũ Hoàng', "Hoàng Anh", "Minh Tùng", "Bảo Lam", "Nguyên Vũ", "Nhật Minh", "Trí Thành"]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('list.ui', self)
        # Thêm danh sách để hiển thị trên list widget
        self.listWidget.addItems(arr)
        # Kết nối sự kiện click vào nút với hàm xử lý
        self.btn_add.clicked.connect(self.add_item)
        self.btn_edit.clicked.connect(self.edit_item)
        self.btn_delete.clicked.connect(self.delete_item)
        self.btn_search.clicked.connect(self.search_item)

    def add_item(self):
        # Lấy text ở lineEdit
        text = self.lineEdit.text().strip()
        # Kiểm tra nếu text rỗng thì thông báo lỗi
        if not text:
            msg_box("Lỗi", "Vui lòng nhập dữ liệu!")
            return
        else:
            # Thêm phần tử vào danh sách
            arr.append(str(text))
            # Cập nhật lại list widget
            self.listWidget.clear()
            self.listWidget.addItems(arr)
            # Xóa text ở lineEdit
            self.lineEdit.setText("")

    def edit_item(self):
        # Lấy index dòng đang chọn trên list widget
        cur = self.listWidget.currentRow()
        # Lấy text ở lineEdit
        text = self.lineEdit.text().strip()
        # Kiểm tra nếu text rỗng thì thông báo lỗi
        if not text:
            msg_box("Lỗi", "Vui lòng nhập dữ liệu!")
            return
        # Kiểm tra nếu không có dòng nào được chọn thì thông báo lỗi
        if cur < 0:
            msg_box("Lỗi", "Vui lòng chọn dòng cần sửa!")
            return
        # Cập nhật phần tử trong danh sách
        arr[cur] = str(text)
        # Cập nhật lại list widget
        self.listWidget.clear()
        self.listWidget.addItems(arr)
        # Xóa text ở lineEdit
        self.lineEdit.setText("")

    def delete_item(self):
        # Lấy index dòng đang chọn trên list widget
        cur = self.listWidget.currentRow()
        # Kiểm tra nếu không có dòng nào được chọn thì thông báo lỗi
        if cur < 0:
            msg_box("Lỗi", "Vui lòng chọn dòng cần xóa!")
            return
        # Xóa phần tử trong danh sách
        arr.pop(cur)
        # Cập nhật lại list widget
        self.listWidget.clear()
        self.listWidget.addItems(arr)
        # Xóa text ở lineEdit
        self.lineEdit.setText("")

    def search_item(self):
        insert_txt = self.lineEdit.text().strip()
        check = False
        check_list = []
        for item in arr:
            if insert_txt.lower() in item.lower():
                check = True
                check_list.append(item)
        # Xóa hết các phần tử ở trên widget
        self.listWidget.clear()
        # add lại cả danh sách vào list widget
        if check == True:
            msg_box('Thành công', f'Có {len(check_list)} kết quả!')
        else:
            check_list.append('item not found')
        self.listWidget.addItems(check_list)

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