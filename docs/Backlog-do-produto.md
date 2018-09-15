| Data       | Versão | Descrição            | Autor             |
|:----------:|:------:|:--------------------:|:-----------------:|
| 02/09/2018 | 1.0 | Criação do documento com template inicial  |Bruna Pinos, Guilherme Lacerda e Ícaro Oliveira|
| 15/09/2018 | 1.1 | Criação do documento com template inicial  |Bruna Pinos, Guilherme Lacerda e Ícaro Oliveira|

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
|FT09|Coleta de métricas|EP03|
|FT10|Criação de relatórios|EP03|
|FT11|Adaptar o Lino para mais de um mensageiro| EP01 & EP02|

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
|US21|Não Funcional|Lino|ter uma identidade visual |me mostrar ao mundo|_Should Have_|FT01|
|US22|Funcional|Lino|ter um fluxo de conversa sobre o cardápio do RU|alertar os usuários sobre as informações do cardápio diário ou semanal|_Should Have_|FT01|
|US23|Não Funcional|Lino|buscar as informações sobre calendário da UnB no semestre| para transferir a informação ao usuário solicitante|_Must Have_|FT03, FT04, FT05, FT06 & FT07|
|US24|Não Funcional|Lino|transformar o PDF do cardápio em texto| para informar o usuário| _Must Have_|FT03, FT04, FT05, FT06 & FT07|

## Intents

| ID | Feature | Intent | Utterances | Entities | Actions |
|:--:|:------:|:------:|:----------:|:--------:|:-------:|
| I01 | - | Iniciar sessão do bot | Olá, meu nome é Lino e estou aqui para ajudar | - | - |
| I02 | FT01 | Obter cardápio do RU no dia | O cardápio do dia é | Cardápio, dia | Buscar cardápio diário e enviar ao solicitante |
| I03 | FT01 | Obter cardápio semanal do RU | O cardápio da semana é | Cardápio, semana | Buscar cardápio da semana e enviar ao solicitante |
| I04 | FT06 | Solicitar declaração de Aluno Regular | Siga as instruções para fazer o _download_ da declaração  | documento, aluno_regular| - |
| I05 | FT06 | Solicitar comprovante de Matrícula | Siga as instruções para fazer o _download_ do comprovante | documento, comprovante_matricula | - |
| I06 | FT06 | Socilitar declaração de Grade Horária | Siga as instruções para fazer o _download_ do documento |  documento, grade_horaria | - |
| I07 | FT05| Tirar dúvida sobre o período de matrícula | O período de matrícula é| periodo, matricula |Buscar período de matrícula e enviar ao solicitante |
| I08 | FT03 | Tirar dúvida sobre o período de trancamento de matéria | O período de trancamento de matéria é ... Porém, se for um caso especial, comunique-se com a secretaria | periodo, trancamento de matéria | Buscar período de trancamento de materia e enviar ao solicitante |
| I09 | FT03 | Tirar dúvida sobre o período de trancamento geral | O período de trancamento geral de matrícula é ... | periodo, trancamento geral | Buscar período de trancamento geral e enviar ao solicitante |
| I10 | FT04 | Saber informações do funcionamento de estágio | No caso de estágios não obrigatórios, você deve fazer... Se for obrigatório, siga... | - | - | 
| I11 | FT07 | Tirar duvida sobre o período de monitoria | O período de inscrição para monitoria é... | periodo, monitoria |Buscar período de monitoria e enviar ao solicitante |

