import subprocess

#Windows - ping 127.0.0.1
#Linux - ping 127.0.0.1 -c 4  #  -c para para , porque senao ele continuaria 4 pings

#quando  capture_output = False  printava a resposta mesmo sem pedir e capture_output = True joga dentro da variavel proc
#text = False o stout sai em b''   text = True sai em texto
proc =subprocess.run(['ping','127.0.0.1'], capture_output=True ,text=True)  #uma lista com os argumnetos do comando

print('-----------------------------------------------------------------')
saida = proc.stdout
print(saida)

print('--------------------OUTRAS FUNCOES-------------------------------')
print(proc.stderr)
print(proc.returncode)
print(proc.args)























