from datetime import datetime
from uuid import uuid4

format_data = "%d/%m/%y %H:%M:%S"

class Ticket():
    
    def __init__(self,incident = "",date_ini=None):
        self.id_ticket = str(uuid4())
        self.incident = incident
        self.date_ini = datetime.now() if date_ini is None else date_ini
        self.date_fin = None
        self.status = ticket_status.open

    def close_ticket(self):
        self.date_fin = datetime.now()
        self.status = ticket_status.solved
    
    def get_sla_hours(self):
        t_fin = self.date_fin
        if self.date_fin is None:
            t_fin = datetime.now()
        return (t_fin-self.date_ini).total_seconds()/(60*60) 

def validate(date_time):
    try:
        return datetime.strptime(date_time,format_data)  
    except ValueError:
        raise ValueError("formato incorrecto")

class ticket_status:
    open = 1
    solved = 2