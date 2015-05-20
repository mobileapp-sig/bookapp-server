# bookapp-server
server for bookapp

# Install

* with python 2.7 or later
```
$ virtualenv env
$ . env/bin/activate
(env) $ pip install django
(env) $ pip install uwsgi
(env) $ pip install mysqlclient 
(env) $ pip install djangorestframework
(env) $ pip install django-rest-framework-social-oauth2
```

* clone repository 
```
(env) $ git clone https://github.com/mobileapp-sig/bookapp-server.git
(env) $ cd bookapp-server
```

* execute mysql as root
```
mysql> CREATE DATABASE bookapp CHARACTER SET utf8; 
mysql> CREATE USER 'bookapp_admin'@'localhost' IDENTIFIED BY 'somepassword!';
mysql> GRANT ALL ON bookapp.* TO 'bookapp_admin'@'localhost';
```

* edit password in my.cnf 
```
password = YOURPASSWORD 
```

* initialize django environment
```
(env) $ python manage.py migrate
(env) $ python manage.py createsuperuser
```

* edit paths in uwsig.ini 

* start uwsgi daemon with uwsgi.ini

* edit nginx.conf and start nginx
```
upstream django-bookapp {
    server unix://UWSGI_SOCKET_PATH;
}

server {
    ...

    location / {
        uwsgi_pass  django-bookapp;
        include     BOOKSERVER_HOME/uwsgi_params;
    }

    location /static {
        alias BOOKSERVER_HOME/static;
    }

    ...
}
```

Reference
https://github.com/PhilipGarnero/django-rest-framework-social-oauth2
