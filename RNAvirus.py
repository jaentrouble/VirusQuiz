import Virus as virus

class Bunyavirus(virus.Virus) :
    def __init__(self) :
        virus.Virus.__init__(self)
        self.strand = 1
        self.gene = virus.RNA()
        self.gene.segmented = 3
        self.gene.segment = {'L' : 8.5,
                             'M' : 5.7,
                             'S' : 0.9}
        self.sense = -1
        self.envelope = True
        self.capsid = True
        self.enzyme = {'L protein' : virus.Enzyme()}
        self.subvirus = [Hantavirus]

    def replication(self, host : virus.Host) :
        if self.place == host.cytosol :
            mrna = self.enzyme['L protein'].do('N_protein_encoded_mrna')
            plus_sense_intermediate = self.enzyme['L protein'].do('self.gene')
            new_RNA = self.enzyme['L protein'].do(plus_sense_intermediate)
            self.migrate(host.cytosol.golgi(self))
            host.exocytosis(Bunyavirus())
        
class Hantavirus(Bunyavirus) :
    def __init__(self) :
        Bunyavirus.__init__(self)
        self.symptom = ['신증후출혈열(HFRS)',
                        '한타바이러스 폐증후군']
        self.infection = {'main' : 'virus particle from dried mouse dropping',
                       'horizontal infection' : 'droplet transmission'}
        self.epidemic = {'small' : ['May',
                                    'June'],
                         'big' : ['October',
                                  'November',
                                  'December']}

###############################################################

class Orthomyxovirus(virus.Virus) :
    def __init__(self):
        """
        Influenza virus
        """
        virus.Virus.__init__(self)
        self.gene = virus.RNA()
        self.strand = 1
        self.sense = -1
        self.envelope = True
        self.capsid = True
        self.segment = 8
        self.strategy = ['genetic reassortment',
                         'easy mutation']
        self.enzyme = {'PA' : virus.Enzyme(),
                       'PB1' : virus.Enzyme(),
                       'PB2' : virus.Enzyme()}
        self.protein = {'HA' : virus.Protein,
                        'NA' : virus.Protein}
        self.latent_period = (1,4) #days
        self.vaccine = {'4 strain' : [2*a, 2*b],
                        '3 strain' : [2*a, 1*b]} #mixture of HA and NA protein
        self.subvirus = [InfluenzaA, InfluenzaB]
        
    def replication(self, host : virus.Host) :
        self.rep_site = host.nucleus
        if 'sialic acid' in host.surface_protein :
            virus.bind(self.protein['HA'], host.surface_protein['sialic acid'])
        if self.place == host.cytosol :
            self.envelope = False
            self.capsid = False
            if self.place == host.nucleus :
                mrna = self.enzyme['PA'].do('transcription')

class InfluenzaA(Orthomyxovirus) :
    def __init__(self):
        Orthomyxovirus.__init__(self)
        self.classification = ['type',
                               'first seperated region',
                               'first seperated date',
                               'HA, NA number']
        self.mutation = 'often'
        self.infect = ['man',
                       'horses',
                       'pigs',
                       'ferrets',
                       'birds'] # wide variety of mammals

class InfluenzaB(Orthomyxovirus) :
    def __init__(self):
        Orthomyxovirus.__init__(self)
        self.classification = ['type',
                               'first seperated region',
                               'first seperated date']
        self.infect = ['mammals only',
                       'mainly man']
        self.mutation = 'no big change'

class InfluenzaC(Orthomyxovirus) :
    """
    not our interest
    """
    pass

###############################################################

class Paramyxovirus(virus.Virus) :
    def __init__(self):
        virus.Virus.__init__(self)
        self.gene = virus.RNA()
        self.strand = 1
        self.sense = -1
        self.segment = False
        self.gene_length = (17,20) #kb
        self.subvirus = [MeaslesVirus,
                         MumpsVirus,
                         RespiratorySyncytialVirus]
        self.infection = {'respiratory droplets' : 'start at respiratory tract'}
        self.protein = {'HN' : 'Viral Attatchment Protein',
                        'F' : 'cell fusion & haemolysis', # makes syncytia
                        'NP' : 'Nucleoprotein'}
        self.charicteristic = ['syncytia']

    def replication(self, host : virus.Host) :
        self.rep_site = host.cytosol

class MeaslesVirus(Paramyxovirus) :
    def __init__(self) :
        Paramyxovirus.__init__(self)
        self.symptom = ['cough',
                        'coryza',#코감기
                        'conjunctivitis',#'3C' symptoms
                        'Koplik spots'] #unique symptom

class MumpsVirus(Paramyxovirus) :
    pass

class RespiratorySyncytialVirus(Paramyxovirus) :
    pass

###############################################################

class Picornavirus(virus.Virus) :
    def __init__(self) :
        virus.Virus.__init__(self)
        self.gene = virus.RNA()
        self.strand = 1
        self.sense = 1
        self.gene_length = (7.2, 8.5) #kb
        self.envelope = False
        self.capsid = True
        self.IRES = virus.RNA() # Translation factor
        self.subvirus = [Poliovirus,
                         Coxsackievirus,
                         Rhinovirus]

    def replication(self, host: virus.Host) :
        self.rep_site = host.cytosol
        if self.place == host.cytosol :
            rna_pol = self.IRES.translate(self.gene)
            minus_gene = rna_pol(self.gene)
            new_gene = rna_pol(minus_gene)

class Poliovirus(Picornavirus) :
    """
    Enterovirus
    """
    def __init__(self) :
        Picornavirus.__init__(self)
        self.symptom = ['polio'] #소아마비
        self.infect_target = ['man']
        self.infection = ['fecal-oral']
        self.pH_range = (3,9)
        self.resistant = ['mild sewage treatment',
                          'heat']
        self.vaccine = 'live vaccine'

    def replication(self, host : virus.Host) :
        Picornavirus.replication(self, host)
        infect_order = {'primary infection' : 'small intestine',
                        'replication' : 'mesenteric lymph node',
                        'primary viraemia' : 'blood',
                        'intraneural spread' : 'CNS'}
        self.symptom.append('paralysis')

class Coxsackievirus(Picornavirus) :
    """
    Enterovirus
    """
    def __init__(self) :
        Picornavirus.__init__(self)
        self.symptom = ['hand-foot-and-mouth disease'] # 수족구병
        self.vaccine = None
        self.medicine = None
        self.GI_tract_replicate = True #Enterovirus
        self.low_pH = True
        self.GI_tract_disease = False

class Rhinovirus(Picornavirus) :
    def __init__(self) :
        Picornavirus.__init__(self)
        self.symptom = ['upper respiratory disease']
        self.host_immunity = False
        self.GI_tract_replicate = False

###############################################################

class Flavivirus(virus.Virus) :
    def __init__(self) :
        virus.Virus.__init__(self)
        self.gene = virus.RNA()
        self.strand = 1
        self.sense = 1
        self.gene_length = (10,10) #kb
        self.envelope = True
        self.capsid = True

    def replication(self, host : virus.Host) :
        self.similar['replication strategy'] = Picornavirus.replication
        self.rep_place = host.cytosol
        self.rep_place += host.cytosol.golgi

class JapanesEncephalitisVirus(Flavivirus):
    def __init__(self) :
        Flavivirus.__init__(self)
        self.latent_period = (7,10)
        self.vaccine = True
        
class DengueVirus(Flavivirus):
    def __init__(self):
        Flavivirus.__init__(self)
        self.clue = ['travel to epidemic region',
                     'exposure']
        self.symptom = {'early' : ['구토',
                                   '식욕부진',
                                   '오심',
                                   '허약'],
                        '1~2 days' : ['반점'],
                        '3~4 days' : ['fever break'],}
        self.epidemic_region = ['oceania',
                                'afreeca'] #tropical region
#-------------------------------------------------------------#
class Rubivirus(virus.Virus) :
    pass

class RubellaVirus(Rubivirus) :
    def __init__(self) :
        Flavivirus.__init__(self)
        self.danger = {'congenital infection' : 'high risk of deformity'}

###############################################################

class Coronavirus(virus.Virus) :
    def __init__(self) :
        virus.Virus.__init__(self)
        self.gene = virus.RNA()
        self.strand = 1
        self.sense = 1
        self.gene_length = (20,30) #kb
        self.envelope = True
        self.capsid = True
        self.temp = (33,35) #celcius
        self.infect_organ = ['upper respiratory tract'] # lower very rare
        self.symptom = ['콧물',
                        '권태감']
        self.latent_period = 3 #days
        self.SARS = ['direct contact with a patien within 10 days',
                     'epidemic area (china, Vietnam)',
                     'fever (>38)',
                     'respiratory symptom']
        self.detect = ['RT-PCR']
        self.biosafety = {'SARS - Coronavirus seperation' : 'BSL-3',
                          'simple diagnosis' : 'BSL-2'}

    def replication(self, host : virus.Host) :
        self.rep_place = host.cytosol
        L_protein = host.cytosol.ribosome(self.gene)
        minus_strand = L_protein(self.gene)

###############################################################

class NoroVirus(virus.Virus) :
    def __init__(self) :
        virus.Virus.__init__(self)
        self.gene = virus.RNA()
        self.sense = 1
        self.strand = 1
        self.envelope = False
        self.capsid = True
        self.infect_minimum = 10 # virions
        self.infect_route = ['fecal - oral',
                             'aerosol of vomit']
        self.symptom = ['diarrhea',
                        'acute gastritis',
                        '30% release virus without any symptoms']
        self.latent_period = (12,48) #hours