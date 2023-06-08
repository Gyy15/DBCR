import os
import cv2
import numpy as np
import torch
import torch.nn as nn
from PIL.Image import Image
import random
import shutil

a = torch.load(r'E:\Code\yolov5-master（ASFF）\runs\train\end\WSODD_v5s6_Trans_Res_Carafe(highest_2)\weights\best.pt')
print(a)
# new_list = []
# path = r'E:\paper_data\WSODD USV_dataset\WSODD USV_dataset\test'
# imglist = os.listdir(path)
# random.shuffle(imglist)
#
# for i in range(0, 10):
#     shutil.move(os.path.join(path, imglist[i]), r'E:\paper_data\test')