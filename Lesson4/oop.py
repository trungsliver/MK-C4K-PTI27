import data_io

class Player:
    def __init__(self, id, name, dob, region, club, rating=None, worth=None):
        self.id = id
        self.name = name
        self.dob = dob
        self.region = region
        self.club = club
        # Nếu có thì định dạng float, không có thì mặc định = 0
        self.rating = float(rating) if rating else 0
        self.worth = float(worth) if worth else 0

    def show_info(self):
        print("===== Player Information =====")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"DOB: {self.dob}")
        print(f"Region: {self.region}")
        print(f"Club: {self.club}")
        print(f"Rating: {self.rating}")
        print(f"Worth: {self.worth}")
        print("===============================")

    def update(self, new_data:dict):
        for key, value in new_data.items():
            # Chỉ khi nào có thuộc tính thì mới gán giá trị (update)
            if value:
                setattr(self, key, value)

class PlayerDatabase:
    def __init__(self, file_path):
        # filepath: đường dẫn đến file dữ liệu
        self.file_path = file_path
        # Danh sách dạng object
        self.players_list = list()
        # Danh sách dang dictionary
        self.players_dict = data_io.load_json_data(file_path)

    # Chuyển đổi từ dict sang object Player
    def dict_to_object(self):
        new_players = []
        for player_data in self.players_dict:
            player = Player(id = player_data["id"],
                            name = player_data['name'],
                            dob = player_data['dob'],
                            region = player_data['region'],
                            club = player_data['club'],
                            rating = player_data['rating'],
                            worth = player_data['worth'])
            new_players.append(player)
        self.players_list = new_players

    # Chuyển từ object => dictionary / json
    def object_to_dict(self):
        json_data = list()
        # Duyệt danh sách object users_list
        for user_data in self.users_list:
            # user_data.__dict__: chuyển dạng object sang dictionary
            json_data.append(user_data.__dict__)
        return json_data

    # Hiển thị toàn bộ thông tin
    def show_all(self):
        for player in self.players_list:
            # display_info(): phương thức của class User
            player.show_info()

    # Tìm object theo tên
    def find_player_by_name(self, name):
        for player in self.players_list:
            if name in player.name:     # Tìm thấy
                return player
        return None    # Không tìm thấy

    # Thêm 1 player mới
    def add_player(self, player_dict):
        # Tạo 1 object mới
            # id sẽ là số index tiếp theo
        player_dict["id"] = len(self.players_list) + 1
        new_player = Player(id = player_dict["id"],
                            name = player_dict['name'],
                            dob = player_dict['dob'],
                            region = player_dict['region'],
                            club = player_dict['club'],
                            rating = player_dict['rating'],
                            worth = player_dict['worth'])
        # Thêm vào danh sách object
        self.players_list.append(new_player)
        # Thêm vào danh sách dictionary
        self.players_dict.append(new_player.__dict__)
        # Ghi dữ liệu vào file
        data_io.write_json_data(self.file_path, self.players_dict)

    # Tìm player và sửa thông tin
    def edit_player(self, edit_name, new_data):
        # Tìm đối tượng
        matched = self.find_player_by_name(edit_name)
        # sửa đối tượng nếu tìm thấy:
        if matched:
            # Sửa trong danh sách object
            matched.update(new_data)
            # Sửa trong danh sách dictionary
            self.object_to_dict()
            # Lưu dữ liệu vào file
            data_io.write_json_data(self.file_path, self.players_dict)

    # Tìm player theo tên và xóa thông tin
    def delete_player(self, delete_name):
        # Tìm đối tượng
        matched = self.find_player_by_name(delete_name)
        # Xóa đối tượng
        if matched:
            # Xóa trong danh sách object
            self.players_list.remove(matched)
            # Xóa trong danh sách dictionary
            self.players_dict.remove(matched.__dict__)
            # Lưu dữ liệu vào file
            data_io.write_json_data(self.file_path, self.players_dict)

    # Tìm danh danh sách player mà tên có chứa chuỗi tìm kiếm
    def search_player(self, search_name):
        # Danh sách lưu kết quả (dạng object)
        matched_players = []
        for player in self.players_list:
            if search_name in player.name:
                matched_players.append(player)
        return matched_players