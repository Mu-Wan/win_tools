import os
import shutil
from collections import namedtuple
from multiprocessing import Pool
import hashlib
from typing import final

import numpy as np
from PIL import Image

pic_type = ['jpg', 'jpeg', 'png']
fir_dir, rec_dir = '重复图片', '无重复图片'
if not os.path.exists('./' + fir_dir):
    os.mkdir('./' + fir_dir)
if not os.path.exists(rec_dir):
    os.mkdir('./' + rec_dir)
src_path = os.getcwd()
dst_same_path = src_path + '\\' + fir_dir
dst_rec_path = src_path + '\\' + rec_dir

if __name__ == "__main__":
    hash_dict, hash_list = {}, []
    for file_name in os.listdir('./'):
        suffix = file_name.split('.')[-1].lower()
        if suffix in pic_type:
            with open(file_name, 'rb') as file:
                hash_value = hashlib.md5(file.read()).hexdigest()
                hash_dict[file_name] = hash_value
                hash_list.append(hash_value)
    final_dict, same_dict = {}, {}
    for k, v in hash_dict.items():
        if hash_list.count(v) == 1:  # 无重复
            final_dict[k] = v
        else:  # 有重复
            if list(final_dict.values()).count(v) == 0:  # 还没有时添加
                final_dict[k] = v
            same_dict.setdefault(v, [])
            same_dict[v].append(k)

    for name in final_dict.keys():
        shutil.copyfile(src_path + '\\' + name, dst_rec_path + '\\' + name)
    j = 0
    for f_list in same_dict.values():
        o = 0
        for name in f_list:
            rename = f'{j}({o})_{name}'
            shutil.copyfile(src_path + '\\' + name,
                            dst_same_path + '\\' + rename)
            o += 1
        j += 1
