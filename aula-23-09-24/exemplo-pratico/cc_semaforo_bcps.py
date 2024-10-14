import threading
import time

# Saldo do usuário
saldo = float(input("Informe o valor do seu saldo anual: "))
saque_mensal = float(input("Informe o valor do saque mensal: "))

# Semáforo para controlar o acesso ao saldo
semaforo = threading.Semaphore(value=1)

# Contador para rastrear quantas vezes o saldo foi atualizado
contador_atualizacoes = 0

def aplicar_saque(mes):
    """Função para aplicar o saque mensal ao saldo"""
    global saldo, contador_atualizacoes

    # Tentando adquirir o semáforo
    semaforo.acquire()  # Se não estiver disponível, a thread vai esperar

    try:
        # Acesso ao saldo
        saldo_atual = saldo
        time.sleep(1)  # Simula um atraso na operação
        saldo_atual -= saque_mensal
        saldo = saldo_atual

        # Incrementa o contador e exibe a atualização
        contador_atualizacoes += 1
        print(f'{contador_atualizacoes}ª atualização (Mês {mes}): Saldo atualizado para {saldo:.2f}')
    
    finally:
        # Libera o semáforo
        semaforo.release()

# Criando uma thread para cada mês (12 meses no total)
threads = [threading.Thread(target=aplicar_saque, args=(mes,)) for mes in range(1, 13)]

# Iniciando todas as threads
for t in threads:
    t.start()

# Esperando todas as threads finalizarem
for t in threads:
    t.join()

print(' ')
print(f'Saldo final após 12 meses: {saldo:.2f}')
