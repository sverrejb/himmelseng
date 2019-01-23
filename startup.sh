#! /bin/bash

echo Starting ...
gunicorn -w 4 -b 0.0.0.0:8900 himmelseng:app --daemon
nginx