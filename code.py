import cv2

image = cv2.imread('G:\Python\Image test\Resize image\orginal image.jpg', cv2.IMREAD_UNCHANGED)

scale_percent = 20

# calculate the 50 percent of original dimensions
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)

# resize image
resized = cv2.resize(image, (width, height))

cv2.imwrite('resized image.jpg', resized)
cv2.imshow('Orginal image', image)
cv2.imshow('Resized image', resized)
cv2.waitKey(0)