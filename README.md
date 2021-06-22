# Projeto Final de Processamento de Imagens 2021 - Relatório Parcial


**Alunos:** Dheniffer Caroline Araújo Pessoa NºUSP: 12116252 e Douglas Queiroz Galúcio Batista Nº USP: 12114819

**Título do Projeto:** Realce e Segmentação aplicados em imagens para detecção do nível do rio em São Carlos.

**Resumo:**

Nos últimos anos, o aumento de eventos de enchentes e inundações vêm afetando o mundo inteiro. No Brasil, frequentemente ocorrem enchentes e inundações, principalmente durante os períodos chuvosos. Esses eventos resultam em grandes prejuízos sociais e econômicos. No município de São Carlos, localizado no interior de São Paulo, constantemente ocorrem episódios de enchentes que acarretam em muitos danos para a população local. À vista disso, esse projeto visa minimizar os danos causados pelas enchentes através da medição dos marcadores do nível de rio e aplica técnicas de realce, restauração e morfologia nas imagens capturadas, a fim de tratar e melhorar a resolução dessas imagens e permitir uma análise mais precisa da medição do nível do rio.


**Objetivo Principal do Projeto:**
Aplicar técnicas de realce, restauração e morfologia em imagens capturadas dos rios de São Carlos, a fim de melhorar a resolução das imagens e permitir uma análise mais precisa da medição do nível do rio. 

**Descrição das Imagens de Entrada:**
As imagens utilizadas nesse projeto são marcadores de nível de rio. Para a realização dos testes iniciais, nós utilizamos imagens de simulação de marcadores elaboradas manualmente pelos autores. Para essa primeira etapa dos testes as imagens se diferenciam pelo ângulo, distância e resolução. 

**Exemplos de imagens de entrada**
Todas as imagens de referência podem ser acessadas neste repositório na pasta “imgs”.


Imagem 1 |Imagem 2
:-------------------------:|:-------------------------:
<img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/teste1.jpeg" width="300" height="300"> | <img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/teste2.jpeg" width="300" height="300"> 

Imagem 3 |Imagem 4
:-------------------------:|:-------------------------:
<img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/teste3.jpeg" width="300" height="300"> | <img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/teste4.jpeg" width="300" height="300">

Imagem 5|Imagem 6  
:-------------------------:|:-------------------------:
<img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/teste5.jpeg" width="300" height="300">  |  <img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/teste7.jpeg" width="300" height="300">


**Materiais e Métodos:**
- Elaborar imagens com ruídos/ocultações nos marcadores para simular um cenário real;
- Simular condições de uma foto real ao invés de usar uma foto sintética;
- Ler as imagens e converter em uma escala de cinza usando o filtro *"grayscale"*;
- Aprimorar imagens para realçar os contornos através da técnica de morfologia;
- Usar técnica de detecção de bordas das imagens, como: *"threshold"* e *"findContour"*;
- Utilizar técnicas de restauração de imagens, como: filtros adaptativos e eliminação de ruídos;

**Código Inicial:**
Os códigos iniciais implementados nos testes podem ser acessados neste repositório na pasta "codes".
O código "teste_v1" pega as imagens, transforma em escala de cinza e então procura os contornos usando o "threshold", "canny" e "findContour" da biblioteca OpenCV sem nenhum melhoramento das imagens. Por fim, é feito um laço de repetição para encontrar as formas geométricas de um retângulo;

No código "teste_v2" usamos a técnica  LBP (Local Binary Pattern) para classificação de textura, além disso utilizamos um filtro morfológico de erosão e dilatação. Usando as funções, respectivamente, "erode" e "dilate". Em seguida, nós implementamos uma técnica de remoção de ruído através do filtro Gaussiano. Finalmente, analisamos as formas geométricas de um retângulo através de um laço de repetição;

No código "teste_v3" utilizamos um filtro 2D (Filtro Linear Arbitrário), em seguida usamos o *"threshold"* e *"findContour"* para detectar os contornos das imagens. Por fim, fizemos um laço de repetição para verificar quais dos contornos têm a forma de um retângulo. Por fim, o algoritmo faz a contagem dos retângulos (barras) encontrados. 
