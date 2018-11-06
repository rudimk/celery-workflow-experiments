import os
import pickle
import library
from celery import Celery
from workflow.errors import HaltProcessing
from workflow.patterns.controlflow import (FOR, IF_ELSE, CMP)

redisUrl = "redis://" + os.getenv('REDIS_HOST') + ":6379/0"
app = Celery('core', broker=redisUrl)


flow = [library.utils.initializeStore, library.agents.getAgent, library.clock.getCurrentTime, library.logger.logResult]
#workflowDefinition1 = '(lp0\nclibrary.agents\ngetAgent\np1\naclibrary.clock\ngetCurrentTime\np2\naclibrary.logger\nlogResult\np3\na.'

#flow = pickle.loads(flow)

flow = [library.utils.initializeStore, library.agents.getAgent, IF_ELSE(CMP(lambda o, e: o['data']['agent']['sex'], 'Male', '=='), [library.logger.logResult], [library.clock.getCurrentTime]), library.logger.logResult]


@app.task
def runWorkflow(data):
    from workflow.engine import GenericWorkflowEngine
    wfe = GenericWorkflowEngine()
    wfe.setWorkflow(flow)
    wfe.process(data)

if __name__ == "__main__":
    runWorkflow.delay([{"start": True}])