
from __future__ import annotations
from abc import ABC , abstractmethod
from typing import Dict, List , Tuple

class Light:
    """Receiver - Luz Inteligente"""

    def __init__(self, name: str , room_name: str) -> None:
        self.name = name
        self.room_name = room_name
        self.color = 'Default color'

    def on(self) -> None:
        print(f'{self.name} no {self.room_name} esta ON')

    def off(self) -> None:
        print(f'{self.name} no {self.room_name} esta OFF')

    def change_color(self,color:str) -> None:
        self.color = color
        print(f'{self.name} no {self.room_name} esta {self.color}')


class ICommand(ABC):
    """Interface de comando - Luz Inteligente"""

    @abstractmethod
    def execute(self) -> None:pass

    @abstractmethod
    def undo(self) -> None:pass


class LightOnCommmand(ICommand):
    """Comando Concreto"""

    def __init__(self,light:Light) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()

class LightChangeColor(ICommand):
    """Comando Concreto"""

    def __init__(self,light:Light , color:str) -> None:
        self.light = light
        self.color = color
        self._old_color = self.light.color

    def execute(self) -> None:
        self._old_color = self.light.color
        self.light.change_color(self.color)

    def undo(self) -> None:
        self.light.change_color(self._old_color)




class RemoteController:
    """Invoker"""
    def __init__(self) -> None:
        self._buttons: Dict[str,ICommand] = {}
        #Listas de coisas que eu quero desfazer  
        self._undos:List[Tuple[str,str]] = []

    def button_add_command(self, name:str , command: ICommand) -> None:
        self._buttons[name] = command

    def button_pressed(self,name:str)->None:
        if name in self._buttons:
            self._buttons[name].execute()
            self._undos.append((name,'execute'))

    def button_undo(self, name:str) -> None:
        if name in self._buttons:
            self._buttons[name].undo()
            self._undos.append((name,'undo'))

    def global_undo(self):
        if not self._undos:
            print('Nothing to undo')
            return None
        
        button_name , action = self._undos[-1]

        if action == 'execute':
            self._buttons[button_name].undo()
        else:
            self._buttons[button_name].execute()

        self._undos.pop()

if __name__ == "__main__":
    bedroom_light = Light('Luz do quarto', 'Quarto')   
    bathroom_light = Light('Luz do banheiro', 'Banheiro')   

    bedroom_light_on =  LightOnCommmand(bedroom_light)
    bathroom_light_on = LightOnCommmand(bathroom_light)
    bedroom_light_blue = LightChangeColor(bedroom_light,'blue')
    bedroom_light_red = LightChangeColor(bedroom_light,'red')

    remote = RemoteController()
    remote.button_add_command('first_button',bedroom_light_on)
    remote.button_add_command('secound_button',bathroom_light_on)
    remote.button_add_command('third_button',bedroom_light_blue)
    remote.button_add_command('fourth_button',bedroom_light_red)


    remote.button_pressed('first_button')
    remote.button_undo('first_button')


    remote.button_pressed('secound_button')
    remote.button_undo('secound_button')


    remote.button_pressed('third_button')
    #remote.button_undo('third_button')


    remote.button_pressed('fourth_button')
    remote.button_undo('fourth_button')

    print()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()
    remote.global_undo()