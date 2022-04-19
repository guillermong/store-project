import pytest
from datetime import datetime,timedelta
from stores.store import Store
from stores.ticket import Ticket,ticket_status

class TestStore():
    @pytest.fixture(autouse=True)
    def setup(self):
        self.s = Store()

    @pytest.fixture()
    def carga_data(self):
        self.s.ticket_add("prueba")
        self.s.ticket_add("prueba1",datetime.now()-timedelta(hours=4))
        ticket = self.s.ticket_add("prueba2",datetime.now()-timedelta(days=1))
        ticket.close_ticket()
    
    @pytest.fixture()
    def auto_carga(self):
        for i in range(100):
            self.s.ticket_add("prueba"+str(i),datetime.now()-timedelta(hours=i+1))
        for item in list(self.s.get_all_tickets().values())[::2]:
            item.close_ticket()
            
    def test_incident_list(self):
        self.s.ticket_add("prueba")
        assert len(self.s.get_all_tickets())==1

    def test_empty_store_incident_status(self):
        r=self.s.incident_status(datetime.now(),datetime.now())
        assert r =={'average_solution': 0, 'closed_cases': 0, 'maximum_solution': 0, 'open_cases': 0}

    def test_inverse_date_incident_status(self):
        r=self.s.incident_status(datetime.now(),datetime.now()-timedelta(days=2))
        assert r == {'average_solution': 0, 'closed_cases': 0, 'maximum_solution': 0, 'open_cases': 0}
        
    def test_open_incident_status(self):
        ticket = self.s.ticket_add("prueba")
        ticket = self.s.ticket_add("prueba1",datetime.now()-timedelta(hours=1))
        ticket = self.s.ticket_add("prueba2",datetime.now()-timedelta(days=1))
        r=self.s.incident_status(datetime.now()-timedelta(days=2),datetime.now())
        assert r == {'average_solution': 8, 'closed_cases': 0, 'maximum_solution': 24, 'open_cases': 3}

    def test_close_incident_status(self,carga_data):
        r=self.s.incident_status(datetime.now()-timedelta(days=2),datetime.now())
        assert r=={'average_solution': 2, 'closed_cases': 1, 'maximum_solution': 24, 'open_cases': 2}
    
    def test__out_rangeincident_status(self,carga_data):
        r=self.s.incident_status(datetime.now()-timedelta(hours=2),datetime.now())
        assert r== {'average_solution': 0, 'closed_cases': 0, 'maximum_solution': 0, 'open_cases': 1}

        r=self.s.incident_status(datetime.now()-timedelta(hours=5),datetime.now())
        assert r=={'average_solution': 2, 'closed_cases': 0, 'maximum_solution': 4, 'open_cases': 2}
    
    def test_incident_status_100(self,auto_carga):
        r=self.s.incident_status(datetime.now()-timedelta(hours=87),datetime.now()-timedelta(hours=33))
        print(r)
        assert r== {'open_cases': 27, 'closed_cases': 27, 'average_solution': 60, 'maximum_solution': 86}