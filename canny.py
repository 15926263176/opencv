import cv2

# 读取图像
img = cv2.imread('C://opencv//2.jpg')

# 将图像转换为灰度图像
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 进行边缘检测
edge = cv2.Canny(gray, 100, 200)

# 保存边缘检测后的图像
cv2.imwrite('edg.jpg', edge)