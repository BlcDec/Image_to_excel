import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('C:/Users/blcdec/project/learn/source/test1.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#灰度图像


edges = cv2.Canny(gray,50,200)
plt.subplot(121),plt.imshow(edges,'gray')
plt.xticks([]),plt.yticks([])
#hough transform
lines = cv2.HoughLines(edges,1,np.pi/180,160)
lines1 = lines[:,0,:]#提取为为二维
# i=0
# font=cv2.InitFont(cv2.CV_FONT_HERSHEY_SCRIPT_SIMPLEX, 1, 1, 0, 3, 8)

points=[[0 for x in range (2)]for y in range (100)]

#print(points)
for rho,theta in lines1[:]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),1)
    # cv2.putText(img,i,(x1,y1),font,(0,255,0))
    # cv2.putText(img, i, (x2, y2),font,(0,255,0))
    # i+=1
    # 画圆1——有规律的画圆
    cv2.circle(img, (100,400),10,(0,255,0),3)  # circle(图像，圆心，半径，颜色)
   # cv2.circle(img, (x2, y2), 10, (0, 0, 0), 2)  # circle(图像，圆心，半径，颜色)
    print(x1,y1,x2,y2)
    num=[x1,y1]
    points.append(num)
    num=[x2,y2]
    points.append(num)

sorted(points,key=lambda x:x[1])
print(points)
plt.subplot(122),plt.imshow(img,)
plt.xticks([]),plt.yticks([])
cv2.imwrite('C:/Users/blcdec/project/learn/source/houghlines3.jpg', img)