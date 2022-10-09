import cv2

img = cv2.imread("solar-system.jpg")
cv2.imshow("Output",img)

cv2.putText(img,
            "Sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )
cv2.putText(img,
            "Luna",
            (80,100),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )