from pywebhdfs.webhdfs import PyWebHdfsClient
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import numpy as np
import os
import sys
from fibrose_import import Callback,EarlyStopping
hdfs = PyWebHdfsClient(host='192.168.43.56',port='9870',user_name='root')  # your Namenode IP & username here
path_data_f0 = '/faari/F0'
path_data_f4 = '/faari/F4'

sys.path.append(path_data_f0)
sys.path.append(path_data_f4)

path2dataf0 = os.path.join(path_data_f0)
path2dataf4 = os.path.join(path_data_f4) 

statusf0=hdfs.list_dir(path_data_f0)['FileStatuses']['FileStatus']
statusf4=hdfs.list_dir(path_data_f4)['FileStatuses']['FileStatus']

full_filenames0=[i['pathSuffix'] for i in statusf0]
full_filenames4=[i['pathSuffix'] for i in statusf4]

full_files0 = [os.path.join(path2dataf0,f) for f in full_filenames0]
full_files4 = [os.path.join(path2dataf4,f) for f in full_filenames4]

data=full_files0+full_files4
datadf=pd.DataFrame(columns=["id","path","label","niveau fibrose"])
for i in full_files0:
     if "f0" in i:
          i=i.replace(path_data_f0,"")
          datadf=datadf.append({"id":i,"path":path_data_f0,"label":0,"niveau fibrose":"F0-f0"},ignore_index=True)
     elif "f1" in i:
          i=i.replace(path_data_f0,"")
          datadf=datadf.append({"id":i,"path":path_data_f0,"label":0,"niveau fibrose":"F0-f1"},ignore_index=True)
for i in full_files4:
     if "f2" in i:
          i=i.replace(path_data_f4,"")
          datadf=datadf.append({"id":i,"path":path_data_f4,"label":1,"niveau fibrose":"F4-f2"},ignore_index=True)
     elif "f4" in i:
          i=i.replace(path_data_f4,"")
          datadf=datadf.append({"id":i,"path":path_data_f4,"label":1,"niveau fibrose":"F4-f4"},ignore_index=True)
          
early_stop_callback = EarlyStopping(
   monitor='val_loss',
   patience=3,
   verbose=False,
   mode='min'
)
