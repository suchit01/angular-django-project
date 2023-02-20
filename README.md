# Project SetUp #


## DJango Setup ##

To setup virtual environment, craete a virtual environment using command:

To create a folder named env, run command:

```
mkdir env
```

```
python -m venv ./env
```

To activate the environment, run command: 

```
.\env\Scripts\activate.bat
```

Now, move to DJango folder

```
cd ./DJango
```

To install dependencies, run command:

```
pip install -r requirements.txt
```

To start the server, run command:

```
cd AssignmentProj

python ./manage.py runserver
```

## Angular Setup ##

Insatll the npm packages required

```
cd ./Angular

npm install
```
Make sure to have angular CLI installed in your system globally or run the command:

```
npm i -g @angular/cli
```

To start the application:

```
ng serve
```