# Lập trình hướng đối tượng
# OOP - Object Oriented Programming

# Tổng quát: OOP là cách mà mô phỏng thế giới thực vào chương trình máy tính

# Class (Lớp):          Đối tượng tổng quát
# Object (Đối tượng):   Đối tượng cụ thể

# Attribute (Thuộc tính):  Đặc điểm của đối tượng
# Method (Phương thức):    Hành động của đối tượng

# Khai báo class (đối tượng tổng quát)
class Human:
    # Hàm khởi tạo 
    def __init__(self, name, age, gender):
        # name, age, gender là thuộc tính (attributes)
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"
    
    def display_info(self):
        print(f'========= DISPLAY INFO =========')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Gender: {self.gender}')
        print(f'================================')

    def sing(self, song):
        print(f'{self.name} is singing {song}')