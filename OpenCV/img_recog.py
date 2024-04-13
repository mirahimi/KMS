import numpy as np
from keras.applications import MobileNetV2
from keras.applications.mobilenet_v2 import preprocess_input
from keras.preprocessing import image
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC

# Load pre-trained MobileNetV2 model
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Function to extract features from images using MobileNetV2
def extract_features(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    features = base_model.predict(x)
    features = np.reshape(features, (features.shape[0], -1))
    return features

# Example image paths and corresponding labels
image_paths = ['image1.png', 'image2.png', 'image3.png']
labels = ['1', '2', '3']

# Extract features from images
X = np.array([extract_features(img_path) for img_path in image_paths])

# Encode labels
le = LabelEncoder()
y = le.fit_transform(labels)

# Train a Support Vector Machine (SVM) classifier
clf = SVC(kernel='linear')
clf.fit(X, y)

# Example image for prediction
test_image_path = 'test_image.jpg'

# Extract features from the test image
test_features = extract_features(test_image_path)

# Predict the label of the test image
predicted_label = clf.predict(test_features)[0]

# Decode the predicted label
predicted_class = le.inverse_transform([predicted_label])[0]

print("Predicted class:", predicted_class)
