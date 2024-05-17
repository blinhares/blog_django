# Criando um Sistema de Blog em Django

## Recursos

- Docker como PosteGress DB;
- Docker com Python (Django e Dependências);

## Como Rodar Localmente

Certifique-se de ter instalado na sua máquina o `Docker` e o `Python`.
Nos arquivos deste repositório você ira encontrar arquivos de configuração do poetry, fique liver para utiliza-los. Na explicação abaixo, nos vamos ignora-los.

### Clonar o Repositório

```bash
git clone https://github.com/blinhares/blog_django.git
```

### Instalar dependências (opcional)

Como as bibliotecas estarão instaladas no nosso docker, nao se faz necessário a instalação das libs no seu python local.

```bash
pip install blog_django/djangoapp/requirements.txt 
```

### Variáveis de ambiente

Para isso vamos trabalhar com arquivos do tipo `.env` na pasta `blog_django/dotenv_files`.
Nessa pasta há um arquivo de exemplo e o modelo exato utilizado neste projeto.
Fique livre para altera-lo. 
Para facilitar, vamos utilizar o mesmo arquivo ja existente, para isso simplesmente renomeamos o arquivo `.env_utilizado_projeto` para `.env`.

### Buildando Suas Imagens

Para dar start ao projeto, vamos construir nosso contêiner através do arquivo `docker-compose.yml` dentro de `/blog_django`.

```bash
sudo docker compose up --build 
```

Se tudo for bem, agora voce deve ter dois conteiners rodando em sua maquina. Para verificar basta executar o comando abaixo:

```bash
docker ps -a
```

A essa altura o projeto ja deve estar rodando no seu endereço local [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

### Criar Django Admin


## Comando Uteis

### Para Buildar os Conteiners

```bash
sudo docker compose up --build --force-recreate

```

### Para Rodar o Conteiner

```bash
sudo docker compose up

```

### Para Rodar o Conteiner em Silencio

```bash
sudo docker compose up -d

```

### Para Desligar o Conteiner

```bash
sudo docker compose down

```

### Executar comando dentro do Conteiner


Com o conteiner rodando, faça:

```bash
docker exec djangoapp <comando>
```

Sem o conteiner Rodando:

```bash
docker compose run --rm djangoapp  <comando>
```

Ex.:

```bash
docker exec djangoapp python -V
```

resulta em:

```bash
Python 3.12.3
```

### Executando o comando no Shell

```Bash
docker compose run --rm djangoapp sh -c '<comando'
```

Ex.:

```Bash
docker compose run --rm djangoapp sh -c 'echo  ola'
```

### Executando o Terminal de Modo interativo

```bash
docker exec -it djangoapp sh
```

## Como utilizar

### Criar um super User

Execute dentro do conteiner o seguinte comando:

```bash
python manage.py createsuperuser
```

Crie um super usuario para voce.