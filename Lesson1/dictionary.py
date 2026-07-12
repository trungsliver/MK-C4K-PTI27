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