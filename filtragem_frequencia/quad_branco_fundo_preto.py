import numpy as np
import matplotlib.pyplot as plt
# 1)  Calcule e visualize o espectro de uma imagem 512x512 pixels:
# a) crie e visualize uma imagem simples – quadrado branco sobre fundo preto;
def create_sinc_square_image(size, square_size):
     # Cria uma imagem preta
    img = np.zeros((size, size))
    # Calcula o centro da imagem
    center = size // 2
    # Calcula a metade do tamanho do quadrado
    half_square = square_size // 2
    # Define o quadrado branco no centro da imagem
    img[center - half_square:center + half_square, center - half_square:center + half_square] = 1
    return img


#b)   calcular e visualizar seu espectro de Fourier (amplitudes);
def fourier_spectrum(image):
    return np.fft.fftshift(np.fft.fft2(image))

#c)    calcular e visualizar seu espectro de Fourier (fases);
def fourier_phase(image):
    return np.fft.fftshift(np.angle(np.fft.fft2(image)))

#d)   obter e visualizar seu espectro de Fourier centralizado;
def fourier_centered(image):
    return np.fft.fft2(image)

#e)   Aplique uma rotação 
def rotate_image(image, angle):
    return np.rot90(image, angle)

#f)   Aplique uma translação nos eixos x e y no quadrado 
def translate_image(image, dx, dy):
    return np.roll(image, (dx, dy), axis=(0, 1))

#g)   Aplique um zoom na imagem
def zoom_image(image, zoom):
    return np.repeat(np.repeat(image, zoom, axis=0), zoom, axis=1)

def fourier_transform(img):
    f_transform = np.fft.fft2(img)
    f_transform_shifted = np.fft.fftshift(f_transform)
    return f_transform_shifted



def main():
     # a) Criar e visualizar uma imagem simples
    img = create_sinc_square_image(256, 50)
    
    # b) Calcular e visualizar o espectro de Fourier (amplitudes)
    img_spectrum = fourier_spectrum(img)
    plt.imshow(np.log(1 + np.abs(img_spectrum)), cmap='gray')
    plt.title('Espectro de Fourier (amplitudes)')
    plt.show()

    # c) Calcular e visualizar o espectro de Fourier (fases)
    img_phase = fourier_phase(img)
    plt.imshow(img_phase, cmap='gray')
    plt.title('Espectro de Fourier (fases)')
    #salvar img na pasta
    plt.savefig('filtragem_frequencia/img_freq/espectro_fases.png')
    plt.show()

    # d) Obter e visualizar o espectro de Fourier centralizado
    img_centered = fourier_centered(img)
    plt.imshow(np.log(1 + np.abs(img_centered)), cmap='gray')
    plt.title('Espectro de Fourier centralizado')
    plt.savefig('filtragem_frequencia/img_freq/espectro_centralizado.png')
    plt.show()

    # e) Aplicar uma rotação
    img_rotated = rotate_image(img, 40)
    plt.imshow(img_rotated, cmap='gray')
    plt.title('Imagem rotacionada')
    plt.savefig('filtragem_frequencia/img_freq/imagem_rotacionada.png')
    plt.show()

    # f) Aplicar uma translação nos eixos x e y
    trans_img = translate_image(img, 50, 50)
    plt.imshow(trans_img, cmap='gray')
    plt.title('Imagem transladada')
    plt.savefig('filtragem_frequencia/img_freq/imagem_transladada.png')
    plt.show()

    # g) Aplicar um zoom na imagem
    zoom_img = zoom_image(img, 2)
    plt.imshow(zoom_img, cmap='gray')
    plt.title('Imagem com zoom')
    plt.savefig('filtragem_frequencia/img_freq/imagem_zoom.png')
    plt.show()




if __name__ == '__main__':
    main()








