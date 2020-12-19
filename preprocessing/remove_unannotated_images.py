import os
import sys
if len(sys.argv)< 3:
    print("Usage: \n python remove_unannotated_images.py path_to_images path_to_annotations")
    exit()
filelist= os.listdir(sys.argv[1])
annotationlist= []

with open(sys.argv[2]+'_annotations.txt') as f:
        for line in f:
            annotationlist.append(line.split()[0])
            if line.split()[0] in filelist:
                filelist.remove(line.split()[0])


for file in filelist:
    if file[-1]=='g':
        os.remove(sys.argv[1]+'/'+file)
        print("Removed {}".format(sys.argv[1]+'/'+file))
               