nomes = []
sobrenomes = []
cpfs = []
enderecos = []
emails = []
celulares = []
senhas = []
saldos = []
variavel = []

def nomeVal():
    nome = input("Insira seu nome: ")
    print(nome)
    if len(nome)<3:
        print("Invalido! Insira novamente: ")
        nomeVal() 
    else:
            pass
    return nome

def sobrenomeVal():
    sobrenome = input("Insira seu sobrenome: ")
    print(sobrenome)
    if len(sobrenome)<3:
        print("Invalido! Insira novamente: ")
        sobrenomeVal()  
    else:
        pass
    return sobrenome

def senhaVal():
    senha = input("Insira sua senha: ")
    if(len(senha)<5):
        print("Invalido! Insira novamente: ")
        senhaVal()
    else:
        return senha

    if "#"in senha:
        return senha 
    else:
        print("Invalido! A senha precisa de pelo menos um caractere especial!")
        senhaVal()

def emailVal():
    email = input("Insira seu e-mail: ")
    if "@" in email: 
        return email
    else:
        print("Invalido! Insira novamente: ")
        emailVal()

def depositar(variavel):
    deposito = float(input("Insira o valor a ser depositado: "))
    if deposito>0:
        print("Valor de R$",deposito,"depositado com sucesso!")
        saldos[variavel]+=deposito
    opcoes(variavel)

def saque(variavel):
    sacar = float(input("Insira a quantia de saque: "))
    if sacar <saldos[variavel]:
        print("O valor de R$",sacar,"foi sacado com sucesso!")
        saldos[variavel]=(saldos[variavel])-(sacar)
    else:
        print("Valor ultrapassou os limites de saldo!")
        operacoes(varialvel)

def verifica(variavel):
    print("Seu saldo equivale a:", saldos[variavel], "R$")
   
def transferencia(variavel):
    dinheiro = float(input("Valor:"))
    if dinheiro>0 and dinheiro<saldos[variavel]:
        saldos[variavel] += saldos[variavel] - (dinheiro)
    else:
        print("Valor ultrapassou os limites de saldo!")
        operacoes(varialvel)

def cancelar(variavel):
    print("Você deseja finalizar esta operação?")
    if "Sim":
        print("Operação finalizada!")
        raise SystemExit 
    else:
        operacoes(variavel)
    return

def consultarC(variavel):
    print("Nome: ",nomes[variavel])
    print("Sobrenome: ",sobrenomes[variavel])
    print("Senha: ",senhas[variavel])
    print("E-mail: ",emails[variavel])
    print("Endereço: ",enderecos[variavel])
    print("CPF: ",cpfs[variavel])
    print("Celular: ",celulares[variavel])
    print("Saldo da conta:",saldos[variavel])

def consultar():
    lista = (len(nomes))
    for variavel in range(lista):
        print("Nome: ",nomes[variavel])
        print("Sobrenome: ",sobrenomes[variavel])
        print("Senha: ",senhas[variavel])
        print("E-mail: ",emails[variavel])
        print("Endereco: ",enderecos[variavel])
        print("CPF: ",cpfs[variavel])
        print("Celular: ",celulares[variavel])
        print("Saldo da conta: ",saldos[variavel])

def deletar(variavel): 
    del nomes[variavel]
    del sobrenomes[variavel]
    del senhas[variavel]
    del emails[variavel]
    del enderecos[variavel]
    del cpfs[variavel]
    del celulares[variavel]
    del saldos[variavel]
    print("Cliente removido: ")
    consultar()

def atualização(variavel):
    opcao = int(input('''
    1-Nome
    2-Sobrenome
    3-CPF
    4-Email
    5-Endereço
    6-Celular
    7-Senha
    Insira a opção que será atualizada: '''))

    if opcao==1:
        nomes[variavel]=nomeVal()
        print("Alterado:")
        consultar()
    elif opcao==2:
        sobrenomes[variavel]=sobrenomeVal()
        print("Alterado:")
        consultar()
    elif opcao==3:
        cpfs[variavel]=input("Insira seu CPF:")
        print("Alterado:")
        consultar()
    elif opcao==4:
        emails[variavel]=input("Insira seu E-mail: ")
        print("Alterado:")
        consultar()
    elif opcao==5:
        enderecos[variavel]=input("Insira seu endereço: ")
        print("Alterado:")
        consultar()
    elif opcao==6:
        celulares[variavel]=input("Insira seu número de celular: ")
        print("Alterado:")
        consultar()
    elif opcao==7:
        senhas[variavel]=senhaVal()
        print("Alterado:")
        consultar()

def administracao(variavel):
    print('''
    1- Consultar um cliente
    2- Consultar lista de clientes
    3- Deletar um cliente
    4- Atualizar dados de um cliente específico.
    5- Sair do menu de administrador   
    ''')
    administrador(variavel) 

def usuario(variavel):
    nomeU = input("Insira seu nome: ")
    senhaU = input("Insira a senha:")
    administracao(variavel)

def cadastro():
    nome = nomeVal()
    sobrenome = sobrenomeVal()
    senha = senhaVal()
    email = emailVal()
    cpf = input("Insira seu CPF:")
    endereco = input("Insira seu endereço:")
    celular = input("Insira seu número de celular:")
    if nome!=False or sobrenome!=False or senha!=False or email!=False:
        nomes.append(nome)
        sobrenomes.append(sobrenome)
        senhas.append(senha)
        emails.append(email)
        enderecos.append(endereco)
        cpfs.append(cpf)
        celulares.append(celular)
        variavel = nomes.index(nome)
        saldos.append(0)
    operacoes(variavel)

def administrador(variavel):
    opcao=(int(input("Insira a opção escolhida: ")))
    if opcao==1:
        variavel = int(input("Insira o número de posição da pessoa a ser buscada: "))
        consultarC(variavel)
    if opcao==2:
        consultar()
    if opcao==3:
        variavel = int(input("Insira o número de posição da pessoa a ser deletada: "))
        deletar(variavel)
    if opcao==4:
        variavel = int(input("Insira o número da posição da pessoa a ser alterada: "))
        atualização(variavel)

def operacoes(variavel):
    while True:
        print('''
        1-Depósito
        2-Saque
        3-Verificação de saldo
        4-Transferência Bancária
        5-Encerrar conta''')
        opcao = int(input("Insira o número da operação escolhida: "))
        if opcao==1:
            depositar(variavel)
        if opcao==2:
            saque(variavel)
        if opcao==3:
            saldos(variavel)
        if opcao==4:
            transferencia(variavel)
        if opcao==5:
            cancelar(variavel)
           
def opcoes(variavel):
    while True:
        print('''
        1-Cadastro de cliente 
        2-Administração
        3-Operações
        4-Sair ''')
        opcao = int(input("Insira o número da opção desejada: "))
        if(opcao==1):
            cadastro()
        if(opcao==2):
            usuario(variavel)
        if(opcao==3):
            operacoes(variavel)
        if(opcao==4):
            raise SystemExit
    return
varialvel = []
opcoes(variavel)

# As operações estão todas funcionando, 
#a única coisa que não consegui fazer rodar foi as consultas,
#quando chega nessa parte da erro;