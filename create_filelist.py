work_root='/home/cd/ad_cure/'
caffe_root= '/home/cd/caffe/'
data_root='/disk/segate/ad_data/2016/'

import os
ad_train = data_root+'TRAIN/ADHC/AD/'
hc_train = data_root+'TRAIN/ADHC/HC/'
ad_test  = data_root+'TEST/TAH/AD/'
hc_test  = data_root+'TEST/TAH/HC/'

fp=open(work_root+'train.txt','w')


for dirname in os.listdir(ad_train):
    for name in os.listdir(ad_train + dirname):
        fp.write('TRAIN/ADHC/AD/'+dirname + '/' + name + ' 1' + '\n')

for dirname in os.listdir(hc_train):
    for name in os.listdir(hc_train + dirname):
        tmp='TRAIN/ADHC/HC/'+dirname + '/' + name
        if os.path.isfile(data_root+tmp):
            fp.write(tmp + ' 2'+'\n')
        else:
            for subname in os.listdir(data_root+tmp):
                fp.write(tmp+'/'+subname+' 2'+'\n')

fp.close()

fp=open(work_root+'test.txt','w')


for dirname in os.listdir(ad_test):
    for name in os.listdir(ad_test + dirname):
        fp.write('TEST/TAH/AD/'+dirname + '/' + name+ ' 1'+'\n' )

for dirname in os.listdir(hc_test):
    for name in os.listdir(hc_test + dirname):
        fp.write('TEST/TAH/HC/'+dirname + '/' + name + ' 2'+'\n')

fp.close()
