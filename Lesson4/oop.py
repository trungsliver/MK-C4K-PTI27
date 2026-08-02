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