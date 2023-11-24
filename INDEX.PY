from datetime import datetime
import random

class Usuario:
    def __init__(self, nome, email, cpf, senha):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.senha = senha

    def login(self, senha, email):
        return self.senha == senha and self.email == email

    def excluir_cadastro(self):
        print(f"Excluindo o cadastro do usuário: {self.nome}")

class ProfissionalSaude(Usuario):
    def __init__(self, nome, email, senha, crp, bonus=0.0):
        super().__init__(nome, email, None, senha)
        self.crp = crp
        self.bonus = bonus
        self.consultas_agendadas = []

    def ganhar_bonus_consulta(self, consulta):
        self.bonus += 100.0
        self.consultas_agendadas.append(consulta)

    def __str__(self):
        return f"Profissional de Saúde [nome={self.nome}, crp={self.crp}, bonus={self.bonus}]"

class Consulta:
    def __init__(self, data_hora, descricao, urgente, profissional_saude, paciente=None):
        self.id_consulta = random.randint(1, 1000)
        self.data_hora = data_hora
        self.descricao = descricao
        self.urgente = urgente
        self.realizada = False
        self.paciente = paciente
        self.profissional_saude = profissional_saude
        self.historico_humor = []

    def marcar_realizada(self):
        self.realizada = True
        self.paciente.historico_consultas.append(self)
        for humor in self.historico_humor:
            self.paciente.historico_humor.append(humor)

    def cancelar_consulta(self):
        if not self.realizada:
            print("Consulta cancelada com sucesso!")
            self.paciente.historico_consultas.remove(self)
        else:
            print("Não é possível cancelar uma consulta já realizada.")

    def adicionar_historico_humor(self, humor):
        self.historico_humor.append((datetime.now(), humor))

    def __str__(self):
        return f"Consulta [id_consulta={self.id_consulta}, data_hora={self.data_hora}, descricao={self.descricao}, urgente={self.urgente}, realizada={self.realizada}]"

class Paciente(Usuario):
    def __init__(self, nome, email, senha, cpf):
        super().__init__(nome, email, cpf, senha)
        self.consultas = []
        self.historico_consultas = []
        self.historico_humor = []

    def agendar_consulta(self, consulta):
        humor = input("Como está seu humor hoje? ")
        consulta.adicionar_historico_humor(humor)  # Adiciona o humor ao histórico da consulta
        self.consultas.append(consulta)
        consulta.profissional_saude.ganhar_bonus_consulta(consulta)
        print(f"Consulta agendada para o paciente: {self.nome}")

    def cancelar_consulta(self, paciente, consulta):
        paciente.consultas.remove(consulta)
        print(f"Consulta cancelada pelo paciente: {paciente.nome}")

    def listar_historico_consultas(self):
        print(f"Histórico de consultas realizadas para o paciente {self.nome}:")
        for consulta in self.historico_consultas:
            if consulta.realizada:
                print(f"Consulta realizada em {consulta.data_hora}: {consulta.historico_humor}")

    def listar_historico_humor(self):
        print(f"Histórico de humor do paciente {self.nome}:")
        for humor in self.historico_humor:
            print(f"Data: {humor[0]}, Humor: {humor[1]}")

    def listar_consultas_agendadas(self):
        if not self.consultas:
            print("Nenhuma consulta agendada.")
        else:
            print("Consultas Agendadas:")
            for consulta in self.consultas:
                print(consulta)

    def excluir_cadastro(self):
        print(f"Excluindo o cadastro do paciente: {self.nome}")
        for consulta in self.consultas:
            consulta.cancelar_consulta()
        self.consultas.clear()
        print("Cadastro do paciente excluído com sucesso!")

    def __str__(self):
        return f"Paciente [nome={self.nome}, email={self.email}, cpf={self.cpf}]"

# Listas para armazenar pacientes e profissionais de saúde
pacientes = []
profissionais_saude = []

def menu():
    opcao = 0
    while opcao != 8:
        opcao = int(input(gerar_menu()))
        if 1 <= opcao <= 8:
            if opcao == 1:
                cadastrar()
            elif opcao == 2:
                realizar_login()
            elif opcao == 3:
                exibir_informacoes()
            elif opcao == 4:
                excluir_cadastro()
            elif opcao == 5:
                excluir_todos()
            elif opcao == 6:
                listar_consultas()
            elif opcao == 7:
                agendar_consulta()
        else:
            print("Opção inválida")

def cadastrar():
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")

    tipo_cadastro = int(input("Escolha o tipo de cadastro:\n1. Profissional de Saúde\n2. Paciente\n"))

    if tipo_cadastro == 1:
        print("Cadastrando Profissional de Saúde...")
        crp = input("CRP do Profissional de Saúde (apenas números): ")
        profissional_saude = ProfissionalSaude(nome, email, senha, crp)
        profissionais_saude.append(profissional_saude)
        print("Profissional de Saúde cadastrado com sucesso!")
    elif tipo_cadastro == 2:
        cpf = input("CPF do Paciente (apenas números): ")
        paciente = Paciente(nome, email, senha, cpf)
        pacientes.append(paciente)
        print("Paciente cadastrado com sucesso!")

    print("Usuário cadastrado com sucesso")

def validar_cpf(cpf):
    # Adicione a validação do CPF conforme necessário
    return True

def email_ja_cadastrado(email):
    return any(paciente.email == email or profissional.email == email for paciente in pacientes for profissional in profissionais_saude)

def realizar_login():
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")

    login_profissional_saude = any(profissional.login(senha, email) for profissional in profissionais_saude)
    login_paciente = any(paciente.login(senha, email) for paciente in pacientes)

    if login_profissional_saude or login_paciente:
        print("Login bem-sucedido")
    else:
        print("Email ou senha inválidos. Tente novamente.")

def exibir_informacoes():
    informacoes = ""

    if profissionais_saude:
        informacoes += "Informações do Profissional de Saúde:\n"
        informacoes += str(profissionais_saude[0]) + "\n"
        informacoes += f"Bônus acumulado: R${profissionais_saude[0].bonus}\n"
        informacoes += "Consultas agendadas:\n"
        if profissionais_saude[0].consultas_agendadas:
            informacoes += "\n".join(map(str, profissionais_saude[0].consultas_agendadas)) + "\n"
        else:
            informacoes += "Nenhuma consulta agendada.\n"

    if pacientes:
        informacoes += "\nInformações dos Pacientes:\n"
        informacoes += "\n".join(map(str, pacientes)) + "\n"

    print(informacoes)

def excluir_cadastro():
    email_excluir = input("Digite o email da conta a ser excluída: ")
    senha_excluir = input("Digite a senha da conta a ser excluída: ")

    profissional_saude_excluir = next((profissional for profissional in profissionais_saude if profissional.login(senha_excluir, email_excluir)), None)
    paciente_excluir = next((paciente for paciente in pacientes if paciente.login(senha_excluir, email_excluir)), None)

    if profissional_saude_excluir:
        excluir_cadastro(profissional_saude_excluir)
    elif paciente_excluir:
        excluir_cadastro(paciente_excluir)
    else:
        print("Email ou senha incorretos. Exclusão falhou.")

def excluir_cadastro(usuario):
    confirmacao = input("Deseja realmente excluir a conta? (s/n): ")

    if confirmacao.lower() == "s":
        usuario.excluir_cadastro()
        print("Cadastro excluído com sucesso")

def excluir_todos():
    confirmacao = input("Deseja realmente excluir todas as contas? (s/n): ")

    if confirmacao.lower() == "s":
        global profissionais_saude
        global pacientes
        profissionais_saude = []
        pacientes = []
        print("Todas as contas foram excluídas com sucesso")

def listar_consultas():
    email = input("Digite o email do paciente: ")
    paciente = next((paciente for paciente in pacientes if paciente.email == email), None)

    if paciente:
        paciente.listar_consultas_agendadas()
        paciente.listar_historico_consultas()
        paciente.listar_historico_humor()
    else:
        print("Paciente não encontrado. Tente novamente.")


def agendar_consulta():
    if pacientes and profissionais_saude:
        email_paciente = input("Digite o email do paciente: ")
        paciente = next((p for p in pacientes if p.email == email_paciente), None)

        if paciente:
            nome_profissional = input("Digite o nome do profissional de saúde: ")
            profissional_escolhido = next((p for p in profissionais_saude if p.nome == nome_profissional), None)

            if profissional_escolhido:
                tipo_consulta = input("Escolha o tipo de consulta:\n1. Normal\n2. Urgente: ")
                urgente = tipo_consulta == "2"

                horario_consulta = input("Digite o horário da consulta (formato: yyyy-MM-dd HH:mm): ")
                horario = datetime.strptime(horario_consulta, "%Y-%m-%d %H:%M")

                descricao_consulta = input("Digite uma descrição para a consulta: ")

                consulta = Consulta(horario, descricao_consulta, urgente, profissional_escolhido, paciente)
                paciente.agendar_consulta(consulta)

                # Marcar a consulta como realizada
                consulta.marcar_realizada()

                print("Consulta agendada com sucesso!")
            else:
                print("Profissional de saúde não encontrado. Tente novamente.")
        else:
            print("Paciente não encontrado. Tente novamente.")
    else:
        print("Nenhuma conta cadastrada ou nenhum profissional de saúde disponível. Crie uma conta primeiro.")

def gerar_menu():
    return "Escolha uma opção:\n" + \
           "1. Cadastrar\n" + \
           "2. Realizar login\n" + \
           "3. Exibir informações\n" + \
           "4. Excluir cadastro\n" + \
           "5. Excluir todos os cadastros\n" + \
           "6. Listar consultas\n" + \
           "7. Agendar consulta\n" + \
           "8. Sair"

# Listas para armazenar pacientes e profissionais de saúde
pacientes = []
profissionais_saude = []

# Função principal
menu()
