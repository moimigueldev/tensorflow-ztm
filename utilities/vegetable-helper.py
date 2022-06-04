import os
import random
import shutil
import glob
from socket import SHUT_RD
from os import rename
from pathlib import Path

rice_names = ['Capsicum', 'Radish', 'Pumpkin', 'Cauliflower', 'Potato', 'Bean', 'Cucumber',
              'Brinjal', 'Cabbage', 'Broccoli', 'Bitter_Gourd', 'Papaya', 'Bottle_Gourd', 'Tomato', 'Carrot']
directory_path = 'vegetebles/train'

# print(len(os.listdir(directory_path)))


# RENAME FILES
# removes all the spaces
# paths = (os.path.join(root, filename)
#          for root, _, filenames in os.walk('/Users/moisesmiguel/code/ml/tensorflow-ztm/utilities/rice-images')
#          for filename in filenames)

# for path in paths:
#     # the '#' in the example below will be replaced by the '-' in the filenames in the directory
#     # newname = path.replace('#', '-')
#     # if newname != path:
#     os.rename(path, path.replace(' ', ''))
#     print(path)


# print(os.listdir(f'{directory_path}/{rice_names[0]}'))
# /Users/moisesmiguel/code/ml/tensorflow-ztm/utilities/rice-images/Arborio/Arborio(1).jpg

target_dir = 'vegetebles/train'
type_dir = 'test_3_percent'
# number_of_samples = 12000  # 80% training
number_of_samples = 300  # # 5% percent


# for name in rice_names:
#     print(name)

# os.chdir('source_image_dir_path')
# dst_dir = "your_destination_dir_path"

# WORKING EXAMPLE (training)
# os.mkdir(type_dir)
# for _, i in enumerate(rice_names):
#     os.mkdir(os.path.abspath(f'{type_dir}/{i}'))
#     list = sorted(os.listdir(
#         f'/Users/moisesmiguel/code/ml/tensorflow-ztm/utilities/rice-images/{i}/'))[:number_of_samples]
#     for f in list:
#         original_path = Path(os.path.abspath(f'{directory_path}/{i}/{f}'))
#         destination = Path(os.path.abspath(f'{type_dir}/{i}'))
#         shutil.copy(original_path, destination)

# WORKING EXAMPLE (testing)
# for _, i in enumerate(rice_names):
#     os.mkdir(os.path.abspath(f'{type_dir}/{i}'))
#     list = sorted(os.listdir(
#         f'/Users/moisesmiguel/code/ml/tensorflow-ztm/utilities/rice-images/{i}/'))[-number_of_samples:]
#     for f in list:
#         original_path = Path(os.path.abspath(f'{directory_path}/{i}/{f}'))
#         destination = Path(os.path.abspath(f'{type_dir}/{i}'))
#         shutil.copy(original_path, destination)

# for f in sorted(os.listdir('/Users/moisesmiguel/code/ml/tensorflow-ztm/utilities/rice-images/Arborio/'))[:5]:
#     # shutil.copy(f, dst_dir)
#     print(f)

# list = sorted(os.listdir(
#     '/Users/moisesmiguel/code/ml/tensorflow-ztm/utilities/rice-images/Arborio/'))[:number_of_samples]
# print(os.path.join('rice-images/Arborio/Arborio(1).jpg'))

# file_name = '/Users/moisesmiguel/code/ml/tensorflow-ztm/utilities/rice-images/Arborio/Arborio (1).jpg'.replace(" ", "")


# shutil.copyfile('/Users/moisesmiguel/code/ml/tensorflow-ztm/utilities/rice-images/Arborio/Arborio(1).jpg',
#                 '/Users/moisesmiguel/code/ml/tensorflow-ztm/utilities/train/rice-images/Arborio/Arborio(1).jpg')


# print(len(os.listdir(f'{type_dir}/Arborio')))
# print(len(os.listdir('rice-images/Arborio')))
# train_list = sorted(os.listdir('train/Arborio'))
# test_list = sorted(os.listdir('test/Arborio'))

# for train_el in train_list:
#     print(train_el)
#     for test_el in test_list:
#         if test_el == train_el:
#             print('yes', test_el)


def clean_spaces(path):
    """
    Walks through all directories within the provided path. 
    Goes through each file and removes spaces in file names.
    """

    paths = (os.path.join(root, filename)
             for root, _, filenames in os.walk(path)
             for filename in filenames)

    for path in paths:
        os.rename(path, path.replace(' ', ''))


def create_dir(type_dir='train', number_of_samples=1200):
    # WORKING EXAMPLE (training)
    """
    Using 'train' in type_dir makes it so it picks number_of_samples from the top of sorted list
    Using 'test' in your type_dir makes it so it picks number_of_samples from the bottom of sorted list
    """
    os.mkdir(type_dir)
    for _, i in enumerate(rice_names):
        os.mkdir(os.path.abspath(f'{type_dir}/{i}'))

        if(type_dir.__contains__('train')):
            print('type: train')
            list = sorted(os.listdir(
                f'/Users/moisesmiguel/code/ml/tensorflow-ztm/utilities/{directory_path}/{i}/'))[:number_of_samples]
        else:
            print('type: test')
            list = sorted(os.listdir(
                f'/Users/moisesmiguel/code/ml/tensorflow-ztm/utilities/{directory_path}/{i}/'))[-number_of_samples:]
        for f in list:
            original_path = Path(os.path.abspath(f'{directory_path}/{i}/{f}'))
            destination = Path(os.path.abspath(f'{type_dir}/{i}'))
            shutil.copy(original_path, destination)


# clean_spaces('/Users/moisesmiguel/code/ml/tensorflow-ztm/utilities/rice-images')
# print('train'.__contains__('train'))
# print('train_5_percent'.__contains__('train'))
# print('5_test_percent'.__contains__('test'))

# Train 80%
# create_dir(type_dir='train_30', number_of_samples=300)

# # train 5%
# create_dir(type_dir='train_5', number_of_samples=750)

# # train 5%
# create_dir(type_dir='train_3', number_of_samples=450)

# # Test 20%
# create_dir(type_dir='test_20', number_of_samples=3000)

# train_list = sorted(os.listdir('train_80/Arborio'))
# test_list = sorted(os.listdir('test_20/Arborio'))


# def check_dups(dir_1, dir_2):

#     # example: check_dups(os.listdir('test_20/Arborio'), os.listdir('train_80/Arborio'))

#     dir_1 = sorted(dir_1)
#     dir_2 = sorted(dir_2)
#     doubles = False

#     for train_el in dir_1:
#         for test_el in dir_2:
#             if test_el == train_el:
#                 print('yes', test_el)
#                 doubles = True

#     return doubles


# check_dups(os.listdir('test_20/Arborio'), os.listdir('train_80/Arborio'))

print(len(os.listdir(f'train_30/Bean')))
