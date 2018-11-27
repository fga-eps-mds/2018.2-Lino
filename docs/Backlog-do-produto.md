| Data       | Versão | Descrição            | Autor             |
|:----------:|:------:|:--------------------:|:-----------------:|
| 02/09/2018 | 1.0 | Criação do documento com template inicial  |Bruna Pinos, Guilherme Lacerda e Ícaro Oliveira|
| 15/09/2018 | 1.1 | Criação do documento com template inicial  |Bruna Pinos, Guilherme Lacerda e Ícaro Oliveira|
| 10/11/2018 | 1.2 | Refatoração do backlog de acordo com nova mudança de escopo | Letícia de Souza |

# Backlog do Produto

## Épicos

|ID| DESCRIÇÃO|
|:--:|:--:|
|EP01|Alertas|
|EP02|Gerenciamento de conversas|

## Features

|ID|DESCRIÇÃO|ÉPICO|
|:--:|:---:|:---:|
|FT01|Envio do cardápio diário do RU| EP01|
|FT02|Envio do cardápio semanal do RU| EP01|
|FT03|Envio do cardápio específico do café da manhã do RU| EP01|
|FT04|Envio do cardápio específico do almoço do RU| EP01|
|FT05|Envio do cardápio específico do jantar do RU| EP01|
|FT06|Informações sobre o trancamento| EP02|
|FT07|Informações sobre a matrícula| EP02|
|FT08|Informações sobre documentos acadêmicos| EP02|
|FT09|Adaptar o Lino para mais de um mensageiro| EP01 & EP02|
|FT10|Registro das notificações| EP01, EP02|
|FT11|Enviar mensagens da comunidade acadêmica| EP01|
|FT12|Envio de mensagens à comunidade acadêmica| EP01|

## Histórias de Usuários

|ID|Tipo|Eu, como|desejo|para|Priorização|_Feature_| Pontuação |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|US01|Funcional|Usuário|ser notificado sobre o cardápio diário do RU|me informar|_Must Have_|FT01, FT09|
|US02|Funcional|Usuário|saber sobre o cardápio geral da semana|me informar|_Must Have_|FT02, FT09|
|US03|Funcional|Usuário|saber sobre o cardápio de uma refeição específica de um período do dia |me informar|_Should Have_|FT04| 8 |
|US04|Funcional|Usuário|gerenciar as notificações do Lino|priorizar as informações|_Must Have_|FT10|
|US05|Não Funcional|Lino|buscar as informações sobre o cardápio do RU na sua página oficial| para transferir a informação ao usuário solicitante|_Must Have_|FT01, FT02, FT03, FT04|
|US06|Não Funcional|Lino|transformar o PDF do cardápio em texto| para informar o usuário| _Must Have_|FT01, FT02, FT03, FT04|
|US07|Não Funcional|Lino|me comunicar com os usuários pelo mensageiro Messenger|enviar mensagens a usuários dessa plataforma|_Must Have_|FT09|
|US08|Não Funcional|Lino|me comunicar com os usuários pelo mensageiro Telegram|enviar mensagens a usuários dessa plataforma|_Must Have_|FT09|
|US09|Funcional|Servidor | enviar uma mensagem via gmail | informar os usuários via lino|_Must Have_|FT04|
|US10|Não Funcional|Lino|desejo receber um email do Servidor(ator)|notificar os usuários|_Must Have_|FT04|
|US11|Não Funcional|Lino|acessar a API do Gmail|enviar as mensagens recebidas aos usuários|_Must Have_|FT04|
|US21|Não Funcional|Lino|ter uma identidade visual |me mostrar ao mundo|_Should Have_|FT01|
|US22|Funcional|Lino|ter um fluxo de conversa sobre o cardápio do RU|alertar os usuários sobre as informações do cardápio diário ou semanal|_Should Have_|FT01|
|US23|Não Funcional|Lino|buscar as informações sobre calendário da UnB no semestre| para transferir a informação ao usuário solicitante|_Must Have_|FT05, FT06, FT08|
|US24|Não Funcional|Lino|transformar o PDF do cardápio em texto| para informar o usuário| _Must Have_|FT01, FT02, FT03, FT04, FT05|
|US25|Funcional|Lino| enviar mensagens sobre o cardápio do café da manhã do dia| para informar o usuário |_Must Have_|FT03|
|US26|Funcional|Lino| enviar mensagens sobre o cardápio do almoço do dia| para informar o usuário |_Must Have_|FT04|
|US27|Funcional|Lino| enviar mensagens sobre o cardápio do jantar do dia| para informar o usuário |_Must Have_|FT05|

## Tasks Histórias de Usuário
|US|ID|Descrição|_Feature_| Pontuação |
|:--:|:--:|:------------:|:-----------:|:--:|
|US01|T01| Realizar o agendamento do envio do cardápio diário aos usuários do *Telegram* e do *Messenger*, informando-os, em um horário determinado| FT01, FT09| - |
|US01|T02|Registrar usuário, do *Telegram* e do *Messenger* que queria receber a notificação do cardápio diário, no banco de dados| FT01, FT09| - |
|US01|T03|Enviar através de mensagens para o usuário cadastrado no *Messenger* | FT01| - |
|US01|T04|Enviar através de mensagens para o usuário cadastrado no *Telegram* | FT01| - |
|US02|T01| Realizar o agendamento do envio do cardápio semanal aos usuários do *Telegram* e do *Messenger*, informando-os, em um horário determinado| FT01, FT09| 5 |
|US02|T02|Registrar usuário, do *Telegram* e do *Messenger* que queria receber a notificação do cardápio semanal, no banco de dados| FT02, FT09| 8 |
|US02|T03|Enviar através de mensagens do cardápio semanal para o usuário cadastrado no *Messenger* | FT02| 5 |
|US02|T04|Enviar através de mensagens do cardápio semanal  para o usuário cadastrado no *Telegram* | FT02| 5 |
|US04|T01| Determinar ação para que o usuário possa retirar ou adicionar permissão de notificação(diário e semanal) no *Messenger*| FT01, FT02, FT10| 5 |
|US04|T02|Determinar ação para que o usuário possa retirar ou adicionar permissão de notificação(diário e semanal) no *Telegramr*| FT01, FT02, FT10| 5 |
|US04|T03|Alterar permissões do usuário do *Messenger*, no banco de dados, de acordo com o recebido pelo Lino | FT10| 13 |
|US04|T04|Alterar permissões do usuário do *Telegram*, no banco de dados, de acordo com o recebido pelo Lino | FT10| 13 |
|US05|T01|Criar JSONs para cardápio semanal, diário e por cada refeição| FT01, FT02, FT03, FT04, FT05| - |
|US05|T02|Fazer comunicação WebCrawler com Lino para recebimento de JSONs| FT10| - |
|US25|T01|Enviar mensagens sobre o cardápio do café da manhã diário para o usuário no Telegram|FT03|3|
|US25|T02|Enviar mensagens sobre o cardápio do café da manhã diário para o usuário no Messenger|FT03|3|
|US25|T03|Criar agendamento do envio do cardápio do café da manhã diário aos usuários do Telegram e do Messenger, informando-os em um horário determinado|FT03|2|
|US26|T01|Enviar mensagens sobre o cardápio do almoço diário para o usuário no Telegram|FT04|3|
|US26|T02|Enviar mensagens sobre o cardápio do almoço diário para o usuário no Messenger|FT04|3|
|US26|T03|Criar agendamento do envio do cardápio do almoço diário aos usuários do Telegram e do Messenger, informando-os em um horário determinado|FT04|2|
|US27|T01|Enviar mensagens sobre o cardápio do jantar diário para o usuário no Telegram|FT05|3|
|US27|T02|Enviar mensagens sobre o cardápio do jantar diário para o usuário no Messenger|FT05|3|
|US27|T03|Criar agendamento do envio do cardápio do jantar diário aos usuários do Telegram e do Messenger, informando-os em um horário determinado|FT05|2|

## Intents

| ID | Feature | Intent | Utterances | Entities | Actions |
|:--:|:------:|:------:|:----------:|:--------:|:-------:|
| I01 | - | Iniciar sessão do bot | Olá, meu nome é Lino e estou aqui para ajudar | - | - |
| I02 | FT01 | Obter cardápio do RU no dia | O cardápio do dia é | Cardápio, dia | Buscar cardápio diário e enviar ao solicitante |
| I03 | FT01 | Obter cardápio semanal do RU | O cardápio da semana é | Cardápio, semana | Buscar cardápio da semana e enviar ao solicitante |
| I04 | FT07 | Solicitar declaração de Aluno Regular | Siga as instruções para fazer o _download_ da declaração  | documento, aluno_regular| - |
| I05 | FT07 | Solicitar comprovante de Matrícula | Siga as instruções para fazer o _download_ do comprovante | documento, comprovante_matricula | - |
| I06 | FT07 | Socilitar declaração de Grade Horária | Siga as instruções para fazer o _download_ do documento |  documento, grade_horaria | - |
| I07 | FT06| Tirar dúvida sobre o período de matrícula | O período de matrícula é| periodo, matricula |Buscar período de matrícula e enviar ao solicitante |
| I08 | FT05 | Tirar dúvida sobre o período de trancamento de matéria | O período de trancamento de matéria é ... Porém, se for um caso especial, comunique-se com a secretaria | periodo, trancamento de matéria | Buscar período de trancamento de materia e enviar ao solicitante |
| I09 | FT05 | Tirar dúvida sobre o período de trancamento geral | O período de trancamento geral de matrícula é ... | periodo, trancamento geral | Buscar período de trancamento geral e enviar ao solicitante |
| I10 | FT03 | Obter o cardápio específico do café da manhã | E no café da manhã de hoje teremos: | café da manhã, café da manhã de hoje, café | Buscar o cardápio do café da manhã e enviar ao solicitante |
| I11 | FT04 | Obter o cardápio específico do almoço | Eai! Então... Pro almoço, nós teremos: | cardápio do almoço, almoço, almoco | Buscar o cardápio do almoço e enviar ao solicitante |
| I12 | FT05 | Obter o cardápio específico do jantar | Para o jantar: | cardápio do jantar, jantar, janta | Buscar o cardápio do jantar e enviar ao solicitante |

## Tasks Intents
|US|ID|Descrição|_Feature_| Pontuação |
|:--:|:--:|:------------:|:-----------:|:--:|
|I04|T01|Criar fluxo de tutorial para orientar os usuários a obter a declaração de aluno regular|FT07|-|
|I05|T01|Criar fluxo de tutorial para orientar os usuários a obter o comprovante de matricula|FT07|-|
|I06|T01|Criar fluxo de tutorial para orientar os usuários a obter a declaração de grade horária|FT07|-|
|I07|T01|Fazer o webcrawler pegar o PDF certo | FT07|-|
|I07|T02|Fazer o webcrawler elaborar o parser | FT07|-|
|I07|T03|Criar fluxo do período de matrícula no Rasa e elaborar modelo de JSON a ser recebido | FT07|-|
|I07|T04|Conectar fluxo ao webcrawler| FT07|-|
|I09|T01|Criar fluxo de conversa para a obtenção do cardápio do café da manhã|FT03|3|
|I10|T01|Criar fluxo de conversa para a obtenção do cardápio do almoço|FT04|3|
|I11|T01|Criar fluxo de conversa para a obtenção do cardápio do jantar|FT05|3|
