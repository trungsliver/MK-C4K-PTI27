import data_io

class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def update(self, new_data:dict):
        for key, value in new_data.items():
            if value:
                setattr(self, key, value)

    def show_info(self):
        print(f"Email: {self.email}. Password: {self.password}")


class UserDatabase:
    def __init__(self, file_path):
        self.file_path = file_path
        # Danh sách dạng object
        self.users_list = list()
        # Danh sách dạng dict
        self.users_dict = data_io.load_json_data(file_path)

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

    # Lấy toàn bộ user dưới dạng string
    def get_all_users(self):
        users = []
        for user in self.users_list:
            users.append(f"Email: {user.email}. Password: {user.password}")
        return users