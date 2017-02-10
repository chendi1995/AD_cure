import caffe
from create_filelist import *

caffe_root= '/home/cd/caffe/'
data_root='/disk/segate/ad_data/2016/'

def c_filelist():
    f = open(work_root + 'create_filelist.py', 'r')
    exec f
    f.close()

def img_convert():
    os.system('rm -rf ' + work_root + 'train_lmdb')
    os.system(caffe_root + 'build/tools/convert_imageset --shuffle --resize_height=256 --resize_width=256 ' + data_root + ' ' + work_root + 'train.txt ' + work_root + 'train_lmdb')
    ##print caffe_root+'build/tools/convert_imgset --shuffle --resize_height=256 --resize_width=256 '+data_root+' '+work_root+'train.txt '+work_root+'train_lmdb'
    os.system('rm -rf ' + work_root + 'test_lmdb')
    os.system(caffe_root + 'build/tools/convert_imageset --shuffle --resize_height=256 --resize_width=256 ' + data_root + ' ' + work_root + 'test.txt ' + work_root + 'test_lmdb')

def compute_mean():
    os.system(caffe_root+'build/tools/compute_image_mean '+work_root+'train_lmdb '+work_root+'mean.binaryproto')

if __name__=='__main__':
    #c_filelist()
    #img_convert()
    #compute_mean()
    caffe.set_device(0)
    caffe.set_mode_gpu()
    solver =caffe.SGDSolver('solver.prototxt')
    solver.solve()
