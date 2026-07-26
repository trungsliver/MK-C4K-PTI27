import data_io

class User:
    def __init__(self, usernmae, email, password):
        self.username = usernmae
        self.email = email
        self.password = password

    def display_info(self):
        print('========== INFO ==========')
        print(f"Username: {self.username}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print('===========================')

class UserDatabase:
    def __init__(self, file_path):
        # file_path: đường dẫn đến file dữ liệu 
        self.file_path = file_path
        # Danh sách dạng object
        self.users_list = list()
        # Danh sách dạng dictionary
        self.users_dict = data_io.load_json_data(file_path)

    # Chuyển đổi từ dictionary sang object
    def dict_to_object(self):
        new_users = []
        # Duyệt danh sách users_dict (đã có data)
        for user_data in self.users_dict:
            # Lấy value trong dictionary gán cho object User
            user = User(user_data['username'], 
                        user_data['email'], 
                        user_data['password'])
            new_users.append(user)
        # Lưu vào thuộc tính users_list
        self.users_list = new_users

    # Chuyển đổi từ object sang dictionary
    def object_to_dict(self):
        json_data = list()
        # Duyệt danh sách object users_list
        for user_data in self.users_list:
            # user_data.__dict__: chuyển dạng object sang dictionary
            json_data.append(user_data.__dict__)
        return json_data

    # Hiển thị tất cả data trong users_list
    def show_all(self):
        for user in self.users_list:
            # display_info(): phương thức của class User
            user.display_info()