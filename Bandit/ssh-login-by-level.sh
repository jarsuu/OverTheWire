#!/bin/bash

if [ -z "$1" ]; then
    echo "Usage: $0 <level>"
    exit 1
fi;

LOGIN_FILE=login.csv
LEVEL="$1"
PASSWORD=$(awk -F',' -v lvl="$LEVEL" '$1 == lvl {print $2}' "$LOGIN_FILE")

if [ -z "$PASSWORD" ]; then
    echo "No password found for level $LEVEL."
    exit 1
fi
    
PORT=2220
DOMAIN=bandit.labs.overthewire.org

sshpass -p "$PASSWORD" ssh -p "$PORT" bandit"$LEVEL"@"$DOMAIN"