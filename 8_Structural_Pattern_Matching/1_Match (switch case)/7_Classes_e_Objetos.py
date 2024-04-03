

# With objects
# case Food(name='rice') | Food(name='banana'):

from dataclasses import dataclass
from re import X

@dataclass
class Command:
    command: str
    directories: list[str]


def execute_command(command):
    match command:
        case Command(command='ls', directories=[_, *_]):
            for directory in command.directories:
                print('$ listing ALL directories from', directory)
        case Command(command='cd', directories=[_, *_]):
            for directory in command.directories:
                print('$ changing to', directory)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')

x = Command('ls', ['/users'])
y = Command('cd', ['/users'])
execute_command(x)
execute_command(y)





