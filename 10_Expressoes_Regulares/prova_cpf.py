import re

exemplo1 = '''
123.456.787-78
458.995.455-54
789.584.958-45
'''



cpf = re.findall(r'^[0-9]{3}\.[0-9]{3}\.[0-9]{3}\-[0-9]{2}$',exemplo1,flags=re.M)
cpf1 = re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}',exemplo1,flags=re.M)
cpf2 = re.findall(r'^(?:\d{3}\.){2}\d{3}\-\d{2}',exemplo1,flags=re.M)
print(cpf2)








