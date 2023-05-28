from sqlalchemy import create_engine, func
from funzioni.inseriscitabelle import Citta, Residenza, Sede, Server, Accedea, Serveraccessi, Tiporeparto, Reparto, Vlan, Partecipa, Magazzino, SetPronto, Colore
from funzioni.inseriscitabelle import Brick, Composto, Permessi, Categoria, Orario, Stipendio, Persona, Dipendente, Acquirente, Vendite, Venduto, Spedizione, Inviato
from sqlalchemy.sql import select, asc, desc
from sqlalchemy.orm import sessionmaker

def visualizzadatotabella(engine,a):
  """
  Questa funzione permette di eseguire qualche SELECT sul db
  """
  conn = engine.connect()
  a = int(a)
  Session = sessionmaker(bind = engine)
  session = Session()

#ogni IF è una query diversa, sono SELECT su varie tabelle con le chiavi esterne in relazione con le chiavi primarie. Con qualche condizione (il WHERE mysql)
#Cambiano le condizioni di ordinamento e di raggruppamento
#se l'utente inserisce 1, si passa alla visualizzazione della tabella completa scelta al secondo menu (con solo qualche join per rendere leggibili i dati in chiave esterna)
     
  if (a==2):                                           #1 non può essere inserito, in quanto con 1 si accede al menu secondario
    print("Persone assegnate ai reparti:\n")
    for o, d, p, r, t in session.query(Orario, Dipendente, Persona, Reparto, Tiporeparto
    ).filter(Dipendente.ID_Persona == Persona.ID_Persona
    ).filter(Persona.ID_Reparto == Reparto.ID_Reparto
    ).filter(Dipendente.ID_Orario == Orario.ID_Orario
    ).filter(Reparto.NomeReparto == Tiporeparto.ID_TipoReparto
 #   ).filter(Tiporeparto.NomeReparto == 'Contabilita'                    #campo messo come esempio
    ).order_by(asc(Tiporeparto.ID_TipoReparto)
    ).all():
      print ("Reparto: {} Nome Dip: {} Cognome Dip: {} Entrata: {} Uscita: {}".
      format(t.NomeReparto, p.Nome, p.Cognome, o.OrarioIngresso, o.OrarioUscita))
      
  elif (a==3):
    print("Set venduti dai dipendenti che guadagnano più di 1500€:\n")
    for s, d, p, v, t, w in session.query(Stipendio, Dipendente, Persona, Venduto, SetPronto, Vendite
    ).filter(Dipendente.ID_Persona == Persona.ID_Persona
    ).filter(Dipendente.ID_Stipendio == Stipendio.ID_Stipendio
    ).filter(Dipendente.ID_Dipendente == Vendite.ID_Dipendente
    ).filter(Venduto.ID_SetPronto == SetPronto.ID_SetPronto
    ).filter(Venduto.ID_Vendita == Vendite.ID_Vendita
    ).filter(Stipendio.Cifra > 1500
    ).order_by(desc(Stipendio.Cifra)
    ).order_by(asc(SetPronto.NomeSet)
    ).all():
      print ("Nome: {} Cognome: {} Stipendio: {} Set: {}".
      format(p.Nome, p.Cognome, s.Cifra, t.NomeSet))
      
  elif (a==4):                               
    print("Incasso Totale delle Sedi:\n")
    for a, w in session.query(func.sum(Vendite.PrezzoTotale), Sede  
    ).filter(Sede.ID_Sede == Reparto.CodiceSede
    ).filter(Magazzino.ID_Reparto == Reparto.ID_Reparto
    ).filter(SetPronto.ID_Magazzino == Magazzino.ID_Magazzino
    ).filter(Venduto.ID_SetPronto == SetPronto.ID_SetPronto
    ).filter(Vendite.ID_Vendita == Venduto.ID_Vendita
    ).order_by(asc(Sede.ID_Sede)
    ).group_by(Sede.ID_Sede
    ).all():
      print ("Sede: {} Incasso: {}".format(w.NomeSede, a))
  elif (a==5):
    print("Set più venduti:\n")
    for u, c, s in session.query(func.sum(Venduto.Prezzo), func.count(Venduto.ID_Venduto), SetPronto  
    ).filter(Venduto.ID_SetPronto == SetPronto.ID_SetPronto
    ).order_by(desc(func.sum(Venduto.Prezzo))
    ).group_by(Venduto.ID_SetPronto
    ).all():
      print ("Set: {} Quantità: {} Incasso: {}".format(s.NomeSet, c, u))
      
  elif (a==11):
    print("Tabella Persona:\n")
    for p, c, r in session.query(Persona , Citta, Residenza
    ).filter(Persona.Residenza == Residenza.ID_Residenza
    ).filter(Residenza.ID_Citta == Citta.ID_Citta
    ).order_by(Persona.ID_Persona
    ).all():
      print ("ID: {} Nome: {} Cognome: {} Residenza: {} {} {} {} CodiceFiscale: {} Cellulare {} E-mail: {} Data di Nascita: {}".
      format(p.ID_Persona, p.Nome, p.Cognome, r.Via, p.Civico, c.NomeCitta, c.CapCitta, p.CodiceFiscale, p.Cellulare, p.E_mail, p.DataNascita))

  elif (a==12):
    print("Tabella Dipendente:\n")
    for p, d, o, s, r, c, t in session.query(Persona , Dipendente, Orario, Stipendio, Reparto, Categoria, Tiporeparto
    ).filter(Persona.ID_Reparto == Reparto.ID_Reparto
    ).filter(Dipendente.ID_Persona == Persona.ID_Persona
    ).filter(Categoria.ID_Categoria == Dipendente.ID_Categoria
    ).filter(Orario.ID_Orario == Dipendente.ID_Orario
    ).filter(Stipendio.ID_Stipendio == Dipendente.ID_Stipendio
    ).filter(Tiporeparto.ID_TipoReparto == Reparto.NomeReparto
    ).order_by(Dipendente.ID_Dipendente
    ).all():
      print ("ID: {} Nome: {} Cognome: {} Reparto: {} Stipendio: {} Categoria {} Orario: {}".
      format(p.ID_Persona, p.Nome, p.Cognome, t.NomeReparto, s.Cifra, c.DescrizioneCategoria, o.OreSettimanali))

  elif (a==13):
    print("Tabella Acquirente:\n")
    for p, a in session.query(Persona , Acquirente
    ).filter(Persona.ID_Persona == Acquirente.ID_Persona
    ).order_by(Acquirente.ID_Acquirente
    ).all():
      print ("ID: {} Nome: {} Cognome: {} Carta di Credito: {} PIN: {} Indice di Gradimento: {}".
      format(a.ID_Acquirente, p.Nome, p.Cognome, a.CartaCredito, a.PIN, a.Gradimento))

  elif (a==14):
    print("Tabella Sede:\n")
    for s, c, r in session.query(Sede , Citta, Residenza
    ).filter(Sede.ViaSede == Residenza.ID_Residenza
    ).filter(Residenza.ID_Citta == Citta.ID_Citta
    ).order_by(Sede.ID_Sede
    ).all():
      print ("ID: {} Sede: {} IP: {} Via: {} {} {} {} E-mail: {}".
      format(s.ID_Sede, s.NomeSede, s.IP_Sede, r.Via, s.CivicoSede, c.NomeCitta, c.CapCitta, s.E_mailSede))

  elif (a==15):
    print("Tabella Reparto:\n")
    for s, r, t in session.query(Sede , Reparto, Tiporeparto
    ).filter(Sede.ID_Sede == Reparto.CodiceSede
    ).filter(Tiporeparto.ID_TipoReparto == Reparto.NomeReparto
    ).order_by(Reparto.ID_Reparto
    ).all():
      print ("ID: {} Reparto: {} Descrizione: {} Telefono: {} E-mail: {} Sede: {}".
      format(r.ID_Reparto, t.NomeReparto, r.DescrizioneReparto, r.TelefonoReparto, r.EmailReparto, s.NomeSede))

  elif (a==16):
    print("Tabella Server:\n")
    for s, r in session.query(Sede , Server
    ).filter(Sede.ID_Sede == Server.ID_Sede
    ).order_by(Server.ID_Server
    ).all():
      print ("ID: {} Server: {} IP: {} Sede: {}".
      format(r.ID_Server, r.DescrizioneServer, r.IP_Server, s.NomeSede))

  elif (a==17):
    print("Tabella Set Disponibili:\n")
    for s, m, r, d, c, z in session.query(SetPronto, Magazzino, Reparto, Sede, Citta, Residenza 
    ).filter(SetPronto.ID_Magazzino == Magazzino.ID_Magazzino
    ).filter(Magazzino.ID_Reparto == Reparto.ID_Reparto
    ).filter(Sede.ID_Sede == Reparto.CodiceSede
    ).filter(Sede.ViaSede == Residenza.ID_Residenza
    ).filter(Residenza.ID_Citta == Citta.ID_Citta
    ).order_by(SetPronto.ID_SetPronto
    ).all():
      print ("ID: {} Nome: {} Descrizione: {} Età Consigliata: {} Quantità: {} Scaffale: {} Magazzino: {} {} {} {}".
      format(s.ID_SetPronto, s.NomeSet, s.DescrizioneSet, s.EtaConsigliata, s.QuantitaDisponibile, m.PosizioneScaffale,  z.Via, d.CivicoSede, c.NomeCitta, c.CapCitta))

  elif (a==18):
    print("Tabella Merce disponibile in magazzino:\n")
    for m, r, d, c, z, p, k in session.query(Magazzino, Reparto, Sede, Citta, Residenza, Tiporeparto, SetPronto 
    ).filter(Tiporeparto.ID_TipoReparto == Reparto.NomeReparto
    ).filter(SetPronto.ID_Magazzino == Magazzino.ID_Magazzino
    ).filter(Magazzino.ID_Reparto == Reparto.ID_Reparto
    ).filter(Sede.ID_Sede == Reparto.CodiceSede
    ).filter(Sede.ViaSede == Residenza.ID_Residenza
    ).filter(Residenza.ID_Citta == Citta.ID_Citta
    ).order_by(Magazzino.ID_Magazzino
    ).all():
      print ("ID: {} Set: {} Scaffale: {} Nome: {} Descrizione: {} Telefono: {} E-mail: {} Via: {} {} {} {}".
      format(m.ID_Magazzino, k.NomeSet, m.PosizioneScaffale, p.NomeReparto, r.DescrizioneReparto, r.TelefonoReparto, r.EmailReparto, z.Via, d.CivicoSede, c.NomeCitta, c.CapCitta))
  else:
    print("Hai digitato un carattere non ammesso")
    a=20
  return(a) 