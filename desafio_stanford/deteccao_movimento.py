import cv2
import numpy as np
import matplotlib.pyplot as plt

def load_video(video_path):
    print(f"Tentando carregar o vídeo: {video_path}")
    cap = cv2.VideoCapture(video_path)  # Tenta carregar o vídeo
    if not cap.isOpened():
        raise FileNotFoundError(f"Não foi possível carregar o vídeo: {video_path}")
    return cap

def process_video(cap, alpha=0.95, theta=0.1):
    vwObj = cv2.VideoWriter('desafio_stanford/img_result_movimento/Background_Subtraction.avi', cv2.VideoWriter_fourcc(*'MJPG'), 30, (int(cap.get(3)), int(cap.get(4))))  # Configurar o gravador de vídeo

    # Ler o primeiro quadro e inicializar o fundo
    ret, first_frame = cap.read()
    if not ret:
        raise ValueError("Não foi possível ler o primeiro quadro.")
    background = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY).astype(np.float64) / 255.0

    frame_count = 0

    while cap.isOpened():
        ret, curr_frame = cap.read()
        if not ret:
            print("Fim do vídeo ou não foi possível ler o quadro.")
            break
        
        currImg = cv2.cvtColor(curr_frame, cv2.COLOR_BGR2GRAY).astype(np.float64) / 255.0  # Ler e converter o quadro atual para escala de cinza
        
        # Acumulação do fundo
        background = alpha * background + (1 - alpha) * currImg
        
        # Calcular a imagem de diferença
        diffImg = np.abs(currImg - background)
        threshImg = diffImg > theta
        
        # Mostrar as imagens
        show_images(currImg, background, diffImg, threshImg, frame_count)

        # Gravar o quadro no vídeo
        curr_frame_bgr = cv2.cvtColor((currImg * 255).astype(np.uint8), cv2.COLOR_GRAY2BGR)  # Converter de volta para BGR para gravar
        vwObj.write(curr_frame_bgr)
        
        # Adicione a impressão do progresso
        print(f"Processando quadro: {frame_count}")
        frame_count += 1

    cap.release()
    vwObj.release()
    cv2.destroyAllWindows()

def show_images(currImg, background, diffImg, threshImg, frame_count):
    plt.figure(figsize=(10, 8))
    plt.subplot(2, 2, 1), plt.imshow(currImg, cmap='gray'), plt.title('New Frame'), plt.axis('off')
    plt.subplot(2, 2, 2), plt.imshow(background, cmap='gray'), plt.title('Background Frame'), plt.axis('off')
    plt.subplot(2, 2, 3), plt.imshow(diffImg, cmap='gray'), plt.title('Difference Image'), plt.axis('off')
    plt.subplot(2, 2, 4), plt.imshow(threshImg, cmap='gray'), plt.title('Thresholded Difference Image'), plt.axis('off')
    
    # Salvar a figura em um arquivo
    plt.savefig(f'desafio_stanford/img_result_movimento/Background_Subtraction_Frame_{frame_count}.png')  # Salvar cada quadro como imagem
    plt.close()  # Fechar a figura após salvar

def main():
    video_path = 'desafio_stanford/img/surveillance.avi'  # Altere para o caminho do seu vídeo
    cap = load_video(video_path)
    
    # Processar o vídeo e subtrair o fundo
    process_video(cap)

if __name__ == '__main__':
    main()
