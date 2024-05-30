# Installation
## Create database (MySQL)
```sql
CREATE DATABASE IF NOT EXISTS `email-microservice` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'email-microservice'@'%' IDENTIFIED BY '<insert_password_here>';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, LOCK TABLES ON `email-microservice`.* TO 'email-microservice'@'%';
```

# Spam Troubleshooting
This project (email-microservice) has no effect on whether sent email ends up in the spam folder or not. You need to troubleshoot your SMTP server settings. Here are some tips what you can do to avoid spam folder:
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
