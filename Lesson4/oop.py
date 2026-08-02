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
        for user in self.users_list:
            # display_info(): phương thức của class User
            user.display_info()