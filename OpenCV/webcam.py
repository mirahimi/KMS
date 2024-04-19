import cv2

# Open the webcam
cap = cv2.VideoCapture(0)

# Capture frame-by-frame
ret, frame = cap.read()

# Save the resulting frame to an image file
cv2.imwrite('webcam_image.jpg', frame)

# When everything is done, release the capture
cap.release()
