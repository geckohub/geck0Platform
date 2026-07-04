from datetime import datetime
from services.scheduler.app import due
def test_due_once():
 now=datetime(2026,7,2,2,0);job={"id":"x","weekday":3,"hour":2,"minute":0};assert due(job,now,{});assert not due(job,now,{"x":"2026-07-02-02-00"})
