# import cowsay # ASCII Art 
import sys
from saying import hello

if len(sys.argv)==2:
    hello(sys.argv[1])
    # cowsay.trex("hello, "+sys.argv[1])