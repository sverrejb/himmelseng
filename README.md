# Himmelseng 🛏
Jeg ønsker meg en himmelseng ...

Himmelseng er en sang som synges i godt lag av studentene i Trondheim. Opphavet til sangen er ukjent, men den ser opprinnelig ut til å komme fra Danmark.
Sangen har et start- og et sluttvers, og innimellom der kommer vers av forskjellig art. Disse følger som regel et mønster med fire linjer, der andre og fjerde linje rimer.
Himmelseng.no ble laget i et forsøk på å samle og bevare de mange versene som finnest i studentmiljøet i Trondheim, samt være til hjelp når sangen synges.

## Oppsett av utviklingsmiljø
* Installer python3 og pip
* Installer virtualenv
* Installer [virtualenvwrapper](http://virtualenvwrapper.readthedocs.io/en/latest/install.html) (Valgfritt, men anbefalt)
* Opprett et virtualenv med python3: `mkvirtualenv --python=/usr/bin/python3 <navn på environment>` (path til python3 kan her variere med OS og oppsett)
* Aktiver environmentet: `workon <navn på environment>`. For å deaktivere env: `deactivate`
* Installer avhengigheter: `pip install -r requirements.txt`
* Ved førstegangsoppsett: Sett opp miljøvariabel: `echo "export FLASK_APP=himmelseng.py" >> $VIRTUAL_ENV/bin/postactivate && workon <navn på environment>` (virtualenv må her reaktiveres for at dette skal tre i kraft)
* Ved førstegangsoppsett: Sett opp lokal sqlitedatabase med: `flask db init && flask db migrate -m "init db" && flask db upgrade`
* Start applikasjon med `flask run`
* Tester kjøres med `nose2`
