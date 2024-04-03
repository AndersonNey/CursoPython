

import re
from pprint import pprint


texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''


# lookhead e lookbehind NAO RETORNAM NADA

# lookhead verifica o que esta na frente
# lookbehind verifica o que esta atras


pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(\w+)',texto))
# [('192.168.0.1', 'active'),
#  ('192.168.0.2', 'inactive'),
#  ('192.168.0.3', 'active'),
#  ('192.168.0.4', 'active'),
#  ('192.168.0.5', 'inactive'),
#  ('192.168.0.6', 'active')]

# Positive lookahead
print('\n\n\n')

pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)',texto))
# ['192.168.0.1', '192.168.0.3', '192.168.0.4', '192.168.0.6']


# Negative lookahead
print('\n\n\n')

pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)',texto))
# ['192.168.0.2', '192.168.0.5']


#OUTROS EXEMPLOS
print('\n\n\n')

pprint(re.findall(r'(?=.*active).+', texto ))   #um problema que acontece é que a palavra inactive tem dentro a palavra active
# ['ONLINE  192.168.0.1 GHIJK active',
#  'OFFLINE  192.168.0.2 GHIJK inactive',
#  'OFFLINE  192.168.0.3 GHIJK active',
#  'ONLINE  192.168.0.4 GHIJK active',
#  'ONLINE  192.168.0.5 GHIJK inactive',
#  'OFFLINE  192.168.0.6 GHIJK active']

print('\n\n\n')

pprint(re.findall(r'(?=.*[^in]active).+', texto ))   
# ['ONLINE  192.168.0.1 GHIJK active',
#  'OFFLINE  192.168.0.3 GHIJK active',
#  'ONLINE  192.168.0.4 GHIJK active',
#  'OFFLINE  192.168.0.6 GHIJK active']


# Positive lookbehind

print('\n\n\n')

#falando para olhar para tras
pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+',texto))
#['192.168.0.1', '192.168.0.4', '192.168.0.5']

#Negative lookbehind

print('\n\n\n')
#falando para olhar para tras
pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+',texto))
# ['192.168.0.2', '192.168.0.3', '192.168.0.6']



#OUTROS EXEMPLOS
print('\n\n\n')



