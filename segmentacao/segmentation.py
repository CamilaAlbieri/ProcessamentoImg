import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
def plotar(img, img_new, nome, kernel):
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title('Imagem Original')
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    plt.subplot(1, 2, 2)
    plt.title(nome + kernel)
    plt.imshow(img_new, cmap='gray')
    plt.axis('off')
    plt.show()

def threshould(img, a, b):
    _, image_thresholded = cv2.threshold(img, a, b, cv2.THRESH_BINARY_INV)
    return image_thresholded

def convolucaoCV2(img, a, b, kernel, kernelName):
    image_filtered = cv2.filter2D(src=img, ddepth=-1, kernel=kernel)
    image_thresholded = threshould(image_filtered, a, b)
    plotar(img, image_filtered, "Imagem Filtrada com OpenCV", kernelName)
    plotar(img, image_thresholded, "Threshold", kernelName)
    return image_filtered, image_thresholded

def detector_bordas_canny(img, sigma, t1, t2):
    # Aplicar filtro gaussiano
    blurred = cv2.GaussianBlur(img, (5, 5), sigma)
    edges = cv2.Canny(blurred, t1, t2)
    plotar(img, blurred, "Imagem Borrada com Gaussiano", "")
    plotar(img, edges, "Detecção de Bordas com Canny", "")
    return edges

if __name__ == "__main__":

    img = Image.open('imgs/FolhaPontos.jpg')
    img2 = Image.open('imgs/FolhaPontosPC.png')
    img3 = Image.open('imgs/FingerPrint.tif')
    img4 = Image.open('imgs/car.tif')
    img5 = Image.open('imgs/biel.png')
    img6 = Image.open('imgs/lena.jpg')

    image = np.array(img.convert("L"))
    image2 = np.array(img2.convert("L"))
    image3 = np.array(img3.convert("L"))
    image4 = np.array(img4.convert("L"))
    image5 = np.array(img5.convert("L"))
    image6 = np.array(img6.convert("L"))

    img_np = np.array(image)
    img_np2 = np.array(image2)
    img_np3 = np.array(image3)
    img_np4 = np.array(image4)
    img_np5 = np.array(image5)
    img_np6 = np.array(image6)

    laplacian = np.array(([0, 1, 0],
                          [1, -4, 1],
                          [0, 1, 0]), dtype="int")
    
    laplacian2 = np.array(([1, 1, 1],
                           [1, -8, 1],
                           [1, 1, 1]), dtype="int")
    
    gauss = np.array(([0.0625, 0.125, 0.0625],
                      [0.1250, 0.250, 0.1250],
                      [0.0625, 0.125, 0.0625]), dtype="float")
    
    convolucaoCV2(img_np, 10, 255, laplacian, "Laplaciano")
    convolucaoCV2(img_np2, 10, 255, laplacian, "Laplaciano")

    plotar(img3, threshould(img_np3, 100, 255), "Imagem com Threshold", "")

    sigma = 1.5
    t1 = 100
    t2 = 255
    
    detector_bordas_canny(img_np4, sigma, t1, t2)
    detector_bordas_canny(img_np5, sigma, t1, t2)
    detector_bordas_canny(img_np6, sigma, t1, t2)