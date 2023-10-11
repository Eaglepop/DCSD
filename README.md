# Deployment

## 0. Prerequisite
### a. Apache Server
### b. mod_wsgi module

## 1. Clone the repository

## 2. Create virtualenv and install the dependencies:
```
sudo -u http python -m venv .venv
sudo -u http pip install -r requirements.txt
```

## 3. Add the following Virtual Host to Apache config
```
<VirtualHost *:8888>
ServerName your.domain.name

DocumentRoot /path/to/cloned/DCSD

WSGIDaemonProcess DCSD user=http group=http threads=4 python-hame=/path/to/.venv/
WSGIProcessGroup DCSD
WSGIApplicationGroup %{GLOBAL}
WSGIScriptAlias / /path/to/wsgi.py

<Directory /path/to/cloned/DCSD>
  Require all granted
</Directory>
</VirtualHost>
```
