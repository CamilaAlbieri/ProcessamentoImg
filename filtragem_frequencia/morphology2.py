import cv2
import numpy as np
import matplotlib.pyplot as plt

def morph_opening_closing(img, kernel):

    # Opening (Erosion followed by Dilation)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    # Closing (Dilation followed by Erosion)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    return opening, closing

def plot_images(img, opening, closing, title):
    # Plot the images
    plt.figure(figsize=(6, 4))

    plt.subplot(2, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(2, 2, 2)
    plt.imshow(opening, cmap='gray')
    plt.title('Opening')
    plt.axis('off')

    plt.subplot(2, 2, 3)
    plt.imshow(closing, cmap='gray')
    plt.title('Closing')
    plt.axis('off')

    plt.suptitle(title, fontsize=16)
    plt.tight_layout()
    plt.show()

def main():
    kernel1 = np.array([[0, 1, 0],
                        [1, 1, 1],
                        [0, 1, 0]], dtype=np.uint8)

    img1 = cv2.imread('img/Imagem2.tif',cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('img/fingerprint.tif',cv2.IMREAD_GRAYSCALE)
    img3 = cv2.imread('img/morfologia1.tif',cv2.IMREAD_GRAYSCALE)
    img4 = cv2.imread('img/morfologia2.tif',cv2.IMREAD_GRAYSCALE)


    opening, closing =  morph_opening_closing(img1, kernel1)
    plot_images(img1, opening, closing,'Image b')

    opening, closing =  morph_opening_closing(img2, kernel1)
    plot_images(img2, opening, closing,'Image c')

    opening, closing =  morph_opening_closing(img3, kernel1)
    plot_images(img3, opening, closing,'Image d')

    opening, closing =  morph_opening_closing(img4, kernel1)
    plot_images(img4, opening, closing,'Image e')


if __name__ == "__main__":
    main()

#Resposta 2
#
#Fechamento: 'b' e 'e' - Abertura: 'd' e 'c'