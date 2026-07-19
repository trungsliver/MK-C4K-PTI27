# Lập trình hướng đối tượng
# OOP - Objeect Oriented Programming

# Tổng quát: OOP là cách mô phỏng các đối tượng trong thế giới thực vào chương trình máy tính.

# Class (lớp):          Đối tượng tổng quát
# Object (đối tượng):   Đối tượng cụ thể

# Attributes (thuộc tính):   Đặc điểm của đối tượng
# Methods (phương thức):     Hành động của đối tượng

class Human:
    # Hàm khởi tạo
    def __init__(self, name, age, gender):
        # name, age, gender là thuộc tính
        self.name = name
        self.age = age
        self.gender = gender
    
    # Phương thức (method)
    def display_info(self):
        print('========== INFO ==========')
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print('===========================')

    # Phương thức hát
    def sing(self, song):
        print(f"{self.name} is singing {song}")

# Khởi tạo đối tượng (object)
h1 = Human('Tùng', 14, 'male')
h2 = Human('Hoàng Anh', 14, 'female')
# Gọi phương thức
h1.display_info()
h2.display_info()
h2.sing('Baby Shark')