import os
from shutil import copyfile
import random
import shutil


def getData(srcdir, test_dstdir, train_dstdir):
    subDirs = os.listdir(srcdir)
    random.shuffle(subDirs)
    le = int(len(subDirs) * 0.8)  # 这个可以修改划分比例
    if not os.path.exists(query_save_path):
        os.makedirs(query_save_path)

    for dir in subDirs[:le]:
        train_tempDir = os.path.join(srcdir, dir)
        if not os.path.exists(train_dstdir):
            os.makedirs(train_dstdir)
        print('-------------train--------')
        print(train_tempDir)
        print()
        for f in os.listdir(train_tempDir):
            shutil.copyfile(os.path.join(train_tempDir, f), os.path.join(train_dstdir, f))

    for dir in subDirs[le:]:
        test_tempDir = os.path.join(srcdir, dir)
        if not os.path.exists(test_dstdir):
            os.makedirs(test_dstdir)
        print('------------test---------')
        print(test_tempDir)
        print()
        files = os.listdir(test_tempDir)
        random.shuffle(files)
        for i, f in enumerate(files):
            if i < 4:
                shutil.copyfile(os.path.join(test_tempDir, f), os.path.join(query_save_path, f))
            else:
                shutil.copyfile(os.path.join(test_tempDir, f), os.path.join(test_dstdir, f))

        # fs=os.listdir(tempDir)
        # random.shuffle(fs)
        # le=int(len(fs)*0.8)  #这个可以修改划分比例
        # for f in fs[le:]:
        # shutil.copyfile(os.path.join(tempDir,f),os.path.join(dstdir,f))


# srcdir = train_save_path
# download_path = '/home/pcl/data/reid/EDSR_gun240x480_X3/gun_reid'
download_path = '/home/pcl/data/7240_gun/gun_reid'
# download_path = '/home/pcl/data/reid/gun480x840_X3_dpsr_x3/gun_reid'
# srcdir = '/home/pcl/data/reid/gun480x840_X3_dpsr_x3/gun_data' + '/bounding_box_train'
srcdir = '/home/pcl/data/7240_gun/gun_data' + '/bounding_box_train'
# srcdir = '/home/pcl/data/reid/EDSR_gun240x480_X3/gun_data' + '/bounding_box_train'
query_save_path = download_path + '/query'
test_dstdir = download_path + '/bounding_box_test'
train_dstdir = download_path + '/bounding_box_train'
getData(srcdir, test_dstdir, train_dstdir)


