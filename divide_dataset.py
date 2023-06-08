import os
import random
import shutil


def split():
    path = r'E:\paper_data\MaSTr1325_masks_512x384'
    sapath = r'E:\1'
    files = os.listdir(path)
    test_rate = 2
    train_rate = 7
    val_rate = 1
    total_rate = test_rate + train_rate + val_rate

    # if not os.path.exists('train'):
    #     os.mkdir('train')
    # if not os.path.exists('test'):
    #     os.mkdir('test')
    # if not os.path.exists('val'):
    #     os.mkdir('val')
    files = os.listdir(path)
    # files.remove('train')
    # files.remove('test')
    lenf = len(files)
    lentest = (lenf * test_rate) // total_rate
    lentrain = (lenf * train_rate) // total_rate
    lenval = lenf - lentest - lentrain

        # 如果你需要同时移动标注(annotations)文件，假设你的标注文件为csv文件，
        # 与图片存储在一起，要将其与图像一并移入val文件夹
        # shutil.move(files[i][:-4]+'.csv','val')

    files = os.listdir(path)
    # files.remove('train')
    # files.remove('test')
    # lenf = len(files)
    indtest = random.sample(files, lentest)
    # print(indtest)
    for i in indtest:
        # print(i)
        shutil.move(os.path.join(path, i), os.path.join(sapath, 'test'))
        files.remove(i)
    indval = random.sample(files, lenval)
    for i in indval:
        shutil.move(os.path.join(path, i), os.path.join(sapath, 'val'))
        files.remove(i)
    # files.remove('train')
    for i in files:
        shutil.move(os.path.join(path, i), os.path.join(sapath, 'train'))


def remove():
    path = r'E:\train\test'
    path1 = r'E:\paper_data\MaSTr1325_masks_512x384'
    path2 = r'E:\mask1\test'
    imglist = os.listdir(path)
    for i in imglist:
        i = i[:-4] + 'm.png'
        # print(i)
        shutil.move(os.path.join(path1, i), os.path.join(path2))


def make_text():
    path = r'E:\train\test'
    imglist = os.listdir(path)
    f = open(path + '/test.txt', 'w')
    for i in imglist:
        f.write('images' + '/' + i + ' ' + 'mask' + '/' +i[:-4] + 'm.png' + '\n')


if __name__ == '__main__':
    make_text()
