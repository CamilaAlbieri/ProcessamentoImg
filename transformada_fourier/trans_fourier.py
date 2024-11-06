import numpy as np
import matplotlib.pyplot as plt

def fourier_transform(image):
    f_transform = np.fft.fft2(image)
    f_shifted = np.fft.fftshift(f_transform)  # Colocar a DC no centro
    return f_shifted

def inverse_fourier_transform(f_shifted):
    f_inv_shifted = np.fft.ifftshift(f_shifted)
    image_back = np.fft.ifft2(f_inv_shifted)
    return image_back

def plot_spectrum_and_phase(f_transform):
    magnitude_spectrum = np.log(np.abs(f_transform) + 1)  # Log para melhor visualização
    phase_spectrum = np.angle(f_transform)

    plt.subplot(1, 2, 1)
    plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum')
    
    plt.subplot(1, 2, 2)
    plt.imshow(phase_spectrum, cmap='gray')
    plt.title('Phase Spectrum')
    
    # Salvar o gráfico em um arquivo
    plt.savefig('/home/camila/Documentos/processamentoImagens/exercicios/transformada_fourier/img_transf/spectrum_phase.png')
    print("Espectro e fase salvos como 'spectrum_phase.png'")
    plt.close()  # Fecha a figura para liberar memória


from mpl_toolkits.mplot3d import Axes3D

def plot_3d_spectrum(f_transform):
    magnitude_spectrum = np.log(np.abs(f_transform) + 1)

    X = np.arange(magnitude_spectrum.shape[1])
    Y = np.arange(magnitude_spectrum.shape[0])
    X, Y = np.meshgrid(X, Y)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, magnitude_spectrum, cmap='viridis')
    plt.title('3D Magnitude Spectrum')

    # Salvar o gráfico 3D em um arquivo
    plt.savefig('transformada_fourier/img_transf/3d_spectrum.png')
    print("Espectro 3D salvo como '3d_spectrum.png'")
    plt.close()


def create_sinc_square_image(size, square_size):
    image = np.ones((size, size))  # Fundo branco
    center = size // 2
    half_square = square_size // 2
    image[center-half_square:center+half_square, center-half_square:center+half_square] = 0  # Quadrado preto
    return image

# Exemplo
sinc_square_img = create_sinc_square_image(256, 50)
plt.imshow(sinc_square_img, cmap='gray')
plt.title('SINC Simulation with Square')
plt.show()


def main():
    image = plt.imread('transformada_fourier/img/newspaper_shot_woman.tif')
    f_shifted = fourier_transform(image)
    plot_spectrum_and_phase(f_shifted)
    plot_3d_spectrum(f_shifted)
    image_back = inverse_fourier_transform(f_shifted)
    plt.imshow(np.abs(image_back), cmap='gray')
    plt.title('Image Back')
    plt.show()

if __name__ == '__main__':
    main()