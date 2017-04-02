from tkinter import *

IGRALEC_1 = 'igralec1'
BARVA_1 = 'blue'
IGRALEC_2 = 'igralec2'
BARVA_2 = 'red'

##OSTEVILCENJE POLJ
## 1  -  -  2  -  -  3
## |  4  -  5  -  6  |
## |  -  7  8  9  -  |
##10 11 12  - 13 14 15
## |  - 16 17 18  -  |
## | 19  - 20  - 21  |
##22  -  - 23  -  - 24

trojke = [(1,2,3), (4,5,6), (7,8,9), (10,11,12),
          (13,14,15), (16,17,18),(19,20,21),(22,23,24),
          (1,10,22),(4,11,19),(7,12,16),(2,5,8),
          (17,20,23),(9,13,18),(6,14,21),(3,15,24)]

def nasprotnik(igralec):
    if igralec == IGRALEC_1:
        return IGRALEC_2
    elif igralec == IGRALEC_2:
        return IGRALEC_1
    else:
        return 'Zgodila se je napaka pri menjavi igralcev'

class Polje():
    def __init__(self, canvas, id_krogca, stevilka_polja):#master?
        self.canvas = canvas #/plosca
        self.id_krogca = id_krogca
        self.stevilka_polja = stevilka_polja
        self.zasedenost = None


    def spremeni_zasedenost(self, igralec=None):
        #spremenimo zasedenost polja: ce na vrsti ni noben igralec, vrne None, sicer pa pripadajoco
        #barvo igralca, ki je na vrsti
        if igralec != IGRALEC_1 and igralec != IGRALEC_2:
            self.zasedenost = None
        else:
            self.zasedenost = igralec


class Igra():
    def __init__(self, gui):
        self.gui = gui
        self.st_zetonov = {IGRALEC_1: 9, IGRALEC_2: 9}
        self.na_potezi = IGRALEC_1
        self.faza = 1
        self.zgodovina = []

    def je_veljavna_poteza(self, index_polja):
        #ob pregledu aktivnega polja, na katerega zelimo igrati, vrne True,
        #ce je poteza veljavna, ter False sicer.
        aktivno_polje = self.gui.slovar_polj[index_polja]
        if self.gui.odstranitev_zetona:
            print('preverjam veljavnost poteze')
            #ce v potezi tece faza odstranitve, pogleda, ce je polje,
            #ki ga je treba odstraniti, nasprotnikovo
            print(aktivno_polje.zasedenost, nasprotnik(self.gui.na_vrsti.get()),
                  self.gui.na_vrsti.get() )
            if aktivno_polje.zasedenost == nasprotnik(self.gui.na_vrsti.get()):
                #TODO ce je polje v trojki, ga ne smem odstraniti, razen
                #ce so vsi zetoni v trojki
                return True
            else:
                return False
        elif self.faza == 1:
        #ce smo v fazi dodajanja zetonov, lahko dodamo zeton na prazno polje
            if aktivno_polje.zasedenost == None:
                return True
            else:
                return False
        else:
            print('Nismo �e tako dale�')

    def preveri_trojke(self, index_polja):
        je_v_trojkah = []
        for trojka in trojke:
            if index_polja in trojka:
                je_v_trojkah.append(trojka)
                if len(je_v_trojkah) == 2:
                    break
        for trojka in je_v_trojkah:
            zasedenost = None
            koncaj = None #kontroliramo, ali se mora zanka prkeiniti ali ne
            for index in trojka: #neki ne dela
                #okupiranost = kdo je po potezi na polju
                #zasedenost = kaksne barve zbiramo v trojki
                okupiranost = self.gui.slovar_polj[index].zasedenost
                if koncaj is None:
                    if okupiranost == None:
                        koncaj = True
                        break
                        #eno polje v trojki je prazno - trojke ni
                    elif zasedenost == None:
                        #nastavimo barvo trojke, ki jo i��emo
                        zasedenost = okupiranost
                    elif zasedenost != okupiranost:
                        #v trojki je kak�na druga�na barva kot prej
                        koncaj = True
                        break
                else:
                    pass
            if koncaj is None:
                print('Nasel sem trojko')
                return True
            
        #�e ni na�el nobene trojke:
        print('Nisem nasel trojke')
        return False


                
