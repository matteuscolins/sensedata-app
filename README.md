# sensedata-app

Criar uma aplicativo em flask que renderize duas páginas a partir dos dados obtidos através da API swapi.dev

1 - Primeira página: Uma tabela com os dados dos personagens do Start Wars com as seguintes features:

  - Suportar paginação de 10 em 10 registros.

  - Ordenação por Nome, Gênero, Peso e Altura dos personagens.

  - Opcao em tela para filtrar po Film, Startship, Vehicles e Planets

2 - Segunda página: Tabela com dados das startships disponíveis: Uma página contendo uma tabela com o score de cada uma das starships fornecidas.

  - Esse score deverá ser composto pelo hyperdrive_rating dividido pelo cost_in_credits da nave.

  - Exibir as naves numa tabela ordenada em ordem decrescente da melhor nave para a pior.

Requisitos técnicos:

  - Desenvolver utilizando Flask

  - Deploy em docker (pontos adicionais se já hospedar em um server pra testarmos)

  - Disponibilizar o código num repositório Git pra avaliarmos.

OBS: Não utilizar helpers prontos da API (como swapi-python).

## Requisitos

- Python >= 3.6
- Flask
- flask-paginate
- gunicorn

## Instalação

### Criação ambiente virtual
```
virtualenv venv
```
### Instalação das dependências
```
pip install -r requirements.txt
```
### Execução
```
flask run
```
### Execução com o Docker
```
docker-compose build && docker-compose up
```


