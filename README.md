# Email Microservice
[![Build Docker Image](https://github.com/jurajmajer/email-microservice/actions/workflows/build-docker-image.yml/badge.svg)](https://github.com/jurajmajer/email-microservice/actions/workflows/build-docker-image.yml)
![pylint Score](https://mperlet.github.io/pybadge/badges/9.74.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/jurajmajer/email-microservice/blob/main/LICENSE)

## Installation on Kubernetes
1. Create database on your DB server. We use MySQL.
```sql
CREATE DATABASE IF NOT EXISTS `email-microservice` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'email-microservice'@'%' IDENTIFIED BY '<insert_password_here>';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, LOCK TABLES ON `email-microservice`.* TO 'email-microservice'@'%';
```
2. Create schema in the database ideally using Alembic migration. If it is not possible, you can use sql script `script/initdb.sql`
3. Review deployment scripts for Kubernetes in folder `infra/k8s`. At minimum you have to modify `1-init.yaml` and set secret values (replace `<define-this>` with actual value).
4. Apply kubernetes scripts:
```
kubectl apply -f infra/k8s/1-init.yaml
kubectl apply -f infra/k8s/2-define-storage.yaml
kubectl apply -f infra/k8s/3-deployment.yaml
```
5. Save your email templates to TEMPLATE_ROOT. See details about TEMPLATE_ROOT structure below.

### Environment variables which need to be set in runtime
* `TEMPLATE_ROOT` - folder where all templates are stored. No default value, must be set.
* `EMAIL_CONTENT_ROOT` - folder where email-microservice will store output of jinja template transformation. It is the email message body. No default value, must be set.
* `ATTACHMENT_ROOT` - folder where email attachments are stored. No default value, must be set when using attachments.
* `SENDER_ADDRESS` - FROM address of emails. No default value, must be set.
* `SENDER_NAME` - FROM name of emails. No default value, optional.
* `SMTP_USERNAME` - username for login to SMTP server. No default value, must be set.
* `SMTP_PASSWORD` - password for login to SMTP server. No default value, must be set.
* `SMTP_SERVER` - URL of SMTP server. No default value, must be set.
* `SMTP_PORT` - SMTP port. Default value: 465
* `DB_URI` - Database connection string. No default value, must be set. E.g.: mysql://email-microservice:<password>@<db-server>/email-microservice

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

## Usage
Other pods should use OpenAPI interface of email-microservice for sending emails. OpenAPI interface does not require any authentication. It is assumed email-microservice is accessible only within the cluster. Swagger documentation is available after installation under [http://\<email-microservice\>/docs](http://email-microservice/docs). Alternatively, you can check out the swagger UI [here](https://jurajmajer.github.io/email-microservice/openapi/).

## Spam Troubleshooting
This project (email-microservice) has no effect on whether sent email ends up in the spam folder or not. You need to troubleshoot your SMTP server settings to avoid spam folder. Here are some tips what you can do:
* Test your emails on [mail-tester.com](https://www.mail-tester.com/)
* Check if Sender Policy Framework (SPF) email authentication is enabled for your domain
* Check if DomainKeys Identified Mail (DKIM) email authentication is enabled for your domain
* Check if Domain-based Message Authentication, Reporting and Conformance (DMARC) email authentication is enabled for your domain

## Contribution / Development
### Generate requirements.txt (Powershell)
Navigate in Powershell to the root folder of project, e.g. `C:\projects\email-microservice` and execute:
```Powershell
.\script\create-pip-requirements.ps1
```

### Generate and apply Alembic migration (Powershell)
Navigate in Powershell to `db` folder of project, e.g. `C:\projects\email-microservice\app\db` and execute:
```Powershell
$env:PYTHONPATH = 'C:/projects/email-microservice/'
$env:DB_URI = 'mysql://email-microservice:<password>@localhost/email-microservice'
alembic revision --autogenerate -m "<custom message>"
alembic upgrade head
```
