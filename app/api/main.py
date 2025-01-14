import logging
import os

import yaml
from fastapi import FastAPI, Response, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from starlette.status import HTTP_204_NO_CONTENT

from app.api.controller import controller
from app.api.controller.schemas import SendEmailItem
from app.bl import orchestrator

app = FastAPI(
    title='Email Microservice API',
    description='Email Microservice API',
    version='0.0.1',
    servers=[
        {'url': 'http://localhost:8000', 'description': 'Development server'},
    ],
)

# Configure logging
log_config_file = 'app/log_conf.yaml'
if os.path.isfile(log_config_file):
    with open(log_config_file, 'rt') as f:
        config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
logger = logging.getLogger(__name__)
logger.info('Starting API...')


@app.post('/sendEmail',
          status_code=HTTP_204_NO_CONTENT,
          responses={'204': {'description': 'Email scheduled for sending'},
                     '500': {'description': 'Internal server error'}},
          tags=['Email Sending'])
def send_message(
        body: SendEmailItem,
        background_tasks: BackgroundTasks,
        db: Session = Depends(controller.get_db),
) -> Response:
    controller.schedule_email(body, db)
    background_tasks.add_task(orchestrator.orchestrate, db)
    return Response(status_code=HTTP_204_NO_CONTENT)
