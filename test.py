from pywebhdfs.webhdfs import PyWebHdfsClient
from pprint import pprint

hdfs = PyWebHdfsClient(host='192.168.43.181',port='9870')  # your Namenode IP & username here
my_dir = '/home'
pprint(hdfs.list_dir(my_dir))
