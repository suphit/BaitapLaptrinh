#cài thêm thư viện PIL để sử dụng

from PIL import Image
import numpy as np

col = Image.open("bird.png")
gray = col.convert('L')

bw = np.asarray(gray).copy()
bw[bw < 128] = 0  #các pixel <128 chuyển về màu đen
bw[bw >= 128] = 255 #các pixel >128 chuyển về màu trắng
imfile = Image.fromarray(bw)
imfile.save("1after.png") #lưu lại ảnh đen trắng
imshow