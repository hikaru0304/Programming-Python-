import os
from array import array

with open('binary.bin','rb') as f:
    data = f.read()
print(data)

# array로 가져오자
data = array.array('B')
with open('binary.bin','rb') as f:
    f.seek(0, os.SEEK_END) #파일 끝으로 간다.
    filesize = f.tell()
    f.seek()
    data.fromfile(f,filesize) #11111111_00000000_01111111
for item in data:
    print(item)