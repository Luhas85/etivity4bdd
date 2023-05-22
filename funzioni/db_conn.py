def collegamentodb():
                       
  user = input ("\nInserisci il nome dell'utente MySql: ")                  # Chiedo i dati utente per la connessione al database
  password = input ("Inserisci la password per " + user + ": ")

  countver=0
  verifica="K"
  while ((verifica!="S")and(verifica!="N")):     #Controllo che l'utente si voglia collegare ad altri db, fino a che  non digita S o N, rimane dentro. il Contatore serve per cambiare la scritta a video.
    if (countver>0):
      verifica = input ("Non hai inserito il carattere corretto. Vuoi collegarti al database di prova? S o N: ")
    else:
      verifica = input ("Vuoi collegarti al database di prova? S o N: ")
      countver=1
    
  if (verifica =="S"):                   #se l'utente inserisce S, i parametri saranno quelli di localhost sulla porta classica e allo schema etivity4
    host = '127.0.0.1'
    port = 3306
    database = 'etivity4'
  else:                                  #altrimenti chiede all'utente di inserire i dati
    host = input ("Inserisci l'indirizzo del server a cui ti vuoi collegare: ")
    port = input ("Inserisci la porta del server a cui ti vuoi collegare: ")
    while ((port.isdigit() == False)or((int(port))>65536)):           #controllo che la porta sia numerica, e che non sia un numero troppo alto
      port = input ("La porta non è valida. Inserisci la porta del server a cui ti vuoi collegare: ")
    port = int(port)             #i parametri di input sono sempre stringhe
    database = input ("Inserisci il database a cui ti vuoi collegare: ")

  import sqlalchemy
  from sqlalchemy import create_engine  
  try:                                          # Provo l'istruzione successiva, in caso di successo restituisco il messaggio di collegamento riuscito, altrimenti segnalo l'errore riscontrato.
    engine = create_engine(
      url="mysql+mysqlconnector://{0}:{1}@{2}:{3}/{4}".format(
        user, password, host, port, database
      )
    )
    print(f"\nConnessione all'indirizzo {host} per l'utente {user} creata con successo.")             #motore creato correttamente
    return (engine)                                                  
  except Exception as ex:
    print("\nNon è possibile collegarsi all'indirizzo a causa del seguente errore: \n", ex)
    return (False)