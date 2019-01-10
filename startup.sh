#! /bin/bash

echo starter

gunicorn -w 4 -b 0.0.0.0:80 himmelseng:app --daemon
nginx