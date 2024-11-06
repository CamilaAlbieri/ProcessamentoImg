import cv2
import numpy as np
import matplotlib.pyplot as plt


def load_image(image_path):
    print(f"Tentando carregar a imagem: {image_path}")
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)  # Tenta carregar a imagem em escala de cinza
    if img is None:
        raise FileNotFoundError(f"Não foi possível carregar a imagem: {image_path}")  # Lança erro se não carregar
    return img.astype(np.float64) / 255.0 

def check_image_size(orig_img, defect_img):
    if orig_img.shape != defect_img.shape:
        raise ValueError('As imagens originais e defeituosas devem ter o mesmo tamanho.')

# Função para alinhar a imagem deslocada
def align_image(defect_img, x_shift, y_shift):
    regist_img = np.zeros_like(defect_img)
    regist_img[y_shift:, x_shift:] = defect_img[:defect_img.shape[0] - y_shift, :defect_img.shape[1] - x_shift]
    return regist_img

# Função para redimensionar a imagem para um tamanho alvo
def resize_image(image, target_shape):
    return cv2.resize(image, (target_shape[1], target_shape[0]))  # Redimensionar para altura x largura

# Função para calcular a diferença entre duas imagens
def calculate_difference(img1, img2):
    return np.abs(img1 - img2)

# Função para exibir as imagens
def show_images(img_list, titles, save_path_prefix='output_', figsize=(15, 5)):
    plt.figure(figsize=figsize)
    for i, img in enumerate(img_list):
        plt.subplot(1, len(img_list), i + 1)
        plt.imshow(img, cmap='gray')
        plt.title(titles[i])
        plt.axis('off')
    
    # Salvar a figura em um arquivo
    plt.savefig(f'desafio_stanford/img_result/{save_path_prefix}{titles[0]}.png')  # Salvar a primeira imagem com o título
    plt.close() 

# Função para detectar defeitos aplicando limiar e máscara de borda
def detect_defects(diff_img, threshold):
    bw_img = diff_img > threshold  # Aplicar limiar
    height, width = bw_img.shape
    border = round(0.05 * width)  # Definir borda como 5% da largura
    border_mask = np.zeros_like(bw_img)
    border_mask[border:height-border, border:width-border] = 1  # Criar máscara de borda
    return bw_img * border_mask  # Aplicar a máscara

# Função para salvar as imagens processadas
def save_images(diff_img1, diff_img2, bw_img):
    cv2.imwrite('desafio_stanford/img_result/Defect_Detection_diff.png', (diff_img1 * 255).astype(np.uint8))
    cv2.imwrite('desafio_stanford/img_result/Defect_Detection_diffRegisted.png', (diff_img2 * 255).astype(np.uint8))
    cv2.imwrite('desafio_stanford/img_result/Defect_Detection_bw.png', (bw_img * 255).astype(np.uint8))

def main():
    orig_img = load_image('/home/camila/Documentos/processamentoImagens/exercicios/desafio_stanford/img/pcb.png')
    defect_img = load_image('/home/camila/Documentos/processamentoImagens/exercicios/desafio_stanford/img/pcbCroppedTranslatedDefected.png')

    try:
        orig_img = load_image('/home/camila/Documentos/processamentoImagens/exercicios/desafio_stanford/img/pcb.png')
        defect_img = load_image('/home/camila/Documentos/processamentoImagens/exercicios/desafio_stanford/img/pcbCroppedTranslatedDefected.png')
    except FileNotFoundError as e:
        print(e)
        exit(1)

    # Verificar se as imagens têm o mesmo tamanho
    if orig_img.shape != defect_img.shape:
        print(f"Redimensionando a imagem defeituosa de {defect_img.shape} para {orig_img.shape}")
        defect_img = resize_image(defect_img, orig_img.shape) 
        
    check_image_size(orig_img, defect_img)

    # Definir o deslocamento que quero
    x_shift = 10
    y_shift = 10

    # Ajustar a imagem deslocada
    img_deslocada = align_image(defect_img, x_shift, y_shift)  

    # Mostrar diferença NÃO alinhada
    diff_img = calculate_difference(orig_img, defect_img)

    # Calcular a diferença entre as imagens alinhadas
    diff_img2 = calculate_difference(orig_img, img_deslocada)

    # Detectar defeitos
    defeitos = detect_defects(diff_img2, 0.15)

    # Mostrar as imagens
    show_images([diff_img, diff_img2, defeitos], ['Diferença', 'Diferença (alinhada)', 'Defeitos'])

    # Salvar as imagens
    save_images(diff_img, diff_img2, defeitos)

if __name__ == '__main__':
    main()
