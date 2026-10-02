salario = float(input("Quanto você recebe por hora: R$"))
hora = float(input("Quantas horas voce Trbalhou esse mes: "))
ganho_mes = (hora * salario) // 1
imposto = ganho_mes * 11 / 100
inss = ganho_mes * 8 / 100
sindicato = ganho_mes * 5 / 100
final = ganho_mes - imposto - inss - sindicato
print(f"Esse mes voce teve um ganho bruto de R${ganho_mes:.0f}\nVocê deve oa inss R${inss:.0f}\nao sindicato R${sindicato:.0f}\nsalario liquido = R${final:.0f}")
