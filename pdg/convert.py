import subprocess
import sys, os
from particle_list import particle_list

for particle in particle_list:
    subprocess.call("convert -trim -adjoin -verbose -density 300 rpp2017-list-%s.pdf -quality 100 rpp2017-list-%s.jpg"%(particle, particle), shell=True)
    subprocess.call("convert rpp2017-list-%s-*.jpg -append images/rpp2017-list-%s.jpg"%(particle, particle), shell=True)
    # for i in xrange(20):
    # if os.path.exists("rpp2017-list-%s-%d.jpg"%(particle, i)):
    # subprocess.call("convert rpp2017-list-%s-%d.jpg -append images/rpp2017-list-%s.jpg"%(particle, i, particle), shell=True)
