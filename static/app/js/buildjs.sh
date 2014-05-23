#!/bin/bash
clear
#tsc --out flowapp.js workspace.ts menus.ts dialogs.ts server.ts listings.ts templating.ts
tsc --out lib/flowapp.js *.ts
echo
echo Done..
echo
echo
