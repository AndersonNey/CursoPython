#Tratando exceçoes

#MAIS OU MENOS. ISSO LEMBRANDO QUE TRATA ERROS É IMPORTANTE PORQUE SE DEIXAR OUTROS ERROS PASSAREM NO PROGRAMA EXISTE CHANCES DE QUEBRAR


print('--------------------MANEIRA SIMPLES QUE NAO É UMA BOA PRATICA-----------------------------------')

try:
    print(a)
except:
    pass

print('------------------------------------MANEIRA MELHOR---------------------------------------------')

try:
    print(a)
except NameError as erro:
    print('VISHHHH deu erro',erro)


print('---------------------------------1------------------------------------------------')

try:
    a = []
    print(a[1])
except NameError as erro:
    print('Deu erro,variavel nao declarada')
except IndexError as erro1:
    print('Deu erro,algo falhou')

except Exception as erro:  #se ocorrer qualquer outra exceçao fora o NameError e IndexError (porque ja esta la emcima) ,sera executado esse comando
    print('ocorreu um erro inesperado')



print('---------------------------------2------------------------------------------------')

try:
    b = {}
    print(b[1])
except NameError as erro:
    print('Deu erro,variavel nao declarada')
except IndexError as erro1:
    print('Deu erro,algo falhou')

except Exception as erro2:  
    print('ocorreu um erro inesperado')

print('---------------------------------3------------------------------------------------')


try:
    print(c)
except (IndexError,NameError) as erro1:
    print('Deu erro,algo falhou')

except Exception as erro2:  
    print('ocorreu um erro inesperado')


print('---------------------------------4------------------------------------------------')

try:
    d = 'aviao'
    print(d)
except (IndexError,NameError) as erro1:
    print('Deu erro,algo falhou')

except Exception as erro2:  
    print('ocorreu um erro inesperado')

else:   #Else sempre é executado quando o codigo do bloco try for executado sem dar erro
    print('Ocorreu tudo OK')


print('---------------------------------5------------------------------------------------')

try:
    e = 'aviao'
    print(e)
except (IndexError,NameError) as erro1:
    print('Deu erro,algo falhou')

except Exception as erro2:  
    print('ocorreu um erro inesperado')

else:  
    print('Ocorreu tudo OK')

finally: # é sempre executado independente se deu erro ou nao
    print('ja foi tudo executado')

print('---------------------------------6------------------------------------------------')

try:
    f = 0
    try:
        a = 1/0
    except:
        print('erro de divisao')
        
except (IndexError,NameError) as erro1:
    print('Deu erro,algo falhou')

except Exception as erro2:  
    print('ocorreu um erro inesperado')

else:
    print('ERRROOO')
finally:
    print('ERRROOO')
    
 