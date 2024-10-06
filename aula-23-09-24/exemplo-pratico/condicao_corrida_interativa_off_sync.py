import threading
import time

# Saldo do salário inicial do usuário
saldo = float(input("Informe o valor do seu Saldo Anual: "))
saque_mensal = float(input("Informe o valor do Saque Mensal: "))

# Contador para rastrear quantas vezes o saldo foi atualizado
contador_atualizacoes = 0

def aplicar_desconto(mes):
    """Função para aplicar o desconto mensal ao salário"""
    global saldo, contador_atualizacoes

    # Captura o salário atual e aplica o desconto
    saldo_atual = saldo
    time.sleep(1)  # Simula um atraso na operação (potencial condição de corrida)
    saldo_atual -= saque_mensal
    saldo = saldo_atual

    # Incrementa o contador e exibe a atualização
    contador_atualizacoes += 1
    print(f'{contador_atualizacoes}ª atualização (Mês {mes}): Saldo atualizado para {saldo:.2f}')

# Criando uma thread para cada mês (12 meses no total)
threads = [threading.Thread(target=aplicar_desconto, args=(mes,)) for mes in range(1, 13)]

# Iniciando todas as threads
for t in threads:
    t.start()

# Esperando todas as threads finalizarem
for t in threads:
    t.join()

print(f'Saldo final após 12 meses: {saldo:.2f}')
