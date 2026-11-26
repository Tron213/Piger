from fastapi import FastAPI, Depends
from schemas import MonitorCreate
from sqlalchemy.orm import Session
from database import get_db
from models import Monitor

app = FastAPI()

@app.post('/monitors', status_code=201)
def create_monitors(monitor: MonitorCreate, db: Session = Depends(get_db)):
    new_monitor = Monitor(host=str(monitor.ip), enabled=True)
    db.add(new_monitor)
    db.commit()
    db.refresh(new_monitor)

    return {'uuid': new_monitor.uuid,
        'ip': new_monitor.host, 
            'enabled': new_monitor.enabled}