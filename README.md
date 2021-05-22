# Project name

### Set the environment
```bash
virtualenv --python=/usr/bin/python3.7 env
source env/bin/activate
pip install -r requirements.txt
```

### Env variables
In the location of setting files, create a `.env` file that looks like this.
```bash
SECRET_KEY=7h^=c#bmb5xs0icn!jfjly95b6343-@si4ce5@)_4c6^tb6ok9
DATABASE_NAME=name
DATABASE_USER=username
DATABASE_PASSWORD=admin
DATABASE_HOST=127.0.0.1
DATABASE_PORT=5432
DEBUG=1   
```

Then 

`python manage.py makemigrations`

`python manage.py migrate`


