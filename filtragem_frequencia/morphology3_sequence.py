import cv2
import numpy as np
import matplotlib.pyplot as plt

def erode(img, kernel,n_iterations):
    erosion = cv2.erode(img, kernel, iterations=n_iterations)
    return erosion

def dilate(img, kernel,n_iterations):
    dilation = cv2.dilate(img, kernel, iterations=n_iterations)
    return dilation

def opening(img, kernel):
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    return opening

def closing(img, kernel):
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    return closing

def plot(img, morph_img, title):
    # Plot the images
    plt.figure(figsize=(6, 4))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(morph_img, cmap='gray')
    plt.title(title)
    plt.axis('off')

    plt.suptitle(title, fontsize=16)
    plt.tight_layout()
    plt.show()


def main():

    kernel1 = np.array([[1, 1, 1],
                        [1, 1, 1],
                        [1, 1, 1]], dtype=np.uint8)
    #image f
    img = cv2.imread('img/noise_rectangle.tif',cv2.IMREAD_GRAYSCALE)

    img_eroded = erode(img, kernel1,22)
    img_dilate = dilate(img_eroded, kernel1,37)

    plot(img, img_eroded, 'Erosão')
    plot(img_eroded, img_dilate, 'Final')

    #image g
    img = cv2.imread('img/text_gaps.tif',cv2.IMREAD_GRAYSCALE)

    img_closing = closing(img, kernel1)
    img_closing2 = closing(img, kernel1)
    img_dilate = dilate(img, kernel1,1)

    plot(img, img_closing, 'Closing')

    #plot(img_closing, img_closing2, 'Closing 2')
    plot(img_closing2, img_dilate, 'Final')

    #tirar borda img h
    img = cv2.imread('img/rosto_perfil.tif',cv2.IMREAD_GRAYSCALE)

    img_erode = erode(img, kernel1,1)

    borda = img - img_erode

    plot(img, borda, 'Borda')
    plot(img, borda, 'Final')


if __name__ == "__main__":
    main()