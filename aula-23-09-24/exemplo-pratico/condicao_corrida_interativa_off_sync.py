import threading  # Importa o módulo threading para criar e controlar threads
import time       # Importa o módulo time para simular atrasos com sleep()

# Solicita ao usuário o saldo anual inicial e o valor do saque mensal
saldo = float(input("Informe o valor do seu Saldo Anual: "))
saque_mensal = float(input("Informe o valor do Saque Mensal: "))

# Contador que rastreia quantas vezes o saldo foi atualizado
contador_atualizacoes = 0

def aplicar_desconto(mes):
    """Função que aplica o desconto mensal ao saldo global"""
    global saldo, contador_atualizacoes  # Permite modificar as variáveis globais saldo e contador

    # Captura o saldo atual antes de aplicar o desconto
    saldo_atual = saldo

    # Simula um atraso na operação para demonstrar uma potencial condição de corrida
    time.sleep(1)

    # Subtrai o valor do saque mensal do saldo atual
    saldo_atual -= saque_mensal

    # Atualiza o saldo global com o novo valor
    saldo = saldo_atual

    # Incrementa o contador que rastreia o número de atualizações e exibe a mensagem
    contador_atualizacoes += 1
    print(f'{contador_atualizacoes}ª atualização (Mês {mes}): Saldo atualizado para {saldo:.2f}')

# Cria uma lista de threads, uma para cada mês (total de 12 meses)
# Cada thread executará a função aplicar_desconto para um mês específico
threads = [threading.Thread(target=aplicar_desconto, args=(mes,)) for mes in range(1, 13)]

# Inicia todas as threads. Cada thread começará a aplicar o desconto de forma concorrente.
for t in threads:
    t.start()

# Espera todas as threads terminarem antes de prosseguir e garante que as threads sejam executadas
for t in threads:
    t.join()

# Exibe o saldo final após os 12 meses de saques
print(' ')
print(f'Saldo final após 12 meses: {saldo:.2f}')
