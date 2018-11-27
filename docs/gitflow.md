| Data | Versão | Descrição | Autor |
|:----:|:------:|:---------:|:-----:|
|27/11/2018|1.0|Primeira versão do documento de gitflow | Guilherme Lacerda |

# Visão Geral

Foi idealizado um _Gitflow_ (fluxo de trabalho) automatizado visando entregas de funcionalidade mais rápidas e de mais qualidade.

Nosso fluxo trabalha com 3 estágios diferentes de verificação para disponibilizar o Lino para o "mundo". Os estágios de **teste**, **build** e **deploy**.

Para que a ideia tornar-se possível utilizamos algumas ferramentas para nos auxiliar, tais como:

* Docker
* DockerHub
* Github
* Gitlab-CI
* Rancher1.6

(IMAGEM DO DEPLOY)

# Fluxo de Trabalho

Quando iniciado o desenvolvimento de uma funcionalidade deve-se primeiro iniciar o docker. E depois do ambiente rodando corretamente, deve-se criar uma _branch_ seguindo a [política de branchs](https://github.com/fga-eps-mds/2018.2-Lino/blob/master/docs/policies/branches.md).

Após a criação da _branch_, os _commits_ devem ser feitos atômicamentes. Cada _commit_, quando dado o _push_ para sua própria _branch_ no repositório do [github](https://github.com/fga-eps-mds/2018.2-Lino) acontece um espelhamento das contribuições para o gitlab, para que consigamos utilizar da ferramenta de continuous integration, gitlabCI. Assim, é testado pelo primeiro estágio do **_deploy_**, descrito na ferramenta do gitlab chamado GitlabCI, **_test_**.

Finalizada a funcionalidade, um _Pull Request_ (PR) é aberto da _branch_ de trabalho para a de homologação, devel. (OBS) Um _pull request_ só pode ser aceito se o estágio de **teste** estiver passado pelo gitlab-CI.

Quando o PR é aceito na devel, ele passa por todos os estágios apresentados anteriormente. Passa pelo estágio de **teste**, o estágio de **build** e por final, se todos os anteriores estiverem funcionando corretamente, passa pelo estágio de **deploy** para o ambiente de homologação.

Todos as alterações e adições de funcionalidades realizadas até a devel são testadas em um ambiente de homologação, após a validação de um usuário real, é aberto o _pull request_ para a MAAASTER.

A _branch_ principal tem como único dever servir para o ambiente de produção. Ou seja, um local onde não há espaço para testes, então todas as alterações feitas devem estar funcionando corretamente. Porém, não podemos confiar 100% em tudo o que aconteceu até aqui, então novamente rodamos os estágios de **_teste_**, **_build_** e **_deploy_** (para o ambiente de produção hospedado no servidor do LAPPIS).

# Tecnologias

## Docker
  O docker teve duas funcionalidades principais, muito positivas para o projeto, padronizar e isolar o ambiente, e utilizar para o **_deploy_** dos serviços.

  No primeiro caso, serviu para padronizar o ambiente de desenvolvimento em qualquer tipo de sistema operacional(SO), tendo em vista que dentro da própria equipe havia uma diversidade de SO's. Assim, conseguiriamos evitar com que acontecesse erros não previstos no ambiente e também no próprio computador pessoal, porque ele utiliza um nível de virtualização maior do que o SO, isolando razoavelmente bem o local de trabalho.

  Em segundo caso, é utilizado para o estágio de **_build_** e de **_deploy_**. Na parte primeira parte, utiliza-se o docker para gerar a imagem e para enviá-la pro _registry_. Dentro do _stage_ de **_deploy_**, utiliza-se da imagem gerada no passo anterior que está armazenada no dockerhub, _registry_.

  Todos os nossos serviços estão sendo buildados via Docker. Assim, mantivemos um padrão ferramental.

## DockerHub
  O DockerHub é uma ferramenta que nos serve como _registry_. Ou seja, é basicamente um repositório de imagens de Docker.

  É uma plataforma considerada a oficial pelo docker, que facilita muito o desenvolvimento e a pesquisa por novas imagens. Então quando as imagens estão disponibilizadas no Dockerhub, fica mais fácil para ser encontrada por outras pessoas. Ademais, é uma ferramenta segura e estável. Estabilidade necessária para o desenvolvimento de projetos longos.

  No estágio de **_build_** são geradas as imagens(docker) e enviadas ao repositório no DockerHub, assim conseguimos armazená-las facilmente para serem utilizadas pelos serviços.

## Github
  É uma ferramenta para controle de versão de arquivos mais utilizado no mundo. Através dela podemos desenvolver projetos na qual diversas pessoas podem contribuir simultaneamente no mesmo, editando e criando novos arquivos e permitindo que os mesmos possam existir sem o risco de suas alterações serem sobrescritas.

  Assim, fizemos o controle do código via Github e adaptamos-o para os padrões de Software Livre.

## Gitlab-CI
  Utilizamos o CI do gitlab para montar e automatizar o nosso _pipeline_ de entrega contínua das dossas funcionalidades.

  É um ponto importantíssimo para o DevOps, pois conseguimos automatizar toda verificação do código e deploy, assim tornamos automático todo o processo.

  Para conseguirmos utilizar o GitlabCI é preciso fazer um _mirror_ do repositório do Github para um repositório no Gitlab. Esse processo é espelhar todo o trabalho que é feito no Hub para o Lab. É uma atividade que acontece automaticamente, através de um _webhook_ que colocamos no GitLab. Toda verificação feita no Lab, nós conseguimos espelhar o resultado no github.

  Após o espelhamento, torna-se possível utilizar o CI do GitLab. Nada mais é do que um _script_ descrito em um arquivo YML. Nesse arquivos são explicitados todos os estágios.

  Não necessariamente devem ser os estágios, com os nomes que definimos. Mas para o nosso contexto e realidade, ficou melhor definido como 3 _stages_: **Test, Build e Deploy**.

  Os estágios definidos no arquivo YML são execudos de modo hierarquico, ou seja, se o Test for definido antes, então ele deve rodar antes do Build e antes do Deploy, isso serve para todos os outros.

### Estágio de Teste
  O estágio de teste acontece em todas as _branchs_ de todos os serviços. Porém, não necessariamente todos os testes tem em todos os serviços, em alguns possui só 1, e em outros a mescla de algum dos três que serão abordados mais tarde.

  É o primeiro _stage_ que roda na verificação da integração contínua. Caso falhe, ele não passa para os próximos passos. Sendo assim, é um facilitador na hora de verificar se está acontecendo algum erro de sintaxe ou de funcionalidade.

  Nas _branchs_ de funcionalidades fazemos somente o estágio de teste. Então, é obrigatório que esteja passando corretamente no CI para que seja aceito o _Pull Request_ para a _branch_ de desenvolvimento, devel.

  Nesse estágio são realizados os testes estáticos, unitários e de contrato.

* **Estáticos:** São os testes que fazem uma verificação da sintaxe do código. Para averiguar se todo código desenvolvido está no padrão da folha de estilo da própria linguagem. No nosso caso segue o padrão do PEP8, que é um padrão para o Python.

* **Unitários:**  É a forma de se testar unidades individuais do código. Unidades podem ser métodos, classes, funcionalidades, módulos, etc. Depende muito do que é a menor parte que seu Software pode ser testado. O objetivo é mostrar que cada unidade atende corretamente sua especificação e segue os critérios de aceitação definidos pelo _Product Owner_.

* **Contrato:** Os contratos são a base de comparação dos testes de contrato de integração. Em forma de arquivos (json, xml, yaml, etc), eles contém dados de requisição, como headers, url destino, protocolo HTTP utilizado e parâmetros de envio, além de dados de retorno, como headers e código HTTP do retorno. Também possuem alguns exemplos de dados e tipagem de todos os dados de resposta. Para o nosso caso, a última informação citada é a mais importante para verificar se houve a quebra de contrato de algum dado recebido.

Como exposto anteriormente, vale relembrar que não necessariamente todos os testes foram aplicados em todos os serviços. Tem serviços que funcionam apenas com o teste estático, outros com unitários, porém temos alguns que utilizam mais de um tipo de teste para verificar toda a funcionalidade.

### Estágio de Build
  O estágio de Build é onde utilizamos o Docker criado para todos os serviços, pela equipe de DevOps.

  É responsável por gerar as imagens do docker e enviá-las ao _registry_ do DockerHub.

  Esse _stage_ é necessário somente em ambiente de homologação e de produção.
