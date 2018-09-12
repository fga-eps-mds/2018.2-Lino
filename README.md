# Lino

# Testando o Lino (Desenvolvimento)

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

# Container pra Desenvolvimento

Caso queira inicilizar o container pra desenvolvimento sem testar no terminal

```
sudo docker-compose up
```
