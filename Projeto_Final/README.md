# Projeto Final de Processamento de Imagens 2021 - Relatório Final - Entrega: 14/07/2021


Dheniffer Caroline Araújo Pessoa NºUSP: 12116252 |Douglas Queiroz Galúcio Batista Nº USP: 12114819
:------------------------------:|:------------------------------:

## Título do Projeto: Técnicas de realce, restauração, segmentação e morfologia aplicadas em imagens para detecção do nível de rios. 

  
### Resumo:

<p align="justify">
Esse projeto visa detectar o nível de rios através da medição de marcadores de nível de água. Para tal fim, foram aplicadas técnicas de realce, restauração, segmentação e morfologia nas imagens capturadas, a fim de tratar e melhorar a resolução dessas imagens e permitir uma análise mais precisa da medição do nível de rios.
</p>



Esse projeto visa minimizar danos causados por enchentes através da medição de marcadores de nível de rio. Para isso, as técnicas de realce, restauração, segmentação e morfologia são aplicadas em imagens

### Objetivo Principal do Projeto:

<p align="justify">
Melhorar o processo de detecção de enchentes através da aplicação de técnicas de processamento de imagens, tais como realce, restauração e morfologia em imagens capturadas dos rios de São Carlos, a fim de  melhorar a resolução das imagens e permitir uma análise mais precisa da medição do nível de água dos rios. 
</p>

### Descrição das Imagens de Entrada:

<p align="justify">
As imagens utilizadas nesse projeto são marcadores de nível de rio. Para a realização dos testes iniciais, nós utilizamos imagens de simulação de marcadores elaboradas manualmente pelos autores. Para essa primeira etapa dos testes as imagens se diferenciam pelo ângulo, distância e resolução. 
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


### Materiais e Métodos:
- Elaborar imagens com ruídos/ocultações nos marcadores para simular um cenário real;
- Simular condições de uma foto real ao invés de usar fotos sintéticas;
- Ler as imagens e converter em uma escala de cinza usando o filtro *"grayscale"*;
- Utilizar técnicas de morfologia para aprimorar imagens e realçar os contornos;
- Usar técnicas de detecção de bordas das imagens, como: *"threshold"* e *"findContours"*;
- Utilizar técnicas de restauração de imagens, como: filtros adaptativos e eliminação de ruídos;

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
