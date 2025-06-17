### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

log = [{'timestamp': '2021-06-23 10:00:00', 'level': 'VAI', 'message': 'conexão realizada com sucesso!'},
{'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}]

for i in log:
    if i['level'] == 'ERROR':
        print(i['message'] + f' no dia {i['timestamp']}')
        print(' ')
    else:
        print(i['message'] + f' realizado no dia {i['timestamp']}')
        print(' ')