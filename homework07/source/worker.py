from jobs import q, update_job_status
import time
import os

@q.worker
def execute_job(jid):
    workerIP = os.environ.get('WORKER_IP')
    update_job_status(jid, 'in progress', workerIP)
    time.sleep(15)
    update_job_status(jid, 'complete', workerIP)

if __name__ == '__main__':
    execute_job()
