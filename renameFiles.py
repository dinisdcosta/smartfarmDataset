import os
import shutil

dir = r'C:\Users\Dinis\Desktop\smartfarmDataset\Images'
dir1 = r'C:\Users\Dinis\Desktop\smartfarmDataset\Images1'
machines = os.listdir(dir)
for machine in machines:
    labels = os.listdir(dir+'\\'+machine)
    for label in labels:
        images = os.listdir(dir+'\\'+machine+'\\'+label)
        for num,image in enumerate(images):
            src = dir+'\\'+machine+'\\'+label+'\\'+image
            dst = dir1+'\\'+machine+'\\'+label+'\\'+machine+'_'+label+'_'+str(num)+'.jpg'
            shutil.copy(src,dst)