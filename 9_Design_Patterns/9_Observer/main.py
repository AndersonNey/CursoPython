


from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List , Dict

class IObservable(ABC):
    """Observable"""


    @property
    @abstractmethod
    def state(self):pass

    @abstractmethod
    def add_observer(self,observer: IObserver ) -> None: pass

    @abstractmethod
    def remove_observer(self,observer: IObserver ) -> None: pass

    @abstractmethod
    def notify_observers(self) -> None: pass



class WeatherStation(IObservable):
    """Observable"""

    def __init__(self):
        self._observers: List[IObserver] = []
        self._state:Dict = {}

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self,state_update:Dict) -> None:
        new_state:Dict = {**self._state, **state_update}  #desempacotando

        if new_state != self._state:
            self._state = new_state
            self.notify_observers()

    def reset_state(self):
        self._state = {}
        self.notify_observers()

    def add_observer(self,observer: IObserver ) -> None:
        self._observers.append(observer)

    def remove_observer(self,observer: IObserver ) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self._observers:
            observer.update()



class IObserver(ABC):
    @abstractmethod
    def update(self) -> None: pass



class Smartphone(IObserver):
    def __init__(self,name, observable : IObservable) -> None:
        self.name = name
        self.observable = observable

    
    def update(self) -> None:
        observable_name = self.observable.__class__.__name__
        print(f'{self.name} o objeto  {observable_name} acabou de ser aualizado => {self.observable.state}')

class Notebook(IObserver):
    def __init__(self,name, observable : IObservable) -> None:
        self.name = name
        self.observable = observable

    def show(self):
        print('Sou o note e vou fazer outra coisa com esses dados',self.observable.state)        

    def update(self) -> None:
        self.show()


if __name__ == "__main__":
    weather_station = WeatherStation()
    smartphone = Smartphone('iphone',weather_station)
    outro_smartphone = Smartphone('outro_smartphone',weather_station)
    notebook = Notebook('acer',weather_station)

    weather_station.add_observer(smartphone)
    weather_station.add_observer(outro_smartphone)
    weather_station.add_observer(notebook)

    weather_station.state ={'temperature': '30'}
    weather_station.state ={'temperature': '32'}
    weather_station.state ={'humidity':'90'}
    weather_station.state ={}   #nesse caso nao alerta porque nada mudou nom  state
    weather_station.state ={}
    weather_station.state ={}
    weather_station.state ={}
    weather_station.state ={}

    weather_station.remove_observer(outro_smartphone)
    weather_station.reset_state()