# jobs.py

import uuid
from hotqueue import HotQueue
import redis
from redis import StrictRedis

q = HotQueue("queue", host='10.109.68.104', port=6379, db=1)
rd = redis.StrictRedis(host='10.109.68.104', port=6379, db=0)

def _generate_jid():
    return str(uuid.uuid4())

def _generate_job_key(jid):
    return 'job.{}'.format(jid)

def _instantiate_job(jid, status, start, end, workerip='None'):
    if type(jid) == str:
        if status=='in progress':  # if it has been taken by a worker, list the worker in the db
            rd.hset(_generate_job_key(jid),'worker', workerip)
        return {'id': jid,
                'status': status,
                'start': start,
                'end': end
        }
    return {'id': jid.decode('utf-8'),
            'status': status.decode('utf-8'),
            'start': start.decode('utf-8'),
            'end': end.decode('utf-8')
    }

def _save_job(job_key, job_dict):
    """Save a job object in the Redis database."""
    rd.hmset(job_key, job_dict)

def _queue_job(jid):
    """Add a job to the redis queue."""
    q.put(jid)

def add_job(start, end, status="submitted"):
    """Add a job to the redis queue."""
    jid = _generate_jid()
    job_dict = _instantiate_job(jid, status, start, end)
    # update call to save_job:
    _save_job(_generate_job_key(jid), job_dict)
    # update call to queue_job:
    _queue_job(jid)
    return job_dict

def update_job_status(jid, newstatus, workerIP):
    """Update the status of job with job id `jid` to status `status`."""
    jid, status, start, end = rd.hmget(_generate_job_key(jid), 'id', 'status', 'start', 'end')
    job = _instantiate_job(jid, status, start, end, workerIP)
    if job:
        job['status'] = newstatus
        _save_job(_generate_job_key(jid), job)
    else:
        raise Exception()

