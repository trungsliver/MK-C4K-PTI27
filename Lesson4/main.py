import oop

# Khởi tạo UserDatabase 
db = oop.PlayerDatabase('data.json')

# Hiển thị số lượng phần tử ở 2 danh sách trong UserDatabase
print('len(db.players_dict):', len(db.players_dict))
print('len(db.players_list):', len(db.players_list))

# Chuyển đổi từ dict sang object
db.dict_to_object()

print('Sau chuyển đổi:')
print('len(db.players_dict):', len(db.players_dict))
print('len(db.players_list):', len(db.players_list))

# Hiển thị toàn bộ phần tử trong danh sách object
db.show_all()