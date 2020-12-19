import os
from PIL import Image
import sys

if len(sys.argv) < 3:
    print("Usage: \n python3 resize.py image_dir output_dir")
    exit()

print(sys.argv[1])
input_path=sys.argv[1]
output_path= sys.argv[2]
newsize= (416,416)

for i in os.listdir(input_path):
    if i[-1]=='g':
        print(i)
        img= Image.open(input_path+i)
        img1= img.resize(newsize)
        img1.save(output_path+i)
        