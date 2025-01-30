import cv2
import numpy as np

def colorido_para_cinza(img) :
    azul = img[:,:,0].astype(np.float32)
    verde = img[:,:,1].astype(np.float32)
    vermelho = img[:,:,2].astype(np.float32)
    cinza = 0.114*azul + 0.587*verde + 0.299*vermelho

    cinza = cinza.astype(np.uint8)
    print(cinza.shape)

    return cinza

def cinza_para_preto_e_branco(img) :
    for i in range(img.shape[0]) :
        for j in range(img.shape[1]) :
            if img[i,j] < 160 :
                img[i,j] = 0
            else :
                img[i,j] = 255

    return img
    

img_bgr = cv2.imread('OIP.jpg')
img_bgr = cv2.resize(img_bgr, (640, 480))

img_cinza = colorido_para_cinza(img_bgr)
img_cinza = cv2.resize(img_cinza, (640, 480))

img_preto_e_branco = img_cinza.copy()
img_preto_e_branco = cinza_para_preto_e_branco(img_preto_e_branco)
img_preto_e_branco = cv2.resize(img_preto_e_branco, (640, 480))

# Exibe a imagem original e a convertida
cv2.imshow("Imagem Original (BGR)", img_bgr)
cv2.imshow("Imagem Convertida (Gray)", img_cinza)
cv2.imshow("Imagem Convertida (Preto e Branco)", img_preto_e_branco)

cv2.waitKey(0)
cv2.destroyAllWindows()