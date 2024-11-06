#Aplicar a transformação de potência (gama), testar vários valores para o parâmetro γ e c=1 "s = crγ"
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def power_transform(image, c, gamma):
    # Cria uma cópia da imagem para não modificar a original
    image = np.array(image)
    # Aplica a transformação de potência
    image = c * np.power(image, gamma)
    # Normaliza os valores para o intervalo [0, 255]
    image = (255 * (image - np.min(image)) / (np.max(image) - np.min(image))).astype(np.uint8)
    return image

def power_transform(image, gamma, c=1):
    # Converte a imagem para um array NumPy e normaliza para o intervalo [0, 1]
    image = np.array(image) / 255.0
    # Aplica a transformação de potência
    image = c * np.power(image, gamma)
    # Normaliza os valores para o intervalo [0, 255] e converte para uint8
    image = (255 * image).astype(np.uint8)
    return image

def main():

    # Abre a imagem
    image = Image.open('img/lena_gray_512.tif').convert('L')
    # Aplica a transformação de potência com γ = 0.5
    transformed_image = power_transform(image, 0.5)

    # Salva a imagem transformada
    Image.fromarray(transformed_image).save('img_transformada/power_transformed.jpg')
    print("Imagem transformada salva com sucesso!")

    # Testa vários valores de γ
    gamma_values = [0.5, 1.5, 2.5, 3.5]  # Teste diferentes valores para γ
    fig, axes = plt.subplots(1, len(gamma_values) + 1, figsize=(15, 5))
    
    # Exibe a imagem original
    axes[0].imshow(image, cmap='gray')
    axes[0].set_title('Original')
    axes[0].axis('off')
    
    # Aplica e exibe a transformação de potência com diferentes valores de γ
    for i, gamma in enumerate(gamma_values):
        transformed_image = power_transform(image, gamma)
        axes[i + 1].imshow(transformed_image, cmap='gray')
        axes[i + 1].set_title(f'γ = {gamma}')
        axes[i + 1].axis('off')
    
    # Exibe os resultados
    plt.savefig('img_transformada/output_gamma_image.png')

if __name__ == '__main__':
    main()