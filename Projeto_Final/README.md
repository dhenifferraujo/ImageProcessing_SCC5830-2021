# Projeto Final de Processamento de Imagens 2021 - Relatório Final - Entrega: 14/07/2021


Dheniffer Caroline Araújo Pessoa NºUSP: 12116252 |Douglas Queiroz Galúcio Batista Nº USP: 12114819
:------------------------------:|:------------------------------:

## Título do Projeto: Técnicas de realce, morfologia e segmentação aplicadas em imagens para detecção do nível de rios. 

  
### Resumo:

<p align="justify">
Esse projeto visa detectar o nível de rios através da medição de marcadores de nível de água. Para tal fim, foram aplicadas técnicas de realce, segmentação e morfologia nas imagens capturadas, a fim de tratar e melhorar a resolução dessas imagens e permitir uma análise mais precisa da medição do nível de rios.
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
Todas as imagens de referência podem ser acessadas neste repositório na pasta “imgs/in”.
</p>

Imagem 1 |Imagem 2
:------------------------------:|:------------------------------:
<img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/in/teste01.jpeg" width="400" height="400"> | <img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/in/teste02.jpeg" width="400" height="400"> 

Imagem 3 |Imagem 4
:-------------------------:|:-------------------------:
<img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/in/teste03.jpeg" width="400" height="400"> | <img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/in/teste08.jpeg" width="400" height="400">

Imagem 5|Imagem 6  
:-------------------------:|:-------------------------:
<img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/in/teste05.jpeg" width="400" height="400">  |  <img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/in/teste11.jpeg" width="400" height="400">


### Etapas e Métodos:
- Elaboração e captura de imagens com simulação de ruídos/interferências nos marcadores para simular um cenário real.
- Leitura e conversão das imagens em uma escala de cinza usando o método *cvtColor()* da biblioteca OpenCV. Esse método converte uma imagem de um espaço de cor para outro.
- Após as imagens serem convertidas em escala de cinza. Aplicamos os métodos morfológicos *erode()* e *dilate()* (erosão e dilatação). Usamos esses métodos para remover ruídos das imagens. 
- Utilizamos o método *threshold()* com binarização de Otsu para segmentar as imagens, ou seja, aplicar o limite (limiar). Optamos por usar a binarização de Otsu porque estamos trabalhando com imagens bimodais. 
- Após as imagens serem segmentadas, aplicamos o método *findCountours()* para encontrar os contornos. Ou seja, encontrar as barras pretas em um fundo branco. 
- Por fim, criamos um laço de repetição para percorrer e contar todos os contornos em forma de retângulo encontrados. Para isso, foi levado em consideração a distância e ângulo em que a imagem foi capturada. Obs: os valores definidos na função para a barra a ser encontrada são uma área entre 1000 a 4000, com proporção de preenchimento entre 9 a 14.5. 

### Resultados:
Todas as imagens de saída podem ser acessadas neste repositório na pasta “imgs/out”.

A seguir é possível visualizar as imagens 7 e 8 em que obtivemos resultados positivos. Isto é, foram encontradas todas as barras. Essas imagens possuem algumas características em comum: as barras nas cores predominantemente escuras e o background totalmente branco. Ou seja, elas possuem poucos ruídos. Acreditamos que obtemos bons resultados por termos utilizado métodos morfológicos que fizeram um processo de erosão e dilatação nas imagens, consequentemente, os contornos ficaram mais lineares, o que acabou facilitando a leitura e montagem dos retângulos das barras. Além disso, a aplicação do método blur deixou as imagens mais "borradas" e realçou as intersecções das cores claras e escuras.  

Imagem 7: Resultado - Sucesso
:------------------------------:
<img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/out/teste01_out.png" width="1000" height="600">

Imagem 8: Resultado - Sucesso
:------------------------------:
<img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/out/teste02_out.png" width="1000" height="600">

A seguir é possível visualizar as imagens 9 e 10 em que obtivemos resultados negativos. Ou seja, algumas barras não foram encontradas. A maioria das imagens que não obtivemos resultados positivos possuíam bastante ruídos no sentido de pouca luminosidade. Observamos que quando a imagem possuía sombra, o método de threshold reconhecia as sombras como uma binarização escura, e consequetemente, as sombras localizadas sob as barras acabaram dificultando o realce do contorno das imagens. Como podemos visualizar nas figuras 9 e 10. Acreditamos que a maior causa desses resultados insatisfatórios são a falta de realce de luminosidade nas áreas sombreadas sob as barras. 

Imagem 9: Resultado - Fracasso
:------------------------------:
<img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/out/teste06_out.png" width="1000" height="600">

Imagem 10: Resultado - Fracasso
:------------------------------:
<img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/out/teste10_out.png" width="1000" height="600">

### Componentes:

Dheniffer Caroline Araújo Pessoa Nº USP: 12116252


Douglas Queiroz Galucio Batista Nº USP: 12114819

Funções: 
- Implementação dos códigos (Dheniffer e Douglas);
- Testes (Dheniffer e Douglas);
- Documentação do código (Dheniffer e Douglas);
- Confecção do relatório (Dheniffer e Douglas). 

### Código do projeto:

<p align="justify">
Os códigos implementados para este projeto final podem ser acessados neste repositório do GitHub na pasta "codes". Além disso, também disponibilizamos uma demo do programa no Google Colaboratory, é possível acessar essa demo neste repositório na pasta "codes/Bars_detections.ipynb"
</p>


