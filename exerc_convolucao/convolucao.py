import cv2
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt


#Função para convolução com OpenCV
def convolve_opencv(image, kernel):
    return cv2.filter2D(image, -1, kernel)

#Função para convolução com Scipy
def convolve_scipy(image, kernel):
    return ndimage.convolve(image, kernel)

#Função para convolução manual
def manual_convolution(img, kernel):
    h, w = img.shape
    kh, kw = kernel.shape
    output = np.zeros_like(img)

    # Aplicar a convolução manualmente
    for i in range(kh//2, h-kh//2):
        for j in range(kw//2, w-kw//2):
            roi = img[i-kh//2:i+kh//2+1, j-kw//2:j+kw//2+1]
            output[i, j] = np.sum(roi * kernel)
    
    return output

# Função para carregar a imagem
def load_image(image_path):
    return cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

def add_caption_above_image(img, caption, font=cv2.FONT_HERSHEY_SIMPLEX, scale=1, thickness=2, color=(0,0,0)):
    """Cria uma área acima da imagem e adiciona a legenda lá"""
    # Dimensões da imagem
    (w, h) = img.shape
    
    # Criar uma área branca para o texto com altura de 30 pixels
    caption_area = np.ones((50, h), dtype=np.uint8) * 255

    # Adicionar texto na área da legenda
    text_size = cv2.getTextSize(caption, font, scale, thickness)[0]
    text_x = (h - text_size[0]) // 2
    text_y = (30 + text_size[1]) // 2
    cv2.putText(caption_area, caption, (text_x, text_y), font, scale, color, thickness)
    
    # Concatenar a área da legenda acima da imagem
    img_with_caption = cv2.vconcat([caption_area, img])
    return img_with_caption

# Função para concatenar imagens em grid
def concatenate_images_with_captions(images, titles):
    """Concatena imagens com legendas em 2 linhas e 4 colunas"""
    # Adicionar as legendas acima das imagens
    images_with_captions = [add_caption_above_image(img, title) for img, title in zip(images, titles)]
    
    # Dividir as imagens em dois grupos (4 imagens por linha)
    upper_row = cv2.hconcat(images_with_captions[:4])
    lower_row = cv2.hconcat(images_with_captions[4:])
    
    # Concatenar as duas linhas verticalmente
    concatenated_image = cv2.vconcat([upper_row, lower_row])
    
    return concatenated_image
     
def main():
    # Carrega a imagem
    img = load_image('img/cameraman.tif')

    # Define o kernel para mascaras: media, convolucao, gaussiana, laplaciana, sobel x, sobel y, gradiente(x,y), laplaciano somado a imagem original
    kernel_media = np.ones((3, 3), np.float32) / 9
    kernel_gaussiano = cv2.getGaussianKernel(3, 1)
    kernel_gaussiano = kernel_gaussiano @ kernel_gaussiano.T
    kernel_laplaciano = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])
    kernel_sobel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    kernel_sobel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    # Aplicar os filtros
    output_media_opencv = convolve_opencv(img, kernel_media)
    output_gaussiano_scipy = convolve_scipy(img, kernel_gaussiano)
    output_laplaciano_manual = manual_convolution(img, kernel_laplaciano)
    output_sobel_x_manual = manual_convolution(img, kernel_sobel_x)
    output_sobel_y_manual = manual_convolution(img, kernel_sobel_y)
    output_gradiente = output_sobel_x_manual + output_sobel_y_manual
    output_laplaciano_soma = cv2.add(img, output_laplaciano_manual)
   
# Preparar as imagens e rótulos para exibição
    images = [img, output_media_opencv, output_gaussiano_scipy, 
              output_laplaciano_manual, output_sobel_x_manual, 
              output_sobel_y_manual, output_gradiente, output_laplaciano_soma]
    
    titles = ['Original', 'Filtro Media (OpenCV)', 'Filtro Gaussiano (Scipy)', 
              'Laplaciano (Manual)', 'Sobel X (Manual)', 'Sobel Y (Manual)', 
              'Gradiente (Sobel X + Y)', 'Laplaciano + Original']

    # Concatenar todas as imagens em uma única imagem com legendas
    concatenated_image = concatenate_images_with_captions(images, titles)
    
    # Salvar e exibir a imagem final
    cv2.imwrite('resultado_convolucao_cameraman.png', concatenated_image)
    cv2.imshow('Imagens com Filtros', concatenated_image)

if __name__ == '__main__':
    main()
