# Installation
## Create database (MySQL)
```sql
CREATE DATABASE IF NOT EXISTS `email-microservice` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'email-microservice'@'%' IDENTIFIED BY '<insert_password_here>';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, LOCK TABLES ON `email-microservice`.* TO 'email-microservice'@'%';
```

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
