#https://github.com/msilvafz/ouvidoria.git
from operacoesbd import*

def menulogin():
    print('Bem vindo a ouvidoria JMD')
    print('[ 1 ] Central de ouvidoria')
    print()
    login = int(input('Digite a opção desejada : '))
    print()

    print('- Para isso vamos precisar de alguns dados: ')
    nome = input('Por favor, qual seu nome? ')
    print()

def menuouvidoria():
    print()
    print('Bem-vindo ao sistema de ouvidoria da JMD')
    print()
    print('1) Problemas Frequentes (Modem, Internet ou Pagamentos)')
    print('2) Cadastrar Ocorrência')
    print('3) Ocorrências Pendentes')
    print('4) Apagar Ocorrência')
    print('5) Consultar ocorrência por código')
    print('6) Listar todas as ocorrências')
    print('7) Sair')
    print()

def problemasFrequentes():
    print()
    print('1 - Problemas com internet lenta')
    print('2 - Problemas com modem')
    print('3 - Problemas com pagamento')
    print('4 - Voltar ao menu inicial')
    print()

def opcoesOcorrencias():
    print()
    print('( 1 ) Reclamações')
    print('( 2 ) Elogios')
    print('( 3 ) Sugestões')
    print()

def inserirReclamacao(conexao, tipo,texto):
    insercao = "insert into ouvidoria (tipo,texto) values (%s,%s)"
    print()
    dados = (tipo, texto)
    insertNoBancoDados(conexao, insercao, dados)
    print('- Ocorrência feita com sucesso, aguarde para ser atendido!')

def inserirOuvidoria(conexao, tipo,texto):
    insercao = "insert into ouvidoria (tipo,texto) values (%s,%s)"
    dados = (tipo, texto)
    insertNoBancoDados(conexao, insercao, dados)
    print('- Ocorrência feita com sucesso, aguarde para ser atendido!')

def listarOuvidoria(conexao,tipo):
    print()
    if tipo == "Reclamação":
        print('-> Reclamações pendentes: ')
    elif tipo == "Elogio":
        print('-> Elogios pendentes: ')
    elif tipo == "Sugestão":
        print('-> Sugestões pendentes: ')
    print()

    consultaOuvidoria = f"select * from ouvidoria where tipo = '{tipo}'"
    listaOuvidoria = listarBancoDados(conexao, consultaOuvidoria)

    if len(listaOuvidoria) == 0:
        print('- Não temos',tipo,'no momento!')
    else:
        print('- Lista de',tipo,':')
        print()
        for i in listaOuvidoria:
            print('- ID: ', i[0])
            print('- Texto: ', i[2])
            print()

def excluirOuvidoria(conexao,tipo):
    print()
    idOuvidoria = int(input('-> Digite o ID da ocorrência que deseja apagar: '))
    print()
    consultaOuvidoria = f"select * from ouvidoria where id = {idOuvidoria} and tipo = '{tipo}'"
    ocorrencia = listarBancoDados(conexao,consultaOuvidoria)

    if len(ocorrencia) == 0:
        if tipo == "Reclamação" or tipo == "Sugestão":
            print('- Não temos nenhuma',tipo,'com este ID!')
        elif tipo == "Elogio":
            print('- Não temos nenhum',tipo, 'com este ID!')

    else:
        removerDaOuvidoria = 'delete from ouvidoria where id = %s'
        dados = (idOuvidoria,)

        excluirBancoDados(conexao, removerDaOuvidoria, dados)

        if tipo == "Reclamação" or tipo == "Sugestão":
            print('-',tipo,'removida com sucesso! ')
        elif tipo == "Elogio":
            print('-',tipo,'removido com sucesso! ')

def pesquisarOuvidoria(conexao):
    print()
    print('> Pesquisa pelo Código <')
    print()

    codigoId = input('- Digite o código da sua ocorrência: ')
    consultaOcorrenciaPorCodigo = 'select * from ouvidoria where id = ' + codigoId

    listaOcorencias = listarBancoDados(conexao, consultaOcorrenciaPorCodigo)
    if len(listaOcorencias) == 0:
        print('Não existe ocorrência com este código')
    else:
        for i in listaOcorencias:
            print('- ID: ', i[0])
            print('- Tipo: ', i[1])
            print('- Texto: ', i[2])
            print()

def todasOcorrenciasOuvidoria(conexao):
    print()
    print('-> Ocorrências pendentes: ')
    print()
    consultarTodasListagens = "select * from ouvidoria"
    listarTodasOcorrencias = listarBancoDados(conexao, consultarTodasListagens)
    for i in listarTodasOcorrencias:
        print('- Tipo: ', i[1])
        print('- Texto: ', i[2])
        print()


