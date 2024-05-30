# Installation
## Create database (MySQL)
```sql
CREATE DATABASE IF NOT EXISTS `email-microservice` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'email-microservice'@'%' IDENTIFIED BY '<insert_password_here>';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, LOCK TABLES ON `email-microservice`.* TO 'email-microservice'@'%';
```

## Environment variables which need to be set in runtime
* `TEMPLATE_ROOT` - folder where all templates are stored. No default value, must be set.
* `EMAIL_CONTENT_ROOT` - folder where email-microservice will store output of jinja template transformation. It is the email message body. No default value, must be set.
* `ATTACHMENT_ROOT` - folder where email attachments are stored. No default value, must be set when using attachments.
* `SENDER_ADDRESS` - FROM address of emails. No default value, must be set.
* `SMTP_USERNAME` - username for login to SMTP server. No default value, must be set.
* `SMTP_PASSWORD` - password for login to SMTP server. No default value, must be set.
* `SMTP_SERVER` - URL of SMTP server. No default value, must be set.
* `SMTP_PORT` - SMTP port. Default value: 465

### TEMPLATE_ROOT structure
email-microservice assumes following structure of TEMPLATE_ROOT folder:

```
TEMPLATE_ROOT
│
└───en
│   │
│   └───<templateId1>
│   │      html.jinja2
│   │      plain.jinja2
│   │  
│   └───<templateId2>
|          html.jinja2
|          plain.jinja2
│
└───de
│   │
│   └───<templateId1>
│   │      html.jinja2
│   │  
│   └───<templateId2>
|          html.jinja2
```
Under TEMPLATE_ROOT there is a set of folders named by languages (`en`, `de` etc.). In every language folder there are folders named by template IDs. In every template ID folder there can be one file for html email content named exactly `html.jinja2` and one file for plain text email content named exactly `plain.jinja2`. It is not required to have both `plain.jinja2` and `html.jinja2`. If e.g. `plain.jinja2` is omitted, it will simply not be included in the email.

# Spam Troubleshooting
This project (email-microservice) has no effect on whether sent email ends up in the spam folder or not. You need to troubleshoot your SMTP server settings to avoid spam folder. Here are some tips what you can do:
* Test your emails on [mail-tester.com](https://www.mail-tester.com/)
* Check if Sender Policy Framework (SPF) email authentication is enabled for your domain
* Check if DomainKeys Identified Mail (DKIM) email authentication is enabled for your domain
* Check if Domain-based Message Authentication, Reporting and Conformance (DMARC) email authentication is enabled for your domain

# Contribution / Development
## Generate requirements.txt (Powershell)
Navigate in Powershell to the root folder of project, e.g. `C:\projects\email-microservice` and execute:
```Powershell
.\script\create-pip-requirements.ps1
```

## Generate and apply Alembic migration (Powershell)
Navigate in Powershell to `db` folder of project, e.g. `C:\projects\email-microservice\app\db` and execute:
```Powershell
$env:PYTHONPATH = 'C:/projects/email-microservice/'
$env:DB_URI = 'mysql://email-microservice:<password>@localhost/email-microservice'
alembic revision --autogenerate -m "<custom message>"
alembic upgrade head
```
