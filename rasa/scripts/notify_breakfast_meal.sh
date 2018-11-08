#!/bin/sh
cd "$(dirname "$0")";
CWD="$(pwd)"
echo $CWD
/usr/local/bin/python3.6 breakfast_notifier.py
