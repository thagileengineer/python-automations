import schedule
import time
from datetime import datetime

def job():
    print(f"Running job at {datetime.now()}")


schedule.every(10).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
