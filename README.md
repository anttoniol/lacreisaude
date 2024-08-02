# Lacrei Saúde API

## Arquitetura

A arquitetura é composta pelo projeto "lacreisaude", implementada utilizando Django e contendo um aplicativo "clinica",
no qual a maior parte da API está localizada.

### Banco de dados 

Para reduzir redundâncias no banco de dados e deixá-lo mais normalizado, decidiu-se construir as seguintes tabelas:

1. Contato: possui registros de contato de profissionais (o que também pode ser usado para salvar o contato de um centro clínico, por exemplo)
2. Endereco: possui registros de endereço de profissionais (o que também pode ser usado para salvar o contato de um centro clínico, por exemplo)
3. Profissional: possui registros de profissionais
4. Consulta: possui registros de consulta

#### Suposições
1. Um endereço pode ser o mesmo para mais de um profissional 
2. Um contato pode ser o mesmo para mais de um profissional
3. Um profissional pode ter mais de um contato

## Instruções de uso

### Requisitos

Este projeto foi feito usando uma versão do Ubuntu, no qual foi necessário instalar os seguintes itens:

1. Python 3.8
2. python3.8-venv (utilizando o comando `sudo apt install python3.8-venv`

### Instalação

1. Na pasta raiz do projeto, criar um ambiente virtual, conforme explicado em https://docs.python.org/3/library/venv.html
2. Para usar o ambiente virtual, executar `source <venv>/bin/activate`, onde "<venv>" é o nome que foi dado ao ambiente virtual
3. Dentro do ambiente virtual, para instalar as bibliotecas necessárias para o projeto, executar o comando `pip install -r requirements.txt`
4. Executar os seguintes comandos:
   1. `python manage.py makemigrations`
   2. `python manage.py migrate`
5. Para executar a API, utilize o comando `python manage.py runserver`. 
6. Para utilizar a API, acesse http://127.0.0.1:8000/clinica/docs/
7. Para interagir com a API utilizando a interface do Django Administration: 
   1. Execute `python manage.py createsuperuser`, para criar um usuário admin
   2. Acesse http://127.0.0.1:8000/admin , usando os dados de usuário criados no subitem anterior
8. Para executar testes, execute o comando `./manage.py test clinica`

## Segurança

Com base nas informações disponíveis em https://docs.djangoproject.com/en/4.2/topics/security/ , o Django já possui
verificações de segurança de inputs de forma embutida, para evitar, por exemplo, SQL injection.

