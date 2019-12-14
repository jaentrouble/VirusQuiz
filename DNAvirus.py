import Virus as virus
import random

class Parvovirus (virus.Virus) :
    def __init__ (self) :
        virus.Virus.__init__(self)
        self.gene = virus.DNA()
        self.strand = 1
        self.sense = random.choice([-1,1]) # becomes dsDNA anyway, so not important
        self.gene_length = (5,5)   #kb
        self.envelope = False
        self.capsid = True
        self.pH_range = [3.0, 9.0]
        self.survive_temp = 56
        self.other_names = ['fifth disease']
        self.subvirus = [B19]

class B19 (Parvovirus) :
    def __init__ (self) :
        Parvovirus.__init__(self)
        self.symptom = ['Facial erythema'] #감염홍반증
        self.infection = 'very common'
        self.immunity = 'once infected immune lifetime'

    def replication (self, host : virus.Host) :
        if self.place == host.nucleus :
            self.capsid = False
            host.nucleus.add(self.gene)
            if host.dna_polymerase(self.gene) :
                self.strand = 2
                excess_DNA = True
            if self.strand == 2 :
                mrna = host.transcription_factor(self.gene)
            capsid = host.cytosol.ribosome(mrna)
            host.nucleus.add(capsid)
            if excess_DNA and host.nucleus.anything.count(capsid) :
                host.lysis()
                B19()

###################################################################

class Adenovirus (virus.Virus) :
    def __init__(self) :
        """
        Common cold virus
        """
        virus.Virus.__init__(self)
        self.strand = 2
        self.gene = virus.DNA()
        self.gene_length = (30,38) #kb
        self.envelope = False
        self.capsid = True
        self.capsid_shape = 'icasahedral' #정이십면체
        self.symptom = ['respiratory infection',
                        'conjunctivitis',
                        'hemorrhagic cystitis',
                        'gastritis',]
        self.culture = 'human epithelium oriented cell'
        self.enzyme = [self.DNA_polymerase]

    def DNA_polymerase(self) :
        pass

###################################################################

class Herpesvirus(virus.Virus) :
    def __init__(self) :
        virus.Virus.__init__(self)
        self.strand = 2
        self.gene = virus.DNA()
        self.envelope = True
        self.capsid = True
        self.subfamily = {'alphaherpesvirinae' : ['HSV',
                                                  'VSV']}
        self.antivirus = {'Acyclovir' : 'Inhibits DNA_polymerase'}
        self.phase = None
        self.subvirus = [HerpesSimpleVirus,
                         VaricellaZosterVirus,
                         EpsteinBarrVirus,]

    def replication(self, host : virus.Host) :
        if self.place == host.cytosol :
            self.envelope = False
        if self.place == host.nucleus :
            self.capsid = False
            if self.phase == 'immediate early':
                self.make('DNA_binding_protein')
            if self.phase == 'early':
                self.make('transcription factor')
                self.make('DNA_polymerase')
            ####### replication of gene #######
            if self.phase == 'late' :
                host.nucleus.dna_polymerase(self.gene)
                excess_DNA = True
                mrna = host.nuceus.transcription_factor(self.gene)
                capsid = host.cytosol.ribosome(mrna)
                new_particle = Herpesvirus()
                new_particle.envelope = False
            if excess_DNA and capsid :
                host.cytosol.golgi(new_particle)
                new_particle.envelope = True

class HerpesSimpleVirus(Herpesvirus) :
    def __init__(self):
        Herpesvirus.__init__(self)
        self.types = ['HSV-1', 'HSV-2']
        self.virus_durability = 'Very weak'
        self.infect_route = {'HSV-1' : ['6month ~ 5yr',
                                        'by kiss',
                                        'by contaminated toothbrush',
                                        'by contaminated dishes'],
                             'HSV-2' : ['Sex',
                                        'Newborn : when birth, from mother']}

    def primary_infection (self, host : virus.Host) :
        host.infected.extend(['mucus membranes of the mouth',
                              'mucus membranes of the throat'])
        self.enter(host.organ.sensory_nerve)
        self.migrate(host.organ.sensory_nerve_ganglia)
        self.latent_infection()

    def latent_infection(self, host : virus.Host) :
        self.mode = 'sleep'
        if host.immunity == 'Bad' :
            self.reccurrent_infection()

    def reccurrent_infection(self, host : virus.Host) :
        self.migrate(host.organ.surface)
        self.replication()

class VaricellaZosterVirus(Herpesvirus) :
    def __init__ (self) :
        Herpesvirus.__init__(self)
        self.symptom = ['chickenpox (varicella)',
                        'herpes zoster',]
        self.similar[HerpesSimpleVirus] = ['latent infect at neuron',
                                           'cytotoxic immunity important',
                                           '수포성 병터']

class EpsteinBarrVirus(Herpesvirus) :
    def __init__(self) :
        Herpesvirus.__init__(self)
        self.symptom = ['Infectious monocleosis',
                        'Burkitts lymphoma',
                        'Hodgkins lymphoma']

###################################################################

class Poxvirus(virus.Virus) :
    def __init__(self) :
        virus.Virus.__init__(self)
        self.gene = virus.DNA()
        self.strand = 2
        self.envelope = True
        self.coremembrane = True #instead of capsid, double membrane
        self.gene_length = (130,300)
        self.size = 'Can be seen by light microscope'
        self.enzymes = {'DNA_dep_RNA_polymerase' : virus.Enzyme()}
        self.infect_route = ['air']
        self.infectious = 'Very infectious'
        self.latent_period = (5,17) # days

    def infection(self, host : virus.Host) :
        host.infected.extend(['upper respiratory tract'])
        self.replication()
        self.migrate(['lymph',
                      'viremia'])
        self.migrate(['dermis',
                      'internal organs'])
        self.symptom.append('pock')
        self.migrate(['secondary viremia'])
        if host.luck :
            host.survive()
            host.symptom = [] #후유증 없음
        else :
            host.die()

    def replication(self, host : virus.Host) :
        if self.place == host.cytosol :
            self.envelope = False
            self.enzymes['uncoatase'] = self.enzymes['DNA_dep_RNA_polymerase'].do('uncoatase')
            self.coremembrane = False
            self.enzymes['DNA polymerase'] = self.enzymes['DNA_dep_RNA_polymerase'].do('DNA polymerase')
            self.enzymes['DNA polymerase'].do(self.gene)

###################################################################
