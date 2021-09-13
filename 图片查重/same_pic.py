import os

import numpy as np
# from pyinstrument import Profiler
from PIL import Image
from multiprocessing import Pool
import shutil

if not os.path.exists('./重复图片'):
    os.mkdir('./重复图片')

src_path = os.getcwd()
dst_path = src_path + '\\重复图片'
file_path = os.listdir('./')
pic_paths = [x for x in file_path if x.split('.')[-1].lower() in ['jpg', 'jpeg', 'png']]
len_paths = len(pic_paths)


def find_img(path: str):
    im, i = Image.open(path), pic_paths.index(path)  # type:Image.Image, int
    for j in range(i + 1, len_paths):
        com_im = Image.open(pic_paths[j])  # type:Image.Image
        if im.size == com_im.size and im.mode == com_im.mode:
            im_arr, com_im_arr = np.array(im), np.array(com_im)
            if abs(np.sum(im_arr - com_im_arr)) < 1:
                return [path, pic_paths[j]]
    return None


if __name__ == "__main__":
    # p = Profiler()
    # p.start()
    pool = Pool(6)
    pic_same = pool.map(find_img, pic_paths)
    pool.close()
    pool.join()
    for pic_names in pic_same:
        if pic_names:
            for pic_name in pic_names:
                try:
                    shutil.move(src_path + '\\' + pic_name, dst_path)
                except shutil.Error as e:
                    continue
    # p.stop()
    # p.print()
