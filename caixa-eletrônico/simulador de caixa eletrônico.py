valor_saque = int(input('Insira o valor do saque: '))
total = valor_saque
cedula = 100
total_cedulas = 0

while True:
  if total >= cedula:
    total -= cedula
    total_cedulas += 1
  else:
    if total_cedulas > 0:
      print(f'Total de {total_cedulas} notas de {cedula}')
    if cedula == 100:
      cedula = 50
    elif cedula == 50:
      cedula = 20
    elif cedula == 20:
      cedula = 10
    elif cedula == 10:
      cedula = 5
    elif cedula == 5:
      cedula = 1
    total_cedulas = 0
    if total == 0:
      break
print('Programa Encerrado')

