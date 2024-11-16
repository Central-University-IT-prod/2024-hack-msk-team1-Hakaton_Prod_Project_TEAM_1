from config import *
from random import choice

class Event:
    
    def __init__(self, id=None, spending=None, date=None, reason=None): # Базовый класс: Event()==None
        self.id = id
        self.spending = spending
        self.date = date
        self.reason = reason

    def fill(self, id): # Заполняет рандомными значениями из файла конфига переменную типа Event: Event().fill()==Заполненный Event
        return Event(id, # FILL RICHARDS
                     choice(SPENDINGS), 
                     choice(DATES), 
                     choice(EVENT_REASONS))
    
    def all(self): # Функция, возвращающая словарь из всех значений Event'a: Event().fill().all()~~{'spendings': 'asdad', 'date': 'qew', 'reason': 'qew'}
        return {"id": self.id,
                "spendings":self.spending,
                "date":self.date,
                "reason":self.reason}