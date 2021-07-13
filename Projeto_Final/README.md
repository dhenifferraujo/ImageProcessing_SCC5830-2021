# Projeto Final de Processamento de Imagens 2021 - Relatório Final - Entrega: 14/07/2021


Dheniffer Caroline Araújo Pessoa NºUSP: 12116252 |Douglas Queiroz Galúcio Batista Nº USP: 12114819
:------------------------------:|:------------------------------:

## Título do Projeto: Técnicas de morfologia e segmentação aplicadas em imagens para detecção do nível de rios. 

  
### Resumo:

<p align="justify">
Esse projeto visa detectar o nível de rios através da medição de marcadores de nível de água. Para tal fim, foram aplicadas técnicas de realce, restauração, segmentação e morfologia nas imagens capturadas, a fim de tratar e melhorar a resolução dessas imagens e permitir uma análise mais precisa da medição do nível de rios.
</p>

### Objetivo Principal do Projeto:

<p align="justify">
Aplicar técnicas de processamento de imagens, tais como realce, restauração, segmentação e morfologia em imagens de marcadores de nível de água, a fim de  melhorar a resolução das imagens e permitir uma análise mais precisa da medição do nível de água de rios. 
</p>

### Descrição das Imagens de Entrada:

<p align="justify">
As imagens utilizadas nesse projeto são marcadores de nível de rio elaboradas pelos próprios autores. Essas imagens diferenciam-se pelo ângulo, distância e resolução. Para simular um ambiente real nos experimentos, nós capturamos as imagens com algumas interferências. De forma que as barras (marcadores de nível) não ficassem totalmente visíveis. 
</p>

### Exemplos de imagens de entrada:

<p align="justify">
Todas as imagens de referência podem ser acessadas no repositório <https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/tree/main/Projeto_Final> na pasta “imgs”.
</p>

Imagem 1 |Imagem 2
:------------------------------:|:------------------------------:
<img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/teste1.jpeg" width="400" height="400"> | <img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/teste2.jpeg" width="400" height="400"> 

Imagem 3 |Imagem 4
:-------------------------:|:-------------------------:
<img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/teste3.jpeg" width="400" height="400"> | <img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/teste4.jpeg" width="400" height="400">

Imagem 5|Imagem 6  
:-------------------------:|:-------------------------:
<img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/teste5.jpeg" width="400" height="400">  |  <img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/teste7.jpeg" width="400" height="400">


### Etapas e Métodos:
- Elaboração e captura de imagens com simulação de ruídos/interferências nos marcadores para simular um cenário real.
- Leitura e conversão das imagens em uma escala de cinza usando o método *cvtColor()* da biblioteca OpenCV. Esse método converte uma imagem de um espaço de cor para outro.
- Após as imagens serem convertidas em escala de cinza. Aplicamos os métodos morfológicos *erode()* e *dilate()* (erosão e dilatação). Usamos esses métodos para remover ruídos das imagens. 
- Utilizamos o método *threshold()* com binarização de Otsu para segmentar as imagens, ou seja, aplicar o limite (limiar). Optamos por usar a binarização de Otsu porque estamos trabalhando com imagens bimodais. 
- Após as imagens serem segmentadas, aplicamos o método *findCountours()* para encontrar os contornos. Ou seja, encontrar as barras pretas em um fundo branco. 
- 
  
  
  
- Utilização de técnicas para a detecção de bordas das imagens capturadas, como: como: *"threshold"* e *"findContours"*;
- Utilização de técnicas de restauração de imagens, como: filtros adaptativos e eliminação de ruídos;
- Utilização de técnicas de morfologia para aprimorar imagens e realçar os contornos;

 

### Código Inicial:

<p align="justify">
Os códigos iniciais implementados nos testes podem ser acessados no repositório do GitHub <https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/tree/main/Projeto_Final> na pasta "codes".
</p>


<p align="justify">
  
O código [teste_v1](https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/codes/teste_v1.py) transforma as imagens em escala de cinza usando o filtro "grayscale" e então procura os contornos usando as funções threshold(), canny() e findContour() da biblioteca OpenCV, ou seja, limiariza as imagens. Por fim, é feito um laço de repetição (loop) para encontrar as formas geométricas de um retângulo na imagem;
  
</p>
 
  
<p align="justify">
  
No código [teste_v2](https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/codes/teste_v2.py) usamos a técnica  LBP (Local Binary Pattern) para classificação de textura, além disso utilizamos um filtro morfológico de erosão e dilatação. Usando os métodos erode() e dilate(). Em seguida, nós implementamos uma técnica de remoção de ruído através do filtro Gaussiano. Finalmente, analisamos as formas geométricas de um retângulo na imagem através de um laço de repetição;
  
</p>

<p align="justify">
  
No código [teste_v3](https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/codes/teste_v3.py) utilizamos um filtro 2D (Filtro Linear Arbitrário), em seguida usamos o threshold() e findContours() para detectar os contornos das imagens. Então, fizemos um laço de repetição para verificar quais dos contornos têm a forma de um retângulo. Por fim, o algoritmo faz a contagem dos retângulos (barras) encontrados na imagem. 
  
</p>
