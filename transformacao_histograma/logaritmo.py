#Aplicar a transformação logarítmica, testar vários valores para o parâmetro c "s = c log (1 + r)"
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def log_transform(image, c):
    # Cria uma cópia da imagem para não modificar a original
    image = np.array(image)
    # Aplica a transformação logarítmica
    image = c * np.log(1 + image)
    # Normaliza os valores para o intervalo [0, 255]
    image = (255 * (image - np.min(image)) / (np.max(image) - np.min(image))).astype(np.uint8)
    return image

# Testa a função com a imagem de exemplo
def main():

    # Abre a imagem
    image = Image.open('img/lena_gray_512.tif').convert('L')
    # Aplica a transformação logarítmica com c = 1
    transformed_image = log_transform(image, 1)

    # Salva a imagem transformada
    #Image.fromarray(transformed_image).save('img_transformada/log_transformed.jpg')
    #print("Imagem transformada salva com sucesso!")

    # Testa vários valores de c
    c_values = [1, 5, 10, 20]  # Teste diferentes valores para c
    fig, axes = plt.subplots(1, len(c_values) + 1, figsize=(15, 5))
    
    # Exibe a imagem original
    axes[0].imshow(image, cmap='gray')
    axes[0].set_title('Original')
    axes[0].axis('off')
    
    # Aplica e exibe a transformação logarítmica com diferentes valores de c
    for i, c in enumerate(c_values):
        transformed_image = log_transform(image, c)
        axes[i + 1].imshow(transformed_image, cmap='gray')
        axes[i + 1].set_title(f'c = {c}')
        axes[i + 1].axis('off')
    
    # Exibe os resultados
    plt.savefig('img_transformada/output_image.png')

if __name__ == '__main__':
    main()







