import os
import shutil
import random

# Đường dẫn gốc chứa thư mục Cat và Dog
source_dir = 'dataset1/PetImages'
output_base_dir = 'dataset1/split_dataset'

# Tạo thư mục train và test
for folder in ['train/Cat', 'train/Dog', 'test/Cat', 'test/Dog']:
    os.makedirs(os.path.join(output_base_dir, folder), exist_ok=True)

# Chia ảnh cho từng lớp
def split_dataset(class_name, train_ratio=0.8):
    src_folder = os.path.join(source_dir, class_name)
    all_images = [img for img in os.listdir(src_folder) if img.lower().endswith(('.jpg', '.png', '.jpeg'))]
    random.shuffle(all_images)

    train_size = int(len(all_images) * train_ratio)
    train_images = all_images[:train_size]
    test_images = all_images[train_size:]

    # Copy ảnh vào các thư mục tương ứng
    for img in train_images:
        src_path = os.path.join(src_folder, img)
        dst_path = os.path.join(output_base_dir, 'train', class_name, img)
        shutil.copy2(src_path, dst_path)

    for img in test_images:
        src_path = os.path.join(src_folder, img)
        dst_path = os.path.join(output_base_dir, 'test', class_name, img)
        shutil.copy2(src_path, dst_path)

split_dataset('Cat')
split_dataset('Dog')

print("Hoàn tất chia dữ liệu.")