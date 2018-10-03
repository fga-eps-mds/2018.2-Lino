
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

#### Testando o Lino

Para testar as alterações feitas no Lino, execute os seguintes comandos no terminal:

1. Crie a imagem do Lino dentro da raiz do repositório:
```
sudo docker build -t lino .
```

2. Inicialize o _container_:
```
sudo docker run --rm -it -v $PWD:/2018.2-Lino lino
```

3. Agora basta testar as novas alterações pelo terminal.

#### Container pra Desenvolvimento

Caso queira inicilizar o container pra desenvolvimento sem testar no terminal

```
sudo docker-compose up
```

### Licença

<p align="justify">&emsp;&emsp; Lino é distribuído sob a licença <a href="https://opensource.org/licenses/MIT">MIT</a>. Consulte <a href="https://github.com/fga-eps-mds/2018.2-Lino/blob/master/LICENSE.md">LICENSE</a> para obter detalhes.</p>

