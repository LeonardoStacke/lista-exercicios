#Leonardo Leschewitz Stacke

viagens = []
total = 0

while True:
    elevador = input("Digite o elevador utilizado (A, B ou C): ")
    periodo = input("Digite o período atual (M = Matutino, V = Vespertino, N = Noturno): ")


    if elevador in ['A', 'B', 'C'] and periodo in ['M', 'V', 'N']:
        viagens.append({'elevador': elevador, 'periodo': periodo})
    else:
        print("Valores inválidos, tente novamente.")
    total = total + 1


    resposta = input("Continuar registrando? (S/N)")
    if resposta.upper() == 'N':
        break

elevadores = {'A': 0, 'B': 0, 'C': 0}
for viagem in viagens:
    elevadores[viagem['elevador']] += 1
elevador_mais_utilizado = max(elevadores, key=elevadores.get)


periodos = {'M': 0, 'V': 0, 'N': 0}
for viagem in viagens:
    periodos[viagem['periodo']] += 1
periodo_mais_utilizado = max(periodos, key=periodos.get)

periodo_mais_utilizado_de_todos = max(periodos.values())

periodo_menos_utilizado = min(periodos.values())
diferenca_porcentual = (periodo_mais_utilizado_de_todos - periodo_menos_utilizado) * 100 / total

print(f"Elevador mais utilizado: {elevador_mais_utilizado}")
print(f"Período de maior fluxo: {periodo_mais_utilizado}")
print(f"Período mais utilizado de todos: {periodo_mais_utilizado_de_todos}")
print(f"Diferença percentual entre o mais e menos utilizados: {diferenca_porcentual:.2f}%")