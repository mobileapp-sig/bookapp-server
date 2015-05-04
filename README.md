# bookapp-server
server for bookapp

# Install

* with python 2.7 or later
```
$ git clone https://github.com/mobileapp-sig/bookapp-server.git
$ cd bookapp-server
$ virtualenv env
$ . env/bin/activate
(env) $ pip install django
(env) $ pip install uwsgi
(env) $ pip install mysqlclient 
```
* clone repository 

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
