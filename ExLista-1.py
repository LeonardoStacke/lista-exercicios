#Leonardo Leschewitz Stacke

sal_minimo = 1320.00

hora_gerente = {
    'M': sal_minimo * 0.15,
    'V': sal_minimo * 0.15,
    'N': sal_minimo * 0.10
}

hora_operario = {
    'M': sal_minimo * 0.14,
    'V': sal_minimo * 0.14,
    'N': sal_minimo * 0.09
}

funcionarios = []

while True:
    nome = input("Nome do funcionário (ou 'encerrar'): ")
    if nome == 'encerrar':
        break

    horas_trabalhadas = input("Horas trabalhadas no mês: ")
    if not horas_trabalhadas.isdigit():
        print("Horas trabalhadas devem ser preenchidas.")
        continue

    turno = input("Turno de trabalho (M = Matutino, V = Vespertino, N = Noturno): ")
    if turno not in ['M', 'V', 'N'] or turno.isdigit():
        print("Turno de trabalho inválido. Use M, V ou N.")
        continue

    categoria = input("Categoria (G = Gerente, O = Operário): ")
    if categoria not in ['G', 'O'] or categoria.isdigit():
        print("Categoria inválida. Use G ou O.")
        continue

    if categoria == 'G':
        valor_hora = hora_gerente[turno]
    else:
        valor_hora = hora_operario[turno]

    salario = int(horas_trabalhadas) * valor_hora

    funcionarios.append({
        'nome': nome,
        'horas_trabalhadas': int(horas_trabalhadas),
        'turno': turno,
        'categoria': categoria,
        'salario': salario
    })

    print(f"Valor da hora trabalhada: R$ {valor_hora:.2f}")
    print(f"{nome} - Salário: R$ {salario:.2f}")


for funcionario in funcionarios:
    print(f"{funcionario['nome']} - Salário: R$ {funcionario['salario']:.2f}")
