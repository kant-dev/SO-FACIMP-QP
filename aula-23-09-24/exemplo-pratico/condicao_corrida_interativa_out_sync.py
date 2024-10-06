import threading
import time

# Saldo do salário inicial do usuário
saldo = float(input("Informe o valor do seu saldo anual: "))
saque_mensal = float(input("Informe o valor do saque mensal: "))

# Mutex para garantir exclusão mútua (evitar condição de corrida)
lock = threading.Lock()

# Contador para rastrear quantas vezes o saldo foi atualizado
contador_atualizacoes = 0

def aplicar_desconto(mes):
    """Função para aplicar o desconto mensal ao salário"""
    global saldo, contador_atualizacoes
    
    # Exclusão mútua: apenas uma thread por vez pode acessar o salário
    with lock:
        saldo_atual = saldo
        time.sleep(1)  # Simula um atraso na operação (pode causar condição de corrida sem o lock)
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
