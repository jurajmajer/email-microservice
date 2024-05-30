import logging
import os
import random
import string
from datetime import datetime
from pathlib import Path

from jinja2 import Template

log = logging.getLogger()
template_root = os.getenv('TEMPLATE_ROOT')
email_content_root = os.getenv('EMAIL_CONTENT_ROOT')
if template_root is None:
    log.error('Environment variable TEMPLATE_ROOT is not set')
if email_content_root is None:
    log.error('Environment variable EMAIL_CONTENT_ROOT is not set')


def compose_email(template_id, template_params, lang):
    template_path = get_template_path(template_id, lang)
    email_content = None
    with open(template_path) as f:
        template = Template(f.read())
        if template_params is not None:
            email_content = template.render(**template_params)
        else:
            email_content = template.render()
    ret_val = get_email_content_filename(template_id, lang)
    Path(os.path.dirname(ret_val)).mkdir(parents=True, exist_ok=True)
    with open(ret_val, 'w', encoding='utf-8') as f:
        f.write(email_content)
    return ret_val


def get_template_path(template_id, lang):
    return os.path.join(template_root, lang, template_id)


def get_email_content_filename(template_id, lang):
    filename = datetime.now().strftime('%Y%m%d-%H%M%S%f') + '-' + ''.join(random.choices(string.ascii_uppercase +
                                                                                         string.digits, k=6)) + '.txt'
    return os.path.join(email_content_root, lang, template_id, filename)
