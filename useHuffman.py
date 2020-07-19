from huffman import HuffmanCoding
import sys
from pathlib import Path
import time

import cv2
path = "tiger.bmp"

image = cv2.imread(path, 0)
cv2.imwrite("tiger_gray.bmp", image)
h = HuffmanCoding(path)

output_path, image_shape = h.compress()
print("Compressed file path: " + output_path)
a = Path("tiger_gray.bmp").stat().st_size
b = Path(output_path).stat().st_size

print("Calculating size")
for i in range(10):
  print(".", end = '')
  time.sleep(1)
decom_path = h.decompress(output_path, image_shape)

print ("compression percent" , 100*(a - b)/a)
print("Decompressed file path: " + decom_path) 
