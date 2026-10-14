
import cv2
import matplotlib.pyplot as plt

# Read the sample image
image = cv2.imread("sample.jpg")

if image is None:
    print("Error: Image not found!")
else:
    # Convert original image to RGB
    original = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display original and grayscale images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(gray, cmap="gray")
    plt.title("Grayscale Image")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    # Save grayscale image
    cv2.imwrite("grayscale_output.jpg", gray)
    print("Practical 1 completed successfully!")
