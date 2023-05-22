from sqlalchemy import create_engine, func
from funzioni.inseriscitabelle import Citta, Residenza, Sede, Server, Accedea, Serveraccessi, Tiporeparto, Reparto, Vlan, Partecipa, Magazzino, SetPronto, Colore
from funzioni.inseriscitabelle import Brick, Composto, Permessi, Categoria, Orario, Stipendio, Persona, Dipendente, Acquirente, Vendite, Venduto, Spedizione, Inviato
from sqlalchemy.sql import select, asc, desc
from sqlalchemy.orm import sessionmaker, close_all_sessions
from datetime import datetime, date

def aggiornadatotabella(engine,a):
  a = int(a)
  Session = close_all_sessions()
  Session = sessionmaker(bind = engine)
  session = Session()

  if (a==1):
    print("Record Precedente:\n")
    for s, r in session.query(Sede , Server
    ).filter(Sede.ID_Sede == Server.ID_Sede
    ).filter(Server.DescrizioneServer == "FileServer"
    ).order_by(Server.ID_Server
    ).all():
      print ("ID: {} Server: {} IP: {} Sede: {}".
      format(r.ID_Server, r.DescrizioneServer, r.IP_Server, s.NomeSede))
    session.query(Server
    ).filter(Server.DescrizioneServer == "FileServer"
    ).update({Server.IP_Server:"10.70.55.38"}) 
    session.commit()
    print("Record aggiornato:\n")                                #Visualizzo la riga aggiornata
    for s, r in session.query(Sede , Server
    ).filter(Sede.ID_Sede == Server.ID_Sede
    ).filter(Server.DescrizioneServer == "FileServer"
    ).order_by(Server.ID_Server
    ).all():
      print ("ID: {} Server: {} IP: {} Sede: {}".
      format(r.ID_Server, r.DescrizioneServer, r.IP_Server, s.NomeSede))     
  elif (a==2):
    print("Tabella Stipendi Precedente:\n")
    for s in session.query(Stipendio 
    ).order_by(Stipendio.ID_Stipendio
    ).all():
      print ("ID: {} Stipendio: {} Ore Straordinari Max: {}".
      format(s.ID_Stipendio, s.Cifra, s.Straordinari))
    session.query(Stipendio
    ).update({Stipendio.Cifra:Stipendio.Cifra*2}) 
    session.commit()
    print("\nTabella Stato attuale:\n")                          #Visualizzo la riga aggiornata
    for s in session.query(Stipendio 
    ).order_by(Stipendio.ID_Stipendio
    ).all():
      print ("ID: {} Stipendio: {} Ore Straordinari Max: {}".
      format(s.ID_Stipendio, s.Cifra, s.Straordinari))
  elif (a==3):
    print("Record Precedente:\n")                             #Visualizzo le righe con sede di Siena
    for c, d, e in session.query(Sede , Citta, Residenza
    ).filter(Sede.ViaSede == Residenza.ID_Residenza
    ).filter(Residenza.ID_Citta == Citta.ID_Citta
    ).filter(Citta.NomeCitta == "Siena"
    ).order_by(Sede.ID_Sede
    ).all():
      print ("ID: {} Nome: {} IP: {} E_mail: {} Via: {} {} {} {}".
      format(c.ID_Sede, c.NomeSede, c.IP_Sede, c.E_mailSede, e.Via, c.CivicoSede, d.NomeCitta, d.CapCitta))
    session.query(Sede
    ).filter(Sede.ViaSede == Residenza.ID_Residenza
    ).filter(Residenza.ID_Citta == Citta.ID_Citta
    ).filter(Citta.NomeCitta == "Siena"
    ).update({Sede.NomeSede:"Nuovo Nome Sede Cambiato"}) 
    session.commit()
    print("Record Aggiornato:\n")                               #Visualizzo la riga aggiornata
    for c, d, e in session.query(Sede , Citta, Residenza
    ).filter(Sede.ViaSede == Residenza.ID_Residenza
    ).filter(Residenza.ID_Citta == Citta.ID_Citta
    ).filter(Citta.NomeCitta == "Siena"
    ).order_by(Sede.ID_Sede
    ).all():
      print ("ID: {} Nome: {} IP: {} E_mail: {} Via: {} {} {} {}".
      format(c.ID_Sede, c.NomeSede, c.IP_Sede, c.E_mailSede, e.Via, c.CivicoSede, d.NomeCitta, d.CapCitta))     
  elif (a==4):
    print("Record Precedente:\n")
    for p, c, r in session.query(Persona , Citta, Residenza
    ).filter(Persona.Residenza == Residenza.ID_Residenza
    ).filter(Residenza.ID_Citta == Citta.ID_Citta
    ).filter(Persona.DataNascita < (datetime.strptime("1980-01-01", '%Y-%m-%d').date())
    ).order_by(Persona.ID_Persona
    ).all():
      print ("ID: {} Nome: {} Cognome: {} Residenza: {} {} {} {} CodiceFiscale: {} Cellulare {} E-mail: {} Data di Nascita: {}".
      format(p.ID_Persona, p.Nome, p.Cognome, r.Via, p.Civico, c.NomeCitta, c.CapCitta, p.CodiceFiscale, p.Cellulare, p.E_mail, p.DataNascita))
    session.query(Persona
    ).filter(Persona.DataNascita < (datetime.strptime("1980-01-01", '%Y-%m-%d').date())
    ).update({Persona.CodiceFiscale:"!!!CAMBIATO!!!"}) 
    session.commit()
    print("Record aggiornato:\n")                                #Visualizzo la riga aggiornata
    for p, c, r in session.query(Persona , Citta, Residenza
    ).filter(Persona.Residenza == Residenza.ID_Residenza
    ).filter(Residenza.ID_Citta == Citta.ID_Citta
    ).filter(Persona.DataNascita < (datetime.strptime("1980-01-01", '%Y-%m-%d').date())     
    ).order_by(Persona.ID_Persona
    ).all():
      print ("ID: {} Nome: {} Cognome: {} Residenza: {} {} {} {} CodiceFiscale: {} Cellulare {} E-mail: {} Data di Nascita: {}".
      format(p.ID_Persona, p.Nome, p.Cognome, r.Via, p.Civico, c.NomeCitta, c.CapCitta, p.CodiceFiscale, p.Cellulare, p.E_mail, p.DataNascita))
  elif (a==5):
    pass
  else:
    print("Hai digitato un carattere non ammesso")
  return(a)  