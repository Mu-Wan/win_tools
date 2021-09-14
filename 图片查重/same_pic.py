import os
import shutil
from collections import namedtuple
from multiprocessing import Pool

import numpy as np
# from pyinstrument import Profiler
from PIL import Image

pic_type = ['jpg', 'jpeg', 'png']
fir_dir, sec_dir = '重复图片', 'same'
if not os.path.exists('./' + fir_dir):
    os.mkdir('./' + fir_dir)
full_dir = './' + fir_dir + '/' + sec_dir
if not os.path.exists(full_dir):
    os.mkdir(full_dir)
src_path = os.getcwd()
dst_path = src_path + '\\' + fir_dir
dst_del_path = dst_path + '\\' + sec_dir

ImgInfo, info_list = namedtuple('ImgInfo', 'size mode name'), []
for file_name in os.listdir('./'):
    suffix = file_name.split('.')[-1].lower()
    if suffix in pic_type:
        img = Image.open(file_name)  # type:Image.Image
        info_list.append(ImgInfo(img.size, img.mode, file_name))


def find_same_img(cur_info: ImgInfo):
    for next_info in info_list[info_list.index(cur_info) + 1:]:
        if cur_info.size == next_info.size and cur_info.mode == next_info.mode:
            with open(cur_info.name, 'rb') as file:
                cur_arr = np.array(Image.open(file))
            with open(next_info.name, 'rb') as file:
                next_arr = np.array(Image.open(file))
            if abs(np.sum(cur_arr - next_arr)) < 1:
                return [cur_info.name, next_info.name]
    return None


if __name__ == "__main__":
    # p = Profiler()
    # p.start()
    pool = Pool(6)
    res = pool.map(find_same_img, info_list)
    pool.close()
    pool.join()
    for pic_names in res:
        if pic_names:
            try:
                shutil.move(src_path + '\\' + pic_names[0], dst_path)
                shutil.move(src_path + '\\' + pic_names[1], dst_del_path)
            except Exception as e:
                if e == shutil.Error:
                    continue
                else:
                    print(e.args)
    # p.stop()
    # p.print()
