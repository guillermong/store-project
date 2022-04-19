""""
Este modulo implementa el store
"""

from audioop import avg
from stores.ticket import Ticket,ticket_status

class Store():

    """Manejador de Incidentes 

    uso basico:

        > import Store
        > store = Store()
        > store.incident_status (date_ini,date_fin)
    
    
    """

    def __init__(self):
        self.tickets = { }

    def ticket_add(self,incident="",date_ini=None):
        ticket = Ticket(incident,date_ini)
        self.tickets[ticket.id_ticket]=ticket
        return ticket

    def get_all_tickets(self):
        return self.tickets
    
    def get_ticket(self,id_ticket=""):
        return self.tickets[id_ticket]

    def incident_status(self,date_ini,date_fin):
        
        l = [ t for t in list(self.tickets.values()) if  t.date_ini >= date_ini and t.date_ini <= date_fin ]
        
        open_dif = [ t.get_sla_hours() for t in l if t.status == ticket_status.open]
        open_case = len(open_dif)
        average_solution = 0
        if open_case > 0:
            average_solution = sum(open_dif)/open_case

        closed_cases = sum( t.status == ticket_status.solved  for t in l)

        maximum_solution = max( (t.get_sla_hours()  for t in l),default=0)
    

        return {'open_cases': int(open_case), 
                'closed_cases': int(closed_cases), 
                'average_solution': int(average_solution), 
                'maximum_solution': int(maximum_solution)
                }