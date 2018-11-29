# Histórico de Revisão

| Data       | Versão | Modificação                                     | Autor                         |
| :--------- | :----- | :---------------------------------------------- | :---------------------------- |
| 30/08/2018 | 1.0    | Criação do documento e adição do tópico 1       | Pedro Rodrigues               |
| 31/09/2018 | 1.1    | Adição do tópico 5                              | Matheus Blanco                |
| 04/09/2018 | 1.2    | Adição do tópico 2                              | Gabriel Braga, Matheus Blanco |
| 05/09/2018 | 1.3    | Adição dos tópicos 2.2                          | Matheus Blanco, Gabriel Braga |
| 05/09/2018 | 1.4    | Adição do tópico 3                              | Gabriel Filipe                |
| 06/09/2018 | 1.5    | Atualiza tópicos 1 e 3                          | Matheus Blanco                |
| 06/09/2018 | 1.6    | Revisão do Diagrama de Relações e do tópico 2.1 | Matheus Blanco, Gabriel Braga |
| 07/09/2018 | 1.7    | Revisão do tópico 2.1                           | Matheus Blanco                |
| 28/11/2018 | 1.8 | Revisão dos textos adequando a atual arquitetura | Guilherme Augusto |
| 28/11/2018 | 1.9 | Inclusão dos textos respectivos à nova arquitetura | Guilherme Augusto |
| 28/11/2018 | 2.0 |Inclusão da parte relacionada ao banco de dados relacionado à nova arquitetura | Guilherme Augusto |
| 29/11/2018 | 2.1 |Reparação de alguns erros de escrita e entendimento no texto| Letícia de Souza |

#### 1. Introdução  

<p  align="justify">    Este documento visa apresentar a arquitetura de software aplicada no desenvolvimento do ChatBot Lino, garantindo uma facilidade de visualização dos requisitos e da estrutura para com os desenvolvedores.</p>

##### 1.1 Finalidade  

<p  align="justify">     Ao esboçar uma visão ampla da arquitetura do ChatBot, é possível evidendiar seus aspectos. Sendo assim, nesse documento buscaremos transparecer as decisões arquiteturais que foram tomadas em relação ao Bot Lino.</p>

##### 1.2 Escopo

<p  align="justify">    O Lino tem como principal objetivo auxiliar a comunidade do Campus do Gama da UnB(FGA) à partir da utilização de tecnologias de fluxo de conversa, mapeamento de sites da rede e de bancos de dados para o registro de usuário e gerenciamento de notificações desejadas. O Lino servirá como um assistente para a comunidade, enviando alertas e novidades relacionadas à comunidade acadêmica, informando alunos sobre determinados procedimentos para retirada de documentos e sobre o cardápio disponibilizado na semana pelo Restaurante Universitário (RU) da FGA, dando a opção de escolherem por uma refeição específica ou o cardápio completo do dia ou da semana.</p>

##### 1.3 Visão Geral

<p  align="justify">    O documento, através de quatro principais tópicos e suas ramificações, visa detalhar a arquitetura e os requisitos do software. Facilitando o desenvolvimento e esclarecendo dúvidas a respeito deste.</p>

Estrutura do documento:  

<html>
<ul>

<li> Introdução; </li>
<li> Representação da Arquitetura; </li>
<li> Metas e Restrições de Arquitetura; </li>
<li> Visão lógica;   </li>

</ul>
</html>

##### 1.4 Definições, Acrônimos e Abreviações

<html>
<ul>

<li> API: Application Programming Interface </li>
<li> DB: Banco de Dados, <i>DataBase</i> </li>

</ul>
</html>

##### 1.5 Referências


> MELO, Thalisson; ALVES, Álax; MARTINS, Lucas; RICHARD, Matheus; BERNARDO, Matheus de Sousa; Joranhezon. <b>Owla:</b> Documento de Arquitetura. Disponível em: <https://github.com/fga-gpp-mds/2016.2-Owla/wiki/Documento-de-Arquitetura>.


> André; Gabriel; Guilherme; ALMEIDA; Weyler. <b>Cidade Democrática:</b> Documento de Arquitetura. Disponível em: <https://github.com/fga-gpp-mds/2016.2-CidadeDemocratica/wiki/Documento-de-Arquitetura>.


#### 2. Representação da Arquitetura

##### 2.1 Diagrama de Relações

<img src="https://user-images.githubusercontent.com/26308278/49151678-c756d280-f2f7-11e8-9584-2dd21b89f508.png" class="center">

<p  align="justify">&emsp;&emsp;O projeto foi modelado para uma arquitetura híbrida, envolvendo a arquitetura de Microsserviços juntamente com elementos da arquitetura de repositórios, representando os serviços internos que serão mostrados posteriormente, integrando com os serviços externos que são consumidos.</p>

<p align="justify">&emsp;&emsp; O desenvolvimento de um diálogo é de grande importância pro contexto do bot, logo, com a característica de <i>Machine Learning</i> para a melhora de suas conversas, é essencial para manter um diálogo apropriado e interativo com o usuário.</p>

<p  align="justify">&emsp;&emsp;O Rasa Core é um dos componentes importantes dentro da arquitetura do Bot, em associação ao Rasa Core, existe outro componente tecnológico atrelado ao ChatBot: <i>Rasa NLU</i>, que trabalha com o processamento natural de linguagem e, a partir dela, o desenvolvedor abre portas relacionadas ao processamento de texto que o permitem criar um ambiente de comunicação mais interativo e humano, podendo assim criar uma comunicação mais fluida e dinâmica com o usuário.</p>

<p align="justify">&emsp;&emsp;A utilização da tecnologia no desenvolvimento de um ChatBot permite a implementação de uma comunicação mais humanizada, permitindo assim uma maior interatividade com o usuário. Com o tempo, a interação com o usuário permitirá ao programa um treinamento dele mesmo para melhor se comunicar com o exterior. Este é o principal objetivo da utilização do <i>Rasa NLU</i> para o processamento de linguagem do projeto em questão.</p>
<p  align="justify">&emsp;&emsp;Algumas dos principais benefícios da tecnologia são:</p>

<html>
<ul>

<li>  Manuseio de conversação com <i>deep learning</i> para auto-evolução; </li>
<li>  <i>Open source</i> e customizável para o panorama do projeto; </li>
<li>  <i>Machine learning</i> integrado para melhores resultados. </li>

</ul>
</html>

<p  align="justify">&emsp;&emsp;A tecnologia irá se comunicar com outras com o intuito de captar e processar informações do exterior, de acordo com as necessidades do usuário.</p>

<p align="justify">&emsp;&emsp;Relacionado a parte de arquitetura de micro serviços, foram definidos 4 serviços internos (serviços a serem implementados), além dos 3 serviços externos (serviços a serem utilizados), sendo eles:</p>

###### 2.1.1 Serviços Internos

<html>
<ul>

<li> <i>WebCrawler</i> do Restaurante Universitário - WebCrawler RU </li>
<li> <i>WebCrawler</i> do Calendário de Matrícula - WebCrawler Matrícula </li>
<li> Serviço para tratamento e envio de informações do <i>Gmail</i> - Lino-Alerta </li>  
<li> Notificações de alerta - Cronjob Lino </li>

</ul>
</html>

###### 2.1.2 Serviços Externos

<html>
<ul>

<li> Serviço de <i>API</i> do <i>Gmail</i> para gerenciamento de notificações dos professores via e-mail </li>
<li> Mensageiro <i>Telegram</i> para interação </li>
<li> Mensageiro do <i>Facebook</i> (<i>Facebook Messenger</i>) </li>

</ul>
</html>

<p align="justify">&emsp;&emsp;Outro fator da arquitetura do projeto é o estilo arquitetural Broker, que tem como principal finalidade servir de intermediário na comunicação entre os micro serviços de forma facilitada através de métodos que permitem flexibilidade de mudanças, escalabilidade e transparência na localização dos serviços, bem como a robustez da comunicação entre os serviços.</p>

<p align="justify">&emsp;&emsp;Além de tais serviços, também existe a integração de um painel para a análise de dados relativos às métricas associadas no Backlog de produto.</p>

##### 2.2 Tecnologias

###### 2.2.1 API Telegram Messenger e API Facebook Messenger

<p  align="justify">&emsp;&emsp;Telegram Messenger e o Facebook Messenger são dois aplicativos de comunicação e bate-papo, comumente utilizados para a conversação em grupo ou de uma pessoa com outra. Os dois aplicativos proveem aos seus usuários desenvolvedores a possibilidade de implementarem diferentes funcionalidades e <i>bots</i>, a partir de suas APIs.</p>

<p  align="justify">&emsp;&emsp;As <i>APIs</i> dessas duas plataformas serão as pontes de comunicação com o usuário. A partir da implementação e integração do código-fonte com o <i>Rasa NLU</i>, o Telegram e o Messenger irão interagir com o aluno, recebendo suas mensagens e respondendo apropriadamente.</p>

###### 2.2.2 MongoDB

<p  align="justify">&emsp;&emsp;A tecnologia MongoDB é um banco de dados <i>open-source</i> orientado a documentos. Classificado como NoSQL, a tecnologia utiliza documentos com padrão JSON.</p>

<p  align="justify">&emsp;&emsp;Esta tecnologia se comunicará com o projeto de maneira que receberá os dados fornecidos pelas conversas e interações realizadas no ChatBot e as armazenará em um banco de dados, para posteriormente serem usadas na metrificação da utilização do ChatBot.</p>

###### 2.2.3 WebCrawler

<p  align="justify">&emsp;&emsp;Um <i>web crawler</i> é um rastreador automatizado utilizado para buscar e atualizar informações específicas de sites espalhados pela internet de maneira sistemática.</p>

<p  align="justify">&emsp;&emsp;Neste projeto, está sendo utilizado dois tipos de <i>WebCrawler</i> para buscar e processar as informações requisitadas pelo usuário. A partir da ação identificada pelo <i>Rasa</i>, os <i>crawlers</i> entraram nos <i>websites</i> determinados (um na página do restaurante universitário e outro na página da secretaria de administração acadêmica) e a partir desse ponto, irá procurar e extrair as informações necessárias relacionadas à cada serviço.</p>

<p  align="justify">&emsp;&emsp;Nesse processamento de informações, a parte funcional dos alertas aos usuários também faz parte do serviço. O alerta tem como finalidade informar o usuário que deseja receber a notificação de algo relacionado ao cardápio, a partir de um agendamento de mensagens para horários específicos. Além disso, ele possibilita também receber notificações relativas à noticias associadas à comunidade acadêmica, onde, inicialmente, apenas professores e servidores teriam acesso.</p>

###### 2.2.4 Flask

<p align="justify">&emsp;&emsp;Flask é um microframework web escrito em Python e baseado na bibliotecas WSGI Werkzeug e Jinja2. Além dele ser facilmente importado para uso em um projeto com base em código python, ele proporciona uma simplicidade nas operações, ao passe que em simples microserviços são facilmente satisfeitos por ele.</p>

##### 2.3 Representação dos Serviços

<p align="justify">&emsp;&emsp;Relacionado aos microserviços propostos pela equipe, faz-se o uso de serviços internos desenvolvidos e os serviços externos, utilizados para atingir a finalidade do Lino. Entre eles, temos:</p>

* <i>Webcrawler</i> do Restaurante Universitário - WebCrawler RU
* <i>Webcrawler</i> do Calendário de Matrícula - WebCrawler Matrícula
* Captação de e-mails através da API <i>G-mail</i> - Lino-Alerta
* Notificações de alerta - Cronjob Lino

Além disso, temos o core do projeto, que apesar da relevância, uma suposta falha não afeta o funcionamento dos demais serviços existes. O Lino, tem a capacidade de fazer, atualmente, uma integração com os mensageiros Telegram e Facebook Messenger, buscando realizar uma comunicação de forma mais natural e entendível, fazendo uso das tecnologias de inteligência artificial para compreensão de linguagem natural e integrando com demais serviços que fornecem informações para o Bot tratar adequadamente.

##### 2.3.1 Webcrawler RU    

<p align="justify">&emsp;&emsp;Este microserviço tem como objetivo principal mapear a busca do cardápio do Restaurante Universitário (RU) específico da Universidade de Brasília, relacionado ao Campus Gama (UnB-FGA). Seu propósito é mapear a página onde o cardápio é disponibilizado, realizar o <i>download</i> do PDF associado a data correta da semana e transcrever a informação de seu conteúdo para texto com a finalidade de utilizar no contexto do envio do cardápio diário, semanal e específico (café da manhã, almoço e jantar), através de mensagens aos usuários dos serviços do <i>Telegram</i> e do <i>Facebook</i>.</p>
<p align="justify">&emsp;&emsp;Ele faz uso das tecnologias <i>Python</i> utilizando o <i>microframework Flask</i> para habilitar as rotas necessárias para a obtenção do cardápio em formato de texto, sendo para o cardápio do dia, da semana e de cardápios específicos citados anteriormente. Também, além das rotas para isso, o serviço utiliza o banco de dados <i>MongoDB</i> para facilitar o acesso à informação e otimizar o custo de envio, pois com os dados salvos no banco de dados, é facilitado o acesso após a solicitação dos usuários específicos de cada mensageiro.</p>
<p align="justify">&emsp;&emsp;Relacionado ao banco de dados associado ao serviço, foi utilizado o mesmo padrão de todos os serviços, o <i>MongoDB</i>. De forma técnica, a estrutura do WebCrawler RU é a estrutura mais complexa dos serviços, contendo sua separação por tipo de cardápio, sendo eles:</p>

* Cardápio do café da manhã
* Cardápio do almoço
* Cardápio do jantar
* Cardápio do dia
* Cardápio da semana

<p align="justify">&emsp;&emsp;A respeito da estrutura geral do banco associado ao WebCrawler RU, temos a seguinte diagramação:</p>

<img src="https://user-images.githubusercontent.com/26308278/49156611-e90a8680-f304-11e8-83bc-421e7020b7fb.png" class="center">

##### 2.3.2 Webcrawler Matrícula

<p align="justify">&emsp;&emsp;O WebCrawler Matrícula tem como finalidade pegar as informações referentes ao calendário de matrícula disponibilizado no site da [SAA](http://www.saa.unb.br/graduacao/62-calendario-de-matricula). Com isso, ele associa qualquer dúvida relacionada ao calendário, enviando-o aos usuários que o solicitaram, no formato de uma imagem PNG, facilitando, portanto, o acesso à informação de forma prática e rápida.</p>
<p align="justify"> Este serviço faz uso das tecnologias <i>Python</i> com o <i>microframework Flask</i> para habilitar rotas que o auxiliam a realizar o download do PDF periodicamente e para acesso em formato de imagem (através do uso de bibliotecas especializadas nessa conversão), realizando o envio adequado aos usuários solicitantes.</p>

##### 2.3.3 Lino-Alerta

<p align="justify">&emsp;&emsp;O serviço Lino-Alerta tem como objetivo alertar os usuários que necessitam receber as notificações da comunidade acadêmica. De forma básica, o sistema trabalha com o uso do <i>MongoDB</i>, banco de dados orientado a documentos, fazendo com que os usuários que estejam registrados em seu sistema (professores e servidores) consigam realizar o envio de uma notícia para o <i>e-mail</i> do Lino, notificando todos os usuários que desejam receber.</p>
<p align="justify">&emsp;&emsp;Tal serviço faz uso das tecnologias <i>Java</i>, especificadamente com o interpretador <i>Node.js</i>, a fim de facilitar na criação de rotas para obtenção dos dados informativos da notícia enviada ao <i>e-mail</i>, trabalhando com requisições temporárias para analisar se existe um novo <i>e-mail</i> recebido pelo Lino.</p>
<p align="justify">&emsp;&emsp;O banco relacionado ao serviço tem uma estrutura mais simples, apenas contendo as informações dos notificadores, recebendo um <i>id</i> para identificá-los individualmente, tratando as permissões apenas aos usuários cadastrados. Estes dados estão sendo registrados de forma manual, não existindo um sistema de cadastro, utilizando a lista disponibilizada pela secretaria da Universidade de Brasília - Campus Gama (UnB-FGA).</p>

<img src="https://user-images.githubusercontent.com/26308278/49170783-10248080-f324-11e8-9f25-b9ade17366a2.png" class="center">

##### 2.3.4 Cronjob Lino

<p align="justify">&emsp;&emsp;O Cronjob Lino é um microserviço especializado em trabalhar com os agendamentos disponibilizados pelo Lino, tratando o envio do cardápio diário, semanal e específico, além do envio das notícias recebidas pelo e-mail do Lino. Seu principal objetivo é se especializar no envio das notificações para os usuários que desejam receber.</p>
<p align="justify">&emsp;&emsp;Para o envio das notificações, o serviço faz uso de um banco modelado para cada tipo de mensageiro, com uma estrutura mais simples que a do <i>WebCrawler RU</i>, mas com as informações necessárias para tratar os dados diretamente com os usuários.</p>

<img src="https://user-images.githubusercontent.com/26308278/49173185-21708b80-f32a-11e8-9fc9-69b9df2d7cf3.png" class="center">

#### 3. Metas e Restrições de Arquitetura

<p align="justify">&emsp;&emsp;As restrições de arquitetura do projeto são:</p>

<html>
<ul>

<li> Utilização de um Banco de Dados <i>MongoDB</i> para cada serviço interno, ou seja, um banco para o <i>WebCrawler RU</i>, um banco para o serviço de tratamento de alertas do <i>Gmail</i>, para o <i>WebCrawler</i> de Matrícula_ e um banco para cada serviço de mensageria que utilizamos (um para o Telegram Messenger e um para o Facebook Messenger). </li>
<li> Utilização da ferramenta Docker para a virtualização dos ambientes de forma prática e adequada </i>
<li> Conexão com a internet necessária. </li>

</ul>
</html>

<p align="justify">    As metas do projeto são:</p>

<html>
<ul>

<li> Disponibilizar um fluxo de conversa com o usuário a fim de atender/suprir as dúvidas em relação à procedimentos voltados à comunidade acadêmica realizados na Universidade de Brasília. </li>
<li> Fornecer aos alunos informações a respeito do cardápio do <i>RU</i> (Restaurante Universitário).</li>
<li> Alertar a comunidade acadêmica à respeito de prazos e avisos importantes, ex.: data de matrícula.</li>
<li> Disponibilizar o sistema a maior quantidade de tempo possível, reconhecendo as limitações dos servidores utilizados para hospedagem do Bot. </li>

</ul>
</html>

#### 4. Visão Lógica

##### 4.1 Diagrama de Pacotes

<p  align="justify">    Neste tópico se encontram o diagrama de pacotes bem como suas explicações e utilidades.</p>

<html>
<ul>

<li> O pacote <i>2018.2-Lino</i> é o pacote principal do projeto e conterá todos os outros sub-pacotes e documentos existentes no projeto. </li>
<li> No pacote <i>docs</i>, serão apresentados os documentos necessários para a compreensão do projeto, bem como pacote <i>policies</i>. </li>
<li> No pacote <i>Policies</i> estão contidas as políticas de boas práticas de programação e uso da plataforma <i>GitHub</i>. </li>

</ul>
</html>

<br>
