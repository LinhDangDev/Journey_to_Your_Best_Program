import os

# Đường dẫn thư mục cha
parent_directory = 'D:\\J2P\\Journey_to_Your_Best_Program\\'

# Tên các thư mục con
folders = ["Challenge 0", "Challenge 1", "Challenge 2", "Challenge 3", "Challenge 4", "Challenge 5"]

# Lặp qua danh sách tên thư mục và tạo từng thư mục
for folder in folders:
    # Đường dẫn đầy đủ đến thư mục con
    path = os.path.join(parent_directory, folder)

    # Kiểm tra xem thư mục đã tồn tại hay chưa
    if not os.path.exists(path):
        # Tạo thư mục mới nếu chưa tồn tại
        os.makedirs(path)
        print(f'Thư mục {folder} đã được tạo.')
    else:
        print(f'Thư mục {folder} đã tồn tại.')
