## Para rodar o bot

* Instale o rasa e suas dependencias, em caso de dúvidas, siga o <a href="http://rasa.com/docs/core/installation/">link</a>

* Utilize o ngrok para expor a porta 5002 pelo seguinte comando no terminal:
```
$ ./ngrok http 5002
```
Para instalar o ngrok siga as instruções do <a href="https://ngrok.com/download">link</a>.

* Vá ao arquivo credentials.yml e preencha com as informações corretas do seu bot do telegram. Para criar seu bot abra o telegram e converse com o @BotFather.

* Após essas configurações feitas rode os seguintes comandos:
```
$ make train-nlu
$ make train-core
$ make run-telegram
```