# Installation
## Create database (MySQL)
```sql
CREATE DATABASE IF NOT EXISTS `email-microservice` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'email-microservice'@'%' IDENTIFIED BY '<insert_password_here>';
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, REFERENCES, INDEX, ALTER, LOCK TABLES ON `email-microservice`.* TO 'email-microservice'@'%';
```

# Contribution / Development
## Generate requirements.txt (Powershell)
```Powershell
PS C:\projects\email-microservice> .\script\create-pip-requirements.ps1
```

## Generate and apply Alembic migration (Powershell)
```Powershell
PS C:\projects\email-microservice\app\db> $env:PYTHONPATH = 'C:/projects/email-microservice/'
PS C:\projects\email-microservice\app\db> $env:DB_URI = 'mysql://email-microservice:<password>@localhost/email-microservice'
PS C:\projects\email-microservice\app\db> alembic revision --autogenerate -m "<custom message>"
PS C:\projects\email-microservice\app\db> alembic upgrade head
```
