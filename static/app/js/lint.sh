#!/bin/bash
for f in *.ts;
do
	tslint -c lintconfig.json -f $f 
done