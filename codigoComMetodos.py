#https://github.com/msilvafz/ouvidoria.git

from operacoesbd import *
from metodos import *


conexao = abrirBancoDados('localhost','root','Matheus7123.','ouvidoria_faculdade')


listaOuvidoria = ['Problemas com internet lenta', 'Problemas com modem', 'Problemas com pagamento']

opcao = 0

login = 0

while login != 2:
    menulogin()

    numeroCelular = int(input('Por favor, digite seu número seguindo o seguinte exemplo: - 839** - '))
    print()
    while numeroCelular <= 10000000000 or numeroCelular >= 99999999999:
        print('Número Inválido')
        numeroCelular = int(input('Por favor, digite seu número seguindo o seguinte exemplo: - 839** - '))
        print()

    cpf = int(input('Agora me diga qual seu CPF: '))
    print()
    while cpf <= 10000000000 or cpf >= 99999999999:
        print('CPF não existe')
        cpf = int(input('Agora me diga qual seu CPF: '))
        print()
    print('- Obrigado, entraremos em contato pelo telefone informado para marcar a data de sua assistência técnica.')
    break

while opcao != 7:

    menuouvidoria()

    opcao = int(input('> Digite o número referente ao problema desejado: '))

    if opcao == 1:
        problemasFrequentes()

        EscolhaOcorrencia = int(input('> Caso seu problema esteja listado acima digite o número: '))

        while EscolhaOcorrencia <= 0 or EscolhaOcorrencia > 4:
            print('Código Inválido!')
            EscolhaOcorrencia = int(input('> Caso seu problema esteja listado acima digite o número: '))
            print()

        if EscolhaOcorrencia != 4:
            inserirReclamacao(conexao, "Reclamação", listaOuvidoria[EscolhaOcorrencia - 1])


    elif opcao == 2:
        opcoesOcorrencias()

        categoria = int(input('> Por favor, digite o número da categoria desejada: '))
        print()

        if categoria == 1:
            reclamacaoCliente = input('> Certo, com poucas palavras me diga qual sua reclamação: ')
            inserirOuvidoria(conexao, "Reclamação",reclamacaoCliente)

        if categoria == 2:
            elogioCliente = input('> Certo, com poucas palavras me diga qual seu elogio: ')
            inserirOuvidoria(conexao, "Elogio",elogioCliente)

        if categoria == 3:
            sugestaoCliente = input('> Certo, com poucas palavras me diga qual seria sua sugestão: ')
            inserirOuvidoria(conexao, "Sugestão",sugestaoCliente)


    elif opcao == 3:
        opcoesOcorrencias()

        ocorrencia = int(input('> Por favor, digite o número da categoria desejada: '))
        print()

        if ocorrencia == 1:
            listarOuvidoria(conexao, "Reclamação")

        if ocorrencia == 2:
            listarOuvidoria(conexao, "Elogio")


        if ocorrencia == 3:
            listarOuvidoria(conexao, "Sugestão")


    elif opcao == 4:
        opcoesOcorrencias()

        apagar = int(input('> Por favor, digite o número da categoria desejada: '))
        print()

        if apagar == 1:
            listarOuvidoria(conexao,"Reclamação")
            excluirOuvidoria(conexao, "Reclamação")

        elif apagar == 2:
            listarOuvidoria(conexao, "Elogio")
            excluirOuvidoria(conexao, "Elogio")

        elif apagar == 3:
            listarOuvidoria(conexao, "Sugestão")
            excluirOuvidoria(conexao, "Sugestão")

    elif opcao == 5:
        pesquisarOuvidoria(conexao)

    elif opcao == 6:
        todasOcorrenciasOuvidoria(conexao)




print('Obrigado, tenha um bom dia!')

encerrarBancoDados(conexao)