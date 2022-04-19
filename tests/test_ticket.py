import datetime
import pytest
import time
from stores.ticket import Ticket,ticket_status

class TestTicket:

    def test_create_ticket(self):
        i = "the floor in the fruit area is dirty"
        s = Ticket(i)
        assert s.incident == i
        assert s.status == ticket_status.open

    def test_close_ticket(self):
        s = Ticket("prueba solved")
        time.sleep(1)
        s.close_ticket()
        assert s.status == ticket_status.solved
        assert isinstance(s.date_fin,datetime.date)
        assert s.date_ini < s.date_fin