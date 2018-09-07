
# Histórico de Revisão

| Data |Versão|Modificação|Autor|
|:-----|:-----|:----------|:----|
|30/08/2018|1.0|Criação do documento e adição do tópico 1|Pedro Rodrigues|
|31/09/2018|1.1|Adição do tópico 5|Matheus Blanco|
|04/09/2018|1.2|Adição do tópico 2|Gabriel Braga, Matheus Blanco|
|05/09/2018|1.3|Adição dos tópicos 2.2|Matheus Blanco, Gabriel Braga|
|05/09/2018|1.4|Adição do tópico 3|Gabriel Filipe|
|06/09/2018|1.5|Atualiza tópicos 1 e 3|Matheus Blanco|
|06/09/2018|1.6|Revisão do Diagrama de Relações e do tópico 2.1|Matheus Blanco, Gabriel Braga|
|07/09/2018|1.6|Revisão do tópico 2.1|Matheus Blanco|

# 1. Introdução  

<p  align="justify">  &emsp;&emsp;Este documento visa apresentar a arquitetura de software aplicada no desenvolvimento do ChatBot Lino, garantindo uma facilidade de visualização dos requisitos e da estrutura para com os desenvolvedores.</p>

## 1.1 Finalidade  

<p  align="justify">  &emsp;&emsp;Este documento trata de uma visão ampla da arquitetura do ChatBot e esboça os aspectos do mesmo. Ele visa transparecer as decisões arquiteturais que foram tomadas em relação ao software.</p>

## 1.2 Escopo

<p  align="justify">  &emsp;&emsp;O ChatBot Lino tem como principal objetivo servir a comunidade do Campus do Gama da UnB(FGA). A partir da utilização de tecnologias de fluxo de conversa, pesquisa na internet e bancos de dados, o ChatBot irá servir como um assistente para a comunidade, enviando alertas, novidades e e-mails, além de ser capaz de informar aos alunos certos procedimentos para retirada de documentos. Toda parte arquitetural do projeto será tratada neste documento e as decisões a serem tomadas acerca do mesmo serão administradas pelos alunos da matéria de Métodos de Desenvolvimento de Software, Alunos da matéria de Engenharia de Produto de Software e a professora da UnB Carla.</p>

## 1.3 Visão Geral

<p  align="justify">  &emsp;&emsp;O documento através de 4 principais tópicos e suas ramificações visa detalhar a arquitetura e os requisitos do software. Facilitando o desenvolvimento e esclarecendo dúvidas.</p>

Estrutura do documento:  

* Introdução;

* Representação da Arquitetura;

* Metas e Restrições de Arquitetura;

* Visão lógica;  

## 1.4 Definições, Acrônimos e Abreviações

* API: Application Programming Interface
* DB: Banco de Dados, <i>DataBase</i> 

## 1.5 Referências


> MELO, Thalisson; ALVES, Álax; MARTINS, Lucas; RICHARD, Matheus; BERNARDO, Matheus de Sousa; Joranhezon. <b>Owla:</b> Documento de Arquitetura. Disponível em: <https://github.com/fga-gpp-mds/2016.2-Owla/wiki/Documento-de-Arquitetura>.


> André; Gabriel; Guilherme; ALMEIDA; Weyler. <b>Cidade Democrática:</b> Documento de Arquitetura. Disponível em: <https://github.com/fga-gpp-mds/2016.2-CidadeDemocratica/wiki/Documento-de-Arquitetura>.


# 2. Representação da Arquitetura

## 2.1 Diagrama de Relações
![enter image description here](https://lh3.googleusercontent.com/jwCBLJTnFdvGMROGYgvyPLIR8osCUmrYvb4vfOe4RBdNCwekRP_7Tx_bkf-8h81PuuxjK43GA-Lx "Diagrama de Relações")

<p  align="justify">  &emsp;&emsp;A arquitetura pensada para este projeto será a arquitetura de repositório. Esta, também conhecida como <i>Blackboard</i> trabalha de maneira que todos os subsistemas manipulam a mesma base de dados. É utilizada principalmente em projetos onde grandes quantidades de dados são manuseados. Suas vantagens são:</p>

* Compartilhamento eficiente de dados;
* <i>Backup</i> centralizado;
* Possibilidade de implementação de proteção de dados;
* Os subsistemas gravadores de dados não precisam saber quem os utilizará;
* Fácil integração de subsistemas.

<p  align="justify">  &emsp;&emsp;A principal tecnologia do ChatBot é o <i>Rasa NLu</i>. Esta tecnologia trabalha com o processamento natural de linguagem, a partir dela o desenvolvedor abre portas relacionadas a processamento de texto que o permitem criar um ambiente de comunicação mais interativo e humano, podendo assim criar uma comunicação mais fluida e dinâmica com o usuário.</p>
<p  align="justify">  &emsp;&emsp;A utilzação da tecnologia no desenvolvimento de um ChatBot permite a implementação de uma comunicação mais humanizada, permitindo assim uma maior interatividade com o usuário. Com o tempo, a interação com o usuário permitirá ao programa um treinamento dele mesmo para melhor se comunicar com o exterior. Este é o principal objetivo da utilização do <i>Rasa NLU</i> para o processamento de linguagem do projeto em questão.</p>
<p  align="justify">  &emsp;&emsp;Algumas dos principais benefícios da tecnologia são:</p>

*  Manuseio de conversação com <i>deep learning</i> para auto-evolução;
*  <i>Open source</i> e customizável para o panorama do projeto;
*  <i>Machine learning</i> integrado para melhores resultados.

<p  align="justify">  &emsp;&emsp;A tecnologia irá se comunicar com outras com o intuito de captar e processar informações do exterior, de acordo com as necessidades do usuário. Na próxima seção serão descritas as tecnologias utilizadas e como elas se relacionam com o <i>Rasa NLU</i>.</p>

## 2.2 Tecnologias

## 2.2.1 API Telegram e API Facebook - Messenger

<p  align="justify">  &emsp;&emsp;Telegram e Messenger são dois aplicativos de comunicação e  bate-papo, comumente utilizados para a conversação em grupo ou de uma pessoa com outra. Os dois aplicativos proveêm aos seus usuários desenvolvedores a possibilidade de implementarem diferentes funcionalidades e <i>bots</i>, a partir de suas APIs.</p>

<p  align="justify">  &emsp;&emsp;As APIs dessas duas plataformas serão as pontes de comunicação com o usuário. A partir da implementação e integração do código-fonte com o <i>Rasa NLU</i>, o Telegram e o Messenger irão interagir com o aluno, recebendo suas mensagens e respondendo apropriadamente.</p>

## 2.2.2 MongoDB

<p  align="justify">  &emsp;&emsp;A tecnologia MongoDB é um banco de dados <i>open-source</i> orientado a documentos. Classificado como NoSQL, a tecnologia utiliza documentos com padrão JSON.</p>

<p  align="justify">  &emsp;&emsp;Esta tecnologia se comunicará com o projeto de maneira que receberá os dados fornecidos pelas conversas e interações realizadas no ChatBot e as armazenará em um banco de dados, para posteriormente serem usadas na metrificação da utilização do ChatBot.</p>

## 2.2.3 Web crawler

<p  align="justify">  &emsp;&emsp;Um <i>web crawler</i> é um Bot de internet utilizado para buscar e atualizar informações específicas de sites espalhados pela internet de maneira sistemática.</p>

<p  align="justify">  &emsp;&emsp;No projeto, o <i>Web crawler</i> será utilizado para buscar e processar as informações requisitadas pelo usuário. A partir da ação identificada pelo <i>Rasa</i>, o <i>crawler</i> irá entrar no website do restaurante universitário e de lá, procurar e extrair as informações sobre o cardápio do dia. Além disso, o <i>crawler</i> irá trabalhar com a API do servidor Gmail e de lá irá extrair os informes e e-mails enviados pelos professores, exibindo-os para os alunos.</p>

## 2.2.4 Elasticsearch

<p  align="justify">  &emsp;&emsp;<i>Elasticsearch</i> é um mecanismo de pesquisa baseado em <i>Representational state transfer</i>(REST) capaz de processar dados, tirados do banco de dados , podendo metrificá-los, funcionando no <i>back-end</i> de m projeto.</p>

<p  align="justify">  &emsp;&emsp;No projeto, o <i>Elasticsearch</i> ira captar os dados armazenados no banco de dados, realizando seu processamento e metrificação para a chegada em conclusões.</p>

## 2.2.5 Kibana

<p  align="justify">  &emsp;&emsp;<i>Kibana</i> é uma ferramenta de visualização que transforma o código de <i>back-end</i> do <i>Elasticsearch</i> em gráficos visualizáveis.</p>

<p  align="justify">  &emsp;&emsp;A ferramenta irá abstrair os dados metrificados captados do <i>Elasticsearch</i> e os transformará em gráficos de fácil análise, agindo como o <i>front-end</i> das metrificações.</p>

# 3. Metas e Restrições de Arquitetura

<p  align="justify">  &emsp;&emsp;As restrições de arquitetura do projeto são:</p>

* Utilização de um Banco de Dados <i>MongoDB</i>.

* Conexão com a internet necessária.

<p  align="justify">  &emsp;&emsp;As metas do projeto são:</p>

* Disponibilizar um fluxo de conversa com o usuário afim de atender/suprir as dúvidas em relação à procedimentos voltados à comunidade acadêmica realizados na Universidade de Brasília.

* Fornecer aos alunos informações a respeito do cardápio do <i>RU</i> (Restaurante Universitário).

* Alertar a comunidade acadêmica à respeito de prazos e avisos importantes, ex.: data de matrícula.

* Disponibilizar o sistema 24 horas por dia, durante 7 dias na semana.

# 4. Visão Lógica

## 4.1 Diagrama de Pacotes

<p  align="justify">  &emsp;&emsp;Neste tópico se encontram o diagrama de pacotes bem como suas explicações e utilidades.</p>


* O pacote <i>2018.2-Lino</i> é o pacote principal do projeto e conterá todos os outros sub-pacotes e documentos existentes no projeto.


* No pacote <i>docs</i>, serão apresentados os documentos necessários para a compreensão do projeto, bem como pacote <i>policies</i>.


* No pacote <i>Policies</i> estão contidas as políticas de boas práticas de programação e uso da plataforma <i>GitHub</i>.
