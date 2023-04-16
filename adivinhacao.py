from random import randint  # e preciso importar a biblioteca random para gerar valores

numero_str = -1  #inicia a variavel com -1 pra nao ter chance de ser igual ao randint
num_correto = randint(0, 20)  #randint(de,ate) gera numeros aleatorios

while (numero_str != num_correto):
  numero_str = input(
    'Digite um numero entre 0 e 20: \n'
  )  #usuario digita o valor e guarda na variavel num_correto
  num_correto = randint(0, 20)
  
  try:
    numero_float = int(numero_str) #converte numero float para inteiro
    if (numero_float != num_correto):
      print('Tente novamente\n')
     
      if numero_float > num_correto:
        print('Seu numero esta maior que o correto\n')
      else:
        print('O numero digitado e menor que o correto\n')

    elif numero_float == num_correto:
      print('Voce acertou\n')
      break

  except:
    print('Isso não é um número\n')

#while(numero_float != num_correto)
