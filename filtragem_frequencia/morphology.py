import cv2
import numpy as np
import matplotlib.pyplot as plt

def apply_morph_operations(img, kernel):
    # Erosion
    erosion = cv2.erode(img, kernel, iterations=1)

    # Dilation
    dilation = cv2.dilate(img, kernel, iterations=1)

    # Opening (Erosion followed by Dilation)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    # Closing (Dilation followed by Erosion)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

    return erosion, dilation, opening, closing



def plot_images(original, erosion, dilation, opening, closing):
    fig = plt.figure(figsize=(12, 8))

    ax = fig.add_subplot(1, 5, 1)
    ax.imshow(1-original, cmap='gray')
    ax.set_title('Original')

    ax = fig.add_subplot(1, 5, 2)
    ax.imshow(1-erosion, cmap='gray')
    ax.set_title('Erosion')

    ax = fig.add_subplot(1, 5, 3)
    ax.imshow(1-dilation, cmap='gray')
    ax.set_title('Dilation')

    ax = fig.add_subplot(1, 5, 4)
    ax.imshow(1-opening, cmap='gray')
    ax.set_title('Opening')

    ax = fig.add_subplot(1, 5, 5)
    ax.imshow(1-closing, cmap='gray')
    ax.set_title('Closing')

    plt.show()
def main():
    # Exemplo de imagem simples, pode ser adaptado para as imagens dos exercícios
    img = cv2.imread('img_morphy/Imagem1.tif', cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread('img_morphy/Imagem2.tif', cv2.IMREAD_GRAYSCALE)
    img3 = cv2.imread('img_morphy/fingerprint.tif', cv2.IMREAD_GRAYSCALE)
    img4 = cv2.imread('img_morphy/morfologia1.tif', cv2.IMREAD_GRAYSCALE)
    img5 = cv2.imread('img_morphy/morfologia2.tif', cv2.IMREAD_GRAYSCALE)
    img6 = cv2.imread('img_morphy/noise_rectangle.tif', cv2.IMREAD_GRAYSCALE)
    img7 = cv2.imread('img_morphy/rosto_perfil.tif', cv2.IMREAD_GRAYSCALE)
    img8 = cv2.imread('img_morphy/text_gaps.tif', cv2.IMREAD_GRAYSCALE)

    kernel1 = np.array([[0, 1, 0],
                        [1, 1, 1],
                        [0, 1, 0]], dtype=np.uint8)


    # Aplicar operações morfológicas com o elemento cruzado
    erosion, dilation, opening, closing = apply_morph_operations(img, kernel1)
    plot_images(img, erosion, dilation, opening, closing)

    erosion, dilation, opening, closing = apply_morph_operations(img2, kernel1)
    plot_images(img2, erosion, dilation, opening, closing)

    erosion, dilation, opening, closing = apply_morph_operations(img3, kernel1)
    plot_images(img3, erosion, dilation, opening, closing)

    erosion, dilation, opening, closing = apply_morph_operations(img4, kernel1)
    plot_images(img4, erosion, dilation, opening, closing)

    erosion, dilation, opening, closing = apply_morph_operations(img5, kernel1)
    plot_images(img5, erosion, dilation, opening, closing)

    erosion, dilation, opening, closing = apply_morph_operations(img6, kernel1)
    plot_images(img6, erosion, dilation, opening, closing)

    erosion, dilation, opening, closing = apply_morph_operations(img7, kernel1)
    plot_images(img7, erosion, dilation, opening, closing)

    erosion, dilation, opening, closing = apply_morph_operations(img8, kernel1)
    plot_images(img, erosion, dilation, opening, closing)

if __name__ == "__main__":
    main()