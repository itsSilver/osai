# osai
# Run backend locally
Download and install
 `python 3.10`

Currently the project is connected with db in digitalocean,
if you want to connect it with your locally db.

Update the database connector in django_project/settings.py
run the command below to create tables in db
`python manage.py migrate`
You can skip this part if you want to work directly in production db.

`pip install -r requirements.txt` in your shell <br>
`python manage.py runserver 8000`

Application will be running at:
http://localhost:8000 <br>

http://localhost:8000/user/register <br>
http://localhost:8000/user/login <br>
http://localhost:8000/user/logout <br>

