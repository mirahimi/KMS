import cv2
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the pretrained VGG16 model
model = VGG16(weights='imagenet')

def classify_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (224, 224))
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)

    preds = model.predict(img)
    decoded_preds = decode_predictions(preds, top=3)[0]  # Get top 3 predictions
    return decoded_preds

# Example usage
image_path = '/home/chin/Codes/KMS/OpenCV/image1.png'  # Replace 'example.jpg' with your image path
predictions = classify_image(image_path)
for pred in predictions:
    print(f'{pred[1]}: {pred[2]}')
