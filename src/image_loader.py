import cv2

img = cv2.imread("data/answer_sheet.png")

print(img.shape)

cv2.imshow("Answer Sheet", img)
cv2.waitKey(0)
cv2.destroyAllWindows()