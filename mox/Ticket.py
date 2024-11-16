from config import *
from random import choice

class Ticket:

    def __init__(self, id=None, spending=None, date_arrive=None, date_comeback=None, race_id=None, home=None, away=None):
        self.id = id
        self.spending = spending
        self.date_arrive = date_arrive
        self.date_comeback = date_comeback
        self.race_id = race_id
        self.home = home
        self.away = away

    def fill(self, id): # FILL RICHARDS
        return Ticket(id, 
                      choice(SPENDINGS), 
                      choice(DATES), 
                      choice(DATES), 
                      choice(TICKET_RACES_ID), 
                      choice(TICKETS), 
                      choice(TICKETS))
    
    def all(self): 
        return {"id": self.id,
            "spending": self.spending,
            "date_arrive": self.date_arrive,
            "date_comeback": self.date_comeback,
            "race_id": self.race_id,
            "home": self.home,
            "away": self.away,
            }