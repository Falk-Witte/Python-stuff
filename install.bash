#!/bin/bash

#installation script for my python stuff

#do not install as root
if (( $EUID == 0 ));
then
    echo "Please do not run as root!"
    exit
fi

#clone repo
git clone https://github.com/Falk-Witte/Python-stuff

#install colorama
colorama=~/.local/lib/python3.10/site-packages/colorama/
colorama2=/usr/lib/python3.10/site-packages/colorama/

if [[ -d $colorama ]] || [[ -d $colorama2 ]]
then
    echo "colorama is installed"
else
    pip install colorama
fi

#install pyfiglet
pyfiglet=/usr/lib/python3.10/site-packages/pyfiglet/
pyfiglet2=~/.local/lib/python3.10/site-packages/pyfiglet/

if [[ -d $pyfiglet ]] || [[ -d $pyfiglet2 ]]
then
    echo "pyfiglet is installed"
else
    pip install pyfiglet
fi

#install py-sudoku
sudoku=/usr/lib/python3.10/site-packages/py_sudoku-1.0.2.dist-info/
sudoku2=~/.local/lib/python3.10/site-packages/py_sudoku-1.0.2.dist-info/

if [[ -d $sudoku ]] || [[ -d $sudoku2 ]]
then
    echo "py-sudoku is installed"
else
    pip install py-sudoku
fi

#self destruct after running
rm -f $0
