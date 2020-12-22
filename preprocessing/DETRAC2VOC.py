

import xml.etree.ElementTree as ET
from xml.dom.minidom import Document
import os
import time
import sys

def ConvertVOCXml(file_path="",file_name=""):
   tree = ET.parse(file_name)
   root = tree.getroot()
   # print(root.tag)

   num=0 


   frame_lists=[]
   output_file_name=""
   for child in root:

      if(child.tag=="frame"):

         doc = Document()

         annotation = doc.createElement('annotation')

         doc.appendChild(annotation)

         #print(child.tag, child.attrib["num"])
         pic_id= child.attrib["num"].zfill(5)
         #print(pic_id)
         output_file_name=root.attrib["name"]+"_img"+pic_id+".xml"
        #  print(output_file_name)

         folder = doc.createElement("folder")
         folder.appendChild(doc.createTextNode("VOC2007"))
         annotation.appendChild(folder)

         filename = doc.createElement("filename")
         pic_name=root.attrib["name"]+"_img"+pic_id+".jpg"
         filename.appendChild(doc.createTextNode(pic_name))
         annotation.appendChild(filename)

         sizeimage = doc.createElement("size")
         imagewidth = doc.createElement("width")
         imageheight = doc.createElement("height")
         imagedepth = doc.createElement("depth")

         imagewidth.appendChild(doc.createTextNode("960"))
         imageheight.appendChild(doc.createTextNode("540"))
         imagedepth.appendChild(doc.createTextNode("3"))

         sizeimage.appendChild(imagedepth)
         sizeimage.appendChild(imagewidth)
         sizeimage.appendChild(imageheight)
         annotation.appendChild(sizeimage)

         target_list=child.getchildren()[0]  
         #print(target_list.tag)
         object=None
         for target in target_list:
             if(target.tag=="target"):
                 #print(target.tag)
                 object = doc.createElement('object')
                 bndbox = doc.createElement("bndbox")

                 for target_child in target:
                     if(target_child.tag=="box"):
                         xmin = doc.createElement("xmin")
                         ymin = doc.createElement("ymin")
                         xmax = doc.createElement("xmax")
                         ymax = doc.createElement("ymax")
                         xmin_value=int(float(target_child.attrib["left"]))
                         ymin_value=int(float(target_child.attrib["top"]))
                         box_width_value=int(float(target_child.attrib["width"]))
                         box_height_value=int(float(target_child.attrib["height"]))
                         xmin.appendChild(doc.createTextNode(str(xmin_value)))
                         ymin.appendChild(doc.createTextNode(str(ymin_value)))
                         if(xmin_value+box_width_value>960):
                            xmax.appendChild(doc.createTextNode(str(960)))
                         else:
                            xmax.appendChild(doc.createTextNode(str(xmin_value+box_width_value)))
                         if(ymin_value+box_height_value>540):
                            ymax.appendChild(doc.createTextNode(str(540)))
                         else:
                            ymax.appendChild(doc.createTextNode(str(ymin_value+box_height_value)))

                     if(target_child.tag=="attribute"):
                         name = doc.createElement('name')
                         pose=doc.createElement('pose')
                         truncated=doc.createElement('truncated')
                         difficult=doc.createElement('difficult')

                         name.appendChild(doc.createTextNode(target_child.attrib["vehicle_type"]))
                         pose.appendChild(doc.createTextNode("Left"))  
                         truncated.appendChild(doc.createTextNode("0")) 
                         difficult.appendChild(doc.createTextNode("0"))  

                         
                         object.appendChild(name)
                         object.appendChild(pose)
                         object.appendChild(truncated)
                         object.appendChild(difficult)
                         
                 bndbox.appendChild(xmin)
                 bndbox.appendChild(ymin)
                 bndbox.appendChild(xmax)
                 bndbox.appendChild(ymax)
                 object.appendChild(bndbox)
                 annotation.appendChild(object)


         file_path_out=os.path.join(file_path,output_file_name)
         f = open(file_path_out, 'w')
         f.write(doc.toprettyxml(indent=' ' * 4))
         f.close()
         num=num+1
   return num

if ( __name__ == "__main__"):
   #print("main")
   if len(sys.argv) <2:
      print("Usage: \n python DETRAC2VOC.py path_to_DETRAC-Train-Annotations-XML-v3_folder")
      exit()
   basePath=sys.argv[1]
   totalxml=os.listdir(basePath)
   total_num=0
   flag=False

   saveBasePath="VOC_XML"
   if os.path.exists(saveBasePath)==False: 
        os.makedirs(saveBasePath)

   start = time.time()
   log=open("xml_statistical.txt","w") 
   for xml in totalxml:
     file_name=os.path.join(basePath,xml)
     print(file_name)
     num=ConvertVOCXml(file_path=saveBasePath,file_name=file_name)
     print(num)
     total_num=total_num+num
     log.write(file_name+" "+str(num)+"\n")
   # End time
   end = time.time()
   seconds=end-start
   print( "Time taken : {0} seconds".format(seconds))
   print(total_num)
   log.write(str(total_num)+"\n")
