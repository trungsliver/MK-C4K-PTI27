import data_io

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def update(self, new_data:dict):
        # Chỉ khi có thuộc tính mới update
        for key, value in new_data.items():
            if value:
                setattr(self, key, value)

    def show_info(self):
        print(f'Email: {self.email} - Password: {self.password}')

class UserDatabase:
    def __init__ (self, file_path):
        # filepath: đường dẫn đến file dữ liệu
        self.file_path = file_path
        # Danh sách dạng object / list
        self.users_list = list()
        # Danh sách dạng dictionary / json
        self.users_dict = data_io.load_json_data(self.file_path)

    # Chuyển danh sách dictonary => object
    def convert_to_object(self):
        new_users = []
        for user_data in self.users_dict:
            user = User(email = user_data["email"],
                        password = user_data["password"])
            new_users.append(user)
        self.users_list = new_users

    # Chuyển danh sách object => dictionary
    def convert_to_dict(self):
        json_data = list()
        for user in self.users_list:
            json_data.append(user.__dict__)
        return json_data
    
    # Thêm user mới (đăng ký)
    def add_user(self, email, password):
        # User dạng object
        obj_user = User(email, password)
        # User dạng dictionary
        dict_user = {
            "email": email,
            "password": password
        }
        # Thêm vào danh sách object
        self.users_list.append(obj_user)
        # Thêm vào danh sách dictionary
        self.users_dict.append(dict_user)
        # Ghi vào file json
        data_io.write_json_data(self.file_path,self.users_dict)
    
    # Tìm object bằng email
    def find_user_by_email(self, email):
        for user in self.users_dict:
            # Tìm thấy
            if user["email"] == email:
                return True
        # Không tìm thấy
        return False
    
    # Check login
    def check_login(self, email, password):
        for user in self.users_dict:
            # Tìm thấy
            if user["email"] == email and user["password"] == password:
                return True
        # Không tìm thấy
        return False
        