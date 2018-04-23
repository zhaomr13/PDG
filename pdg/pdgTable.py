import os
class Particle(object):

    def __init__(self):
        self.name = ""
        self.mass = -1
        self.charge = -1
        self.life = -1
        self.evtgenname = ""
        self.pythiaid = -1
        self.geantid = -1
        self.maxwidth = -1

class PDGTable(object):
    ins = None
    def __init__(self):
        self.table = {}
        self.read_table()

    @classmethod
    def instance(cls):
        if cls.ins is None:
            cls.ins = PDGTable()
        return cls.ins


    def read_table(self):
        f = open(os.path.dirname(__file__) + "/data/ParticleTable.txt")
        for line in f.readlines():
            if not line: break
            if line[0] == "#": continue
            line = line.split()
            particle = Particle()
            particle.name = line[0]
            particle.geantid = line[1]
            particle.pdgid = line[2]
            particle.charge = line[3]
            particle.mass = line[4]
            particle.life = line[5]
            particle.evtgenname = line[6]
            particle.pythiad = line[7]
            particle.maxwidth = line[8]
            self.table[particle.name] = particle

    def get_infomation(self, name):
        particle = self.table.get(name, None)
        if particle:
            return """Mass: {0} [GeV]
Lifetime: {1} [s]
Charge: {2}
MaxWidth: {3}
PDG ID: {4}
""".format(particle.mass,
           particle.life,
           particle.charge,
           particle.maxwidth,
           particle.pdgid)
        else:
            return "Particle not found."
