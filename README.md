# Projeto_ETL_coderhouse

Autores: João Natã da Silva; Lays da Silva; Leticia Fagundes Netto; Lucas de Sousa Cavalcanti.

Esse projeto tem como objetivo fazer uma extração completa de dados de uma API, para que possamos fazer análise, processar informações e armazenar dados.

Bibliotecas utilizadas:
- Requests: fazer requisições HTTP.
- Json: manupulação de dados JSON.
- Pandas: manipulação e Análise de Dados.
- Numpy: operações em arrays multidimensionais.
- sqlite3: módulo integrado ao python que permite a interação com bancos de dados.
- Datatime: manipulação com datas e horários.
- plyer: utilização de notificações.

API utilizada:
https://brasilapi.com.br/api/banks/v1

Descrição do Projeto
Dentre as etapas do projeto, podemos classificar por ordem:
1. Criar um sistema de notificação para caso ocorra algum erro durante a extração dos dados.
2. Fazer uma requisição à API para obter os dados.
3. Transformar os dados extraídos em um DataFrame.
4. Obter 3 tabelas derivadas do DataFrame.
5. Trata as tabelas obtidas para prepará-las para o armazenamento (exemplo: apagar dados duplicados).
6. Armazena os dados em um banco de dados.
7.	Validação e visualização dos dados.
8.	Disponibilização do projeto no GitHub.
