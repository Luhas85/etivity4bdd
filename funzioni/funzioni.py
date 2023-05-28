from sqlalchemy import MetaData, Table, Column, Integer, String, Time, Float, Date, ForeignKey, create_engine 
from sqlalchemy.orm import DeclarativeBase
class Base (DeclarativeBase):
  pass

def sceltautente(collegamentoeffettuato):
  """
  Questa funzione mette l'utente a scelta dell'operazione da effettuare
  """
  global engine
  engine = collegamentoeffettuato  
   
  operazioneutente = input ("\nQuale operazione vuoi svolgere sul database:\n\
  1_Creare una tabella\n\
  2_Inserire un nuovo dato\n\
  3_Visualizzare i dati\n\
  4_Aggiornare i dati\n\
  5_Cancellare i dati\n\
  6_Uscire dal programma\n")
                                                 #controlla quale è la scelta utente, e a seconda del tasto pigiato chiama la funzione per svolgere quell'attività.
  if (operazioneutente == "1"):                  #ritorna 1 per ogni operazione, 0 se l'utente vuole chiudere il programma.
    from funzioni.inseriscitabelle import creatabella
    operazionedafare = creatabella(engine)       #riga 277 del file inseriscitabelle
    return (1)
  elif (operazioneutente == "2"):
    operazionedafare = inseriscidatitabella()  
    return (1)    
  elif (operazioneutente == "3"):
    operazionedafare = visualizzadatitabella()      
    return (1)
  elif (operazioneutente == "4"):
    operazionedafare = aggiornadatitabella()
    return (1)    
  elif (operazioneutente == "5"):
    operazionedafare = cancelladatitabella()
    return (1)    
  elif (operazioneutente == "6"):
    return (0)                                         
  else:                                  #se arriva qui vuol dire che è stata scritta una stringa scorretta.
    print ("\nHai fatto una scelta non consentita. Riprova")
    return (1)

#Le funzioni a scelta dell'utente sono tutte simili, viene elencato un menu, e in base alla scelta dell'utente si rimanda al corrispettivo file .py in cui la funzione si sviluppa (aggiornadati.py per aggiornare ad esempio)


def visualizzadatitabella():
  richiestaquery=0
  from funzioni.visualizzadati import visualizzadatotabella           #si importa la funzione dal file visualizzadati
  while (richiestaquery != 6):
    richiestaquery = input("\nScegli quale informazione chiedere al database:\n\
     1_Visualizzare tutti i dati di una tabella\n\
     2_Vedere quali persone sono assegnate ai reparti\n\
     3_Vedere il nome dei set venduti dai dipendenti che guadagnano più di 1500€ \n\
     4_Quanto hanno incassato le varie sedi\n\
     5_Vedere quali set sono stati venduti di più\n\
     6_Uscire dalle opzioni di scelta\n")
    
    if ((richiestaquery.isdigit() == False)or(richiestaquery=="0")or((int(richiestaquery)>6)or(int(richiestaquery)<0))):   #controlla che il campo inserito sia un numero, che non sia 0, e che sia compreso nel range delle scelte
      print ("Errore,Riprova")
    else:
      richiestaquery = int(richiestaquery)     
      if (richiestaquery==1):
        richiestaquery = input("\nScegli quale tabella visualizzare (Digitare entrambe le Cifre):\n\
         11_Persona\n\
         12_Dipendente\n\
         13_Acquirente\n\
         14_Sede\n\
         15_Reparto\n\
         16_Server\n\
         17_Set Pronti\n\
         18_Merce disponibile in magazzino\n")    
        if ((richiestaquery.isdigit() == False)or(richiestaquery=="0")or((int(richiestaquery)>18)or(int(richiestaquery)<11))):
          print ("Errore,Riprova")
          richiestaquery = 0
        else:
          richiestaquery = int(richiestaquery)     
      if (richiestaquery==6):      
        pass
      else:
        visualizzato = visualizzadatotabella(engine,richiestaquery)
  return (1)
  
  
  
  
  
def inseriscidatitabella():

  sceglicosainserire = input ("Se vuoi inserire un dato manuale digita S altrimenti verrà popolato tutto il database con i dati standard: ")
  if (sceglicosainserire == "S"):
  
    from funzioni.inseriscidati import inserimentomanuale
  
    richiestaquery=0
    while (richiestaquery != 5):
      richiestaquery = input("\nScegli quale dato aggiornare nel database:\n\
     1_Inserisci due sedi\n\
     2_Inserisci un dipendente\n\
     3_Inserisci un Set\n\
     4_Inserisci un server e una vlan\n\
     5_Uscire dalle opzioni di scelta\n") 
      if ((richiestaquery.isdigit() == False)or(richiestaquery=="0")or((int(richiestaquery)>5)or(int(richiestaquery)<0))):           
        print("Hai digitato un carattere non ammesso")
      else:
        richiestaquery = int(richiestaquery)
        if (richiestaquery==5):      
          pass
        else:
          inserito = inserimentomanuale(engine,richiestaquery) 
  else:
    from funzioni.inseriscidati import faiinserimento  
    inseritodati = faiinserimento (engine)
 
  return (1)






def aggiornadatitabella():       
 
  richiestaquery=0
  from funzioni.aggiornadati import aggiornadatotabella
  while (richiestaquery != 5):
    richiestaquery = input("\nScegli quale dato aggiornare nel database:\n\
     1_Modificare l'IP del FileServer\n\
     2_Raddoppiare tutti gli stipendi\n\
     3_Modificare il nome delle sedi di Siena in *Nuovo Nome Sede Cambiato*\n\
     4_Modificare il codice fiscale delle persone nate prima del 1980\n\
     5_Uscire dalle opzioni di scelta\n")
    if ((richiestaquery.isdigit() == False)or(richiestaquery=="0")or((int(richiestaquery)>5)or(int(richiestaquery)<0))):
      print("Hai digitato un carattere non ammesso")
    else:      
      richiestaquery = int(richiestaquery)
      if (richiestaquery==5):      
        pass
      else:
        aggiornato = aggiornadatotabella(engine,richiestaquery)
  return (1)
  

  
  
  
  
  
  
def cancelladatitabella():
 
  from funzioni.cancelladati import cancellatuttodef, cancelladatotabella  
  sceglicosainserire = input ("Se vuoi cancellare tutto il database digita S altrimenti passa all'opzione successiva: ")
  if (sceglicosainserire == "S"):  
    sceglicosainserire = input ("Sei sicuro? perderai tutti i dati. Digita S: ")
    if (sceglicosainserire == "S"):
      cancellato = cancellatuttodef(engine) 
      pass
  else:
    richiestaquery = input("\nScegli quale dato vuoi cancellare dal database:\n\
     1_Cancellare la sede di Siena\n\
     2_Cancellare Luca Pacchierotti\n\
     3_Cancellare la Categoria B3\n\
     4_Cancellare il Domain Controller\n\
     5_Svuotare tutta la tabella Spedizione\n\
     6_Uscire dalle opzioni di scelta\n")
    if ((richiestaquery.isdigit() == False)or(richiestaquery=="0")or((int(richiestaquery)>6)or(int(richiestaquery)<0))): 
      print("Hai digitato un carattere non ammesso")
    else:      
      richiestaquery = int(richiestaquery)
      cancellato = cancelladatotabella(engine,richiestaquery)
  return (1)
