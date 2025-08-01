# Ks_Financial-helper
A financial helper with ML on django with aiogram's interface

Сервис для Django (/etc/systemd/system/django.service):
[Unit]
Description=Django Web Server
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/path/to/project
ExecStart=/path/to/venv/bin/python manage.py runserver 0.0.0.0:8000
Restart=always

[Install]
WantedBy=multi-user.target

Сервис для бота (/etc/systemd/system/bot.service):
[Unit]
Description=Telegram Bot
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/path/to/project
ExecStart=/path/to/venv/bin/python manage.py runbot
Restart=always

[Install]
WantedBy=multi-user.target