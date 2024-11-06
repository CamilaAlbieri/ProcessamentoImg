#2.     Crie filtros passa-baixa do tipo ideal, butterworth e gaussiano e aplique-o às imagens disponibilizadas. Visualize o seguinte:

#a)    a imagem inicial;
import numpy as np
import matplotlib.pyplot as plt

def ideal_lowpass_filter(shape, cutoff):
    """ Cria um filtro passa-baixa ideal """
    P, Q = shape
    H = np.zeros((P, Q))
    for u in range(P):
        for v in range(Q):
            D = np.sqrt((u - P/2)**2 + (v - Q/2)**2)
            if D <= cutoff:
                H[u, v] = 1
    return H

def butterworth_lowpass_filter(shape, cutoff, order):
    """ Cria um filtro passa-baixa Butterworth """
    P, Q = shape
    H = np.zeros((P, Q))
    for u in range(P):
        for v in range(Q):
            D = np.sqrt((u - P/2)**2 + (v - Q/2)**2)
            H[u, v] = 1 / (1 + (D / cutoff)**(2 * order))
    return H

def gaussian_lowpass_filter(shape, cutoff):
    """ Cria um filtro passa-baixa Gaussiano """
    P, Q = shape
    H = np.zeros((P, Q))
    for u in range(P):
        for v in range(Q):
            D = np.sqrt((u - P/2)**2 + (v - Q/2)**2)
            H[u, v] = np.exp(-(D**2) / (2 * (cutoff**2)))
    return H

def visualize_filtering(image, filter, filtered_image):
    """Visualiza a imagem original, o filtro e a imagem filtrada."""
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    axes[0].imshow(image, cmap='gray')
    axes[0].set_title("Imagem Original")
    axes[0].axis('off')
    
    axes[1].imshow(np.log1p(filter), cmap='gray')  # Usando log1p para melhor visualização
    axes[1].set_title("Filtro Passa-Baixa")
    axes[1].axis('off')
    
    axes[2].imshow(filtered_image, cmap='gray')
    axes[2].set_title("Imagem Filtrada")
    axes[2].axis('off')
    
    plt.tight_layout()
    plt.show()

def main():
    # Carregar a imagem
    img = plt.imread('/home/camila/Documentos/processamentoImagens/exercicios/transformada_fourier/img/periodic_noise.png')
    
    # Calcular o espectro de Fourier da imagem
    img_spectrum = np.fft.fftshift(np.fft.fft2(img))
    
    # Criar filtros passa-baixa
    shape = img.shape
    cutoff = 50
    order = 2
    H_ideal = ideal_lowpass_filter(shape, cutoff)
    H_butterworth = butterworth_lowpass_filter(shape, cutoff, order)
    H_gaussian = gaussian_lowpass_filter(shape, cutoff)
    
    # Aplicar os filtros à imagem
    img_filtered_ideal = np.abs(np.fft.ifft2(np.fft.ifftshift(img_spectrum * H_ideal)))
    img_filtered_butterworth = np.abs(np.fft.ifft2(np.fft.ifftshift(img_spectrum * H_butterworth)))
    img_filtered_gaussian = np.abs(np.fft.ifft2(np.fft.ifftshift(img_spectrum * H_gaussian)))
    
    # Visualizar os resultados
    visualize_filtering(img, H_ideal, img_filtered_ideal)
    visualize_filtering(img, H_butterworth, img_filtered_butterworth)
    visualize_filtering(img, H_gaussian, img_filtered_gaussian)

if __name__ == "__main__":
    main()


