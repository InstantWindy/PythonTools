# *_*coding: utf-8 *_*
# Author --LiMing--

import os
import random
import shutil
import time


def copyFile(fileDir, class_name):
    image_list = os.listdir(fileDir)  # get image path
    image_number = len(image_list)

    train_number = int(image_number * train_rate)
    train_sample = random.sample(image_list, train_number)  # from image_list get 0.8 raito image.
    test_sample = list(set(image_list) - set(train_sample))
    sample = [train_sample, test_sample]

    # copy image to dst folder
    for k in range(len(save_dir)):
        if os.path.isdir(save_dir[k]):
            for name in sample[k]:
                # print('-----------------------------')
                # print(os.path.join(fileDir, name),os.path.join(save_dir[k] , name))
                # print('-----------------------------')
                shutil.copy(os.path.join(fileDir, name), os.path.join(save_dir[k], name))
        else:
            os.makedirs(save_dir[k] + class_name)
            for name in sample[k]:
                shutil.copy(os.path.join(fileDir, name), os.path.join(save_dir[k] + class_name + '/', name))


if __name__ == '__main__':
    time_start = time.time()

    '''
    首先划分好guns，然后根据guns划分balls
    '''
    # orignal image path
    origion_path = '/home/pcl/data/dataset_ball/'
    gun_train_dir = '/home/pcl/data/dataset_guns/train/'
    gun_test_dir = '/home/pcl/data/dataset_guns/test/'

    # save path
    save_train_dir = '/home/pcl/data/dataset_balls/train/'
    save_test_dir = '/home/pcl/data/dataset_balls/test/'
    save_dir = [save_train_dir, save_test_dir]
    for dirs in save_dir:
        if not os.path.exists(dirs):
            os.makedirs(dirs)

    pre_dir = [gun_train_dir, gun_test_dir]
    for i in range(len(pre_dir)):
        for file in os.listdir(pre_dir[i]):
            fname = os.path.basename(file)
            src_dir = os.path.join(origion_path, fname)
            dst_dir = os.path.join(save_dir[i], fname)
            shutil.copy(src_dir, dst_dir)
    print('------------------finish!----------------------')

    '''
    首先划分好guns，
    '''
    # # orignal image path
    # origion_path = '/home/pcl/data/dataset_gun/'
    # # save path
    # save_train_dir = '/home/pcl/data/dataset_guns/train/'
    # save_test_dir = '/home/pcl/data/dataset_guns/test/'
    # save_dir = [save_train_dir, save_test_dir]
    # for dirs in save_dir:
    #     if not os.path.exists(dirs):
    #         os.makedirs(dirs)
    # # # train set ratio
    # train_rate = 0.7
    # file_list = os.listdir(origion_path)
    # num_classes = len(file_list)
    # for i in range(num_classes):
    #     class_name = file_list[i]
    #     image_Dir = os.path.join(origion_path, class_name)
    #     print('-----------------------------')
    #     print('image_dir:',image_Dir)
    #     print('-----------------------------')
    #     copyFile(image_Dir, class_name)
    #     print('%s split finish' % class_name)

    time_end = time.time()
    print('---------------')
    print('total time: %s!' % (time_end - time_start))