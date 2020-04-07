# api-code-7
Desenvolvimento de uma API em Python, Flesk e MongoDB para fins de avaliação da empresa Code 7 (Grupo Connverte)

# Preparação do ambiente de desenvolvimento

1) Para rodar a aplicação, primeiramente instale as dependecias, execeutando o seguinte trechos de código (dentro da pasta do projeto):

>>  pip install -r dependencias.txt

# Obs: Primordial que a versão instalada do python seja > 2.7.

2) Para criar a database com as devidas coleções, siga:

2.1: Insira a sequência abaixo de comandos no seu terminal (considerando que o MongoDB está devidamente instalado, caso não esteja acesse: https://docs.mongodb.com/manual/tutorial/install-mongodb-enterprise-on-ubuntu/)

>>  mongo
>>  use portal_noticias

2.2: Agora para criar as colletions: 

>>  db.noticias.insertMany([
        {titulo: 'Texto de boas vindas', texto: 'Apenas uma saudação, querido leitor!', id_autor: 1},
        {titulo: 'Segunda parte: o grande desafio!', texto: 'Será mesmo que deu certo? Veremos em breve!', id_autor: 1},
        {titulo: 'É dada a hora!', texto: 'Acredito eu que tudo tennha dado certo sim, confiamos em seu trabalho!', id_autor: 1}
    ])

>>  db.autor.insertOne(
        {id: 1, nome: 'Luan Said Meira'}
    )

>> db.noticias.createIndex( { titulo: "text", texto: "text" } ) 
>> db.autor.createIndex(nome : "text")

Obs: O código acima serve para posteriormente utilizarmos o query selector "$text", no qual pede para que os campos tenham um index para ser feita a busca.

2.3: Verificar se a criação e inserção ocorreu corretamente:
>>   show dbs
(Caso a sua tabela conste na lista, deu tudo certo!)

Para mais informações, dúvidas ou conteúdo: https://www.tutorialspoint.com/mongodb/mongodb_create_database.htm

3) START no projeto:

3.1: Entre na pasta do projeto e execute:
>> python run-app.py

Para testar as requisições, utilize o postman, inserindo as devidas urls com os parametros necessário. Na pasta "step-by-step-postman", voce encontra uma sequencia de imagens com exemplos de entrada para cada tipo de requisição (GET, POST, DELETE) com as devidas urls.

