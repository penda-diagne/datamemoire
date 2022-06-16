import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import numpy as np
import os
import sys
path_data_f0 = "hdfs://192.168.43.181:9870/home/datamemoire/F0"

sys.path.append(path_data_f0)

path2dataf0 = os.path.join(path_data_f0)

full_filenames0 = os.listdir(path2dataf0)

full_files0 = [os.path.join(path2dataf0,f) for f in full_filenames0]

data=full_files0
datadf=pd.DataFrame(columns=["id","path","label","niveau fibrose"])

datadf.head()
