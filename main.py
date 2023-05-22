import funzioni.db_conn, funzioni.funzioni                  #importo i file esterni al main
from funzioni.db_conn import collegamentodb                 #importo le funzioni in più che ci sono dentro
from funzioni.funzioni import sceltautente

collegamentoeffettuato = collegamentodb()                   #come prima operazione mi collego al database, nel file funzioni/db_conn

if (collegamentoeffettuato != False):                       #se il motore non viene creato non entra nel programma
  while ( (sceltafattautente := sceltautente(collegamentoeffettuato)) == 1):   #Viene richiamata la funzione sceltautente, e rimarrà nel ciclo fino a che il valore sarà 1 (la funzione restituisce sempre 1, tranne il caso
    continue                                                                   #in cui l'utente dichiari di voler uscire).  
    
print ("\nArrivederci")
 