# businessCard
This is basic Django authentication web app. The user can sign-up, sign-in, update, delete and logout. The endpoints explanation are given below.

## Requirements 

```pip install django==3.0.3
pip install psycopg2
pip install django-cors-headers
```

##### You must have postgres installed, name and password of the user handy, <a href="https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04">for ubuntu installation you check this link.</a>



```cd BusinessCard```

<p>In setting.py change the database details (username,password and databasename) line number 91</p>

``` cd .. ```

<p>To setup the database and run server</p>

 ```
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py showmigrations
python3 manage.py runserver
```

<p>Usage using curl: The return type of every API is Json object</p> 

<ul>
  <li>First get the token using: Returns {"token":"","sessionid":}</li>

```curl -v -c cookies.txt -b cookies.txt http://127.0.0.1:8000/getToken/ ```

<li>To sign up: If successful redirects to get user data endpoint</li>

```curl -v -c cookies.txt -b cookies.txt -d "username=&password1=&password2=&csrfmiddlewaretoken=&image=" host/signup/```

<li>Or to login: If successful redirects to get user data endpoint</li>

```curl -v -c cookies.txt -b cookies.txt -d "username=&password=&csrfmiddlewaretoken=" host/login/```

<li>Get User data: If logged-in or signed-up, returns {"Status_code":"",Status:"","user_data":{"name":"","image":""}}</li>

```curl -v -c cookies.txt -b cookies.txt http://127.0.0.1:8000/users/id/```

<li>Update the user data: If successful redirects to get user data endpoint</li>

```curl -v -c cookies.txt -b cookies.txt -d "name=&image=&csrfmiddlewaretoken=" host/users/id/```

<li>Delete the user: If successful returns {"Status_code":"","Status":"","user_id":""}</li>

```curl -H "X-CSRFToken: " -X DELETE -v -c cookies.txt -b cookies.txt -d "csrfmiddlewaretoken=" host/users/id/```

<li>Logout</li>

```curl -H "X-CSRFToken: " -X DELETE -v -c cookies.txt -b cookies.txt -d "csrfmiddlewaretoken=" host/logout/```

</ul>
