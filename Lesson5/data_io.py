import json

# Đọc dữ liệu
def load_json_data(file_path):
    dict_data = list()
    # with open(): dùng để mở file, tự động đóng sau khi thực hiện
    # 'r': thao tác đọc file
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    dict_data.extend(data)
    return dict_data

# Ghi dữ liệu
def write_json_data(file_path, json_data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(json_data, file)