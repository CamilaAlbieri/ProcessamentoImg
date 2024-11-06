#Implemente a representação de cada plano de bits das imagens.

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def bit_plane_slice(image, bit):
    # Converte a imagem para um array NumPy
    image = np.array(image)
    # Cria uma máscara para extrair o plano de bits desejado
    mask = 2 ** bit
    # Aplica a máscara para extrair o plano de bits
    bit_plane = (image & mask)
    return bit_plane

def main():
    # Abre a imagem
    image = Image.open('img/lena_gray_512.tif').convert('L')
    
    # Exibe os planos de bits de 0 a 7
    fig, axes = plt.subplots(1, 8, figsize=(20, 5))
    
    for i in range(8):
        bit_plane = bit_plane_slice(image, i)
        axes[i].imshow(bit_plane, cmap='gray')
        axes[i].set_title(f'Bit {i}')
        axes[i].axis('off')
    
    # Exibe os resultados
    plt.savefig('img_transformada/bit_plane_image.png')

if __name__ == '__main__':
    main()