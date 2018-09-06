|Data| Versão |Modificação|Autor|
|:---:|:---:|:---:|:--:|
| 25/08/2018 |   1.0  | Criação do Documento| MDS (todos) |
| 27/08/2018 |   1.1  | Adição dos tópicos 3, 3.2, 3.3 e 3.4 | Guilherme Marques |
| 28/08/2018 |   1.2  | Adição da seção Introdução | Matheus Blanco |
| 28/08/2018 |   1.3  | Adição dos tópicos 3.5.1 e 3.5.2 | Guilherme Marques |
| 28/08/2018 |   1.4  | Revisão do tópico 1.4 | Matheus Blanco |
| 28/08/2018 |   1.5  | Adição do tópico 3.6 | Guilherme Marques |
| 28/08/2018 |   1.6  | Adição dos tópicos 4, 4.1 e 4.2 | Pedro Rodrigues |
| 28/08/2018 |   1.7  | Adição dos tópicos 5 | Pedro Rodrigues |
| 28/08/2018 |   1.8  | Revisão dos tópicos 4.2 e 5 | Pedro Rodrigues |
| 29/08/2018 |   1.9  | Adição do tópico 3.7 e revisão dos tópicos 3.5 e 3.6 | Guilherme Marques |
| 28/08/2018 |   1.10  | Adição do tópico 2 | Gabriel Braga |
| 28/08/2018 |   1.11  | Revisão do tópico 2.3 | Gabriel Braga |
| 06/09/2018 |   2.0  | Revisão do tópico 2.1, 3, 3.4, 8.1, 8.2 | Matheus Blanco |

# 1. Introdução

<p aligng="justify"> &emsp;&emsp;O documento de visão define o escopo de alto nível e o propósito do software a ser desenvolvido. Esse visa estabelecer as expectativas e reduzir os riscos do produto protegendo o cliente e os desenvolvedores do projeto.</p>

## 1.1 Finalidade

<p aligng="justify"> &emsp;&emsp;O documento presente tem, por finalidade, apresentar e estabelecer uma visão ampla sobre o ChatBot Lino de modo que deixe claro sua proposta, características, utilidades e funcionalidades.</p>

## 1.2 Escopo

<p aligng="justify"> &emsp;&emsp;O ChatBot Lino é um projeto realizado para as disciplinas Métodos de Desenvolvimento de <i>Software</i> (MDS) e Engenharia de Produto de <i>Software</i> (EPS), do curso Engenharia de <i>Software</i> da Faculdade UnB Gama (FGA) da Universidade de Brasília (UnB).</p>
<p aligng="justify"> &emsp;&emsp;O projeto, a ser realizado pela equipe 4, composta por alunos das duas disciplinas, e com orientação da professora Carla Rocha possui como objetivo a comunicação direta com o aluno matriculado na instituição de ensino superior. A partir da interação com o ChatBot, o usuário poderá requisitar deste serviços, ajudas, notícias e informes relacionados à faculdade e à universidade, como o passo-a-passo necessário para a emissão de determinado documento ou informações sobre a alimentação provida pelo Restaurante Universitário.

## 1.3 Definições, Acrônimos e Abreviações

* UnB - Universidade de Brasília
* MDS - Métodos de Desenvolvimento de <i>Software</i>
* EPS - Engenharia de Produto de <i>Software</i>
* Lino - O nome do ChatBot
* ChatBot - Programa de computador capaz de conduzir uma conversação através de via auditiva ou texto

## 1.4 Referências

>MINISTÉRIO DA SAÚDE - DEPARTAMENTO DE INFORMÁTICA. Coordenação-Geral de Análise e Manutenção. Guia de Preenchimento: Documento de Visão de Sistema. [S.l.: s.n.], 2018. 1 p;

>DOCUMENTO de Visão. 2017. Disponível em: <a href="https://github.com/fga-eps-mds/2017.1-Trezentos/wiki/Documento-de-Vis%C3%A3o#3-partes-envolvidas" target="_blank">https://github.com/fga-eps-mds/2017.1-Trezentos/wiki/Documento-de-Vis%C3%A3o#3-partes-envolvidas</a>. Acesso em: 2 de set. 2018

>2018.1-DR-DOWN: Documento de Visão. 2018. Disponível em: <a href="https://github.com/fga-eps-mds/2018.1-Dr-Down/blob/develop/docs/mds/VISION_DOCUMENT.md"target="_blank">https://github.com/fga-eps-mds/2018.1-Dr-Down/blob/develop/docs/mds/VISION_DOCUMENT.md</a>. Acesso em: 2 de set. 2018;

# 2. Posicionamento
## 2.1 Oportunidade de Negócio

<p align="justify"> &emsp;&emsp;Atualmente, as informações são repassadas para os estudantes através dos murais e redes sociais da Universidade. Para obter tais informações, deve-se acessar o portal Matrícula Web e em alguns casos comparecer na secretaria para retirada.</p>

<p align="justify"> &emsp;&emsp;Isso configura uma situação de dificuldade na obtenção das determinadas informações. Muitas vezes o aluno não tem a disponibilidade de comparecer ao local onde se encontram as informações, perdendo-as desta maneira. A forma do aluno se comunicar com a faculdade e os professores ainda não é realizada de maneira fácil e dinâmica. Dessa forma, o ChatBot se propôe a solucionar tais desafios.</p>

<p align="justify"> &emsp;&emsp;O ChatBot oferecerá o serviço automatizado de alertar os alunos a cerca de informações importantes sobre a universidade, além de fornecer instruções necessárias para a visualização e retirada de documentos. Dessa forma, aumenta-se a velocidade e a facilidade de acesso à documentação e informação, atualmente fornecida pela secretaria.</p>

## 2.2 Descrição do Problema
<table class="tg">
  <tr>
    <td class="tg-s6z2">O problema de</td>
    <td class="tg-031e">Desatualização dos estudantes e demora para retirada de documentos</td>
  </tr>
  <tr>
    <td class="tg-s6z2">Afeta</td>
    <td class="tg-031e">Agilidade de atualização</td>
  </tr>
  <tr>
    <td class="tg-s6z2">Cujo impacto é</td>
    <td class="tg-031e">Falta de informação e atraso</td>
  </tr>
  <tr>
    <td class="tg-s6z2">Uma boa solução seria</td>
    <td class="tg-031e">Automatização de todo o processo</td>
  </tr>
</table>


## 2.3 Sentença de Posição do Produto

<table class="tg">
  <tr>
    <td class="tg-s6z2">Para</td>
    <td class="tg-031e">Universidades</td>
  </tr>
  <tr>
    <td class="tg-s6z2">Que</td>
    <td class="tg-031e">Desejam acelerar o fornecimento de documentos e informação aos estudantes</td>
  </tr>
  <tr>
    <td class="tg-s6z2">O Lino</td>
    <td class="tg-031e">É um ChatBot</td>
  </tr>
  <tr>
    <td class="tg-s6z2">Que</td>
    <td class="tg-031e">Visa facilitar a interação entre Universidade e Aluno                                                                                 </td>
  </tr>
  <tr>
    <td class="tg-s6z2">Diferente de</td>
    <td class="tg-031e">Paginas em rede sociais</i>                                                                                 </td>
  </tr>
  <tr>
    <td class="tg-s6z2">Nosso produto</td>
    <td class="tg-031e">Instruciona alunos e fornece informações em menor tempo a cerca da Universidade                                                                                  </td>
  </tr>
</table>


# 3. Descrições dos Envolvidos e dos Usuários

Os principais Envolvidos neste projeto serão por parte da equipe de desenvolvimento, gestores e monitores, sendo que esses não necessariamente irão ser usuários do aplicativo.

Já os usuários que irão interagir são alunos da Fga, sejam eles de graduação ou pós-graduação.

Os principais artefatos que o Bot Lino propõe é a maior agilidade e facilidade na transmissão de informação de assuntos e perguntas frequentes em relação a faculdade.

## 3.2 Resumo dos Envolvidos

|Nome|Descrição|Responsabilidades|
|:----:|:----:|:----:|
|Equipe de desenvolvimento de *Software*|Estudantes da Disciplina Métodos de Desenvolvimento de *Software*|Desenvolvimento e Testes do *Software* descrito no documento|
|Equipe de Engenharia de Produto de *Software*|Estudantes da Disciplina Engenharia de Produto de *Software*|Gestão da Equipe de Desenvolvimento, bem como manutenção de ambientes e entrega contínua|
|Orientador|Professora na Universidade de Brasília, no campus Faculdade Gama (FGA - UnB), atual professora das disciplinas Métodos de Desenvolvimento de *Software* e Engenharia de Produto de *Software*.|Orientar as equipe de desenvolvimento e gestão em eventuais dúvidas.|

## 3.3 Resumo dos Usuários

|Nome|Descrição|Responsabilidades|
|:---:|:---:|:---:|
|Alunos|Aqueles que frequentam a Fga e porventura tenham dúvidas acerca de assuntos da Universidade|Interagir com o Bot por meio do Telegram, retirar dúvidas e receber notificações|

## 3.4 Principais Necessidades dos Usuários e dos Envolvidos

Os usuários realizarão a interação com o Bot por meio do Telegram e Messenger do Facebook, serviços de mensagens instantâneas, a qualquer momento que tenham questões sobre procedimentos da Faculdade, e receberão notificações sobre o calendário do semestre.

## 3.5 Perfis dos Envolvidos

### 3.5.1 Equipe de Desenvolvimento de *Software*
|Perfil|--|
|:-:|:-|
|Representantes|Gabriel Braga Mendes, Gabriel Filipe Manso Araujo, Guilherme Marques Rosa, Matheus Salles Blanco, Pedro Rodrigues Pereira.|
|Descrição|Desenvolvimento do *Software*.|
|Tipo|Estudantes da Universidade de Brasília, da disciplina de Métodos de Desenvolvimento de *Software*.|
|Responsabilidades|Desenvolver, testar e implantar o *software*.|
|Critérios de Sucesso|Finalizar o desenvolvimento e realizar a entrega do bot no tempo estipulado.|
|Envolvimento|Alto.|
|Problemas/Comentários|Desenvolver o software no tempo estabelecido pela equipe de EPS. Inexperiência da equipe com a linguagem de programação utilizada para desenvolver o software.|

### 3.5.2 Equipe de Engenharia de Produto de *Software*

|Perfil|--|
|:-:|:-|
|Representantes|Bruna Pinos de Oliveira, Guilherme Augusto Nunes Silva, Guilherme Guimarães Lacerda, Ícaro Pereira de Oliveira, Letícia de Souza Santos.|
|Descrição|Gerenciamento do Projeto.|
|Tipo|Estudantes da Universidade de Brasília, da disciplina de Engenharia de Produto de *Software*.|
|Responsabilidades|Monitorar, motivar, orientar e preparar a equipe de desenvolvimento. Definir prazos para as atividades propostas.|
|Critérios de Sucesso|Manter os prazos estabelecidos sem atraso, e gerenciar a qualidade do *software* em desenvolvimento, finalizando o projeto no tempo estipulado.|
|Envolvimento|Alto.|
|Problemas/Comentários|Organizar prazos e metas de acordo com o tempo disponível.|

### 3.5.3 Orientador

|Perfil|--|
|:-:|:-|
|Representantes|Professora Carla Silva Rocha Aguiar|
|Descrição|Professora na Universidade de Brasília, no campus Faculdade Gama (FGA - UnB), atual professora das disciplinas Métodos de Desenvolvimento de *Software* e Engenharia de Produto de *Software*.|
|Tipo|Orientadora e avaliadora que dará suporte a respeito do desenvolvimento do Bot.|
|Responsabilidades|Avaliar a equipe de desenvolvimento e gestão e orientá-los em eventuais dúvidas.|
|Critérios de Sucesso|Observar o sucesso da equipe de desenvolvimento.|
|Envolvimento|Médio.|
|Problemas/Comentários|--|

## 3.6 Perfis dos Usuários

### 3.6.1 Alunos

|Perfil|--|
|:-:|:-|
|Representantes|Alunos da Universidade de Brasilia, no campus Faculdade do Gama (FGA - UnB).|
|Descrição|Alunos que tenham dúvidas acerca da Faculdade.|
|Tipo|Estudantes da Universidade que tenham dúvidas e necessitem de notificações sobre o calendário do semestre.|
|Responsabilidades|Interagir com o Bot por meio do Telegram ou Messenger, retirar dúvidas e receber notificações.|
|Critérios de Sucesso|Realizar interações flúidas com o Bot.|
|Envolvimento|Alto.|
|Problemas/Comentários|Não possuir cadastro no Telegram.|

## 3.7 Principais Necessidades dos Usuários ou dos Envolvidos

|Necessidade|Prioridade|Preocupação|Solução Proposta|Solução Atual|
|:---|:---|:---|:---|:---|
|Retirar dúvidas frequentes de alunos da Universidade.|Alta.|Falta de interação com o Bot.|Um ChatBot de Telegram e Messenger que responda as dúvidas trazidas por alunos.|Perguntar diretamente na Secretaria da Faculdade.|
|Receber notificações sobre o calendário de atividades da Faculdade.|Alta.|Notificações ignoradas.|Mensagens enviadas pelo ChatBot, avisando de eventos e datas importantes durante o semestre.|Pesquisas e avisos em grupos de Facebook.|

# 4.Descrição da Solução

## 4.1 Perpectiva do Produto

<p align="justify"> &emsp;&emsp;O ChatBot Lino tem como objetivo automatizar operações de secretariado, permitindo a redistribuição de informações universitárias como datas e prazos de incrição. Ainda é capaz de ensinar o usuário um caminho pra facilitar uma emissão de um documento Universitário e avisar periodicamente eventos de forma prévia.</p>

## 4.2 Resumo dos recursos

| Benefício para o Cliente | Recursos de suporte |
|:---:|:---:|
|Fornece avisos sobre datas de eventos e prazos de inscrição|O ChatBot Lino utiliza informações públicas da universidade para gerar os avisos para o usuário, ainda estes combinando de acordo com o assunto que o usuário deseja receber|
|Capacidade de interação entre usuário e o Lino|A partir de um fluxo de diálogo, Lino é capaz de sguir uma conversa não linear e interagir de forma descontraída e informativa|
|Facilidade em emissão de documentos universitários|Lino quando questionado sobre documentos prontamente demonstra de forma prática como emitir e obter os documentos a partir das plataformas online da universidade|

# 5. Recursos do Produto

O ChatBot Lino é capaz de realizar:

* Avisos prévios de eventos;
* Avisos prévios de prazos de inscrição;
* Resposta a dúvidas comuns entre os alunos;
* Fluxo de conversa com o usuário;
* Tutoriais para emissão de documentos universitários;

# 6. Requisitos Funcionais

# 7. Restrições

*	Uso da Internet.
* Projeto deve ser finalizado até 29/11/2018.
* Conhecimento básico da Português.
* Conhecimento básico de Inglês.

# 8. Intervalos de qualidade

## 8.1 Requisitos de Implementação

Para maior eficiência, o ChatBot será desenvolvido para ser utilizado em conjunto das plataformas <i>Messenger</i> e <i>Telegram</i>, dois programas largamente utilizados pela comunidade para a comunicação, onde a implementação de funcionalidades se mostra viável.

## 8.2 Requisitos de Sistema

<p align="justify"> &emsp;&emsp;Esta aplicação deverá ser acessada através de dispositivos que possuem as aplicações <i>Messenger</i> e <i>Telegram</i> em que o sistema operacional é variável de acordo com o dispositivo de utilização, podendo ser: <i>Android</i>, <i>iOS</i>, <i>Windows</i>, <i>Linux</i>, <i>ChromeOS</i>...</p>

## 8.3 Requisitos de Design

<p align="justify"> &emsp;&emsp;A composição deste <i>software</i> será feita de maneira a tornar sua utilização autoexplicativa e fácil, para acesso em tempo real, ou seja, atendendo todas as especificações de boas práticas referentes à experiência de usuário.</p>
