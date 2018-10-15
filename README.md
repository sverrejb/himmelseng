# Himmelseng 🛏
Jeg ønsker meg en himmelseng ...

Himmelseng er en sang som synges i godt lag av studentene i Trondheim. Opphavet til sangen er ukjent, men den ser opprinnelig ut til å komme fra Danmark.
Sangen har et start- og et sluttvers, og innimellom der kommer vers av forskjellig art. Disse følger som regel et mønster med fire linjer, der andre og fjerde linje rimer.
Himmelseng.no ble laget i et forsøk på å samle og bevare de mange versene som finnest i studentmiljøet i Trondheim, samt være til hjelp når sangen synges.

## Development
* Install python3 and pip
* Install virtualenv
* Install [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html) (Optional)
* Create a virtualenv with python3: `mkvirtualenv --python=$(which python3) <name of environment>
* Activate environment: `workon <name of environment>`. To deactivate env: `deactivate`
* Install dependencies: `pip install -r requirements.txt`
* On first time setup: Sett envirionment variable: `echo "export FLASK_APP=himmelseng.py" >> $VIRTUAL_ENV/bin/postactivate && workon <navn på environment>` (virtualenv must be reactivated)
* On first time setup: Create local sqlite database: `flask db init && flask db migrate -m "init db" && flask db upgrade`
* Start application with `flask run`
* Run tests with `nose2`
