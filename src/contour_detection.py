import cv2

img = cv2.imread(
    "data/binary_answer_sheet.png",
    cv2.IMREAD_GRAYSCALE
)

# DAY 4.2 - DILATION
kernel = cv2.getStructuringElement(
    cv2.MORPH_RECT,
    (7,7)
)

dilated = cv2.dilate(
    img,
    kernel,
    iterations=1
)

contours, hierarchy = cv2.findContours(
    dilated,   # <- use dilated image
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

# Convert grayscale to color for drawing
box_img = cv2.cvtColor(
    dilated,   # <- visualize dilated image
    cv2.COLOR_GRAY2BGR
)

for contour in contours:

    area = cv2.contourArea(contour)

    if area > 100:

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            box_img,
            (x, y),
            (x+w, y+h),
            (0,255,0),
            2
        )

        print(
            "Area:",
            area,
            "Position:",
            x, y,
            "Size:",
            w, h
        )

cv2.imshow("Original Binary", img)
cv2.imshow("Dilated Image", dilated)
cv2.imshow("Bounding Boxes", box_img)

cv2.waitKey(0)
cv2.destroyAllWindows()