#!/usr/bin/python

import sys
import os
import subprocess

pdg_root = os.environ["PDGPATHROOT"]

if not pdg_root:
    print("Please set environment PDGPATHROOT first!")
    exit(0)

if (pdg_root[-1] == "/"): pdg_root = pdg_root[:-1]
import imp
config = imp.load_source("config", "%s/config.py"%pdg_root)

def match(particle, candidate):
    for i in particle:
        if i not in candidate.lower():
            return False
    return True

argc = len(sys.argv) - 1

if argc == 0 :
    print """# ----------------------------------- #
# Look up particles in pdg
# pdg particle_name (roughly)
# ----------------------------------- #
    """
    exit(0)

pl = imp.load_source("config", "%s/2017/listings/particle_list.py"%pdg_root)
particle = sys.argv[1].lower()

candidates=[]
for candidate in pl.particle_list:
    if match(particle, candidate):
        candidates.append(candidate)

if not candidates:
    print("Particle not found!")
    exit(0)

for index, candidate in enumerate(candidates):
    print("[%d].  %s"%(index, candidate))

index = int(input())
subprocess.Popen("%s %s/2017/listings/rpp2017-list-%s.pdf"%(config.pdf_viewer, pdg_root, candidates[index]), shell=True)
