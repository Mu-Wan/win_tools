import os
import shutil
from PIL import Image

appro_per = 1.2  # 近方的宽高比
base_path = os.getcwd()
pic_path = [base_path + '\\横', base_path + '\\竖', base_path + '\\方', base_path + '\\近方']
pic_sec_path = [pic_path[0] + '\\1080', pic_path[0] + '\\2k', pic_path[0] + '\\none',
                pic_path[1] + '\\1080', pic_path[1] + '\\2k', pic_path[1] + '\\none',
                pic_path[2] + '\\1080', pic_path[2] + '\\2k', pic_path[2] + '\\none',
                pic_path[3] + '\\1080', pic_path[3] + '\\2k', pic_path[3] + '\\none']

for path in pic_path:
    if not os.path.exists(path):
        os.mkdir(path)
for path in pic_sec_path:
    if not os.path.exists(path):
        os.mkdir(path)

file_list = [base_path + '\\' + x for x in os.listdir(base_path)
             if x.endswith(('.jpg', '.jpeg', '.gif', '.png', '.bmp'))]
size_list = [Image.open(file_name).size for file_name in file_list]
width_list = [x[0] for x in size_list]
height_list = [x[1] for x in size_list]
# 横图
hor_1080 = [i for i in range(len(size_list)) if height_list[i] * appro_per < width_list[i] and width_list[i] >= 1920]
hor_2k = [i for i in range(len(size_list)) if height_list[i] * appro_per < width_list[i] and width_list[i] >= 2560]
hor_none = [i for i in range(len(size_list)) if height_list[i] * appro_per < width_list[i] < 1920]
# 竖图
ver_1080 = [i for i in range(len(size_list)) if height_list[i] > width_list[i] * appro_per and height_list[i] >= 1920]
ver_2k = [i for i in range(len(size_list)) if height_list[i] > width_list[i] * appro_per and height_list[i] >= 2560]
ver_none = [i for i in range(len(size_list)) if 1920 > height_list[i] > width_list[i] * appro_per]
# 方图
square_1080 = [i for i in range(len(size_list)) if width_list[i] == height_list[i] and width_list[i] >= 1080]
square_2k = [i for i in range(len(size_list)) if width_list[i] == height_list[i] and width_list[i] >= 2560]
square_none = [i for i in range(len(size_list)) if width_list[i] == height_list[i] and width_list[i] < 1080]
# 近方图
appro_sq_1080 = [i for i in range(len(size_list))
                 if 1080 <= height_list[i] < width_list[i] <= height_list[i] * appro_per
                 or 1080 <= width_list[i] < height_list[i] <= width_list[i] * appro_per]
appro_sq_2k = [i for i in range(len(size_list))
               if 2560 <= height_list[i] < width_list[i] <= height_list[i] * appro_per
               or 2560 <= width_list[i] < height_list[i] <= width_list[i] * appro_per]
appro_sq_none = [i for i in range(len(size_list))
                 if height_list[i] < width_list[i] <= height_list[i] * appro_per < 1080
                 or width_list[i] < height_list[i] <= width_list[i] * appro_per < 1080]
for i in hor_1080:
    shutil.copy(file_list[i], pic_sec_path[0])
for i in hor_2k:
    shutil.copy(file_list[i], pic_sec_path[1])
for i in hor_none:
    shutil.copy(file_list[i], pic_sec_path[2])
for i in ver_1080:
    shutil.copy(file_list[i], pic_sec_path[3])
for i in ver_2k:
    shutil.copy(file_list[i], pic_sec_path[4])
for i in ver_none:
    shutil.copy(file_list[i], pic_sec_path[5])
for i in square_1080:
    shutil.copy(file_list[i], pic_sec_path[6])
for i in square_2k:
    shutil.copy(file_list[i], pic_sec_path[7])
for i in square_none:
    shutil.copy(file_list[i], pic_sec_path[8])
for i in appro_sq_1080:
    shutil.copy(file_list[i], pic_sec_path[9])
for i in appro_sq_2k:
    shutil.copy(file_list[i], pic_sec_path[10])
for i in appro_sq_none:
    shutil.copy(file_list[i], pic_sec_path[11])
