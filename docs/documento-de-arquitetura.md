| Data | Versão | Modificação | Autor |
|:---:|:--:|:---:|:---:|
| 30/08/2018 | 1.0 | criação do documento e adição do tópico 1 | Pedro R. |

# 1. Introdução

<p align="justify"> &emsp;&emsp;Este documento visa apresentar a arquitetura de software aplicada no desenvolvimento do Assistente Virtual Lino, garantindo uma facilidade de visualização dos requisitos e da estrutura para com os desenvolvedores.</p>

## 1.1 Finalidade

<p align="justify"> &emsp;&emsp;Este documento trata de uma visão ampla da arquitetura do Asistente Virtual e esboça os aspectos do mesmo. Ele visa transparecer as decisões arquiteturais que foram tomadas em relação ao software.</p>

## 1.2 Escopo

<p align="justify"> &emsp;&emsp;O Assistente Virtual Lino tem como principal objetivo servir a comunidade do Campus do Gama da UnB(FGA). Toda parte arquitetural do projeto será tratada neste documento e as decisões a serem tomadas acerca do mesmo serão administradas pelos alunos da matéria de Métodos de Desenvolvimento de Software, Alunos da matéria de Engenharia de Produto de Software e a professora da UnB Carla.</p>

## 1.3 Visão Geral

<p align="justify"> &emsp;&emsp;O documento através de 5 principais tópicos e suas ramificações visa detalhar a arquitetura e os requisitos do software. Facilitando o desenvolvimento e esclarecendo dúvidas.</p>

Estrutura do documento:

* introdução;
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

# 5 Visão Lógica

## 5.1 Diagrama de Pacotes

[comment]: <> (![diagrama de pacotes](https://cloud.githubusercontent.com/assets/26308278/24575617/81346186-1681-11e7-8e9e-22b94584f9d9.jpg))

<p align="justify"> &emsp;&emsp;Neste tópico se encontram o diagrama de pacotes bem como suas explicações e utilidades.</p>

* O pacote <i>2018.2-Lino</i> é o pacote principal do projeto e conterá todos os outros sub-pacotes e documentos existentes no projeto.

* No pacote <i>docs</i>, serão apresentados os documentos necessários para a compreensão do projeto, bem como pacote <i>policies</i>.

* No pacote <i>Policies</i> estão contidas as políticas de boas práticas de programação e uso da plataforma <i>GitHub</i>.