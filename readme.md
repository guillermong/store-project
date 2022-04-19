# Store

** Store ** es una prueba de store en python

```python
>>> from datetime import datetime,timedelta
>>> from stores.store import Store
>>> s = Store()
>>> ticket = s.ticket_add("prueba")
>>> print(ticket.get_sla_hours())
0.0
>>> print(s.incident_status(datetime.now()-timedelta(days=2),datetime.now()))
{'open_cases': 1, 'closed_cases': 0, 'average_solution': 0, 'maximum_solution': 0}
´´´

## Test Unit

Para ejecutar las pruebas automaticas se debe instalar la libreria pytest

```console
pip install pytest
´´´

y ejecutar en el directorio Store_project
```console
pytest 
´´´
o 
```console
python -m pytest 
´´´