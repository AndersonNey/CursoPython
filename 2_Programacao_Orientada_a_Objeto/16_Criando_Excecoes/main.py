class TaErradoError(Exception):
    pass


def testar():
    raise TaErradoError('Errado!')

try:
    testar()
except TaErradoError as oi:
    print(f'DEU ESSE ERRO --> {oi}')
