import cv2

img = cv2.imread("data/diag.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 15)

contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    area = cv2.contourArea(contour)

    if area<=3:
        cv2.drawContours(binary, [contour], -1, 0, thickness=cv2.FILLED)

cv2.imshow("Answer Sheet", img)
cv2.imshow("Binary Image", binary)
cv2.imwrite("data/binary_answer_sheet.png", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()