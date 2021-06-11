1-#Install Python First (download and install it on PC)
2-#Install & Create Virtual Environment for Django project
pip install virtualenv

#create virtualenv
virtualenv -p python3 envBlog [or] py -m venv envBlog

#Active virtualenv
envBlog\Scripts\activate.bat 
or
D:\vs_code\Django2021\Blog>envBlog\Scripts\activate.bat
 [A] Yes to All
 A
 
#if not create or Active Virtualenv then run this command[Set-ExecutionPolicy unrestricted] on Windows PowerShell
PS C:\WINDOWS\system32> Set-ExecutionPolicy unrestricted

#Install Django
py -m pip install Django

#Create Django project
django-admin startproject website

#Run Django project
python manage.py runserver

[The install worked successfully! Congratulations!]

#create Django App (Blog)
$ cd website
python manage.py startapp Blog

#Create Table and database 
$ python manage.py makemigrations
$ python manage.py migrate

#Create Super User (admin user)
$python manage.py createsuperuser
{   Username (leave blank to use 'lenovo'): admin1
    Email address: gohildb.dev@gmail.com
    Password: 
}

#create Blog App [Dynamic App]
$python manage.py startapp Blog





