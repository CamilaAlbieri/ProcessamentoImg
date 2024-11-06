#Implementar a equalização do histograma manualmente e utilizando bibliotecas: OpenCV, Pillow, numpy, etc;

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps

def histogram_equalization_manual(image):
    # Calcula o histograma da imagem
    image = np.array(image)
    histogram, bins = np.histogram(image.flatten(), 256, [0, 256])
    cdf = histogram.cumsum()
    cdf_normalized = cdf * histogram.max() / cdf.max()
    
    # Equaliza o histograma
    equalized_image = np.interp(image.flatten(), bins[:-1], cdf_normalized)
    equalized_image = equalized_image.reshape(image.shape)
    
    return equalized_image

def histogram_equalization_opencv(image):
    # Equaliza o histograma usando a função cv2.equalizeHist
    equalized_image = cv2.equalizeHist(image)
    
    return equalized_image

def histogram_equalization_pillow(image):
    # Converte a imagem para o modo 'L' (escala de cinza)
    image = image.convert('L')
    # Equaliza o histograma usando a função ImageOps.equalize
    equalized_image = ImageOps.equalize(image)
    
    return equalized_image

def main():
    # Abre a imagem
    image = cv2.imread('img/lena_gray_512.tif', cv2.IMREAD_GRAYSCALE)
    
    # Equaliza o histograma manualmente
    equalized_image_manual = histogram_equalization_manual(image)
    
    # Equaliza o histograma usando OpenCV
    equalized_image_opencv = histogram_equalization_opencv(image)
    
    # Equaliza o histograma usando Pillow
    image_pillow = Image.open('img/lena_color_512.tif')
    equalized_image_pillow = histogram_equalization_pillow(image_pillow)
    
   # Exibe a imagem original e as imagens equalizadas lado a lado
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))  # 1 linha, 4 colunas
    
    # Exibe a imagem original (em escala de cinza)
    axes[0].imshow(image, cmap='gray')
    axes[0].set_title('Imagem Original')
    axes[0].axis('off')
    
    # Exibe a imagem equalizada manualmente
    axes[1].imshow(equalized_image_manual, cmap='gray')
    axes[1].set_title('Equalização Manual')
    axes[1].axis('off')
    
    # Exibe a imagem equalizada com OpenCV
    axes[2].imshow(equalized_image_opencv, cmap='gray')
    axes[2].set_title('Equalização OpenCV')
    axes[2].axis('off')
    
    # Exibe a imagem equalizada com Pillow
    axes[3].imshow(equalized_image_pillow, cmap='gray')
    axes[3].set_title('Equalização Pillow')
    axes[3].axis('off')
    
    plt.tight_layout()
    plt.savefig('img_transformada/equalize_image.png')

if __name__ == '__main__':
    main()