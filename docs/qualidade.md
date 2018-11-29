# Considerações sobre a aplicação de Testes de Software

| Data       | Versão | Descrição       | Autor          |
| :--------: | :----: | :-------------: | :------------: |
| 27/11/2018 | 1.0    | Primeira versão | Icaro Oliveira |

## Objetivo

O objetivo desse documento é explicitar como, quais e porquês das adoções de cada tipo de teste durante o desenvolvimento do produto.
Como muitas das decisões acertadas foram documentadas em _issues_ e podem não ficar claras para algum contribuidor, fez-se a necessidade de reunir e encadear o estágio atual de maturidade no quesito de QA.

## Riscos no contexto de _chatbots_

No contexto em que o produto está inserido, da arquitetura e das tecnologias adotadas, foram encontradas dificuldades e riscos: ainda não existe uma técnica sólida para a aplicação de testes tradicionais em chatbots. 

Com esta dificuldade e riscos em mente, buscou-se mitigar os riscos da qualidade do software com três tipos de testes, aproveitando a arquitetura de microsserviços utilizada e o [_Gitflow_](https://github.com/fga-eps-mds/2018.2-Lino/blob/docs/gitflow.md) idealizado. São eles: testes estáticos, testes unitários, testes de contrato e testes de usabilidade.

## Estratégia de aplicação de testes

Durante o desenvolvimento da aplicação, encontramos diversos tipos de microsserviços, cada um com uma particularidade diferente. 

Assim, aproveitamos a oportunidade da independência que cada microsserviço dá para utilizar a melhor linguagem de programação para cada problema. Por exemplo, para os _crawlers_ foi utilizado Python. Para o serviço de envio de _emails_, foi utilizado NodeJS devido a fácil integração com a API do Gmail.

Dado isso, pôde-se obter controle sobre cada objetivo do microsserviço e da categoria de testes para eles. É importante ressaltar que todos os serviços passaram pelo estágio de **testes estáticos**.

### Core (Lino)

Sendo o serviço mais importante, é necessário que haja uma atenção especial às anomalias encontradas. Ao mesmo tempo, como mencionado na seção anterior, não foram utilizados testes de maneira "tradicional" no código, com exceção dos testes estáticos.

Para mitigar erros, houve uma atenção especial para os serviços que ele consome. Foram realizados **testes de usabilidade** como forma de identificar falhas de fluxo, erros fatais e principalmente dificuldades na execução dos fluxos.


### API Alertas

No contexto desse microsserviço, ela é um _middleware_ entre a API do Gmail e o Lino. Portanto, há uma dependência com um serviço externo e por isso é necessário garantir que esses serviços estão integrados.

Logo, testes foram aplicados para garantir esa **integração**. Além disso, foram utilizados testes de **unidade** para especificar que todas as funções retornavam objetos existentes e o objeto era enviado através das requisições para o Core.

### API WebCrawlers Matricula e RU

No contexto destes microsserviços, precisa-se garantir que a estrutura do JSON enviado é exatamente a mesma esperada pelo Core. Nesse caso, o uso de **testes de contrato** foi necessária.

Além destes, também houveram testes de unidade, da mesma forma e com o mesmo objetivo que o serviço de Alertas.

## Tecnologias

Nos serviços de Matricula e RU foi utilizado o Pytest, tanto para os testes quanto para os reports. No serviço de Alertas, foi utlizado o Mocha para testes e o Instambul para reports.

Nos testes de usabilidade, foi utilizado um formulário no Google Forms.

## Resultados

Os resultados podem ser vistos em reports para cada tipo de teste, em cada serviço:

### Core

Os **resultados dos testes de usabilidade** tiveram bastante impacto em refatorações, principalmente de intents, pois o objetivo era manter a quantidade de informações enviadas suficiente.

![](https://i.imgur.com/wdXkdJf.png)

Acima, resultado no fluxo de notificação. Impacto das respostas motivou refatoração e utilização de botões para agilizar o fluxo. 


![Imgur](https://i.imgur.com/OPU1Fod.png)

Acima, os resultados para o fluxo de cardápio para uma refeição específica no fluxo do RU. Os valores indicam: 3 - Satisfatório; 1 - Muito pouco; 5 - Exagerado)


![Imgur](https://i.imgur.com/ixnPKQ7.png)

Acima, os feedbacks dos avaliadores e dos usuários para o fluxo de cardápio do RU. Estes motivaram a refatoração do fluxo para o RU.

### Serviços
A **cobertura de código** para testes nos **serviços** foi de:

#### API Matricula
![](https://i.imgur.com/mvYG6lT.png)

### API Alertas
![](https://i.imgur.com/kvqTZOr.png)
