# etivity4bdd
Progetto E-tivity 4 Basi di Dati Unicusano

1_Il progetto si lancia eseguendo il file main.py  
2_Inserire i parametri di connessione al database (inserendo S dopo utente e password il motore creato sarà su 127.0.0.1:3306/etivity4)  

3_Inizialmente il db sarà vuoto, digitare 1 per creare le tabelle  
&nbsp&nbsp3.1_Nel sottomenu NON digitare S per creare tutte le tabelle del progetto e-tivity3  
&nbsp&nbsp3.2_Digitando S si accede a una funzione che permette di creare una tabella dinamica, con parametri definiti dall'utente (nometabella, numerodicampi, tipididato delle colonne etc.)  

4_Mancano i dati dentro le tabelle, digitare 2 per inserire i dati del progetto
  4.1_Nel sottomenu NON digitare S per inserire tutti i record del progetto e-tivity3
  4.2_Digitando S si accede a un sottomenu in cui si può scegliere quali dati aggiungere al database
  
5_A questo punto si possono usare le altre funzioni, 3-4 e 5 per visualizzare i dati, aggiornare i record o cancellare.

6_Digitando 3 si accede a un menu con delle query a scelta. Digitando 1 si accede a un sottomenu dove verranno elencate 8 tabelle di cui poter vedere il contenuto integrale.
NOTA: Nel primo menu, per poter visualizzare le opzioni 4 e 5, l'sql_mode "only_full_group_by" deve essere disabilitato

7_Con 4 si accede al menu di UPDATE, dove saranno elencati 4 record modificabili

8_L'ultima funzione, di cancellazione, sarà attivata digitando 5. 
  8.1_Digitando S (e confermando) verranno completamente rimosse tutte le tabelle del DB e si tornerà allo stato iniziale.
  8.2_Non digitando S si accede al sottomenu dove scegliere quali record (o tabelle) cancellare.

Grazie per l'attenzione,
Saluti.
  
