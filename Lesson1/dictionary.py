# CRUD: Create - Read - Update - Delete

# Create - Khởi tạo
dict1 = {}
dict2 = {
    # các cặp key - value
    'name': 'Minh Tùng',
    'age': 14,
    'gender': 'female',
    'school': "MindX"
}

# Read - Đọc dữ liệu
    # Truy cập bằng key
print('Name:', dict2['name'])
    # Sử dụng phương thức get()
        # Nếu không tồn tại key -> None/Giá trị mặc định
print('Girlfriend:', dict2.get('girlfriend'))  
print('Money:', dict2.get('money', 0))  
    # Duyệt toàn bộ key-value
for key, value in dict2.items():
    print(f'{key}: {value}')

# Update - chỉnh sửa / cập nhật dữ liệu
    # Thêm cặp key - value mới
dict2['laptop'] = 'Macbook Air'
    # Chỉnh sửa phần tử
dict2['gender'] = 'male'

# Delete - xóa dữ liệu
    # Xóa theo key
del dict2['school']
    # Xóa theo key, trả về value
value = dict2.pop('age')
print('Phần tử vừa xóa:', value)

# Kiểm tra key có tồn tại hay không
print('name' in dict2)  # True
print('girlfriend' in dict2)  # False

# Lấy tất cả cặp key-value: items()
print(dict2.items())
# Lấy tất cả key: keys()
print(dict2.keys())
# Lấy tất cả value: values()
print(dict2.values())

# Hàm map(function, iterable):
    # function: hàm xử lý, hàm biến đổi dữ liệu
    # iterable: danh sách, chuỗi, dictionary,...

# Ví dụ: Cho danh sách tên học sinh
# Yêu cầu: Dùng map() để thêm tên lớp vào sau tên học sinh
# Ví dụ: Đức Trung -> Đức Trung - PTI27
arr = ['Thành', 'Minh', 'Tùng', 'Lam', 'Vũ', 'Hoàng', 'Đức Anh', 'Hiếu']

    # Cách 1: Dùng hàm xác định
def add_class(student, class_name = 'PTI27'):
    return f'{student} - {class_name}'
arr1 = map(add_class, arr)
print(list(arr1))

    # Cách 2: Dùng hàm không xác định - lambda function
arr2 = map(lambda student: f'{student} - PTI27', arr)
print(list(arr2))

# Bài tập: Cho danh sách tên học sinh viết hoa lộn xộn
# Yêu cầu: Dùng map() để chuẩn hóa tên học sinh (viết hoa chữ cái đầu, các chữ cái còn lại viết thường)
name_list = ['tRi tHaNH', 'mInh TuNG', 'vU hOANg', 'dUc aNH', 'nhAT mINH', 'bAo lAM', 'dUC hieU', 'nguYen vU']

    # Cách 1: Dùng hàm xác định
def convert_name(name):
    # title(): Viết hoa chữ cái đầu, các chữ cái còn lại viết thường
    return name.title()
name1 = map(convert_name, name_list)
print(list(name1))

    # Cách 2: Dùng hàm không xác định - lambda function
name2 = map(lambda name: name.title(), name_list)
print(list(name2))