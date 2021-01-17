#!/bin/sh

rm Jaewon_total_record.txt Kyeongmin_total_record.txt Kyungho_total_record.txt

if [ $# -ne 1 ]; then
	echo "Usage: ./test.sh TheNumberOfSimulation"
	echo "Example: ./test.sh 100"
else
	var=1
	time=$1
	while [ $var -le $time ];
	do
		if [ $var -eq $time ];then
			python3 Baskin31_GameTable.py | grep 'records'
		else
			python3 Baskin31_GameTable.py | grep 'dontwantprint'
		fi
		var=$((var+1))
	done
fi

