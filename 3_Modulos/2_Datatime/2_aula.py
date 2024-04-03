#https://docs.python.org/3/library/calendar.html


from datetime import datetime
from locale import setlocale, LC_ALL   #localizacao

from calendar import mdays    ##quantos dias tem cada mes

setlocale(LC_ALL, '') #vai usar o local padrao do computador
# se eu quisesse enviar a localizacao explicitamente e o formato do arqivo(eu acho)      setlocale(LC_ALL, 'pt_BR.utf-8')

#sexta , 13 de junho de 2018   para exibir uma data dessa maneira assim nao da sem precisar importa outro modulo

print('------------------EXEMPLO 1---------------------------')
#formatacao portugues

dt = datetime.now()
formatacao1 = dt.strftime('%A,%d de %B de %Y')
formatacao2 = dt.strftime('%d/%m/%Y %H:%M:%S')

print(formatacao1)
print(formatacao2)

print('------------------EXEMPLO 2---------------------------')
#!!!!!!!!!!!!!!!!!!!!!NAO FUNCIONA EM ANO BISSEXTO!!!!!!!!!!!!!!!!!!!
#ultimo dia do mes

#o indice 0 nao tem valor porque nao existe mes 0
print(mdays)

dt1 = datetime.now()
mes_atual = int(dt1.strftime('%m'))

print(mes_atual,mdays[mes_atual])  #pegando o ultimo dia do mes ,mas é na gambiarra perfeita , ja que mdays conta quantos dias tem o mes



print('------------------EXEMPLO 3-----PROFESSOR-------------')

# Na aula anterior, você viu como utilizar mdays de calendar 
# (que pega a quantidade de dias do mês) para pegar o último 
# dia do mês. Isso pode não funcionar como esperado em ano bissexto.

# Você também pode utilizar a função monthrange de calendar para 
# pegar o número do dia na semana (entre 0-6) e último dia do mês 
# (entre 28-31), exemplo:

#-------------------------------------------------------------------------
from calendar import monthrange
 
# Retorna uma tupla contendo o número do dia na semana (0-6)
# e último dia de fevereiro de 2020
print(monthrange(2020, 2))
 
# Saída - (5, 29)
# O 5 significa que é um sábado
# O 29 significa que este é o último dia do mês
#-------------------------------------------------------------------------

# O número do dia na semana vai de 0 a 6 (segunda é 0, domingo é 6).
# Caso queira retornar apenas um valor, você pode fazer o desempacotamento, assim:



#-------------------------------------------------------------------------
from calendar import monthrange
dia_semana, ultimo_dia = monthrange(2020, 2)
print(ultimo_dia)  # Saída: 29 (último dia de fevereiro de 2020)

#-------------------------------------------------------------------------
# Você também pode criar uma lista, assim como mdays, contendo todos os últimos dias de meses do ano atual:

#-------------------------------------------------------------------------

from datetime import datetime
from calendar import monthrange
 
ultimos_dias_de_meses_do_ano_atual = [
    monthrange(datetime.now().year, mes)[1] for mes in range(1, 13)
]
print(ultimos_dias_de_meses_do_ano_atual)
# Saída: [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Observação: meu ano atual é 2020 neste momento
#-------------------------------------------------------------------------
# Isso deve solucionar os problemas do ano bissexto.











