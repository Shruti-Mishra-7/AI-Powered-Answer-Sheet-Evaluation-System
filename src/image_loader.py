import cv2

img = cv2.imread("data/answer_sheet.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

print(img.shape)
print(gray.shape)

print("Original Pixel:", img[0][0])
print("Gray Pixel:", gray[0][0])

cv2.imshow("Answer Sheet", img)
cv2.imshow("Gray Scale", gray)
cv2.imwrite("data/gray_answer_sheet.png", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()