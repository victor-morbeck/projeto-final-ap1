def main():

#Função que irá listar as opções do Menu
    medicos =[]
    ponteiro = Menu()
    while ponteiro != 5:
        if ponteiro == 1:
            print('Menu Médicos')
            subponteiro = MenuMedicos()
            while subponteiro != 6:
                if subponteiro == 1:
                    print('Listar Todos os Médicos')
                    ListarMedicos()
                elif subponteiro == 2:
                    print('Pesquisar Médico Específico')
                    ListarMedicoEspecifico()
                elif subponteiro == 3:
                    print('Cadastrar Médico')
                    CadastroMedico()


                elif subponteiro == 4:
                    print('Alterar Cadastro')
                    AlterarCadastroMedico()
                elif subponteiro == 5:
                    print('Excluir Cadastro')
                    ExcluirCadastroMedico()

                else:
                    print('Opcão Inválida')

                subponteiro = MenuMedicos()

        elif ponteiro == 2:
            print('Menu de Pacientes')
            subponteiro = MenuPacientes()
            while subponteiro != 6:
                if subponteiro == 1:
                    print('Listar Todos os Pacientes')
                    ListarPacientes()
                elif subponteiro == 2:
                    print('Pesquisar Médico Paciente Específico')
                    ListarPacienteEspecifico()
                elif subponteiro == 3:
                    print('Cadastrar Paciente')
                    CadastroPaciente()
                elif subponteiro == 4:
                    print('Alterar Cadastro')
                    AlterarCadastroPaciente()
                elif subponteiro == 5:
                    print('Excluir Cadastro')
                    ExcluirCadastroPaciente()

                else:
                    print('Opcão Inválida')

                subponteiro = MenuPacientes()
        elif ponteiro == 3:
            print('Menu de Consultas')
            subponteiro = MenuConsultas()
            while subponteiro != 6:
                if subponteiro == 1:
                    print('Listar Todos as Consultas')
                    ListarConsultas()

                elif subponteiro == 2:

                    print('Pesquisar Consulta Específica')
                    ListarConsultaEspecifica()

                elif subponteiro == 3:
                    print('Cadastrar Consulta')
                    CadastrarConsulta()
                elif subponteiro == 4:
                    print('Alterar Cadastro')
                    AlterarConsulta()

                elif subponteiro == 5:
                    print('Excluir Cadastro')

                    ExcluirConsulta()
                else:
                    print('Opcão Inválida')

                subponteiro = MenuConsultas()
        elif ponteiro ==4:
            print('Relatórios')
            subponteiro = MenuRelatorios()
            while subponteiro != 4:
                if subponteiro == 1:
                    print('Relatório Médico')
                    RelatorioMedico()
                elif subponteiro ==2:
                    print('Relatório Pacientes')
                    RelatorioPaciente()
                elif subponteiro == 3:
                    print('Relatório Consultas')
                    RelatorioConsulta()
                else:
                    print('Opção inválida')
                subponteiro =MenuRelatorios()



        ponteiro = Menu()
    print('Programa Encerrado')


def Menu():
    print('[1] Médicos')
    print('[2] Pacientes')
    print('[3] Consultas')
    print('[4] Relatórios')
    print('[5] Encerrar')
    valor = int(input('Digite o número correspondente de cada opção:' '\n'))
    return valor

def MenuMedicos():
    print('[1] Listar Médicos')
    print('[2] Listar Médico específico ')
    print('[3] Cadastrar Médico')
    print('[4] Alterar Cadastro')
    print('[5] Excluir Cadastro')
    print('[6] Sair')
    valor = int(input('Digite o número correspondente de cada opção:' '\n'))
    return valor

def MenuPacientes():
    print('[1] Listar Pacientes')
    print('[2] Listar Paciente Específico')
    print('[3] Cadastar Paciente')
    print('[4] Alterar Cadastro')
    print('[5] Excluir Cadastro')
    print('[6] Sair')
    valor = int(input('Digite o número correspondente de cada opção:' '\n'))
    return valor

def MenuConsultas():
    print('[1] Listar Consultas')
    print('[2] Listar Consulta Específica')
    print('[3] Cadastar Consulta')
    print('[4] Alterar Cadastro')
    print('[5] Excluir Cadastro')
    print('[6] Sair')
    valor = int(input('Digite o número correspondente de cada opção:' '\n'))
    return valor
def MenuRelatorios():
    print('[1] Relatório Médicos')
    print('[2] Relatório Pacientes')
    print('[3] Relatório Consultas')
    print('[4] Sair')
    valor = int(input('Informe a opção:''\n'))
    return valor

def CadastroMedico():
    medico =[]
    medicos = CarregaArquivoMedico()
    cadastro = input('Digite o CRM do médico ou tecle ENTER para sair')
    while cadastro != '':
        valor = VerificaCodigo(cadastro,medicos)
        if valor == False:
            print('Esse Código já foi cadastrado')
        else:
            medico.append(cadastro)
            medico.append(input('Digite o nome do médico'))
            medico.append(input('Digite a data de nascimento ''xx/xx/xxx'))
            medico.append(input('Digite a especialidade'))
            medico.append(input('Digite em qual Instituição se formou'))
            medico.append(input('Digite o E-mail'))
            medico.append(input('Digite o Telefone'))
        medicos.append(medico)
        medico =[]


        AtualizarArquivoMedico(medicos)



        cadastro = input('Digite o CRM do médico ou tecle ENTER para sair')

def ListarMedicos():
    medicos = CarregaArquivoMedico()
    medicos = CarregaArquivoMedico()
    if medicos == []:
        print('Não há medicos cadastrados')
        return 'erro'
    for medico in medicos:
        print('Código:', medico[0])
        print('Nome:', medico[1])
        print('Data de Nascimento:', medico[2])
        print('Especialidade:', medico[3])
        print('Instituição de Formação:', medico[4])
        print('E-mail:', medico[5])
        print('Telefone:', medico[6])
        print('----------------------------')

def ListarMedicoEspecifico():
    medicos = CarregaArquivoMedico()
    if medicos == []:
        print('Não há medicos cadastrados')
        return 'erro'
    crm = input('Digite o CRM do médico que deseja procurar:')
    for c in range(len(medicos)):
            if crm == medicos[c][0]:
                print('Código:', medicos[c][0])
                print('Nome:', medicos[c][1])
                print('Data de Nascimento:',medicos[c][2])
                print('Especialidade:', medicos[c][3])
                print('Instituição de Formação:', medicos[c][4])
                print('E-mail:', medicos[c][5])
                print('Telefone:', medicos[c][6])
                print('----------------------------')
                return c
            else:
                print('Cadastro não Encontrado')

def AlterarCadastroMedico():
    medicos = CarregaArquivoMedico()
    ListarMedicos()
    crm = input('Digite o CRM do médico que deseja alterar dados')
    for c in range(len(medicos)):

                    if crm == medicos[c][0]:
                        print(f'[1]Código:', medicos[c][0])
                        print(f'[2]Nome:', medicos[c][1])
                        print(f'[3]Data de Nascimento:', medicos[c][2])
                        print(f'[4]Especialidade:', medicos[c][3])
                        print(f'[5]Instituição de Formação:', medicos[c][4])
                        print(f'[6]E-mail:', medicos[c][5])
                        print(f'[7]Telefone:', medicos[c][6])
                        print('----------------------------')
                        valor = int(input('Digite a opção correspondente ao dado que deseja alterar:'))
                        if valor == 1:
                            del medicos[c][0]

                            cod = input('Digite o novo CRM')
                            val = VerificaCodigo(cod,medicos)
                            if val == True:
                                medicos[c].insert(0, cod)
                                print('Alterado com Sucesso')
                            else:
                                print('Código Existente')
                        elif valor ==2:
                            del medicos[c][1]
                            nome = input('Digite o novo Nome')
                            medicos[c].insert(1, nome)
                            print('Alterado Com Sucesso')
                        elif valor ==3:
                            del medicos[c][2]
                            data = input('Insira a nova data de nascimento')
                            medicos[c].insert(2, data)
                            print('Alterado com Sucesso')
                        elif valor ==4:
                            del medicos[c][3]
                            esp = input('Insira a nova Especialidade')
                            medicos[c].insert(3, esp)
                            print('Alterado com Sucesso')
                        elif valor ==5:
                            del medicos[c][4]
                            it = input('Insira a nova Instituição de Formação')
                            medicos[c].insert(4, it)
                            print('Alterado com Sucesso')
                        elif valor ==6:
                            del medicos[c][5]

                            email = input('Insira o novo E-mail:')
                            medicos[c].insert(5, email)
                        elif valor ==7:
                            del medicos[c][6]
                            tel = input('Insira o novo Telefone:')
                            medicos[c].insert(6, tel)
                        else:
                            print('Opção inválida')


                        AtualizarArquivoMedico(medicos)
def ExcluirCadastroMedico():
    medicos = CarregaArquivoMedico()
    ListarMedicos()
    crm = input('Digite o CRM do médico que deseja excluir do bando de dados')
    for c in range(len(medicos)):
        if crm == medicos[c][0]:
            print(f'[1]Código:', medicos[c][0])
            print(f'[2]Nome:', medicos[c][1])
            print(f'[3]Data de Nascimento:', medicos[c][2])
            print(f'[4]Especialidade:', medicos[c][3])
            print(f'[5]Instituição de Formação:', medicos[c][4])
            print(f'[6]E-mail:', medicos[c][5])
            print(f'[7]Telefone:', medicos[c][6])
            print('----------------------------')

            ponteiro = input('Deseja Excluir Esse Cadastro?''\n''Tecle 1 para SIM e 2 para NÃO''\n')
            if ponteiro == '1':
                del medicos[c]
                AtualizarArquivoMedico(medicos)
                print('Cadastro Excluído')

            else:
                print('Voltando ao Menu')
            return c
        else:
            print('CRM não Encontrado')
def CadastroPaciente():
    paciente =[]
    pacientes = CarregaArquivoPaciente()
    cadastro = input('Digite o CPF do paciente ou tecle ENTER para sair')
    while cadastro != '':
        valor = VerificaCodigo(cadastro,pacientes)
        if valor == False:
            print('Esse Código já foi cadastrado')
        else:
            paciente.append(cadastro)
            paciente.append(input('Digite o nome do paciente'))
            paciente.append(input('Digite a data de nascimento ''xx/xx/xxx'))
            paciente.append(input('Digite o sexo'))
            paciente.append(input('Digite o plano de Saúde'))
            paciente.append(input('Digite o E-mail'))
            paciente.append(input('Digite o Telefone'))
        pacientes.append(paciente)
        paciente =[]

        AtualizarArquivoPaciente(pacientes)


        cadastro = input('Digite o CPF do paciente ou tecle ENTER para sair')

def ListarPacientes():
    pacientes = CarregaArquivoPaciente()
    if pacientes == []:
        print('Não há pacientes cadastrados')
        return 'erro'
    for paciente in pacientes:
        print('Código:', paciente[0])
        print('Nome:', paciente[1])
        print('Data de Nascimento:', paciente[2])
        print('Sexo:', paciente[3])
        print('Plano de Saúde:', paciente[4])
        print('E-mail:', paciente[5])
        print('Telefone:', paciente[6])
        print('----------------------------')

def ListarPacienteEspecifico():
    pacientes = CarregaArquivoPaciente()
    if pacientes == []:
        print('Não há pacientes cadastrados')
        return 'erro'
    cpf = input('Digite o CPF do paciente que deseja procurar:')
    for c in range(len(pacientes)):
            if cpf == pacientes[c][0]:
                print('Código:', pacientes[c][0])
                print('Nome:', pacientes[c][1])
                print('Data de Nascimento:',pacientes[c][2])
                print('Sexo:', pacientes[c][3])
                print('Plano de Saúde:', pacientes[c][4])
                print('E-mail:', pacientes[c][5])
                print('Telefone:', pacientes[c][6])
                print('----------------------------')
                return c
            else:
                print('Cadastro não Encontrado')

def AlterarCadastroPaciente():
    pacientes = CarregaArquivoPaciente()
    ListarPacientes()
    cpf = input('Digite o CPF do paciente que deseja alterar dados')
    for c in range(len(pacientes)):

                    if cpf == pacientes[c][0]:
                        print(f'[1]Código:', pacientes[c][0])
                        print(f'[2]Nome:', pacientes[c][1])
                        print(f'[3]Data de Nascimento:', pacientes[c][2])
                        print(f'[4]Sexo:', pacientes[c][3])
                        print(f'[5]Plano de Saúde:', pacientes[c][4])
                        print(f'[6]E-mail:', pacientes[c][5])
                        print(f'[7]Telefone:', pacientes[c][6])
                        print('----------------------------')
                        valor = int(input('Digite a opção correspondente ao dado que deseja alterar:'))
                        if valor == 1:
                            del pacientes[c][0]

                            cod = input('Digite o novo CPF')
                            val = VerificaCodigo(cod,pacientes)
                            if val == True:
                                pacientes[c].insert(0, cod)
                                print('Alterado com Sucesso')
                            else:
                                print('Código Existente')
                        elif valor ==2:
                            del pacientes[c][1]
                            nome = input('Digite o novo Nome')
                            pacientes[c].insert(1, nome)
                            print('Alterado Com Sucesso')
                        elif valor ==3:
                            del pacientes[c][2]
                            data = input('Insira a nova data de nascimento')
                            pacientes[c].insert(2, data)
                            print('Alterado com Sucesso')
                        elif valor ==4:
                            del pacientes[c][3]
                            esp = input('Insira o Sexo')
                            pacientes[c].insert(3, esp)
                            print('Alterado com Sucesso')
                        elif valor ==5:
                            del pacientes[c][4]
                            it = input('Insira o novo Plano de Saúde:')
                            pacientes[c].insert(4, it)
                            print('Alterado com Sucesso')
                        elif valor ==6:
                            del pacientes[c][5]

                            email = input('Insira o novo E-mail:')
                            pacientes[c].insert(5, email)
                        elif valor ==7:
                            del pacientes[c][6]
                            tel = input('Insira o novo Telefone:')
                            pacientes[c].insert(6, tel)
                        else:
                            print('Opção inválida')


                        AtualizarArquivoPaciente(pacientes)
def ExcluirCadastroPaciente():
    pacientes = CarregaArquivoPaciente()
    ListarPacientes()
    cpf = input('Digite o CPF do paciente que deseja excluir do banco de dados')
    for c in range(len(pacientes)):
        if cpf == pacientes[c][0]:
            print(f'[1]Código:', pacientes[c][0])
            print(f'[2]Nome:', pacientes[c][1])
            print(f'[3]Data de Nascimento:', pacientes[c][2])
            print(f'[4]Sexo:', pacientes[c][3])
            print(f'[5]Plano de Saúde:', pacientes[c][4])
            print(f'[6]E-mail:', pacientes[c][5])
            print(f'[7]Telefone:', pacientes[c][6])
            print('----------------------------')

            ponteiro = input('Deseja Excluir Esse Cadastro?''\n''Tecle 1 para SIM e 2 para NÃO''\n')
            if ponteiro == '1':
                del pacientes[c]
                AtualizarArquivoPaciente(pacientes)
                print('Cadastro Excluído')

            else:
                print('Voltando ao Menu')
            return c
        else:
            print('CRM não Encontrado')





def VerificaCodigo(codigo,lista):
    for c in lista:
        if codigo == c[0]:
            return False
        else:
            return True

def CarregaArquivoMedico():

    import os
    if not os.path.isfile('medicos.txt'):
        arquivo = open('medicos.txt', 'w')
        arquivo.close()

    arquivo = open('medicos.txt', 'r')
    medicos = []

    for linha in arquivo:
        medico = linha.replace('\n','')
        medico = medico.split(';')

        medicos.append(medico)
    arquivo.close()

    return medicos
def AtualizarArquivoMedico(medicos):

    arquivo = open('medicos.txt', 'w')


    for c in range(len(medicos)):
        linha = ''

        for i in range(len(medicos[c])):
            linha += medicos[c][i] + ';'

        linha = linha[:-1] + '\n'
        arquivo.write(linha)
    arquivo.close()
def CarregaArquivoPaciente():

    import os
    if not os.path.isfile('pacientes.txt'):
        arquivo = open('pacientes.txt', 'w')
        arquivo.close()

    arquivo = open('pacientes.txt', 'r')
    pacientes = []

    for linha in arquivo:
        paciente = linha.replace('\n','')
        paciente = paciente.split(';')

        pacientes.append(paciente)
    arquivo.close()

    return pacientes
def AtualizarArquivoPaciente(pacientes):

    arquivo = open('pacientes.txt', 'w')


    for c in range(len(pacientes)):
        linha = ''

        for i in range(len(pacientes[c])):
            linha += pacientes[c][i] + ';'

        linha = linha[:-1] + '\n'
        arquivo.write(linha)
    arquivo.close()

def CarregaArquivoConsulta():
    import os
    if not os.path.isfile('consultas.txt'):
        arquivo = open('consultas.txt', 'w')
        arquivo.close()

    arquivo = open('consultas.txt', 'r')
    consultas = []

    for linha in arquivo:
        consulta = linha.replace('\n', '')
        consulta = consulta.split(';')

        consultas.append(consulta)
    arquivo.close()

    return consultas
def AtualizarArquivoConsulta(consultas):
    arquivo = open("consultas.txt", "w")

    for c in range(len(consultas)):
        linha = ''

        for i in consultas[c]:
            if type(i) is str:
                linha += i + ';'

            else:
                for j in i:
                    linha += j + ';'

        linha = linha[:-1]
        linha += '\n'
        arquivo.write(linha)

    arquivo.close()
def CadastrarConsulta():
    consultas = CarregaArquivoConsulta()
    medicos = CarregaArquivoMedico()
    pacientes = CarregaArquivoPaciente()
    consulta = []
    ListarMedicos()
    crm = str(input('Digite o CRM do médico para a consulta'))
    for c in range(len(medicos)):
        if crm == medicos[c][0]:
            print('Cadastro encontrado')
            if consultas == []:
                consulta.append(crm)
                print('Cadastrando CRM')
            else:
                for i in range(len(consultas)):
                    if crm == consultas[i][0]:
                        print('CRM já cadastrado na consulta')

                        CadastrarConsulta()
                    else:
                        consulta.append(crm)
                        print('Cadastrando CRM')
        else:
            print('Não foi encontrado médico cadastrado com esse CRM')
            CadastrarConsulta()
    ListarPacientes()
    cpf = str(input('Digite o CPF do paciente para a consulta'))
    for paciente in range(len(pacientes)):
        if cpf == pacientes[paciente][0]:
            print('Cadastro encontrado')
            if consultas == []:
                consulta.append(cpf)
                print('Cadastrando CPF')
            else:
                for pc in range(len(consultas)):
                    if cpf == consultas[pc][1]:
                        print('CPF já cadastrado na consulta')

                        CadastrarConsulta()
                    else:
                        consulta.append(cpf)
                        print('Cadastrado com sucesso')
        else:
            print('Não há cadastro de cliente com esse CPF')
            CadastrarConsulta()
    data = input('Informe a data da consulta a ser marcada')
    if consultas ==[]:
        consulta.append(data)
        print('Cadastrando Data')
    else:
        for dt in range(len(consultas)):
            if data == consultas[dt][2]:
                print('Data já cadastrada na consulta')
                CadastrarConsulta()
            else:
                consulta.append(data)
                print('Cadastrado com sucesso')
    hora = input('Informe a hora da consulta a ser marcada')
    if consultas == []:
        consulta.append(hora)
        print('Cadastrando Hora')
    else:
        for hr in range(len(consultas)):
            if hora == consultas[hr][3]:
                print('Hora já cadastrada na consulta')
                CadastrarConsulta()
            else:
                consulta.append(hora)
                print('Cadastrado com Sucesso')
    diagnostico = input('Informe o diagnóstico do paciente')
    if consultas == []:
        consulta.append(diagnostico)
        print('Cadastrando Diagnostico')
    else:
        for dg in range(len(consultas)):
            if diagnostico == consultas[dg][4]:
                print('Diagnostico já cadastrado')
                CadastrarConsulta()
            else:
                consulta.append(diagnostico)
                print('Cadastrado com Sucesso')
    remedios = input('Informe o medicamento indicado ao paciente:''\n')
    while remedios != '':
        consulta.append(remedios)
        print('Medicamento adicionado!')
        remedios = input('Informe outro medicamento ou tecle ENTER para sair')



    consultas.append(consulta)

    AtualizarArquivoConsulta(consultas)
def ListarConsultas():
    consultas = CarregaArquivoConsulta()
    if consultas == []:
        print('Não há consultas cadastradas')
        print('--------------------------')
        return 'erro'


    for consulta in range(len(consultas)):
        print('CRM:', consultas[consulta][0])
        print('CPF:', consultas[consulta][1])
        print('Data da consulta:', consultas[consulta][2])
        print('Hora da consulta:', consultas[consulta][3], 'horas')
        print('Diagnóstico:', consultas[consulta][4])
        consulta1 = consultas[consulta][5:]
        for i in range(len(consulta1)):
            print('Medicamentos:', consulta1[i])

        print('------------------------------------------')

def ListarConsultaEspecifica():
    consultas = CarregaArquivoConsulta()
    if consultas == []:
        print('Não há consultas cadastradas')
        return 'erro'
    crm = input('Informe o crm do médico para específicar a consulta:''\n')

    for consulta in range(len(consultas)):
        if crm == consultas[consulta][0]:
            print('CRM:', consultas[consulta][0])
            print('CPF:', consultas[consulta][1])
            print('Data da consulta:', consultas[consulta][2])
            print('Hora da consulta:', consultas[consulta][3])
            print('Diagnóstico:', consultas[consulta][4])
            consulta1 = consultas[consulta][5:]
            for c in range(len(consulta1)):
                print('Medicamentos:', consulta1[c])
            print('---------------------------------')

def AlterarConsulta():
    consultas = CarregaArquivoConsulta()
    medicos = CarregaArquivoMedico()
    pacientes = CarregaArquivoPaciente()
    ListarConsultas()

    crm = input('Informe o CRM do médico para localizar a consulta:''\n')

    for c in range(len(consultas)):
        if crm == consultas[c][0]:
            print('Alteração de dados')
            print(f'[1] CRM:', consultas[c][0])
            print(f'[2] CPF:', consultas[c][1])
            print(f'[3] Data da consulta', consultas[c][2])
            print(f'[4] Hora da consulta:', consultas[c][3])
            print(f'[5] Diagnóstico:', consultas[c][4])
            consulta1 = consultas[c][5:]
            for i in range(len(consulta1)):
                print('[6] Medicamentos:',consulta1[i])
            print('----------------------------')

            ponteiro = int(input('Escolha uma opção:''\n'))

            if ponteiro == 1:
                print('Alterar CRM')
                del consultas[c][0]
                codigo = input('Digite o CRM atualizado')
                for medico in range(len(medicos)):
                    if codigo == medicos[medico][0]:
                        consultas[c].insert(0, codigo)
                        print('Alterado com Sucesso')
            elif ponteiro ==2:
                print('Alterar CPF:')
                del consultas[c][1]
                cpf = input('Digite o CPF atualizado')
                for paciente in range(len(pacientes)):
                    if cpf == pacientes[paciente][0]:
                        consultas[c].insert(1, cpf)
                        print('Alterado com Sucesso')
            elif ponteiro == 3:
                print('Alterar Data')
                del consultas[c][2]
                data = input('Informe a nova Data da consulta')
                for dt in range(len(consultas)):
                    if data == consultas[dt][2]:
                        print('Essa data já está ocupada')
                    else:
                        consultas[c].insert(2, data)
            elif ponteiro == 4:
                del consultas[c][3]
                print('Alterar Hora')
                hora = input('Informe o horário da consulta')
                for hr in range(len(consultas)):
                    if hora == consultas[hr][3]:
                        print('Essa hora já está ocupada')
                    else:
                        consultas[c].insert(3, hora)
            elif ponteiro == 5:
                print('Alterar Diagnóstico')
                del consultas[c][4]
                diagnostico = input('Informe o novo Diagnóstico')
                consultas[c].inser(4, diagnostico)
            elif ponteiro ==6:
                print('Alterar Medicamentos')
                for cs in range(len(consulta1)):
                    print('Medicamentos:', consulta1[cs])
                print('---------------------------')
                remedio = input('Informe o nome do medicamento que deseja alterar:''\n')
                for x in range(len(consulta1)):
                    if remedio == consulta1[x]:
                        del consulta1[x]
                        rm = input('Digite o novo medicamento')
                        consulta1.insert(x, rm)
                        del consultas[c][5:]
                        consultas[c].append(consulta1)
                        print('Alterado Com SUcesso')






        AtualizarArquivoConsulta(consultas)

def ExcluirConsulta():
    consultas = CarregaArquivoConsulta()
    ListarConsultas()
    crm = input('Informe o crm do médico da consulta que deseja apagar:''\n')
    for c in range(len(consultas)):
        if crm == consultas[c][0]:

            print(f'[1] CRM:', consultas[c][0])
            print(f'[2] CPF:', consultas[c][1])
            print(f'[3] Data da consulta', consultas[c][2])
            print(f'[4] Hora da consulta:', consultas[c][3])
            print(f'[5] Diagnóstico:', consultas[c][4])
            consulta1 = consultas[c][4:]
            for i in range(len(consulta1)):
                print('[6] Medicamentos:', consulta1[i])
            print('----------------------------')
        ponteiro = int(input('Deseja excluir essa consulta? Tecle 1 para SIM e 2 para NAO'))
        if ponteiro == 1:
            del consultas[c]
            print('Consulta apagado com sucesso')
        else:
            print('Retornando ao menu')
            return c
    else:
        print('Consulta não encontrada')
    AtualizarArquivoConsulta(consultas)


def RelatorioMedico():
    medicos = CarregaArquivoMedico()
    esp = input('Informe a especialidade para filtrar todos os médicos da lista:''\n')
    while esp != '':
        for c in range(len(medicos)):
            if esp == medicos[c][3]:
                print(f'Código:', medicos[c][0])
                print(f'Nome:', medicos[c][1])
                print(f'Data de Nascimento:', medicos[c][2])
                print(f'Especialidade:', medicos[c][3])
                print(f'Instituição de Formação:', medicos[c][4])
                print(f'E-mail:', medicos[c][5])
                print(f'Telefone:', medicos[c][6])
                print(f'----------------------------')
                return c

            else:
                return False


def RelatorioPaciente():
    pacientes = CarregaArquivoPaciente()
    plano = input('Informe o Plano de Saúde para filtrar a lista de pacientes:''\n')
    for c in range(len(pacientes)):
        if plano == pacientes[c][4]:
            print('Código:', pacientes[c][0])
            print('Nome:', pacientes[c][1])
            print('Data de Nascimento:',pacientes[c][2])
            print('Sexo:', pacientes[c][3])
            print('Plano de Saúde:', pacientes[c][4])
            print('E-mail:', pacientes[c][5])
            print('Telefone:', pacientes[c][6])
            print('---------------------------------------')
            return c
        else:
            'erro'


        
def RelatorioConsulta():
    consultas = CarregaArquivoConsulta()
    data = input('Informe a data para buscar consultas:''\n')
    data1 = input('Informe a segunda data para buscar consultas''\n')
    for consulta in range(len(consultas)):
        if consultas[consulta] != data or data1:
            print('CRM:', consultas[consulta][0])
            print('CPF:', consultas[consulta][1])
            print('Data da consulta:', consultas[consulta][2])
            print('Hora da consulta:', consultas[consulta][3])
            print('Diagnóstico:', consultas[consulta][4])
            consulta1 = consultas[consulta][5:]
            for c in range(len(consulta1)):
                print('Medicamentos:', consulta1[c])
            print('---------------------------------')







#Programa Principal:
print('Bem vindo ao Sistema de Dados do Hospital São Carlos!')
main()
