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
        