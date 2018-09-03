| Data       | Versão | Descrição            | Autor             |
|:----------:|:------:|:--------------------:|:-----------------:|
| 02/09/2018 | 1.0 | Criação do documento com template inicial  |Bruna Pinos, Guilherme Lacerda e Ícaro Oliveira|

# Backlog do Produto

## Épicos

|ID| DESCRIÇÃO|
|:--:|:--:|
|EP01|Alertas|
|EP02|Gerenciamento de conversas|
|EP03|Monitoramento em uso|

## Features

|ID|DESCRIÇÃO|ÉPICO|
|:--:|:---:|:---:|
|FT01|Notificação do cardápio do RU| EP01|
|FT02|Envio de mensagens à comunidade acadêmica| EP01|
|FT03|Informações sobre o trancamento| EP02|
|FT04|Informações sobre estágio| EP02|
|FT05|Informações sobre a matrícula| EP02|
|FT06|Informações sobre documentos acadêmicos| EP02|
|FT07|Informações sobre monitoria e tutoria| EP02|
|FT08|Informações sobre desligamento|EP02|
|FT09|Coleta de métricas|EP03|
|FT10|Criação de relatórios|EP03|
|FT11|Adptar o Lino para mais de um mensageiro| EP01 & EP02|

## Histórias de Usuários

|ID|Tipo|Eu, como|desejo|para|Priorização|_Feature_|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|US01|Funcional|Usuário|ser notificado sobre o cardápio diário do RU|me informar|_Must Have_|FT01|
|US02|Funcional|Usuário|saber sobre o cardápio geral da semana|me informar|_Must Have_|FT01|
|US03|Funcional|Usuário|saber sobre o cardápio de uma refeição específica de um período|me informar|_Should Have_|FT01|
|US04|Funcional|Usuário|gerenciar as notificações do Lino|priorizar as informações|_Must Have_|FT01 & FT02|
|US05|Não Funcional|Lino|buscar as informações sobre o cardápio do RU na sua página oficial| para transferir a informação ao usuário solicitante|_Must Have_|FT01|
|US06|Não Funcional|Lino|transformar o PDF do cardápio em texto| para informar o usuário| _Must Have_|FT01|
|US07|Não Funcional|Lino|me comunicar com os usuários pelo mensageiro Messenger|enviar mensagens a usuários dessa plataforma|_Must Have_|FT11|
|US08|Não Funcional|Lino|me comunicar com os usuários pelo mensageiro Telegram|enviar mensagens a usuários dessa plataforma|_Must Have_|FT11|
|US09|Funcional|Servidor|enviar uma mensagem via Lino|os usuários|_Must Have_|FT02|
|US10|Não Funcional|Lino|desejo receber um email do Servidor(ator)|notificar os usuários|_Must Have_|FT02|
|US11|Não Funcional|Lino|acessar a API do Gmail|enviar as mensagens recebidas aos usuários|_Must Have_|FT02|
|US12|Não Funcional|Lino|armazenar o conteúdo das conversas em um banco de dados|fornecer métricas|_Could Have_|FT09 & FT10|
|US13|Não Funcional|Lino|coletar dados do banco|criar a métrica de Etapas de conversação|_Could Have_|FT09 & FT10|
|US14|Não Funcional|Lino|coletar dados do banco|criar a métrica de Gatilhos de Confusão|_Could Have_|FT09 & FT10|
|US15|Não Funcional|Lino|coletar dados do banco|criar a métrica de Número total de usuários|_Could Have_|FT09 & FT10|
|US16|Não Funcional|Lino|coletar dados do banco|criar a métrica de Taxa de Satisfação|_Could Have_|FT09 & FT10|
|US17|Funcional|Analista de Dados|visualizar a métrica Etapas de conversação|analisar o desempenho do Lino|_Could Have_|FT10|
|US18|Funcional|Analista de Dados|visualizar a métrica Gatilhos de confusão|analisar o desempenho do Lino|_Could Have_|FT10|
|US19|Funcional|Analista de Dados|visualizar a métrica Número de usuários|analisar o impacto do Lino na comunidade|_Could Have_|FT10|
|US20|Funcional|Analista de Dados|visualizar a métrica Taxa de satisfação|analisar o impacto do Lino na comunidade|_Could Have_|FT10|

## Intents
