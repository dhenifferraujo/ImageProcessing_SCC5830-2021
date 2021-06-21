# Projeto Final de Processamento de Imagens 2021 - Relatório Parcial


**Alunos:** Dheniffer Caroline Araújo Pessoa NºUSP: 12116252 e Douglas Queiroz Galúcio Batista Nº USP: 12114819

**Título do Projeto:** Realce e Segmentação aplicados em imagens para detecção do nível do rio em São Carlos.

**Resumo:**

Nos últimos anos, o aumento de eventos de enchentes e inundações vêm afetando o mundo inteiro. No Brasil, frequentemente ocorrem enchentes e inundações, principalmente durante os períodos chuvosos. Esses eventos resultam em grandes prejuízos sociais e econômicos. No município de São Carlos, localizado no interior de São Paulo, constantemente ocorrem episódios de enchentes que acarretam em muitos danos para a população local. À vista disso, esse projeto visa minimizar os danos causados pelas enchentes através da medição do nível de rio obtida por meio de um sensor câmera e marcadores que funcionam como ponto de referência e aplica técnicas de realce e segmentação das imagens capturadas pela câmera, a fim de tratar e melhorar a resolução das imagens e permitir uma análise mais precisa da medição do nível do rio. Além disso, um algoritmo de Redes Neurais é utilizado para o mapeamento da quantidade de marcadores não submersos na água.


**Objetivo Principal do Projeto:**
Aplicar técnicas de realce e segmentação em imagens capturadas dos rios de São Carlos, a fim de melhorar a resolução das imagens e permitir uma análise mais precisa da medição do nível do rio. 

**Descrição das Imagens de Entrada:**
As imagens utilizadas nesse projeto são marcadores de nível de rio. Para a realização dos testes iniciais, nós utilizamos imagens de simulação de marcadores elaboradas por nós mesmos. Para essa primeira etapa dos testes as imagens se diferenciam pelo ângulo, distância e resolução. 

**Exemplos de imagens de entrada**
Todas as imagens de referência podem ser acessadas neste repositório na pasta “imgs”.


Imagem 1 |Imagem 2
:-------------------------:|:-------------------------:
<img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/teste1.jpeg" width="300" height="300">
<img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/teste2.jpeg" width="300" height="300">

Imagem 3 |Imagem 4
:-------------------------:|:-------------------------:
<img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/teste3.jpeg" width="300" height="300">  |  <img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/teste4.jpeg" width="300" height="300">

Imagem 5|Imagem 6  
:-------------------------:|:-------------------------:
<img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/teste5.jpeg" width="300" height="300">  |  <img src="https://github.com/dhenifferraujo/ImageProcessing_SCC5830-2021/blob/main/Projeto_Final/imgs/teste7.jpeg" width="300" height="300">


  
  
  
  
**Materiais e Métodos:**
