# Criando um sistema de Blog em Django.

## Recursos

- Docker como PosteGress DB;
- Docker com Python (Django e Dependencias);

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

### Executar comando dentro do conteiner


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