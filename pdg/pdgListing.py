#!/usr/bin/python3

import sys
import os
import subprocess
import imp

class PDGListing(object):
    ins = None
    def __init__(self):
        pass

    @classmethod
    def instance(cls):
        if cls.ins is None:
            cls.ins = PDGTable()
        return cls.ins

    def match(self, particle, candidate):
        for i in particle:
            if i not in candidate.lower():
                return False
        return True

    def lookup(self, particle):
        particle = particle.lower()

        import pdg.particle_list as pl

        candidates=[]
        for candidate in pl.particle_list:
            if self.match(particle, candidate):
                candidates.append(candidate)

        if not candidates:
            print("Particle not found!")
            exit(0)

        for index, candidate in enumerate(candidates):
            print("[%d].  %s"%(index, candidate))

        index = int(input())
        subprocess.Popen("open %s/data/2017/listings/rpp2017-list-%s.pdf"%(os.path.dirname(__file__), candidates[index]), shell=True)
