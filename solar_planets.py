import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,  
           "Sun",
           (10, 320),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1,  
           color=(255,0,0)
           )
cv2.putText(img,  
           "Mercury",
           (20, 250),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Venus",
           (40, 200),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Earth",
           (60, 200),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Mars",
           (80, 200),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Jupiter",
           (100, 300),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Saturn",
           (200, 270),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Uranus",
           (300, 260),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.putText(img,  
           "Neptune",
           (400, 250),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=0.5,  
           color=(255,255,255)
           )
cv2.imshow("output",img)
cv2.waitKey(0)