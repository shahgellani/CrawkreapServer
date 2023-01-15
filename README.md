# CrawlReap

## Project Description

TODO TODO TODO TODO TODO

## Project CConfiguration


#### Clone Crawlreap source code from bitbucket using below command

```bash
git clone git@github.com:shahgellani/CrawkreapServer.git
```

#### First we need to create a virtual environment.
#### It's better to create virtual env in root directory of project
```bash
python -m venv /path/to/directory

```

#### Activate the virtual environment
On Unix or MacOS,
```angular2html
Using the bash shell: source /path/to/venv/bin/activate
Using the csh shell: source /path/to/venv/bin/activate.csh
Using the fish shell: source /path/to/venv/bin/activate.fish
```

On windows
```angular2html
Using the Command Prompt: path\to\venv\Scripts\activate.bat
Using PowerShell: path\to\venv\Scripts\Activate.ps1
```


#### Install Requirements using below command

```bash
pip install -r requirements.txt
```

#### Run migrations for location tracking to migrate in MongoDB

```bash
python manage.py migrate
```

#### Run project

```bash
python manage.py runserver
```

## API's
* Users




