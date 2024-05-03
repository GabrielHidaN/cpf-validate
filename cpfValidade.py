
while True:

  cpf_digitado = input('Digite o CPF que deseja Verificar: (sem pontos. ex:   53819436014)\n')
  try:
     cpf_digitado = int(cpf_digitado)
  except ValueError:
     print('Digite um Valor valido. ( Modelo de CPF: 53819436014) \n')
