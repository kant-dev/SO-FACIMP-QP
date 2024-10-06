import threading
import time

# Saldo da conta bancária (compartilhado entre os dois processos)
saldo = 1400

def atualizar_saldo(valor):
    """Função para simular a atualização do saldo bancário"""
    global saldo
    saldo_atual = saldo
    time.sleep(1)  # Simula um atraso na operação
    saldo_atual += valor
    saldo = saldo_atual
    print(f'Saldo atualizado: {saldo}')

# Criando duas threads que tentam atualizar o saldo ao mesmo tempo
t1 = threading.Thread(target=atualizar_saldo, args=(500,))
t2 = threading.Thread(target=atualizar_saldo, args=(-200,))
t3 = threading.Thread(target=atualizar_saldo, args=(500,))
t4 = threading.Thread(target=atualizar_saldo, args=(-200,))
t5 = threading.Thread(target=atualizar_saldo, args=(500,))
t6 = threading.Thread(target=atualizar_saldo, args=(500,))
t7 = threading.Thread(target=atualizar_saldo, args=(-200,))
t8 = threading.Thread(target=atualizar_saldo, args=(-800,))



# Iniciando as threads
t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()

# Esperando as threads finalizarem
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()

print(f'Saldo final: {saldo}')
