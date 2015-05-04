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

...

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
