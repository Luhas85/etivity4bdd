from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Time, Float, Date, ForeignKey

from funzioni.inseriscitabelle import Citta, Residenza, Sede, Server, Accedea, Serveraccessi, Tiporeparto, Reparto, Vlan, Partecipa, Magazzino, SetPronto, Colore
from funzioni.inseriscitabelle import Brick, Composto, Permessi, Categoria, Orario, Stipendio, Persona, Dipendente, Acquirente, Vendite, Venduto, Spedizione, Inviato
from sqlalchemy.orm import sessionmaker, close_all_sessions

def faiinserimento(engine):
  """
  Questa Funzione popola il Database con il dati del DB di esempio fatto nell'etivity 3
  """
  conn = engine.connect()
  Session = close_all_sessions()
  resultcit = conn.execute(Table.insert(Citta), [ {'ID_Citta':1, 'NomeCitta' : 'Siena', 'CapCitta' : 53100} ,
                                                  {'ID_Citta':2, 'NomeCitta' : 'Firenze', 'CapCitta' :  50121} ,
                                                  {'ID_Citta':3, 'NomeCitta' : 'Poggibonsi', 'CapCitta' :  53036} ,
                                                  {'ID_Citta':4, 'NomeCitta' : 'Asciano', 'CapCitta' :  53041} ,
                                                  {'ID_Citta':5, 'NomeCitta' : 'Grosseto', 'CapCitta' :  58100} , 
                                                  {'ID_Citta':6, 'NomeCitta' : 'Otranto', 'CapCitta' :  76576} ,                                                
                                                  {'ID_Citta':7, 'NomeCitta' : 'Parigi', 'CapCitta' :  10000} ,                                                
                                                  {'ID_Citta':8, 'NomeCitta' : 'Caltanissetta', 'CapCitta' :  12312} ,                                                
                                                  {'ID_Citta':9, 'NomeCitta' : 'Asti', 'CapCitta' :  21400} , 
                                                  {'ID_Citta':10, 'NomeCitta' : 'Linate', 'CapCitta' :  22300} , 
                                                  {'ID_Citta':11, 'NomeCitta' : 'Antraccoli', 'CapCitta' :  32433} , 
                                                  {'ID_Citta':12, 'NomeCitta' : 'Lucca', 'CapCitta' :  43444} ])

  resultres = conn.execute(Table.insert(Residenza), [ {'ID_Residenza':1,'ID_Citta':1,'Via':'Toselli'} ,
                                                      {'ID_Residenza':2,'ID_Citta':1,'Via':'Piazza del Campo'},
                                                      {'ID_Residenza':3,'ID_Citta':1,'Via':'Piazza Amendola'},
                                                      {'ID_Residenza':4,'ID_Citta':2,'Via':'Lungarno Ridolfi'},
                                                      {'ID_Residenza':5,'ID_Citta':2,'Via':'Piazzale Michelangelo'}, 
                                                      {'ID_Residenza':6,'ID_Citta':3,'Via':'Tal del Tali'},                                                
                                                      {'ID_Residenza':7,'ID_Citta':3,'Via':'Ludovico Ariosto'},                                               
                                                      {'ID_Residenza':8,'ID_Citta':4,'Via':'Borgaccio'},                                              
                                                      {'ID_Residenza':9,'ID_Citta':4,'Via':'Romituzzo'},
                                                      {'ID_Residenza':10,'ID_Citta':4,'Via':'Senese'}, 
                                                      {'ID_Residenza':11,'ID_Citta':4,'Via':'Fiume'}, 
                                                      {'ID_Residenza':12,'ID_Citta':5,'Via':'Le Roselle'}, ])

  resultsed = conn.execute(Table.insert(Sede), [ {'ID_Sede':1,'NomeSede':'Centrale','IP_Sede':'10.71.72.201','Centralino_Sede':577123456,'E_mailSede':'centrale@bricklink.it','ViaSede':5,'CivicoSede':28} ,
                                                 {'ID_Sede':2,'NomeSede':'Prima Filiale','IP_Sede':'10.72.72.201','Centralino_Sede':577253455,'E_mailSede':'primafiliale@bricklink.it','ViaSede':3,'CivicoSede':25} ,
                                                 {'ID_Sede':3,'NomeSede':'Parco dei Principi','IP_Sede':'10.73.72.201','Centralino_Sede':577128598,'E_mailSede':'parcoprincipi@bricklink.it','ViaSede':1,'CivicoSede':108} ,
                                                 {'ID_Sede':4,'NomeSede':'Maresi','IP_Sede':'10.74.72.201','Centralino_Sede':577888954,'E_mailSede':'maresi@bricklink.it','ViaSede':12,'CivicoSede':66}])
 
  resultser = conn.execute(Table.insert(Server), [ {'ID_Server':1 , 'DescrizioneServer':'Domain Controller' , 'IP_Server':'10.71.55.26' , 'ID_Sede':1} ,
                                                   {'ID_Server':2,'DescrizioneServer':'Centralino','IP_Server':'10.71.55.108','ID_Sede':1} ,
                                                   {'ID_Server':3,'DescrizioneServer':'Backup','IP_Server':'10.71.108.108','ID_Sede':1} ,
                                                   {'ID_Server':4,'DescrizioneServer':'FileServer','IP_Server':'10.71.55.33','ID_Sede':1} ,
                                                   {'ID_Server':5,'DescrizioneServer':'Contabilita','IP_Server':'10.72.55.36','ID_Sede':2} ,                                 
                                                   {'ID_Server':6,'DescrizioneServer':'Personale','IP_Server':'10.73.55.38','ID_Sede':3}])
                                                   
  resultacc = conn.execute(Table.insert(Accedea), [ {'ID_Accesso':1 , 'ID_Server':1 , 'ID_Sede':1 , 'Motivo':'Autenticazione'} ,
                                                    {'ID_Accesso':2 , 'ID_Server':2 , 'ID_Sede':1 , 'Motivo':'Telefonate'} ,
                                                    {'ID_Accesso':3 , 'ID_Server':5 , 'ID_Sede':1 , 'Motivo':'Entrate'} , 
                                                    {'ID_Accesso':4 , 'ID_Server':1 , 'ID_Sede':2 , 'Motivo':'Autenticazione'} , 
                                                    {'ID_Accesso':5 , 'ID_Server':2 , 'ID_Sede':2 , 'Motivo':'Telefonate'} , 
                                                    {'ID_Accesso':6 , 'ID_Server':1 , 'ID_Sede':3 , 'Motivo':'Autenticazione'} , 
                                                    {'ID_Accesso':7 , 'ID_Server':2 , 'ID_Sede':3 , 'Motivo':'Telefonate'} , 
                                                    {'ID_Accesso':8 , 'ID_Server':1 , 'ID_Sede':4 , 'Motivo':'Autenticazione'} , 
                                                    {'ID_Accesso':9 , 'ID_Server':2 , 'ID_Sede':4 , 'Motivo':'Telefonate'} , 
                                                    {'ID_Accesso':10 , 'ID_Server':4 , 'ID_Sede':1 , 'Motivo':'Condivisione'} , 
                                                    {'ID_Accesso':11 , 'ID_Server':4 , 'ID_Sede':2 , 'Motivo':'Condivisione'} , 
                                                    {'ID_Accesso':12 , 'ID_Server':1 , 'ID_Sede':3 , 'Motivo':'Condivisione'}])

  resultsacc = conn.execute(Table.insert(Serveraccessi), [ {'ID_ServerAccessi':1,'ID_ServerIN':1,'ID_ServerOUT':2,'Motivo':'Autenticazione'} , 
                                                           {'ID_ServerAccessi':2,'ID_ServerIN':1,'ID_ServerOUT':4,'Motivo':'Autenticazione'} , 
                                                           {'ID_ServerAccessi':3,'ID_ServerIN':1,'ID_ServerOUT':5,'Motivo':'Autenticazione'} , 
                                                           {'ID_ServerAccessi':4,'ID_ServerIN':1,'ID_ServerOUT':6,'Motivo':'Autenticazione'} , 
                                                           {'ID_ServerAccessi':5,'ID_ServerIN':6,'ID_ServerOUT':1,'Motivo':'DatisuiDipendenti'}])

  resulttre = conn.execute(Table.insert(Tiporeparto), [ {'ID_TipoReparto':1 , 'NomeReparto':'Personale' , 'DescrizioneReparto':'Si occupa della gestione dei dipendenti'} , 
                                                        {'ID_TipoReparto':2 , 'NomeReparto':'Produzione' , 'DescrizioneReparto':'Organizza la Produzione dei Mattoncini'} , 
                                                        {'ID_TipoReparto':3 , 'NomeReparto':'Contabilita' , 'DescrizioneReparto':'Gestisce i conti'} , 
                                                        {'ID_TipoReparto':4 , 'NomeReparto':'Magazzino' , 'DescrizioneReparto':'Controlla lo stoccaggio'}])

  resultrep = conn.execute(Table.insert(Reparto), [ {'ID_Reparto':1,'NomeReparto':1,'DescrizioneReparto':'UfficioCentrale','TelefonoReparto':577898898,'EmailReparto':'personale1@bricklink.it','CodiceSede':1} , 
                                                    {'ID_Reparto':2,'NomeReparto':1,'DescrizioneReparto':'SedeDistaccataPaghe','TelefonoReparto':577587142,'EmailReparto':'personale2@bricklink.it','CodiceSede':2} , 
                                                    {'ID_Reparto':3,'NomeReparto':1,'DescrizioneReparto':'ControlloOrari','TelefonoReparto':577123698,'EmailReparto':'personale3@bricklink.it','CodiceSede':3} , 
                                                    {'ID_Reparto':4,'NomeReparto':1,'DescrizioneReparto':'Permessi','TelefonoReparto':577444555,'EmailReparto':'personale4@bricklink.it','CodiceSede':4} , 
                                                    {'ID_Reparto':5,'NomeReparto':4,'DescrizioneReparto':'Fabbrica','TelefonoReparto':577898897,'EmailReparto':'produzione1@bricklink.it','CodiceSede':1} , 
                                                    {'ID_Reparto':6,'NomeReparto':3,'DescrizioneReparto':'Bilancio','TelefonoReparto':577898896,'EmailReparto':'contabilita1@bricklink.it','CodiceSede':1} , 
                                                    {'ID_Reparto':7,'NomeReparto':3,'DescrizioneReparto':'Entrate','TelefonoReparto':577587143,'EmailReparto':'contabilita2@bricklink.it','CodiceSede':2} , 
                                                    {'ID_Reparto':8,'NomeReparto':3,'DescrizioneReparto':'Spese','TelefonoReparto':577123699,'EmailReparto':'contabilita3@bricklink.it','CodiceSede':3} , 
                                                    {'ID_Reparto':9,'NomeReparto':2,'DescrizioneReparto':'Stoccaggio','TelefonoReparto':577812547,'EmailReparto':'magazzino1@bricklink.it','CodiceSede':1} , 
                                                    {'ID_Reparto':10,'NomeReparto':2,'DescrizioneReparto':'Appoggio','TelefonoReparto':577155874,'EmailReparto':'magazzino2@bricklink.it','CodiceSede':4}])

  resultvla = conn.execute(Table.insert(Vlan), [ {'ID_Vlan':1,'DescrizioneVlan':'Contabilita'} , 
                                                 {'ID_Vlan':2,'DescrizioneVlan':'Produzione'} , 
                                                 {'ID_Vlan':3,'DescrizioneVlan':'Legale'} , 
                                                 {'ID_Vlan':4,'DescrizioneVlan':'Spedizioni'} , 
                                                 {'ID_Vlan':5,'DescrizioneVlan':'Personale'}])

  resultpar = conn.execute(Table.insert(Partecipa), [ {'ID_Partecipa':1,'ID_vlan':1,'ID_reparto':6,'Motivo':'Contabilita'} , 
                                                      {'ID_Partecipa':2,'ID_vlan':1,'ID_reparto':7,'Motivo':'Contabilita'} , 
                                                      {'ID_Partecipa':3,'ID_vlan':1,'ID_reparto':8,'Motivo':'Contabilita'} , 
                                                      {'ID_Partecipa':4,'ID_vlan':5,'ID_reparto':6,'Motivo':'FarePaghe'} , 
                                                      {'ID_Partecipa':5,'ID_vlan':5,'ID_reparto':1,'Motivo':'Personale'} , 
                                                      {'ID_Partecipa':6,'ID_vlan':5,'ID_reparto':2,'Motivo':'Personale'} , 
                                                      {'ID_Partecipa':7,'ID_vlan':5,'ID_reparto':3,'Motivo':'Personale'} , 
                                                      {'ID_Partecipa':8,'ID_vlan':5,'ID_reparto':4,'Motivo':'Personale'}])

  resultmag = conn.execute(Table.insert(Magazzino), [ {'ID_Magazzino':1,'ID_Reparto':9,'PosizioneScaffale':12} , 
                                                      {'ID_Magazzino':2,'ID_Reparto':9,'PosizioneScaffale':15} , 
                                                      {'ID_Magazzino':3,'ID_Reparto':9,'PosizioneScaffale':18} , 
                                                      {'ID_Magazzino':4,'ID_Reparto':9,'PosizioneScaffale':21} , 
                                                      {'ID_Magazzino':5,'ID_Reparto':9,'PosizioneScaffale':24} , 
                                                      {'ID_Magazzino':6,'ID_Reparto':9,'PosizioneScaffale':27} , 
                                                      {'ID_Magazzino':7,'ID_Reparto':9,'PosizioneScaffale':30} , 
                                                      {'ID_Magazzino':8,'ID_Reparto':9,'PosizioneScaffale':33} , 
                                                      {'ID_Magazzino':9,'ID_Reparto':9,'PosizioneScaffale':36} , 
                                                      {'ID_Magazzino':10,'ID_Reparto':10,'PosizioneScaffale':5} , 
                                                      {'ID_Magazzino':11,'ID_Reparto':10,'PosizioneScaffale':10} , 
                                                      {'ID_Magazzino':12,'ID_Reparto':10,'PosizioneScaffale':15} , 
                                                      {'ID_Magazzino':13,'ID_Reparto':10,'PosizioneScaffale':20} , 
                                                      {'ID_Magazzino':14,'ID_Reparto':10,'PosizioneScaffale':25} , 
                                                      {'ID_Magazzino':15,'ID_Reparto':10,'PosizioneScaffale':30}])

  resultspr = conn.execute(Table.insert(SetPronto), [ {'ID_SetPronto':1,'NomeSet':'Friends','DescrizioneSet':'Per giocare con gli amici','EtaConsigliata':6,'QuantitaDisponibile':9,'ID_Magazzino':9} , 
                                                      {'ID_SetPronto':2,'NomeSet':'Frozen','DescrizioneSet':'Il castello di Elsa','EtaConsigliata':6,'QuantitaDisponibile':4,'ID_Magazzino':3} , 
                                                      {'ID_SetPronto':3,'NomeSet':'Rollercoaster','DescrizioneSet':'Bellissime montagne russe','EtaConsigliata':15,'QuantitaDisponibile':5,'ID_Magazzino':1} , 
                                                      {'ID_SetPronto':4,'NomeSet':'MillenniumFalcon','DescrizioneSet':'il set più ricercato','EtaConsigliata':8,'QuantitaDisponibile':12,'ID_Magazzino':5} , 
                                                      {'ID_SetPronto':5,'NomeSet':'StrangerThings','DescrizioneSet':'Il sottosopra','EtaConsigliata':12,'QuantitaDisponibile':35,'ID_Magazzino':7} , 
                                                      {'ID_SetPronto':6,'NomeSet':'Nintendo','DescrizioneSet':'La console anni 90','EtaConsigliata':5,'QuantitaDisponibile':11,'ID_Magazzino':12} , 
                                                      {'ID_SetPronto':7,'NomeSet':'JurassicPark','DescrizioneSet':'Rivivi le emozioni del Trex','EtaConsigliata':11,'QuantitaDisponibile':9,'ID_Magazzino':13} , 
                                                      {'ID_SetPronto':8,'NomeSet':'TrenoPasseggeri','DescrizioneSet':'Il treno city con i passeggeri','EtaConsigliata':3,'QuantitaDisponibile':0,'ID_Magazzino':4} , 
                                                      {'ID_SetPronto':9,'NomeSet':'TrenoMerci','DescrizioneSet':'I vagoni per il trasporto del carbone','EtaConsigliata':4,'QuantitaDisponibile':3,'ID_Magazzino':2}])

  resultscol = conn.execute(Table.insert(Colore), [ {'ID_Colore':1,'Nome':'Grigio','Esadecimale':'808080','R':128,'G':128,'B':128} , 
                                                    {'ID_Colore':2,'Nome':'Argento','Esadecimale':'c0c0c0','R':192,'G':192,'B':192} , 
                                                    {'ID_Colore':3,'Nome':'Beige','Esadecimale':'f5f5dc','R':245,'G':245,'B':220} , 
                                                    {'ID_Colore':4,'Nome':'Marrone','Esadecimale':'800000','R':128,'G':0,'B':0} , 
                                                    {'ID_Colore':5,'Nome':'Lime','Esadecimale':'00ff00','R':0,'G':255,'B':0} , 
                                                    {'ID_Colore':6,'Nome':'Verde','Esadecimale':'008000','R':0,'G':128,'B':0} , 
                                                    {'ID_Colore':7,'Nome':'Acquamarina','Esadecimale':'7fffd4','R':127,'G':255,'B':212}])

  resultsbri = conn.execute(Table.insert(Brick), [ {'ID_Brick':1,'Tipologia':'1x1','ID_Colore':1,'QuantitaDisponibile':200,'ID_Magazzino':1} , 
                                                   {'ID_Brick':2,'Tipologia':'2x1','ID_Colore':2,'QuantitaDisponibile':250,'ID_Magazzino':1} , 
                                                   {'ID_Brick':3,'Tipologia':'3x1','ID_Colore':3,'QuantitaDisponibile':125,'ID_Magazzino':1} , 
                                                   {'ID_Brick':4,'Tipologia':'4x1','ID_Colore':4,'QuantitaDisponibile':800,'ID_Magazzino':1} , 
                                                   {'ID_Brick':5,'Tipologia':'5x1','ID_Colore':5,'QuantitaDisponibile':320,'ID_Magazzino':1} , 
                                                   {'ID_Brick':6,'Tipologia':'6x1','ID_Colore':6,'QuantitaDisponibile':0,'ID_Magazzino':1} , 
                                                   {'ID_Brick':7,'Tipologia':'2x2','ID_Colore':7,'QuantitaDisponibile':36,'ID_Magazzino':9} , 
                                                   {'ID_Brick':8,'Tipologia':'2x3','ID_Colore':1,'QuantitaDisponibile':158,'ID_Magazzino':11} , 
                                                   {'ID_Brick':9,'Tipologia':'2x4','ID_Colore':2,'QuantitaDisponibile':54,'ID_Magazzino':12} , 
                                                   {'ID_Brick':10,'Tipologia':'2x5','ID_Colore':3,'QuantitaDisponibile':22,'ID_Magazzino':13} , 
                                                   {'ID_Brick':11,'Tipologia':'2x6','ID_Colore':4,'QuantitaDisponibile':125,'ID_Magazzino':15} , 
                                                   {'ID_Brick':12,'Tipologia':'3x3','ID_Colore':5,'QuantitaDisponibile':135,'ID_Magazzino':2} , 
                                                   {'ID_Brick':13,'Tipologia':'3x4','ID_Colore':6,'QuantitaDisponibile':160,'ID_Magazzino':10} , 
                                                   {'ID_Brick':14,'Tipologia':'3x5','ID_Colore':7,'QuantitaDisponibile':150,'ID_Magazzino':14} , 
                                                   {'ID_Brick':15,'Tipologia':'3x6','ID_Colore':1,'QuantitaDisponibile':222,'ID_Magazzino':6} , 
                                                   {'ID_Brick':16,'Tipologia':'4x4','ID_Colore':2,'QuantitaDisponibile':98,'ID_Magazzino':6} , 
                                                   {'ID_Brick':17,'Tipologia':'4x5','ID_Colore':3,'QuantitaDisponibile':55,'ID_Magazzino':6} , 
                                                   {'ID_Brick':18,'Tipologia':'4x6','ID_Colore':4,'QuantitaDisponibile':40,'ID_Magazzino':3} , 
                                                   {'ID_Brick':19,'Tipologia':'5x5','ID_Colore':5,'QuantitaDisponibile':140,'ID_Magazzino':2} , 
                                                   {'ID_Brick':20,'Tipologia':'5x6','ID_Colore':6,'QuantitaDisponibile':400,'ID_Magazzino':11} , 
                                                   {'ID_Brick':21,'Tipologia':'6x6','ID_Colore':7,'QuantitaDisponibile':235,'ID_Magazzino':5}])

  resultscom = conn.execute(Table.insert(Composto), [ {'ID_Composizione':1,'ID_SetPronto':1,'ID_Brick':2,'Numero':8} , 
                                                      {'ID_Composizione':2,'ID_SetPronto':1,'ID_Brick':3,'Numero':55} , 
                                                      {'ID_Composizione':3,'ID_SetPronto':1,'ID_Brick':4,'Numero':21} , 
                                                      {'ID_Composizione':4,'ID_SetPronto':2,'ID_Brick':12,'Numero':140} , 
                                                      {'ID_Composizione':5,'ID_SetPronto':2,'ID_Brick':5,'Numero':66} , 
                                                      {'ID_Composizione':6,'ID_SetPronto':3,'ID_Brick':6,'Numero':87} , 
                                                      {'ID_Composizione':7,'ID_SetPronto':3,'ID_Brick':16,'Numero':98} , 
                                                      {'ID_Composizione':8,'ID_SetPronto':3,'ID_Brick':14,'Numero':12} , 
                                                      {'ID_Composizione':9,'ID_SetPronto':4,'ID_Brick':19,'Numero':46} , 
                                                      {'ID_Composizione':10,'ID_SetPronto':4,'ID_Brick':20,'Numero':87} , 
                                                      {'ID_Composizione':11,'ID_SetPronto':4,'ID_Brick':14,'Numero':47}])

  resultsper = conn.execute(Table.insert(Permessi), [ {'ID_Permessi':1,'Ferie':27,'Studio':6,'Visite':3,'centoquattro':25} , 
                                                      {'ID_Permessi':2,'Ferie':28,'Studio':6,'Visite':3,'centoquattro':28} , 
                                                      {'ID_Permessi':3,'Ferie':29,'Studio':7,'Visite':3,'centoquattro':35} , 
                                                      {'ID_Permessi':4,'Ferie':30,'Studio':7,'Visite':4,'centoquattro':38} , 
                                                      {'ID_Permessi':5,'Ferie':31,'Studio':8,'Visite':4,'centoquattro':45} , 
                                                      {'ID_Permessi':6,'Ferie':32,'Studio':8,'Visite':4,'centoquattro':48}])

  resultscat = conn.execute(Table.insert(Categoria), [ {'ID_Categoria':1,'Max_Stipendio':1600.00,'Min_Stipendio':1300.00,'PermessiCategoria':1,'DescrizioneCategoria':'A'} , 
                                                       {'ID_Categoria':2,'Max_Stipendio':1700.00,'Min_Stipendio':1400.00,'PermessiCategoria':2,'DescrizioneCategoria':'A3'} , 
                                                       {'ID_Categoria':3,'Max_Stipendio':1800.00,'Min_Stipendio':1400.00,'PermessiCategoria':2,'DescrizioneCategoria':'B'} , 
                                                       {'ID_Categoria':4,'Max_Stipendio':1900.00,'Min_Stipendio':1600.00,'PermessiCategoria':3,'DescrizioneCategoria':'B3'} , 
                                                       {'ID_Categoria':5,'Max_Stipendio':2000.00,'Min_Stipendio':1650.00,'PermessiCategoria':4,'DescrizioneCategoria':'C'} , 
                                                       {'ID_Categoria':6,'Max_Stipendio':2100.00,'Min_Stipendio':1800.00,'PermessiCategoria':5,'DescrizioneCategoria':'C6'} , 
                                                       {'ID_Categoria':7,'Max_Stipendio':2300.00,'Min_Stipendio':2000.00,'PermessiCategoria':6,'DescrizioneCategoria':'D'} , 
                                                       {'ID_Categoria':8,'Max_Stipendio':5000.00,'Min_Stipendio':2100.00,'PermessiCategoria':6,'DescrizioneCategoria':'D3'}])

  resultsora = conn.execute(Table.insert(Orario), [ {'ID_Orario':1,'OreSettimanali':36,'OrarioIngresso':'08:00:00','OrarioUscita':'16:00:00','Flessibilita':30,'Max_Straordinari':10,'Max_OreAssenza':15} , 
                                                    {'ID_Orario':2,'OreSettimanali':36,'OrarioIngresso':'16:00:00','OrarioUscita':'00:00:00','Flessibilita':30,'Max_Straordinari':10,'Max_OreAssenza':15} , 
                                                    {'ID_Orario':3,'OreSettimanali':38,'OrarioIngresso':'08:00:00','OrarioUscita':'16:00:00','Flessibilita':15,'Max_Straordinari':15,'Max_OreAssenza':15} , 
                                                    {'ID_Orario':4,'OreSettimanali':38,'OrarioIngresso':'16:00:00','OrarioUscita':'00:00:00','Flessibilita':15,'Max_Straordinari':15,'Max_OreAssenza':15} , 
                                                    {'ID_Orario':5,'OreSettimanali':39,'OrarioIngresso':'08:00:00','OrarioUscita':'16:00:00','Flessibilita':20,'Max_Straordinari':20,'Max_OreAssenza':10} , 
                                                    {'ID_Orario':6,'OreSettimanali':39,'OrarioIngresso':'16:00:00','OrarioUscita':'00:00:00','Flessibilita':20,'Max_Straordinari':20,'Max_OreAssenza':10} , 
                                                    {'ID_Orario':7,'OreSettimanali':40,'OrarioIngresso':'08:00:00','OrarioUscita':'16:00:00','Flessibilita':45,'Max_Straordinari':25,'Max_OreAssenza':30} , 
                                                    {'ID_Orario':8,'OreSettimanali':40,'OrarioIngresso':'16:00:00','OrarioUscita':'00:00:00','Flessibilita':45,'Max_Straordinari':25,'Max_OreAssenza':30}])

  resultssti = conn.execute(Table.insert(Stipendio), [ {'ID_Stipendio':1,'Cifra':1403.16,'Straordinari':10} , 
                                                       {'ID_Stipendio':2,'Cifra':1516.18,'Straordinari':12} ,
                                                       {'ID_Stipendio':3,'Cifra':1625.33,'Straordinari':8} ,
                                                       {'ID_Stipendio':4,'Cifra':1835.24,'Straordinari':10} ,
                                                       {'ID_Stipendio':5,'Cifra':2010.10,'Straordinari':20} ,
                                                       {'ID_Stipendio':6,'Cifra':2125.42,'Straordinari':10} ,
                                                       {'ID_Stipendio':7,'Cifra':2518.18,'Straordinari':21} ,
                                                       {'ID_Stipendio':8,'Cifra':4025.36,'Straordinari':20} ,
                                                       {'ID_Stipendio':9,'Cifra':3126.18,'Straordinari':20}])

  resultspers = conn.execute(Table.insert(Persona), [ {'ID_Persona':1,'Nome':'Luca','Cognome':'Pacchierotti','Residenza':5,'Civico':1,'CodiceFiscale':'BFGRVQ55P15A363O','Sesso':'m','E_mail':'a@bricklink.it','Cellulare':'3333381245','DataNascita':'1985-02-16','LuogoNascita':3,'ID_Reparto':1} ,  
                                                      {'ID_Persona':2,'Nome':'Mino','Cognome':'Reitano','Residenza':6,'Civico':6,'CodiceFiscale':'DQRNBM64D12H531H','Sesso':'m','E_mail':'b@bricklink.it','Cellulare':'3333381246','DataNascita':'1985-03-24','LuogoNascita':4,'ID_Reparto':2} ,  
                                                      {'ID_Persona':3,'Nome':'Rino','Cognome':'Gaetano','Residenza':7,'Civico':78,'CodiceFiscale':'ZBTTNI33C63A071R','Sesso':'m','E_mail':'c@bricklink.it','Cellulare':'3333381247','DataNascita':'1959-07-17','LuogoNascita':5,'ID_Reparto':3} ,  
                                                      {'ID_Persona':4,'Nome':'Claudio','Cognome':'Baglioni','Residenza':8,'Civico':45,'CodiceFiscale':'FRRDVH94P61F607Z','Sesso':'m','E_mail':'d@bricklink.it','Cellulare':'3333381248','DataNascita':'1973-12-14','LuogoNascita':6,'ID_Reparto':5} ,  
                                                      {'ID_Persona':5,'Nome':'Gianna','Cognome':'Nannini','Residenza':9,'Civico':32,'CodiceFiscale':'ZCRMHF95H03H011W','Sesso':'f','E_mail':'e@bricklink.it','Cellulare':'3333381249','DataNascita':'1992-08-03','LuogoNascita':7,'ID_Reparto':6} ,  
                                                      {'ID_Persona':6,'Nome':'Alessio','Cognome':'Spezia','Residenza':10,'Civico':44,'CodiceFiscale':'MNHDCK62M06C848E','Sesso':'m','E_mail':'alessiospezia@gmail.com','Cellulare':'3333381250','DataNascita':'1982-11-25','LuogoNascita':8,'ID_Reparto':None} ,  
                                                      {'ID_Persona':7,'Nome':'Mbala','Cognome':'Nzola','Residenza':11,'Civico':55,'CodiceFiscale':'FYFGMX36P42A396X','Sesso':'m','E_mail':'mbalaspezia@gmail.com','Cellulare':'3333381251','DataNascita':'1975-04-12','LuogoNascita':9,'ID_Reparto':None} ,  
                                                      {'ID_Persona':8,'Nome':'Niccolo','Cognome':'Machiavelli','Residenza':12,'Civico':66,'CodiceFiscale':'DLRVKT62M42G020S','Sesso':'m','E_mail':'niccolocarte@libero.it','Cellulare':'3333381252','DataNascita':'1986-09-30','LuogoNascita':10,'ID_Reparto':None} ,  
                                                      {'ID_Persona':9,'Nome':'Andrea','Cognome':'Orario','Residenza':7,'Civico':45,'CodiceFiscale':'ZCTENI33C63A571R','Sesso':'f','E_mail':'andrea@hotmai.it','Cellulare':'5455545455','DataNascita':'1988-03-30','LuogoNascita':7,'ID_Reparto':None}])  
                                                      
  resultsdip = conn.execute(Table.insert(Dipendente), [ {'ID_Dipendente':1,'ID_Persona':1,'ID_Responsabile':1,'isResponsabile':1,'ID_Orario':3,'ID_Stipendio':8,'ID_Categoria':8} , 
                                                        {'ID_Dipendente':2,'ID_Persona':2,'ID_Responsabile':1,'isResponsabile':0,'ID_Orario':4,'ID_Stipendio':2,'ID_Categoria':3} , 
                                                        {'ID_Dipendente':3,'ID_Persona':3,'ID_Responsabile':1,'isResponsabile':0,'ID_Orario':5,'ID_Stipendio':3,'ID_Categoria':4} ,   
                                                        {'ID_Dipendente':4,'ID_Persona':4,'ID_Responsabile':1,'isResponsabile':0,'ID_Orario':6,'ID_Stipendio':4,'ID_Categoria':5} ,                                                         
                                                        {'ID_Dipendente':5,'ID_Persona':5,'ID_Responsabile':1,'isResponsabile':0,'ID_Orario':7,'ID_Stipendio':5,'ID_Categoria':7}])

  resultsacq = conn.execute(Table.insert(Acquirente), [ {'ID_Acquirente':1,'CartaCredito':'5957469592594597','PIN':12345,'Gradimento':8,'ID_Persona':6} , 
                                                        {'ID_Acquirente':2,'CartaCredito':'6333966253986332','PIN':23456,'Gradimento':7,'ID_Persona':7} , 
                                                        {'ID_Acquirente':3,'CartaCredito':'9698468633634438','PIN':12345,'Gradimento':4,'ID_Persona':8} ,   
                                                        {'ID_Acquirente':4,'CartaCredito':'9695439935434541','PIN':13333,'Gradimento':6,'ID_Persona':9}])

  resultsvene = conn.execute(Table.insert(Vendite), [ {'ID_Vendita':1,'TassazioneIVA':22,'PrezzoTotale':200.50,'ScontoProgressivo':2,'ID_Acquirente':1,'DataVendita':'2023-05-08','ID_Dipendente':1,'ID_Transazione':'xderer45getrgt'} ,  
                                                      {'ID_Vendita':2,'TassazioneIVA':18,'PrezzoTotale':150.67,'ScontoProgressivo':5,'ID_Acquirente':1,'DataVendita':'2023-04-12','ID_Dipendente':1,'ID_Transazione':'ggtgetrg54356'} ,  
                                                      {'ID_Vendita':3,'TassazioneIVA':22,'PrezzoTotale':180.00,'ScontoProgressivo':6,'ID_Acquirente':2,'DataVendita':'2023-01-12','ID_Dipendente':2,'ID_Transazione':'5365grhte566'} ,  
                                                      {'ID_Vendita':4,'TassazioneIVA':22,'PrezzoTotale':200.00,'ScontoProgressivo':0,'ID_Acquirente':3,'DataVendita':'2022-12-18','ID_Dipendente':2,'ID_Transazione':'etget6356hhh'} ,  
                                                      {'ID_Vendita':5,'TassazioneIVA':0,'PrezzoTotale':865.00,'ScontoProgressivo':10,'ID_Acquirente':4,'DataVendita':'2022-11-19','ID_Dipendente':3,'ID_Transazione':'trey321bg56'} ,  
                                                      {'ID_Vendita':6,'TassazioneIVA':10,'PrezzoTotale':321.50,'ScontoProgressivo':2,'ID_Acquirente':3,'DataVendita':'2022-11-25','ID_Dipendente':4,'ID_Transazione':'heeter657hyh'} ,  
                                                      {'ID_Vendita':7,'TassazioneIVA':15,'PrezzoTotale':1500.20,'ScontoProgressivo':15,'ID_Acquirente':2,'DataVendita':'2223-12-18','ID_Dipendente':5,'ID_Transazione':'beety652sfgf'} ,  
                                                      {'ID_Vendita':8,'TassazioneIVA':22,'PrezzoTotale':55.30,'ScontoProgressivo':0,'ID_Acquirente':1,'DataVendita':'2019-05-05','ID_Dipendente':1,'ID_Transazione':'tgt6898bgsw3'} ,  
                                                      {'ID_Vendita':9,'TassazioneIVA':22,'PrezzoTotale':120.60,'ScontoProgressivo':0,'ID_Acquirente':4,'DataVendita':'2023-01-15','ID_Dipendente':5,'ID_Transazione':'hyehy776hyh'} ,  
                                                      {'ID_Vendita':10,'TassazioneIVA':10,'PrezzoTotale':920.00,'ScontoProgressivo':10,'ID_Acquirente':2,'DataVendita':'2022-12-17','ID_Dipendente':4,'ID_Transazione':'hyhe356hyhe'}])  
                                                        
  resultsveno = conn.execute(Table.insert(Venduto), [ {'ID_Venduto':1,'ID_Vendita':1,'ID_SetPronto':1,'Prezzo':106.10} , 
                                                      {'ID_Venduto':2,'ID_Vendita':1,'ID_SetPronto':1,'Prezzo':25.53} , 
                                                      {'ID_Venduto':3,'ID_Vendita':1,'ID_SetPronto':2,'Prezzo':68.87} , 
                                                      {'ID_Venduto':4,'ID_Vendita':2,'ID_SetPronto':4,'Prezzo':52.00} , 
                                                      {'ID_Venduto':5,'ID_Vendita':2,'ID_SetPronto':3,'Prezzo':98.67} , 
                                                      {'ID_Venduto':6,'ID_Vendita':3,'ID_SetPronto':5,'Prezzo':80.00} , 
                                                      {'ID_Venduto':7,'ID_Vendita':3,'ID_SetPronto':5,'Prezzo':100.00} , 
                                                      {'ID_Venduto':8,'ID_Vendita':4,'ID_SetPronto':9,'Prezzo':200.00} , 
                                                      {'ID_Venduto':9,'ID_Vendita':5,'ID_SetPronto':4,'Prezzo':865.00} , 
                                                      {'ID_Venduto':10,'ID_Vendita':6,'ID_SetPronto':3,'Prezzo':290.00} , 
                                                      {'ID_Venduto':11,'ID_Vendita':6,'ID_SetPronto':8,'Prezzo':31.50} , 
                                                      {'ID_Venduto':12,'ID_Vendita':7,'ID_SetPronto':5,'Prezzo':1500.20} , 
                                                      {'ID_Venduto':13,'ID_Vendita':8,'ID_SetPronto':2,'Prezzo':50.30} , 
                                                      {'ID_Venduto':14,'ID_Vendita':8,'ID_SetPronto':1,'Prezzo':5.00} , 
                                                      {'ID_Venduto':15,'ID_Vendita':9,'ID_SetPronto':6,'Prezzo':120.60} , 
                                                      {'ID_Venduto':16,'ID_Vendita':10,'ID_SetPronto':2,'Prezzo':920.00}])

  resultsspe = conn.execute(Table.insert(Spedizione), [ {'ID_Spedizione':1,'ID_Acquirente':1,'TempiSpedizione':7200,'SpeseSpedizione':10.00,'Giorno':'2023-05-08'} ,                                                       
                                                        {'ID_Spedizione':2,'ID_Acquirente':2,'TempiSpedizione':7200,'SpeseSpedizione':8.65,'Giorno':'2023-04-13'} ,
                                                        {'ID_Spedizione':3,'ID_Acquirente':3,'TempiSpedizione':3600,'SpeseSpedizione':18.20,'Giorno':'2022-12-19'} ,                                                       
                                                        {'ID_Spedizione':4,'ID_Acquirente':4,'TempiSpedizione':5400,'SpeseSpedizione':12.00,'Giorno':'2022-11-20'} ,
                                                        {'ID_Spedizione':5,'ID_Acquirente':2,'TempiSpedizione':9000,'SpeseSpedizione':15.00,'Giorno':'2022-12-18'} ,                                                       
                                                        {'ID_Spedizione':6,'ID_Acquirente':4,'TempiSpedizione':5400,'SpeseSpedizione':6.35,'Giorno':'2023-01-17'}])

  resultsinv = conn.execute(Table.insert(Inviato), [ {'ID_Invio':1,'ID_Vendita':1,'ID_Spedizione':1} , 
                                                     {'ID_Invio':2,'ID_Vendita':2,'ID_Spedizione':1} , 
                                                     {'ID_Invio':3,'ID_Vendita':3,'ID_Spedizione':2} , 
                                                     {'ID_Invio':4,'ID_Vendita':7,'ID_Spedizione':2} , 
                                                     {'ID_Invio':5,'ID_Vendita':4,'ID_Spedizione':3} , 
                                                     {'ID_Invio':6,'ID_Vendita':6,'ID_Spedizione':3} , 
                                                     {'ID_Invio':7,'ID_Vendita':5,'ID_Spedizione':4} , 
                                                     {'ID_Invio':8,'ID_Vendita':10,'ID_Spedizione':5} , 
                                                     {'ID_Invio':9,'ID_Vendita':9,'ID_Spedizione':6}])

  conn.commit()    
  return (True)
  
  
def inserimentomanuale(engine,a):
  """
  Funzione che Inserisce Record Scelti
  """
  from sqlalchemy.sql import select, asc, desc
  from sqlalchemy.orm import sessionmaker

  conn = engine.connect()
  a = int(a)
  Session = close_all_sessions()
  Session = sessionmaker(bind = engine)
  session = Session()
  
  if (a==1):

            #creo le varie query per aggiungere, e poi con la session add_all e commit le eseguo sul db e mostro la tabella aggiornata (visibile anche dal menu visualizza 
    print("\n Attenzione, per creare una sede sarà necessario inserire prima la dipendenza nella tabella Residenza e Citta per l'indirizzo\n\
           Verranno inserite due sedi, 1 con un indirizzo già valido, 1 in cui verrà aggiunto")
    c1 = Sede(NomeSede  = 'Palazzo dei Priori', IP_Sede = '10.75.72.201', ViaSede = 11 , CivicoSede = 33)
    c2 = Citta(NomeCitta = 'Napoli', CapCitta = 34321)
    c3 = Residenza(ID_Citta = 13, Via = 'Della Peronospora')
    c4 = Sede(NomeSede  = 'Poggio a Caiano', IP_Sede = '10.76.72.201', ViaSede = 13, CivicoSede = 55)
    session.add_all([c1, c2, c3, c4])
    session.commit()
   
    print("Tabella Sede Aggiornata:\n")
    for s, c, r in session.query(Sede , Citta, Residenza
    ).filter(Sede.ViaSede == Residenza.ID_Residenza
    ).filter(Residenza.ID_Citta == Citta.ID_Citta
    ).order_by(Sede.ID_Sede
    ).all():
      print ("ID: {} Sede: {} IP: {} Via: {} {} {} {} E-mail: {}".
      format(s.ID_Sede, s.NomeSede, s.IP_Sede, r.Via, s.CivicoSede, c.NomeCitta, c.CapCitta, s.E_mailSede))
 
  elif (a==2):
    c1 = Persona(Nome = 'Alberto',Cognome='Camerini', Residenza=10,Civico=5,CodiceFiscale='OOORRR54K876G',Sesso='m',E_mail='ac@mtv.it',Cellulare=3453453451,DataNascita='1965-07-07',LuogoNascita=2,ID_Reparto=2)
    c2 = Dipendente(ID_Persona  = 10, ID_Responsabile=1, isResponsabile = 0, ID_Orario = 4 , ID_Stipendio = 6, ID_Categoria = 5)
    session.add_all([c1, c2])
    session.commit()
   
    print("Tabella Dipendenti Aggiornata:\n")
    for d, p in session.query(Dipendente , Persona
    ).filter(Dipendente.ID_Persona == Persona.ID_Persona
    ).order_by(Dipendente.ID_Dipendente
    ).all():
      print ("ID: {} Nome: {} Cognome: {} Cellulare: {} E-mail: {}".
      format(d.ID_Dipendente, p.Nome, p.Cognome, p.Cellulare, p.E_mail))
 
  elif (a==3):
    c1 = SetPronto(NomeSet = 'Helicarrier',DescrizioneSet='Avengers', EtaConsigliata=10,QuantitaDisponibile=5,ID_Magazzino=9)
    session.add(c1)
    session.commit()
   
    print("Tabella dei Set Aggiornata:\n")
    for d in session.query(SetPronto
    ).order_by(SetPronto.ID_SetPronto
    ).all():
      print ("ID: {} Nome: {} Descrizione: {} Quantità: {} Età Consigliata: {}".
      format(d.ID_SetPronto, d.NomeSet, d.DescrizioneSet, d.QuantitaDisponibile, d.EtaConsigliata))
   
  elif (a==4):
    c1 = Server(DescrizioneServer='Server Multimediale',IP_Server='10.74.55.83',ID_Sede=4)
    c2 = Vlan(DescrizioneVlan = 'Affari Legali')
    session.add_all([c1, c2])
    session.commit()
   
    print("Tabella Server Aggiornata:\n")
    for d in session.query(Server
    ).order_by(Server.ID_Server
    ).all():
      print ("ID: {} Descrizione: {} IP:{}".format(d.ID_Server, d.DescrizioneServer, d.IP_Server))
    print("Tabella Vlan Aggiornata:\n")
    for d in session.query(Vlan
    ).order_by(Vlan.ID_Vlan
    ).all():
      print ("ID: {} Vlan: {}".format(d.ID_Vlan, d.DescrizioneVlan))
  elif (a==5):
    pass
  else:
    print("Hai inserito un carattere non ammesso. \n")
    
  return (True)