import os
from shutil import copyfile
import random
import shutil
'''
将枪球中的数据划分ReID格式的文件，先运行prepare_id.py文件，再运行prepare_data.py文件
'''
download_path = '/home/pcl/data/dataset_gun'
train_path = download_path + '/bounding_box_train'
train_save_path = '/home/pcl/data/data_guns' + '/bounding_box_train'
if not os.path.exists(train_save_path):
    os.makedirs(train_save_path)

for root, dirs, files in os.walk(train_path, topdown=True):
    for name in files:
        if not name[-3:]=='jpg':
            continue
        ID  = name.split('_')
        src_path = train_path + '/' + name
        dst_path = train_save_path + '/' + ID[0]
        if not os.path.isdir(dst_path):
            os.mkdir(dst_path)
        copyfile(src_path, dst_path + '/' + name)