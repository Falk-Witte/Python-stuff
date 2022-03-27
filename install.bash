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
if [[ -a ${colorama} ]]
then
    echo "colorama is installed"
else
    pip install colorama
fi

#install pyfiglet
if [[ -a ${pyfiglet} ]]
then
    echo "pyfiglet is installed"
else
    pip install pyfiglet
fi

#install py-sudoku
if [[ -a ${py-sudoku} ]]
then
    echo "py-sudoku is installed"
else
    pip install py-sudoku
fi

#self destruct after running
rm -f $0