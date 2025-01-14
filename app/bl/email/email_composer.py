import logging
import os
import random
import string
from datetime import datetime
from pathlib import Path

from jinja2 import Template

from app.bl import util

log = logging.getLogger(__name__)
template_root = util.read_env_var('TEMPLATE_ROOT')
email_content_root = util.read_env_var('EMAIL_CONTENT_ROOT')


def compose_email(template_id, template_params, lang):
    template_folder = get_template_folder(template_id, lang)
    output_filename = get_output_filename(template_id, lang)
    Path(os.path.dirname(output_filename)).mkdir(parents=True, exist_ok=True)
    ret_val = [None, None]

    plain_content = transform_template(os.path.join(template_folder, 'plain.jinja2'),
                                       template_params)
    if plain_content is not None:
        ret_val[0] = output_filename + '.plain'
        with open(ret_val[0], 'w', encoding='utf-8') as f:
            f.write(plain_content)
    html_content = transform_template(os.path.join(template_folder, 'html.jinja2'),
                                      template_params)
    if html_content is not None:
        ret_val[1] = output_filename + '.html'
        with open(ret_val[1], 'w', encoding='utf-8') as f:
            f.write(html_content)

    return ret_val


def transform_template(template_file, template_params):
    if not os.path.isfile(template_file):
        return None
    with open(template_file, encoding='utf-8') as f:
        template = Template(f.read())
        if template_params is not None:
            return template.render(**template_params)
        return template.render()


def get_template_folder(template_id, lang):
    return os.path.join(template_root, lang, template_id)


def get_output_filename(template_id, lang):
    filename = datetime.now().strftime('%Y%m%d-%H%M%S%f') + \
               '-' + ''.join(random.choices(string.ascii_uppercase +
                                            string.digits, k=6))
    return os.path.join(email_content_root, lang, template_id, filename)
