import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("image.jpg")

# Check if image is loaded
if image is None:
    print("Image not found. Check the image name and folder.")
else:
    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Show original image
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    # Show grayscale image
    plt.subplot(1, 2, 2)
    plt.imshow(gray_image, cmap="gray")
    plt.title("Gray-Scale Image")
    plt.axis("off")

    plt.show()
