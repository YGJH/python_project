# import matplotlib.pyplot as plt
# import cv2
# import numpy as np

# image = cv2.imread("CatchaImage.jpg")
# if image is None:
#     print("Image not found or path is incorrect.")
#     exit()
# # else:
# #     image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# #     plt.imshow(image_rgb)
# #     plt.show()



# kernel = np.ones((1,1) , np.uint8)
# image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY) #grayscale conversion
# plt.imshow(image)
# plt.show()

# erosion = cv2.erode(image , kernel , iterations = 1)
# plt.imshow(erosion)
# plt.show()

# kernel_size = 3
# blur_gray = cv2.GaussianBlur(image,(kernel_size, kernel_size), 0)
# # blurred = cv2.GaussianBlur(erosion , (7, 7) , 0)
# plt.imshow(blur_gray)
# plt.show()

# edged = cv2.Canny(blur_gray , 100 , 300)

# # plt.imshow(edged)
# # plt.show()
# dilation = cv2.dilate(edged , np.ones((2,2),np.uint8) , iterations=1)
# plt.imshow(dilation)
# plt.show()

# contours, hierarchy = cv2.findContours(dilation.copy() , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# cnts = sorted([(c , cv2.boundingRect(c)[0]) for c in contours], key = lambda x : x[1])

# ary = []
# for (c,_) in cnts:
#     (x,y,w,h) = cv2.boundingRect(c)
#     if w > 10 and h + 10:
#         ary.append((x,y,w,h))


# fig = plt.figure()
# for id, (x,y,w,h) in enumerate(ary):
#     roi = dilation[y:y + h , x:x + w]
#     thresh = roi.copy()
#     a=fig.add_subplot(1,len(ary),id+1)
#     plt.imshow(thresh)
#     plt.show()


import pytesseract
from PIL import Image

image = Image.open('CatchaImage.png')
result = pytesseract.image_to_string(image)
print(result)