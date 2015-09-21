#!/bin/bash

FILE=$1
LIMIT=10

if [[ ! -z "$2" ]]
then
    LIMIT=$2
fi

awk '{print $1}' $FILE | sort | uniq -c | sort -nr | awk "FNR <= $LIMIT"
