### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.


dados_usuario = {'nome':'Haniel Freitas','idade':26,'email':'hanielfreitas3@gmail.com'}

if 16 <= dados_usuario['idade'] <= 65:
    if '@' not in dados_usuario['email'] or '.' not in dados_usuario['email']:
        print('E-mail inválido')
    else:
        print("Dados de usuário válidos")
else:
    print('idade não permitida')