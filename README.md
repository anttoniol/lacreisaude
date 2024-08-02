# Lacrei Saúde APi

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

1. Na pasta raiz do projeto, criar um ambiente virtual, conforme explicado em https://docs.python.org/3/library/venv.html
2. Dentro do ambiente virtual, para instalar as bibliotecas necessárias para o projeto, executar o comando `pip install -r requirements.txt`
3. Executar os seguintes comandos:
   1. `python manage.py makemigrations`
   2. `python manage.py migrate`
3. Para executar a API, utilize o comando `python manage.py runserver`. 
4. Para utilizar a API, acesse http://127.0.0.1:8000/clinica/docs/
5. Para interagir com a API utilizando a interface do Django Administration, acesse `http://127.0.0.1:8000/admin/`, usando "admin" como usuário e senha
6. Para executar testes, execute o coamando `./manage.py test clinica`

## Segurança

Com base nas informações disponíveis em https://docs.djangoproject.com/en/5.0/topics/security/ , o Django já possui
verificações de segurança de inputs de forma embutida, para evitar, por exemplo, SQL injection.

