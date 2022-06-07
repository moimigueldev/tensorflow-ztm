import os
import shutil
from pathlib import Path

class_names = ['dogs', 'cats']
directory_path = 'train_10_percent'

# print(len(os.listdir(directory_path + '/' + 'dogs')))
# print(len(os.listdir(directory_path + '/' + 'cats')))


def check_dups(dir_1, dir_2):
    dir_1 = sorted(dir_1)
    dir_2 = sorted(dir_2)
    doubles = False

    for train_el in dir_1:
        for test_el in dir_2:
            if test_el == train_el:
                print('yes', test_el)
                doubles = True

    return doubles


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
    for _, i in enumerate(class_names):
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


# clean_spaces('/Users/moisesmiguel/code/ml/tensorflow-ztm/utilities/pet-images')
# Train full
# create_dir(type_dir='train_10_percent', number_of_samples=400)
# check_dups(os.listdir('train_10_percent/dogs'), os.listdir('test/dogs'))
