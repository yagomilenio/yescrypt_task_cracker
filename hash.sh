#!/bin/bash


for i in `cat passwd`; do 
	mkpasswd -m yescrypt -R 11 "$i" >> hashes.txt
done
