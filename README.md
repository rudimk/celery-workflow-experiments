# celery-workflow-experiments
A repo containing some experiments for running workflows on Celery.

## Instructions

To run the Celery worker, navigate to `engine/` and run `REDIS_HOST=localhost celery -A core worker --loglevel=info`. 

To run the Flower dashboard for inspecting Celery, run `REDIS_HOST=localhost flower -A core --port=5555`.

Finally, define workflows in `engine/core.py` and then run `REDIS_HOST=localhost python core.py`.

