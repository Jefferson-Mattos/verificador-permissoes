#!/bin/bash

if [ -n "$1" ];then
	python3 check.py "$1"
else
	python3 check.py
fi
