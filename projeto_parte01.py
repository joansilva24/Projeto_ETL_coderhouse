from plyer import notification

from datetime import date,datetime,timedelta

notification.notify (
    title = 'título da notificação',
    message = 'Mensagem da notificação',
    app_name = 'nome do aplicativo',
    timeout = 10
)


def alerta(nivel,base,etapa):
    if nivel == 1:
        nivel = 'Alerta baixo'
    elif nivel == 2:
        nivel = 'Alerta médio'
    elif nivel == 3:
        nivel = 'Alerta alto'
    
    return notification.notify (
    title = f'ATENÇÃO {nivel}',
    message = f'Falha no carregamento da base {base} na estapa {etapa}.\n{str(datetime.now())}',
)


alerta(1,'Bancos','CARREGAMENTO')


import requests

api = requests.get('https://brasilapi.com.br/api/banks/v1')
api.status_code



if api.status_code == 200:
    data_json = api.json()
else:
    alerta(1,'Bancos','CARREGAMENTO')


if api.status_code == 200:
    data_json = api.json()
else:
    print('Erro ao acessar a API')


data_json


import pandas as pd

bancos = pd.DataFrame(data_json)
bancos


df_selic = bancos[bancos['name'].str.contains("Selic", case=False, na=False)]
print(df_selic)


df_brasil = bancos[bancos['name'].str.contains("Brasil", case=False, na=False)]
print(df_brasil)


import sqlite3
conn = sqlite3.connect('DataBase')
bancos.to_sql('Bancos',conn,if_exists='replace',index=False)
conn.close()

