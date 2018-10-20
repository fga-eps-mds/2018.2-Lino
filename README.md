
<p align="center">
  <img src="https://user-images.githubusercontent.com/18364727/46375175-19b5a300-c669-11e8-898e-00b4f5a1fed4.png">
</p>

<h1 align="center"> Lino - O bot da Universidade</h1>
<p align="center">
  <img width="15" src="https://user-images.githubusercontent.com/18364727/46375818-d2c8ad00-c66a-11e8-95a3-a4f80e984a35.png">
  <a href="https://www.facebook.com/Lino-303317230254781/?modal=admin_todo_tour" margin=50>Facebook</a>
  <img width="15" src="https://user-images.githubusercontent.com/18364727/46376121-9a759e80-c66b-11e8-8aa0-6c4cf887089e.png">
  <a href="https://web.telegram.org/#/im?p=@lino_o_bot">@lino_o_bot</a>
</p>
  <p align="center">
    <a href="https://botlino.github.io/docs/"><strong>Visite nossa página &raquo;</strong></a>
    <br>
    <br>
    <a href="https://github.com/BotLino/Lino-WebCrawler">Web Crawler</a>
    &middot;
    <a href="https://github.com/BotLino/Lino-Alerta">Alerta</a>
    &middot;
    <a href="https://github.com/BotLino/Lino-API-Mensageiros">API de Mensageiros</a>
  </p>
</p>

### Sobre o projeto

<p align="justify"> &emsp;&emsp;
  O projeto Lino é um bot que visa orientar, alertar e tirar dúvidas a respeito dos assuntos mais procurados na Universidade de Brasília - Campus FGA. Para apoio ao Bot, um painel de controle de métricas que acompanha sua eficiência durante seu uso em produção.</p>

<p align="justify"> &emsp;&emsp;
  Como principais funcionalidade, tem-se:
</p>


### Utilização

&emsp;&emsp; O Lino se encontra nas plataformas <a href="https://www.facebook.com/Lino-303317230254781/?modal=admin_todo_tour" margin=50>Facebook Mensseger</a> e <a href="https://web.telegram.org/#/im?p=@lino_o_bot">Telegram</a>

### Principais funcionalidades

* Alerta do cardápio (semanal, diário e por refeição);
* Alerta de emails enviados pelos dos funcionário do campus;
* Explicações das documentações mais procuradas.

### Guia de Contribuição

#### Políticas

As políticas de _branches_, _commits_, _pull requests_ e _issues_ se encontram [aqui](https://github.com/fga-eps-mds/2018.2-Lino/tree/master/docs/policies)

#### Desenvolvimento

Para começar a desenvolver precisamos fazer algumas mudanças no código para que funcione localmente.

Todas as mudanças estão descritas no código onde deve ser alterado, só que você não vai precisar sair procurando, eu vou lhe dizer onde que é.

1. Altere o banco que deseja utilizar no arquivo notifier.py e no notifications.py
```
# If you have your own database, changes to ('database', <PORT>)
client = MongoClient('mongodb://mongo-ru:27017/lino_ru')
```

2. Caso esteja trabalhando com o Telegram, adicione o token nos arquivos notifier e no notifications.py
```
# If you want to use your own bot to development add the bot token as
# second parameters
telegram_token = os.getenv('ACCESS_TOKEN', '')
```

3. Caso esteja rodando o webcrawler local, altere a URL no arquivo notifier e no menu.py
```
# Change the url if you have your own webcrawler server
response = requests.get('http://<imagem_crawler>:<porta_crawler>/cardapio/{}'.format(day)).json()
```

4. Caso queira usar com os mensageiros o Lino, utilize o ngrok para expor para o mundo
```
./ngrok http <porta_bot>
```

5. Adicione as credenciais do bot no train-messenger ou no train-telegram (Exemplo abaixo sobre o Telegram)
```
# If you want to use your own bot to development
# add the bot credentials as second parameters
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN', '')
VERIFY = os.getenv('VERIFY', '')
# the webhook URL is one that ngrok generates (https)
WEBHOOK_URL = os.getenv('WEBHOOK_URL', '')
```

5. Agora está tudo certinho pra você começar a desenvolver e testar o bot :)


#### Testando o Lino no Terminal

Para testar as alterações feitas no Lino, execute os seguintes comandos no terminal:

1. Crie a imagem do Lino:
```
sudo docker build -t lino .
```

2. Inicialize o _container_:
```
sudo docker run --rm -it -p 5002:5002 -v $PWD:/2018.2-Lino lino
```

3. Agora basta testar as novas alterações pelo terminal.

#### Testando o Lino nos Mensageiros

1. Crie a imagem do Lino:
```
sudo docker build -t <imagem_nome> -f docker/<Mensageiro>.Dockerfile .
```

2. Inicialize o _container_:
```
sudo docker run --rm -it -v $PWD:/2018.2-Lino <imagem_nome>
```

3. Agora basta testar as novas alterações pelo terminal.

#### Container pra Desenvolvimento

1. Caso queira inicilizar um ambiente de desenvolvimento com todos os serviços
```
# Altere a imagem que deseja (qual mensageiro ou terminal) dentro do docker-compose
sudo docker-compose up --build
```

### Licença

<p align="justify">&emsp;&emsp; Lino é distribuído sob a licença <a href="https://opensource.org/licenses/MIT">MIT</a>. Consulte <a href="https://github.com/fga-eps-mds/2018.2-Lino/blob/master/LICENSE.md">LICENSE</a> para obter detalhes.</p>
