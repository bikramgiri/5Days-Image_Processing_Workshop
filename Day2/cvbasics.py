# Python program to explain cv2.imshow() method

# importing cv2
import cv2

# path
path = r'./rajeshdai.jpg'

# Reading an image in default mode
imageColor = cv2.imread(path)

# Window name in which image is displayed
window_name = 'rajeshsir'

# Using cv2.imshow() method
# Displaying the image
cv2.imshow(window_name, imageColor)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)
print("Rajesh Dai in color")
print(imageColor)
cv2.waitKey()


imageBW = cv2.imread(path,0) #grayscale read
# print(image)
cv2.imshow("b&w",imageBW)
cv2.waitKey()
print("Rajesh Dai in BW")
print(imageBW)
cv2.waitKey()



image2 = cv2.imread(r'ORL(old)\p1\8.jpg',0)
cv2.imshow("1st ORl image",image2)
cv2.waitKey()
print("1st orl image")
print(type(image2))
print(image2)

print("new line \n")
cv2.waitKey()

imageB = cv2.imread(r'ORL(new)\s1\1.pgm',0)
image3=cv2.resize(imageB,(50,50))
cv2.imshow("2nd ORL image",image3)
cv2.waitKey()
print("2nd orl image") #2nd orl image
print(type(image3)) #2nd orl image
print(image3) #2nd orl image

print("shape of images") #shape of images
print(image2.shape) #shape of images
print(image3.shape) #shape of images
 
# closing all open windows
cv2.destroyAllWindows()