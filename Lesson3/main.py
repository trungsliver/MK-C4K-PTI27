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