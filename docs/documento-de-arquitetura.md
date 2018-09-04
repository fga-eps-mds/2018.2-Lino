
# Histórico de Revisão

| Data | Versão | Modificação | Autor |

|:---:|:--:|:---:|:---:|

| 30/08/2018 | 1.0 | criação do documento e adição do tópico 1 | Pedro R. |

| 31/08/2018 | 1.1 | Adição do Tópico 5 | Matheus Blanco |

| 03/09/2018 | 1.2 | Adição do tópico 4.1 | Matheus Blanco |


# 1. Introdução  

<p  align="justify">  &emsp;&emsp;Este documento visa apresentar a arquitetura de software aplicada no desenvolvimento do Assistente Virtual Lino, garantindo uma facilidade de visualização dos requisitos e da estrutura para com os desenvolvedores.</p>

## 1.1 Finalidade  

<p  align="justify">  &emsp;&emsp;Este documento trata de uma visão ampla da arquitetura do Asistente Virtual e esboça os aspectos do mesmo. Ele visa transparecer as decisões arquiteturais que foram tomadas em relação ao software.</p>

## 1.2 Escopo

<p  align="justify">  &emsp;&emsp;O Assistente Virtual Lino tem como principal objetivo servir a comunidade do Campus do Gama da UnB(FGA). Toda parte arquitetural do projeto será tratada neste documento e as decisões a serem tomadas acerca do mesmo serão administradas pelos alunos da matéria de Métodos de Desenvolvimento de Software, Alunos da matéria de Engenharia de Produto de Software e a professora da UnB Carla.</p>

## 1.3 Visão Geral

<p  align="justify">  &emsp;&emsp;O documento através de 5 principais tópicos e suas ramificações visa detalhar a arquitetura e os requisitos do software. Facilitando o desenvolvimento e esclarecendo dúvidas.</p>

Estrutura do documento:  

* Introdução;

* Representação da Arquitetura;

* Metas e Restrições de Arquitetura;

* Visão de Casos de Uso;

* Visão lógica;  

## 1.4 Definições, Acrônimos e Abreviações

* API: Application Programming Interface

## 1.5 Referências


> MELO, Thalisson; ALVES, Álax; MARTINS, Lucas; RICHARD, Matheus; BERNARDO, Matheus de Sousa; Joranhezon. <b>Owla:</b> Documento de Arquitetura. Disponível em: <https://github.com/fga-gpp-mds/2016.2-Owla/wiki/Documento-de-Arquitetura>.


> André; Gabriel; Guilherme; ALMEIDA; Weyler. <b>Cidade Democrática:</b> Documento de Arquitetura. Disponível em: <https://github.com/fga-gpp-mds/2016.2-CidadeDemocratica/wiki/Documento-de-Arquitetura>.

  
> Universidade Federal do Paraná, FUNPAR. <b>RUP - Especificação de Casos de Uso:</b> Template base para construção do documento de arquitetura. Disponível em: <http://www.funpar.ufpr.br:8080/rup/webtmpl/templates/a_and_d/rup_sad.htm>.


# 2. Representação da Arquitetura


## 2.1 Diagrama de Relações

![enter image description here](https://lh3.googleusercontent.com/nMYBeLvvaVKwu2c-waT1X-9L6UVI-J-NqWhznjnaZJVtrsP77vP_tuNlgxYyBoGlYrMDokhxp3vF=s2000 "Diagrama de Relações")

  
# 3. Metas e Restrições de Arquitetura

# 5. Visão Lógica

  
## 5.1 Diagrama de Pacotes

<p  align="justify">  &emsp;&emsp;Neste tópico se encontram o diagrama de pacotes bem como suas explicações e utilidades.</p>

  
* O pacote <i>2018.2-Lino</i> é o pacote principal do projeto e conterá todos os outros sub-pacotes e documentos existentes no projeto.

  
* No pacote <i>docs</i>, serão apresentados os documentos necessários para a compreensão do projeto, bem como pacote <i>policies</i>.

  
* No pacote <i>Policies</i> estão contidas as políticas de boas práticas de programação e uso da plataforma <i>GitHub</i>.