import os
import shutil
from PIL import Image
import numpy as np

appro_per = 1.2  # 近方的宽高比
base_path = os.getcwd()
pic_path = [base_path + '\\横', base_path + '\\竖', base_path + '\\方', base_path + '\\近方', base_path + '\\壁纸']
pic_sec_path = [pic_path[0] + '\\1080', pic_path[0] + '\\2k', pic_path[0] + '\\none',
                pic_path[1] + '\\1080', pic_path[1] + '\\2k', pic_path[1] + '\\none',
                pic_path[2] + '\\1080', pic_path[2] + '\\2k', pic_path[2] + '\\none',
                pic_path[3] + '\\1080', pic_path[3] + '\\2k', pic_path[3] + '\\none',
                pic_path[4] + '\\1080', pic_path[4] + '\\2k']

for path in pic_path:
    if not os.path.exists(path):
        os.mkdir(path)
for path in pic_sec_path:
    if not os.path.exists(path):
        os.mkdir(path)

file_list = [base_path + '\\' + x for x in os.listdir(base_path)
             if x.endswith(('.jpg', '.jpeg', '.gif', '.png', '.bmp'))]
size_list = np.array([Image.open(file_name).size for file_name in file_list])
width_arr, height_arr = size_list.T
# 条件
w1920, h1920, w2560, h2560, w_none, h_none = (width_arr >= 1920), (height_arr >= 1920), (width_arr >= 2560), \
                                             (height_arr >= 2560), (width_arr < 1920), (height_arr < 1920)
hor, ver, square = (width_arr > height_arr * appro_per), (height_arr > width_arr * appro_per), (width_arr == height_arr)
appro_hor = (height_arr < width_arr) & (width_arr < height_arr * appro_per)
appro_ver = (width_arr < height_arr) & (height_arr < width_arr * appro_per)
# 横图索引
hor_1080, hor_2k, hor_none = np.where(hor & w1920), np.where(hor & w2560), np.where(hor & w_none)
# 竖图索引
ver_1080, ver_2k, ver_none = np.where(ver & h1920), np.where(ver & h2560), np.where(ver & h_none)
# 方图索引
square_1080, square_2k, square_none = np.where(square & w1920), np.where(square & w2560), np.where(square & w_none)
# 近似方图索引
appro_sq_1080 = np.append(np.where(appro_hor & w1920), np.where(appro_ver & h1920))
appro_sq_2k = np.append(np.where(appro_hor & w2560), np.where(appro_ver & h2560))
appro_sq_none = np.append(np.where(appro_hor & w_none), np.where(appro_ver & h_none))
# 壁纸索引
wall_1080, wall_2k = np.where((height_arr == 1080) & (width_arr == 1920)), \
                     np.where((height_arr == 1440) & (width_arr == 2560))
pic_list = [hor_1080, hor_2k, hor_none, ver_1080, ver_2k, ver_none, square_1080, square_2k, square_none,
            appro_sq_1080, appro_sq_2k, appro_sq_none, wall_1080, wall_2k]
# print(pic_list)
for i in range(len(pic_list)):
    if len(pic_list[i]) == 1:
        pic_list[i] = pic_list[i][0]
    for j in pic_list[i]:
        shutil.copy(file_list[j], pic_sec_path[i])
