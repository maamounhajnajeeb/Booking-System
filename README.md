## Booking System
Django web api that makes booking easier for travel offices.

## Motivation
As a first task I worked on in my Internship at **Remo Start**, 
I tried to spare no effort on this project to make it as good as
 I can, especially that this is my first expermient with Rest API world.

## Cloning this project
Initially, you need python 3.10 or higher installed on your local machine, then:
- Open a folder and build virtual environment within it via these commands:
1. `virtualenv .venv`
2. `.venv\scripts\activate` for windows</br>
(if you user mac or linux, do this instead:
`source .venv/bin/activate`)
- Next, clone the repo:</br>
`git clone https://github.com/maamounhajnajeeb/Booking-System.git`
- Now it's dependencies' time:</br>
`pip install -r requirements.txt`</br>
here  you have to wait for some time until the dependencies installed suucessfully</br>
actually the dependencies aren't that much (you can check them form **requirements.txt** file)
- After that, write Django magic commands:</br>
`python manage.py migrate`</br>
`python manage.py runserver`</br>