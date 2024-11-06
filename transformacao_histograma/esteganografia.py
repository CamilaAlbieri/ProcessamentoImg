#hidden message image manual

from PIL import Image

def message_to_binary(message):
    #convert message to binary
    return ''.join([format(ord(i), "08b") for i in message])

def binary_to_message(binary_message):
    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))
    return message

def hide_message_gray(image, message, output_path):
    # Certifica-se de que a imagem está em escala de cinza
    image = image.convert('L')
    pixels = image.load()

    # Converte a mensagem para binário e adiciona finalizador
    binary_message = message_to_binary(message) + '1111111111111110'

    binary_index = 0
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = pixels[i, j]
            if binary_index < len(binary_message):
                # Modifica o LSB do pixel
                pixels[i, j] = (pixel & ~1) | int(binary_message[binary_index])
                binary_index += 1

            if binary_index >= len(binary_message):
                break

    # Salva a nova imagem com a mensagem oculta
    image.save(output_path)
    print(f"Mensagem oculta na imagem: {output_path}")

def recupera_message_gray(image_path):
    # Abre a imagem no modo de escala de cinza (L)
    image = Image.open(image_path).convert('L')
    pixels = image.load()

    binary_message = ''
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            pixel = pixels[i, j]
            binary_message += str(pixel & 1)  # Pega o bit menos significativo

    # Procura o finalizador de mensagem (1111111111111110) para saber onde a mensagem termina
    end_of_message = binary_message.find('1111111111111110')

    # Se o finalizador for encontrado, cortamos o binário até ali
    if end_of_message != -1:
        binary_message = binary_message[:end_of_message]

    # Converte o binário de volta para uma string de texto
    return binary_to_message(binary_message)

def hide_message_rgb(image, message, output_path):
    # Garante que a imagem está no modo RGB
    image = image.convert('RGB')
    pixels = image.load()

    # Converte a mensagem para binário e adiciona um finalizador
    binary_message = message_to_binary(message) + '1111111111111110'

    binary_index = 0
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]

            if binary_index < len(binary_message):
                # Modifica o bit menos significativo de R
                r = (r & ~1) | int(binary_message[binary_index])
                binary_index += 1
            if binary_index < len(binary_message):
                # Modifica o bit menos significativo de G
                g = (g & ~1) | int(binary_message[binary_index])
                binary_index += 1
            if binary_index < len(binary_message):
                # Modifica o bit menos significativo de B
                b = (b & ~1) | int(binary_message[binary_index])
                binary_index += 1

            # Atualiza o pixel com os novos valores
            pixels[i, j] = (r, g, b)

            # Se já codificamos toda a mensagem, saímos do loop
            if binary_index >= len(binary_message):
                break
        if binary_index >= len(binary_message):
            break

    # Salva a imagem com a mensagem escondida
    image.save(output_path)
    print(f"Mensagem oculta na imagem RGB: {output_path}")

def retrieve_message_rgb(image_path):
    # Abre a imagem no modo RGB
    image = Image.open(image_path).convert('RGB')
    pixels = image.load()

    binary_message = ''
    for i in range(image.size[0]):
        for j in range(image.size[1]):
            r, g, b = pixels[i, j]
            # Obtém os bits menos significativos de R, G e B
            binary_message += str(r & 1)
            binary_message += str(g & 1)
            binary_message += str(b & 1)

    # Procura o finalizador de mensagem e recupera a parte relevante
    end_of_message = binary_message.find('1111111111111110')
    binary_message = binary_message[:end_of_message]

    return binary_to_message(binary_message)

def main():
    # Abre a imagem
    image = Image.open('img/lena_gray_512.tif')
    image_color = Image.open('img/lena_color_512.tif')

    ###### GRAY #######
    # Mensagem a ser escondida
    mensagem_gray = 'Consegui fazer isso'

    # Esconde a mensagem e salva a imagem resultante
    output_path = 'img_hidden/lena_gray_hidden.png'
    #hide_message_gray(image, mensagem_gray, output_path)


    # Agora recupera a mensagem da imagem que acabou de ser salva
    mensagem_recuperada = recupera_message_gray(output_path)
    print("Mensagem recuperada:", mensagem_recuperada)

    ####### RGB #######
    # Mensagem a ser escondida
    #mensagem_cor = 'acho que foi'

    # Esconde a mensagem e salva a imagem resultante
    #output_path = 'img_hidden/lena_color_hidden.png'
    #output_path_cor = 'img_hidden/esteganografia.png'
   # hide_message_rgb(image_color, mensagem_cor, output_path_cor)

    # Agora recupera a mensagem da imagem que acabou de ser salva
    #mensagem_recuperada_cor = retrieve_message_rgb(output_path_cor)
    #print("Mensagem recuperada:", mensagem_recuperada_cor)

    #msg_bin = message_to_binary('cansei')
    #print(msg_bin)

    #bin_to_msg = binary_to_message(msg_bin)
    #print(bin_to_msg)




if __name__ == '__main__':
    main()