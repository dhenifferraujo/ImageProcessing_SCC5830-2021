# -*- coding: utf-8 -*-
"""Enchentes_V1.ipynb

Bibliotecas utilizadas para o seguinte teste foram:


*   OpenCV
*   NumPy
*   Glob
*   Matplotlib


O Diretório possui imagens de câmera de celular, câmera webcam logitech e print de computador.

Considerei o fato de que a parte preta da imagem é um retângulo e contei quantos retângulos existem nas imagens.

É claro que deve existir outra abordagem.

Precisa acrescentar ruídos, treinar e pesquisar outras abordagens.

**Segue o algoritmo abaixo:**
"""

import numpy as np
import glob
import cv2
import os
from matplotlib import pyplot as plt
#from picamera import PiCamera
import time

# camera = PiCamera() 

# camera.start_preview()
# time.sleep(4)
# camera.capture('imgs/image.jpg')
# camera.stop_preview()


for file in glob.glob("imgs/*"):
  img = cv2.imread(file)
  h,w = img.shape[0:2]
  cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  
  ret, limites = cv2.threshold (cinza, 127, 255, 0)
  bordas = cv2.Canny(img, 50, 200, None, 3)
  
  contours, hierarchy = cv2.findContours(limites, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  contador = 0
  
  for valores in contours:
    x,y,w,h = cv2.boundingRect(valores)
    ar = w / float(h)
    shape = "quadrado" if ar >= 0.95 and ar <= 1.05 else "retangulo"
    if(shape == "retangulo"):
      contador+=1
      
  print("O Arquivo {}, possui um total de {} linhas pretas".format(os.path.basename(file), contador))
  
  plt.subplot(121),plt.imshow(img, cmap = 'gray')
  plt.title('Original'), plt.xticks([]), plt.yticks([])
  plt.subplot(122),plt.imshow(bordas,cmap = 'gray')
  plt.title('Bordas Cinza'), plt.xticks([]), plt.yticks([])
  plt.show()