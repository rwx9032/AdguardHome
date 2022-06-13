import base64
import sys
import re
 
def ToFile(txt, file):
    with open(txt, 'r') as fileObj:
        base64_data = fileObj.read()
        ori_image_data = base64.b64decode(base64_data)
        fout = open(file, 'wb')
        fout.write(ori_image_data)
        fout.close()
        
ToFile("./gfwlist.txt",'gfwlist_deocode.txt')
