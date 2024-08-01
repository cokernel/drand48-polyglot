#!/bin/bash

ruby driver.rb > ruby.txt
python driver.py > python.txt

diff ruby.txt python.txt
