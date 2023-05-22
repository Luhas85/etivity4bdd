from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Time, Float, Date, ForeignKey, inspect
from funzioni.funzioni import Base
from funzioni.inseriscitabelle import Citta, Residenza, Sede, Server, Accedea, Serveraccessi, Tiporeparto, Reparto, Vlan, Partecipa, Magazzino, SetPronto, Colore
from funzioni.inseriscitabelle import Brick, Composto, Permessi, Categoria, Orario, Stipendio, Persona, Dipendente, Acquirente, Vendite, Venduto, Spedizione, Inviato
from sqlalchemy.orm import sessionmaker, close_all_sessions

def cancellatuttodef(engine):
  """
  Questa funzione ispeziona il db e Cancella tutte le tabelle, equivalente del Truncate
  """
  Session = close_all_sessions()
  Base.metadata.reflect(engine)                  #si crea il metadata in base al db attuale, non serve definire le classi
  Base.metadata.drop_all(engine)
    
  return(True)  

def cancelladatotabella(engine,a):
  """
  Funzione che cancella il singolo Record dal db, ci sono 4 delete a scelta dell'utente. Per le chiavi esterne ho messo nelle classi on cascade delete.
  """
  from sqlalchemy.sql import select, asc, desc
  from sqlalchemy.orm import sessionmaker
  
  conn = engine.connect()
  a = int(a)
  Session = sessionmaker(bind = engine)
  session = Session()

  if (a==1):                       #guardo quale caso ha scelto l'utente
    print("Tabella Precedente:\n")                             #Visualizzo la tabella per cancellare la sede di Siena
    for c, d, e in session.query(Sede , Citta, Residenza
    ).filter(Sede.ViaSede == Residenza.ID_Residenza
    ).filter(Residenza.ID_Citta == Citta.ID_Citta
    ).all():
      print ("ID: {} Nome: {} IP: {} E_mail: {} Via: {} {} {} {} ".format(c.ID_Sede, c.NomeSede, c.IP_Sede, c.E_mailSede, e.Via, c.CivicoSede, d.NomeCitta, d.CapCitta))
    session.query(Sede 
    ).filter(Sede.ViaSede == Residenza.ID_Residenza
    ).filter(Residenza.ID_Citta == Citta.ID_Citta
    ).filter(Citta.NomeCitta == "Siena"
    ).delete()
    session.commit()
    print("\nTabella Stato attuale:\n")                          #Visualizzo la tabella aggiornata
    for c, d, e in session.query(Sede , Citta, Residenza
    ).filter(Sede.ViaSede == Residenza.ID_Residenza
    ).filter(Residenza.ID_Citta == Citta.ID_Citta
    ).all():
      print ("ID: {} Nome: {} IP: {} E_mail: {} Via: {} {} {} {} ".format(c.ID_Sede, c.NomeSede, c.IP_Sede, c.E_mailSede, e.Via, c.CivicoSede, d.NomeCitta, d.CapCitta))
      
  elif (a==2):
    print("Tabella Precedente:\n")                             #Visualizzo la tabella per cancellare Luca Pacchierotti
    for c  in session.query(Persona
    ).all():
      print ("ID: {} Nome: {} Cognome: {} CodiceFiscale: {} E-mail: {}".format(c.ID_Persona, c.Nome, c.Cognome, c.CodiceFiscale, c.E_mail))
    session.query(Persona                                    #Cancello il dato
     ).filter(Persona.Nome == "Luca"
     ).filter(Persona.Cognome == "Pacchierotti"
     ).delete()
    session.commit()
    print("\nTabella Stato attuale:\n")                          #Visualizzo la tabella aggiornata
    for c  in session.query(Persona
    ).all():
      print ("ID: {} Nome: {} Cognome: {} CodiceFiscale: {} E-mail: {}".format(c.ID_Persona, c.Nome, c.Cognome, c.CodiceFiscale, c.E_mail))

  elif (a==3):
    print("Tabella Precedente:\n")                             #Visualizzo la tabella per cancellare la Categoria B3
    for c in session.query(Categoria
    ).all():
      print ("ID: {} Max: {} Min: {} Permessi: {} Descrizione: {}".format(c.ID_Categoria, c.Max_Stipendio, c.Min_Stipendio, c.PermessiCategoria, c.DescrizioneCategoria))
    session.query(Categoria                                    #Cancello il dato
     ).filter(Categoria.DescrizioneCategoria == "B3"
     ).delete()
    session.commit()
    print("\nTabella Stato attuale:\n")                          #Visualizzo la tabella aggiornata
    for c in session.query(Categoria      
    ).all():
      print ("ID: {} Max: {} Min: {} Permessi: {} Descrizione: {}".format(c.ID_Categoria, c.Max_Stipendio, c.Min_Stipendio, c.PermessiCategoria, c.DescrizioneCategoria))    

  elif (a==4):
    print("Tabella Precedente:\n")                             #Visualizzo la tabella per cancellare il server. Ci sono relazioni doppie con la tabella accedea
    for c in session.query(Server
    ).all():
      print ("ID: {} Descrizione: {} Ip: {} ID_Sede: {}".format(c.ID_Server, c.DescrizioneServer, c.IP_Server, c.ID_Sede))
    session.query(Server                                       #Cancello il dato
     ).filter(Server.DescrizioneServer == "Domain Controller"
     ).delete()
    session.commit()
    print("\nTabella Stato attuale:\n")                        #Visualizzo la tabella aggiornata
    for c in session.query(Server
    ).all():
      print ("ID: {} Descrizione: {} Ip: {} ID_Sede: {}".format(c.ID_Server, c.DescrizioneServer, c.IP_Server, c.ID_Sede))
  elif (a==5):
    print("Tabella Precedente:\n")                                 #Visualizzo la tabella Inviato prima della cancellazione
    for s, a, p in session.query(Spedizione, Acquirente, Persona
    ).filter(Acquirente.ID_Acquirente == Spedizione.ID_Acquirente
    ).filter(Acquirente.ID_Persona == Persona.ID_Persona
    ).all():
      print ("ID: {} Destinatario: {} {} Giorno Invio: {} Spese di Spedizione: {}".format(s.ID_Spedizione, p.Nome, p.Cognome, s.Giorno, s.SpeseSpedizione))
    Session = close_all_sessions()
    session.query(Spedizione                                          #Cancello il dato
     ).delete()
    session.commit()
    print("\nTabella Stato Attuale:\n")                             #Visualizzo la tabella per cancellare il server. Ci sono relazioni doppie con la tabella accedea
    for s, a, p in session.query(Spedizione, Acquirente, Persona
    ).filter(Acquirente.ID_Acquirente == Spedizione.ID_Acquirente
    ).filter(Acquirente.ID_Persona == Persona.ID_Persona
    ).all():
      print ("ID: {} Destinatario: {} {} Giorno Invio: {} Spese di Spedizione: {}".format(s.ID_Spedizione, p.Nome, p.Cognome, s.Giorno, s.SpeseSpedizione))
  elif (a==6):
    pass
  else:
    print("Hai inserito un carattere non ammesso. \n")
  return(True)  