import oop

# Khởi tạo database (UserDatabase)
db = oop.UserDatabase("data.json")

# Test data dạng dictionary
print('Độ dài users_dict:', len(db.users_dict))

# Test data dạng object
print('Độ dài users_list:', len(db.users_list))

# Test chuyển đổi từ dictionary sang object
db.dict_to_object()
print('users_list sau chuyển đổi:', len(db.users_list))

# Ví dụ users_list trong database:
user_list_example = [
    oop.User('trithanh', 'thanhscp@gmail.com', '123456'),
    oop.User('hoanganh', 'heosua@gmail.com', '123456'),
    oop.User('vuhoang', 'vuhoangiuem@gmail.com', '123456'),
]

# Test phương thức show_all()
print('Hiển thị tất cả data trong users_list:')
db.show_all()

# Test phương thức find_user_by_username()
result = db.find_user_by_username('duc')
print('Kết quả tìm kiếm: ')
for user in result:
    user.display_info()