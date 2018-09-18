## =============================
## main.py
## authors:
##           Chen Zhang
##           Deepika Vinodkumar
##           Deesha Shingadia
##           Tejaswini Koduru
##           Megha Dhoke
##           Chunhua Yang
##           Kalyan Kumar Yalagandula
## date: Nov. 1st 2015
## version: 1
## class: Python Fall 2015, Dr. Riehle
from sys import *;
import main
import profile;
import cProfile;
def foo():
	print("hello");
foo()

cProfile.run(main.Game());

#profile.run(foo());


