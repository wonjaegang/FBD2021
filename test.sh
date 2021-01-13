#!/bin/sh

var=1
time=10000
while [ $var -le $time ];
do
	if [ $var -eq $time ];then
		python3 Baskin31_GameTable.py | grep 'ecord'
	else
		python3 Baskin31_GameTable.py | grep 'asdasdasd'
	fi
	var=$((var+1))
	#echo $var
done
