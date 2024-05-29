import os
import shutil
import numpy as np
import random
# 设置主文件夹路径和目标文件夹路径
main_folder = '/home/user9/USenhance2023/datasets/ultrasound/train'
high_quality_destination_train = '/home/user9/USenhance2023/datasets/ultrasound/train_high'
low_quality_destination_train = '/home/user9/USenhance2023/datasets/ultrasound/train_low'

high_quality_destination_valid = '/home/user9/USenhance2023/datasets/ultrasound/valid_high'
low_quality_destination_valid = '/home/user9/USenhance2023/datasets/ultrasound/valid_low'
# 创建目标文件夹，如果它们不存在
os.makedirs(high_quality_destination_train, exist_ok=True)
os.makedirs(low_quality_destination_train, exist_ok=True)
os.makedirs(low_quality_destination_valid, exist_ok=True)
os.makedirs(high_quality_destination_valid, exist_ok=True)
train_size = 0.7
valid_size = 0.3


# 遍历主文件夹中的所有子文件夹
for subdir in os.listdir(main_folder):
    subdir_path = os.path.join(main_folder, subdir)
    if os.path.isdir(subdir_path):
        # 处理 high_quality 文件夹
        high_quality_path = os.path.join(subdir_path, 'high_quality')
        if os.path.exists(high_quality_path) and os.path.isdir(high_quality_path):
            file_path_list = os.listdir(high_quality_path)
            
            file_size = len(file_path_list)
            index = np.arange(file_size)
            
            random.shuffle(index)
            train_index = index[:int(file_size * train_size)]
            valid_index = index[int(file_size * train_size):]
            
            for i in train_index:  
                file_path = os.path.join(high_quality_path, file_path_list[i])
                if os.path.isfile(file_path):
                    shutil.copy(file_path, high_quality_destination_train)
                        
            for i in valid_index:
                file_path = os.path.join(high_quality_path, file_path_list[i])
                if os.path.isfile(file_path):
                    shutil.copy(file_path, high_quality_destination_valid)
        

        # 处理 low_quality 文件夹
        low_quality_path = os.path.join(subdir_path, 'low_quality')
        if os.path.exists(low_quality_path) and os.path.isdir(low_quality_path):
            file_path_list = os.listdir(low_quality_path)
            
            for i in train_index:
                file_path = os.path.join(low_quality_path, file_path_list[i])
                if os.path.isfile(file_path):
                    shutil.copy(file_path, low_quality_destination_train)
                        
            for i in valid_index:
                file_path = os.path.join(low_quality_path, file_path_list[i])
                if os.path.isfile(file_path):
                    shutil.copy(file_path, low_quality_destination_valid)
       
print("文件复制完成。")
