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
Aplicar técnicas de processamento de imagens, tais como realce, restauração, segmentação e morfologia em imagens de marcadores de nível de água. 

### Descrição das Imagens de Entrada:

<p align="justify">
As imagens utilizadas nesse projeto são simuladores de marcadores de nível de rio elaboradas pelos próprios autores. Essas imagens diferenciam-se pelo ângulo, distância e resolução. Para simular um ambiente real nos experimentos, nós capturamos as imagens com algumas interferências. De forma que as barras (marcadores de nível) não ficassem totalmente visíveis. 
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
- Por fim, criamos um laço de repetição para percorrer e contar todos os contornos em forma de retângulo encontrados. Para isso, foi levado em consideração a distância e ângulo em que a imagem foi capturada. Obs: os valores definidos na função para a barra a ser encontrada são uma área entre 1000 a 4000, com proporção de preenchimento entre 9 a 14.5. 
 
### Código do projeto:

<p align="justify">
Os códigos implementados para este projeto final podem ser acessados no repositório do GitHub <https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/tree/main/Projeto_Final> na pasta "codes".
</p>


