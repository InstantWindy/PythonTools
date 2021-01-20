
import os
import random
import shutil
import time
import glob

download_path = 'dataset_unlabel'
save_gun_dir = 'SR/dataset_guns/'
save_ball_dir = 'SR/dataset_balls/'

save_dir = [save_gun_dir, save_ball_dir]
for dirs in save_dir:
    if not os.path.exists(dirs):
        os.makedirs(dirs)

i = 8083
for root, dirs, files in os.walk(download_path):
    # root:dataset_unlabel\search_cam2\374
    # dirs:[]
    # files:['259_ball.jpg', '259_gun.jpg']
    if not dirs:
        list_files = sorted(glob.glob(os.path.join(root, '*.jpg')))
        for idx, f in enumerate(list_files):
            print(f)
            filename = os.path.basename(f)
            fname,flag=filename.split('_')
            # print(flag)
            if flag=='gun.jpg':
                shutil.copy(os.path.join(f), os.path.join(save_gun_dir,str(i)+'_'+fname+'.jpg'))
            elif flag=='ball.jpg':
                shutil.copy(os.path.join(f), os.path.join(save_ball_dir,str(i)+'_'+fname+'.jpg'))
            else:
                print('error')
            if (idx+1) % 2==0:
                i+=1




# list_files=sorted(glob.glob(os.path.join(download_path, '*.jpg')))
# print('total images:',len(list_files))
# i = 8083
# for idx, f in enumerate(list_files):
#     print(f)
#     filename = os.path.basename(f)
#     fname,flag=filename.split('_')
#     if flag=='gun':
#         shutil.copy(os.path.join(f), os.path.join(save_gun_dir,str(i)+fname, '.jpg'))
#     elif flag=='ball':
#         shutil.copy(os.path.join(f), os.path.join(save_ball_dir,str(i)+fname, '.jpg'))
#     else:
#         print('error')
#     if (idx+1) % 2==0:
#         i+=1


