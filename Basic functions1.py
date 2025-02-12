import cv2,os
img=cv2.imread("opencv-assets-main\star addition.jpeg")
img2=cv2.imread("opencv-assets-main\diamond addition.jpeg")
sum=cv2.addWeighted(img,0.1,img2,0.9,1)
cv2.imshow("sum",sum)
cv2.waitKey(0)
test=cv2.subtract(img,img2)
cv2.imshow("test",test)
cv2.waitKey(0)
ghost=cv2.imread("opencv-assets-main\ghost.png")
ghost_small=cv2.resize(ghost,(100,100))
cv2.imshow("ghost_small",ghost_small)
cv2.waitKey(0)
blur1=cv2.imread("opencv-assets-main\Bilateral.jpg")
g_blur=cv2.GaussianBlur(blur1,(31,31),sigmaX=0,sigmaY=0)
cv2.imshow("g_blur",g_blur)
cv2.waitKey(0)
b_blur=cv2.bilateralFilter(blur1,21,sigmaColor=51.5,sigmaSpace=7.7)
cv2.imshow("b_blur",b_blur)
cv2.waitKey(0)
salt=cv2.imread("opencv-assets-main\salt and pepper grains.jpeg")
grains=cv2.medianBlur(salt,5)
cv2.imshow("grains",grains)
cv2.waitKey(0)
# try out these blurs and addition & subtraction on different images! ( you might want to resize the images!
