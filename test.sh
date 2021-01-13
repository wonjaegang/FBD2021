#!/bin/sh

var=1
time=10000

while [ $var -le $time ];
do
	if [ $var -eq $time ];then
		python3 Baskin31_GameTable.py | grep 'records'
	else
		python3 Baskin31_GameTable.py | grep 'dontwantprint'
	fi
	var=$((var+1))
	#echo $var
done
