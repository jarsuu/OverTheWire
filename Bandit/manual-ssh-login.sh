#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage $0: <bandit_level> <password>"
    exit 1
fi

LEVEL=$1
PASSWORD=$2
PORT=2220
DOMAIN=bandit.labs.overthewire.org

sshpass -p "$PASSWORD" ssh -p "$PORT" bandit"$LEVEL"@"$DOMAIN"
