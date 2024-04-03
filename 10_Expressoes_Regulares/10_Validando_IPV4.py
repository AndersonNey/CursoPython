# 0.0.0.0  -  255.255.255.255       ipv4

# 025.258.963-10


import re

cpf = '025.258.963-10'
cpf_reg_exp = re.compile(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$')
print(cpf_reg_exp.search(cpf))




ip_reg_exp = re.compile(r'''
    ^
    (?:
    25[0-5] | # 250-255
    2[0-4][0-9] | # 200 - 249
    1[0-9]{2}| #100-199
    [1-9][0-9] | # 10-99
    [0-9] # 0-9
   )
    \.
    (?:
    25[0-5] | # 250-255
    2[0-4][0-9] | # 200 - 249
    1[0-9]{2}| #100-199
    [1-9][0-9] | # 10-99
    [0-9] # 0-9
   )
    \.
    (?:
    25[0-5] | # 250-255
    2[0-4][0-9] | # 200 - 249
    1[0-9]{2}| #100-199
    [1-9][0-9] | # 10-99
    [0-9] # 0-9
   )
    \.
    (?:
    25[0-5] | # 250-255
    2[0-4][0-9] | # 200 - 249
    1[0-9]{2}| #100-199
    [1-9][0-9] | # 10-99
    [0-9] # 0-9
   )
   $
''', flags=re.X) #esse flag permite comentar dentro da expressao


for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip , ip_reg_exp.findall(ip))

print('================================================')

#SEGUNDA OPCAO

ip_reg_exp1 = re.compile(r'''
    ^
    (?:
        (?:
            25[0-5] | # 250-255
            2[0-4][0-9] | # 200 - 249
            1[0-9]{2}| #100-199
            [1-9][0-9] | # 10-99
            [0-9] # 0-9
        )
            \.
    ){3}
        (?:
            25[0-5] | # 250-255
            2[0-4][0-9] | # 200 - 249
            1[0-9]{2}| #100-199
            [1-9][0-9] | # 10-99
            [0-9] # 0-9
        )$


''', flags=re.X) #esse flag permite comentar dentro da expressao




for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip , ip_reg_exp1.findall(ip))


print('================================================')

#TERCEIRA OPCAO

ip_reg_exp2 = re.compile(r'''
    ^
    (?:
        (?:
            25[0-5] | # 250-255
            2[0-4][0-9] | # 200 - 249
            1[0-9]{2}| #100-199
            [1-9][0-9] | # 10-99
            [0-9] # 0-9
        )
            \.?     #falando que o ponto é opcional
    ){4}
    \b   #garantindo que termine com espaco e nao com ponto
    $


''', flags=re.X) #esse flag permite comentar dentro da expressao




for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip , ip_reg_exp2.findall(ip))


print('================================================')

#QUARTA OPCAO

ip_reg_exp3 = re.compile(r'^(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]|[0-9])\.?){4}\b$')


for i in range(301):
    ip = f'{i}.{i}.{i}.{i}'
    print(ip , ip_reg_exp3.findall(ip))













