import os
import library
from celery import Celery

redisUrl = "redis://" + os.getenv('REDIS_HOST') + ":6379/0"
app = Celery('workflow_sample', broker=redisUrl)

flow = [library.agents.getAgent, library.clock.getCurentTime]


@app.task
def runWorkflow(data):
    from workflow.engine import GenericWorkflowEngine
    wfe = GenericWorkflowEngine()
    wfe.setWorkflow(flow)
    wfe.process(data)
