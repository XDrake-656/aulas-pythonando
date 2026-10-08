salario = float(input("Quanto você recebe por hora: R$"))
hora = float(input("Quantas horas voce Trbalhou esse mes: "))
ganho_mes = (hora * salario) // 1
imposto = ganho_mes * 11 / 100
inss = ganho_mes * 8 / 100
sindicato = ganho_mes * 5 / 100
final = ganho_mes - imposto - inss - sindicato
print(f"Salario bruto: {int(ganho_mes)}")
print(f"INSS: {int(inss)}")
print(f"SINDICATO: {int(sindicato)}")
print(f"Salario liquido: {int(final)}")
