# Sistema de Gerenciamento de Consultas Médicas

Este é um sistema simples de gerenciamento de consultas médicas em Python. O sistema permite o cadastro de profissionais de saúde e pacientes, agendamento de consultas, rastreamento de histórico de consultas e histórico de humor do paciente.

## Funcionalidades

- **Cadastro de Usuários:**
  - Profissionais de saúde podem ser cadastrados informando nome, email, senha e CRP (Conselho Regional de Psicologia).
  - Pacientes podem ser cadastrados informando nome, email, senha e CPF.

- **Login:**
  - Usuários podem realizar o login fornecendo seu email e senha.

- **Agendamento de Consultas:**
  - Pacientes podem agendar consultas com profissionais de saúde.
  - O sistema registra o humor do paciente no momento do agendamento.

- **Histórico de Consultas:**
  - O histórico de consultas realizadas é mantido para cada paciente.
  - O histórico inclui a data e hora da consulta, descrição, status (realizada ou não) e histórico de humor.

- **Bônus para Profissionais de Saúde:**
  - Profissionais de saúde acumulam bônus ao realizar consultas.

- **Exclusão de Cadastro:**
  - Usuários podem excluir suas contas, e todas as consultas associadas são canceladas.

- **Listagem de Consultas:**
  - Pacientes podem listar suas consultas agendadas e visualizar o histórico de consultas realizadas.

## Requisitos e Como Executar

1. **Requisitos:**
   - Certifique-se de ter o Python 3.x instalado.

2. **Execução:**
   - Clone o repositório:
     ```bash
     git clone https://github.com/sPaulinSlatt/Projeto-Agendamento-Psicologo.git
     ```
   - Navegue até o diretório do projeto e execute:
     ```bash
     python INDEX.py
     ```



