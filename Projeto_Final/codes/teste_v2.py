#Importação das bibliotecas necessárias
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import glob


# Definição da função morfológica
def morph_function(matinput):
  kernel =  cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))

  morph = cv2.erode(matinput,kernel,iterations=1)
  morph = cv2.dilate(morph,kernel,iterations=2)
  morph = cv2.erode(matinput,kernel,iterations=1)
  morph = cv2.dilate(morph,kernel,iterations=1)

  return morph


# Análise das características
def analyze_blob(matblobs,countours_frame, file):

  blobs,_ = cv2.findContours(matblobs,cv2.RETR_LIST ,cv2.CHAIN_APPROX_SIMPLE)
  valid_blobs = []

  for i,bar in enumerate(blobs):
    rot_rect = cv2.minAreaRect(bar)
    b_rect = cv2.boundingRect(bar)


    (cx,cy),(sw,sh),angle = rot_rect
    rx,ry,rw,rh = b_rect

    box = cv2.boxPoints(rot_rect)
    box = np.int0(box)

    # Desenhando o contorno da área da barra encontrada
    frame = cv2.drawContours(countours_frame,[box],0,(0,0,255),1)

    on_count = cv2.contourArea(bar)
    total_count = sw*sh
    if total_count <= 0:
      continue

    if sh > sw :
      temp = sw
      sw = sh
      sh = temp

      
    #print('Area: ', sw * sh)

    # Área mínima 
    if sw * sh < 1400:
      continue

    # Área máxima
    if sw * sh > 1750:
      continue  


    # Proporção da barra
    rect_ratio = sw / sh

    #print('rect_ratio:', rect_ratio)

    if rect_ratio <= 10 or rect_ratio >= 14.5:
      continue

    # Proporção do preenchimento
    fill_ratio = on_count / total_count
    #print('fill_ratio: ', fill_ratio)

    if fill_ratio < 0.2 :
      continue

    #print('countours_frame[int(cy),int(cx),0] ->', countours_frame[int(cy),int(cx),0])
    # Remove as barras que são mais claras
    if countours_frame[int(cy),int(cx),0] > 75:
      continue

    valid_blobs.append(bar)

  if valid_blobs:
    #print("Number of Bars : " ,len(valid_blobs))
    print("O Arquivo {}, possui um total de {} linhas pretas".format(os.path.basename(file), len(valid_blobs)))
  cv2.imshow("countours_frame_in",countours_frame)

  return valid_blobs


def main_process():

  # camera = PiCamera() 

  # camera.start_preview()
  # time.sleep(4)
  # camera.capture('../imgs/in/image.jpg')
  # camera.stop_preview()

  for file in glob.glob("../imgs/in/*"):

    img = cv2.imread(file)  
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Função Gaussiana para adicionar ruído (blur)
    blurred = cv2.GaussianBlur(gray,(3,3),-1)
    
    # Aplicando a técnica 'thresholding Otsu'
    # Extrair a característica da binarização da imagem
    # Otsu thresholding     
    ret, thresh1 = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)  
    # cv2.imshow("thresholding",thresh1)
    # cv2.waitKey(1)

    matmorph = morph_function(thresh1)
    # cv2.imshow("matmorph",matmorph)
    # cv2.waitKey(1)

    display_color = cv2.cvtColor(gray,cv2.COLOR_GRAY2BGR)
    valid_blobs = analyze_blob(matmorph,display_color, file)


    for b in range(len(valid_blobs)):
      cv2.drawContours(display_color,valid_blobs,b,(0,255,255),-1)

    # cv2.imshow("display_color",display_color)
    # cv2.imwrite('../imgs/out/saida7.png', display_color)
    # cv2.waitKey(0)

    
    plt.subplot(131),plt.imshow(img, cmap = 'gray')
    plt.title('Original'), plt.xticks([]), plt.yticks([])
    plt.subplot(132),plt.imshow(thresh1,cmap = 'gray')
    plt.title('Segmentação'), plt.xticks([]), plt.yticks([])
    plt.subplot(133),plt.imshow(display_color,cmap = 'gray')
    plt.title('Barras encontradas'), plt.xticks([]), plt.yticks([])
    plt.show()






if __name__ == '__main__':
  main_process()