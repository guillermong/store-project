from datetime import datetime,timedelta
from stores.store import Store
from stores.ticket import Ticket,ticket_status

s = Store()
ticket = s.ticket_add("prueba")
print(ticket.get_sla_hours())
print(s.incident_status(datetime.now()-timedelta(days=2),datetime.now()))