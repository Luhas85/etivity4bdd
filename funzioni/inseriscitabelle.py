from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Time, Float, Date, ForeignKey
from funzioni.funzioni import Base
from sqlalchemy.orm import Relationship

#Qui si definiscono tutte le classi del Database di esempio, con le relazioni tra le varie tabelle e l'impostazione in caso di delete

class Citta(Base): 
  __tablename__ = 'citta'
  ID_Citta = Column(Integer, primary_key = True, autoincrement=True)
  NomeCitta = Column(String(45))
  CapCitta = Column(Integer)
  ResiCittRel = Relationship("Residenza", back_populates="CittResiRel" , cascade ="all,delete-orphan")
  PersCittRel = Relationship("Persona", back_populates="CittPersRel" , cascade ="all,delete-orphan")  
  
class Residenza(Base): 
  __tablename__ = 'residenza'
  ID_Residenza = Column(Integer, primary_key = True, autoincrement=True)
  ID_Citta = Column(Integer, ForeignKey(('citta.ID_Citta'), ondelete='cascade'))
  Via = Column(String(45))
  CittResiRel = Relationship("Citta", back_populates="ResiCittRel")
  SedeResiRel = Relationship("Sede", back_populates="ResiSedeRel", cascade ="all,delete-orphan")
  PersResiRel = Relationship("Persona", back_populates="ResiPersRel", cascade ="all,delete-orphan")  

class Sede(Base):   #Relazione con Server molti a molti
  __tablename__ = 'sede'
  ID_Sede = Column(Integer, primary_key = True, autoincrement=True)
  NomeSede = Column(String(45))
  IP_Sede = Column(String(45))
  Centralino_Sede = Integer
  E_mailSede = Column(String(45))
  ViaSede = Column(Integer, ForeignKey(('residenza.ID_Residenza'), ondelete='cascade'))
  CivicoSede = Column(Integer)
  RepaSedeRel = Relationship("Reparto", back_populates="SedeRepaRel", cascade ="all,delete-orphan")
  AcceSedeRel = Relationship("Accedea", back_populates="SedeAcceRel", cascade ="all,delete-orphan")
  ResiSedeRel = Relationship("Residenza", back_populates="SedeResiRel")  
  
class Server(Base): 
  __tablename__ = 'server'
  ID_Server = Column(Integer, primary_key = True, autoincrement=True)
  DescrizioneServer = Column(String(45))
  IP_Server = Column(String(45))
  ID_Sede = Column(Integer)
  AcceServRel = Relationship("Accedea", back_populates="ServAcceRel" , cascade ="all,delete-orphan")
  SaccServRelUno = Relationship("Serveraccessi", foreign_keys='Serveraccessi.ID_ServerIN' , back_populates="ServSaccRelUno", cascade ="all,delete-orphan")
  SaccServRelDue = Relationship("Serveraccessi", foreign_keys='Serveraccessi.ID_ServerOUT' , back_populates="ServSaccRelDue", cascade ="all,delete-orphan")   
  
class Accedea(Base): 
  __tablename__ = 'accedea'
  ID_Accesso = Column(Integer, primary_key = True, autoincrement=True)
  Motivo = Column(String(45))
  ID_Sede = Column(Integer, ForeignKey(('sede.ID_Sede'), ondelete='cascade'))
  ID_Server = Column(Integer, ForeignKey(('server.ID_Server'), ondelete='cascade'))
  ServAcceRel = Relationship("Server", back_populates="AcceServRel") 
  SedeAcceRel = Relationship("Sede", back_populates="AcceSedeRel")

class Serveraccessi(Base): 
  __tablename__ = 'serveraccessi'
  ID_ServerAccessi = Column(Integer, primary_key = True, autoincrement=True)
  ID_ServerIN = Column(Integer, ForeignKey(('server.ID_Server'), ondelete='cascade'))
  ID_ServerOUT = Column(Integer, ForeignKey(('server.ID_Server'), ondelete='cascade')) 
  Motivo = Column(String(45))   
  ServSaccRelUno = Relationship("Server", foreign_keys='Serveraccessi.ID_ServerIN' , back_populates="SaccServRelUno") 
  ServSaccRelDue = Relationship("Server", foreign_keys='Serveraccessi.ID_ServerOUT' , back_populates="SaccServRelDue")
  
class Tiporeparto(Base): 
  __tablename__ = 'tiporeparto'
  ID_TipoReparto = Column(Integer, primary_key = True, autoincrement=True)
  NomeReparto = Column(String(45))
  DescrizioneReparto = Column(String(45))
  RepaTipoRel = Relationship("Reparto", back_populates="TipoRepaRel", cascade ="all,delete-orphan")
  
class Reparto(Base): 
  __tablename__ = 'reparto'
  ID_Reparto = Column(Integer, primary_key = True, autoincrement=True)
  NomeReparto = Column(Integer, ForeignKey(('tiporeparto.ID_TipoReparto'), ondelete='cascade'))
  DescrizioneReparto = Column(String(45))
  TelefonoReparto = Column(Integer)
  EmailReparto = Column(String(45))
  CodiceSede = Column(Integer, ForeignKey(('sede.ID_Sede'), ondelete='cascade'))
  SedeRepaRel = Relationship("Sede", back_populates="RepaSedeRel")
  TipoRepaRel = Relationship("Tiporeparto", back_populates="RepaTipoRel")
  PartRepaRel = Relationship("Partecipa", back_populates="RepaPartRel", cascade ="all,delete-orphan")
  PersRepaRel = Relationship("Persona", back_populates="RepaPersRel", cascade ="all,delete-orphan")
  MagaRepaRel = Relationship("Magazzino", back_populates="RepaMagaRel", cascade ="all,delete-orphan")
  
class Vlan(Base): 
  __tablename__ = 'vlan'
  ID_Vlan = Column(Integer, primary_key = True, autoincrement=True)
  DescrizioneVlan = Column(String(45))
  PartVlanRel = Relationship("Partecipa", back_populates="VlanPartRel", cascade ="all,delete-orphan")  

class Partecipa(Base): 
  __tablename__ = 'partecipa'
  ID_Partecipa = Column(Integer, primary_key = True, autoincrement=True)
  ID_vlan = Column(Integer, ForeignKey(('vlan.ID_Vlan'), ondelete='cascade')) 
  ID_reparto = Column(Integer, ForeignKey(('reparto.ID_Reparto'), ondelete='cascade')) 
  Motivo = Column(String(45))
  RepaPartRel = Relationship("Reparto", back_populates="PartRepaRel")  
  VlanPartRel = Relationship("Vlan", back_populates="PartVlanRel") 
  
class Magazzino(Base): 
  __tablename__ = 'magazzino'
  ID_Magazzino = Column(Integer, primary_key = True, autoincrement=True)
  ID_Reparto = Column(Integer, ForeignKey(('reparto.ID_Reparto'), ondelete='cascade')) 
  PosizioneScaffale = Column(String(45))
  RepaMagaRel = Relationship("Reparto", back_populates="MagaRepaRel")
  BricMagaRel = Relationship("Brick", back_populates="MagaBricRel", cascade ="all,delete-orphan")
  SetProntoMagaRel = Relationship("SetPronto", back_populates="MagaSetProntoRel", cascade ="all,delete-orphan")
  
class SetPronto(Base): 
  __tablename__ = 'setpronto'
  ID_SetPronto = Column(Integer, primary_key = True, autoincrement=True)
  NomeSet = Column(String(45))
  DescrizioneSet = Column(String(45))
  EtaConsigliata = Column(Integer)
  QuantitaDisponibile = Column(Integer)
  ID_Magazzino = Column(Integer, ForeignKey(('magazzino.ID_Magazzino'), ondelete='cascade'))
  MagaSetProntoRel = Relationship("Magazzino", back_populates="SetProntoMagaRel")
  CompSetProntoRel = Relationship("Composto", back_populates="SetProntoCompRel", cascade ="all,delete-orphan")
  VendutoSproRel = Relationship("Venduto", back_populates="SproVendutoRel", cascade ="all,delete-orphan")
  
class Colore(Base): 
  __tablename__ = 'colore'
  ID_Colore = Column(Integer, primary_key = True, autoincrement=True)
  Nome = Column(String(45))
  Esadecimale = Column(String(45))
  R = Column(Integer)
  G = Column(Integer)
  B = Column(Integer)
  BricColoRel = Relationship("Brick", back_populates="ColoBricRel", cascade ="all,delete-orphan")
  
class Brick(Base): 
  __tablename__ = 'brick'
  ID_Brick = Column(Integer, primary_key = True, autoincrement=True)
  Tipologia = Column(String(45))
  ID_Colore = Column(Integer, ForeignKey(('colore.ID_Colore'), ondelete='cascade')) 
  QuantitaDisponibile = Column(Integer)
  ID_Magazzino = Column(Integer, ForeignKey(('magazzino.ID_Magazzino'), ondelete='cascade'))
  MagaBricRel = Relationship("Magazzino", back_populates="BricMagaRel")
  ColoBricRel = Relationship("Colore", back_populates="BricColoRel")
  CompBricRel = Relationship("Composto", back_populates="BricCompRel", cascade ="all,delete-orphan")
  
class Composto(Base): 
  __tablename__ = 'composto'
  ID_Composto = Column(Integer, primary_key = True, autoincrement=True)
  ID_SetPronto = Column(Integer, ForeignKey(('setpronto.ID_SetPronto'), ondelete='cascade'))
  ID_Brick = Column(Integer, ForeignKey(('brick.ID_Brick'), ondelete='cascade'))  
  Numero = Column(Integer)  
  SetProntoCompRel = Relationship("SetPronto", back_populates="CompSetProntoRel")
  BricCompRel = Relationship("Brick", back_populates="CompBricRel")
  
class Permessi(Base): 
  __tablename__ = 'permessi'
  ID_Permessi = Column(Integer, primary_key = True, autoincrement=True)
  Ferie = Column(Integer)
  Studio = Column(Integer)
  Visite = Column(Integer)
  centoquattro = Column(Integer)
  CatePermRel = Relationship("Categoria", back_populates="PermCateRel", cascade ="all,delete-orphan")

class Categoria(Base): 
  __tablename__ = 'categoria'
  ID_Categoria = Column(Integer, primary_key = True, autoincrement=True)
  Max_Stipendio = Column(Float)
  Min_Stipendio = Column(Float)
  PermessiCategoria = Column(Integer, ForeignKey(('permessi.ID_Permessi'), ondelete='cascade'))  
  Numero = Column(Integer)  
  DescrizioneCategoria = Column(String(45))
  DipeCateRel = Relationship("Dipendente", back_populates="CateDipeRel", cascade ="all,delete-orphan")
  PermCateRel = Relationship("Permessi", back_populates="CatePermRel")
 
class Orario(Base): 
  __tablename__ = 'orario'
  ID_Orario = Column(Integer, primary_key = True, autoincrement=True)
  OreSettimanali = Column(Integer)
  OrarioIngresso = Column(Time)
  OrarioUscita = Column(Time)
  Flessibilita = Column(Integer)  
  Max_Straordinari = Column(Integer)
  Max_OreAssenza = Column(Integer)
  DipeOrarRel = Relationship("Dipendente", back_populates="OrarDipeRel", cascade ="all,delete-orphan")
  
class Stipendio(Base): 
  __tablename__ = 'stipendio'
  ID_Stipendio = Column(Integer, primary_key = True, autoincrement=True)
  Cifra = Column(Float)
  Straordinari = Column(Integer)
  DipeStipRel = Relationship("Dipendente", back_populates="StipDipeRel", cascade ="all,delete-orphan")
  
class Persona(Base): 
  __tablename__ = 'persona'
  ID_Persona = Column(Integer, primary_key = True, autoincrement=True)
  Nome = Column(String(45))
  Cognome = Column(String(45))
  Residenza = Column(Integer, ForeignKey(('residenza.ID_Residenza'), ondelete='cascade'))  
  Civico = Column(Integer)
  CodiceFiscale = Column(String(45))
  Sesso = Column(String(45))
  E_mail = Column(String(45))
  Cellulare = Column(String(45))
  DataNascita = Column(Date)
  LuogoNascita = Column(Integer, ForeignKey(('citta.ID_Citta'), ondelete='cascade'))  
  ID_Reparto = Column(Integer, ForeignKey(('reparto.ID_Reparto'), ondelete='cascade')) 
  RepaPersRel = Relationship("Reparto", back_populates="PersRepaRel")
  CittPersRel = Relationship("Citta", back_populates="PersCittRel")
  ResiPersRel = Relationship("Residenza", back_populates="PersResiRel")
  DipePersRel = Relationship("Dipendente", back_populates="PersDipeRel", cascade ="all,delete-orphan")
  AcquiPersRel = Relationship("Acquirente", back_populates="PersAcquiRel", cascade ="all,delete-orphan")  
  
class Dipendente(Base): 
  __tablename__ = 'dipendente'
  ID_Dipendente = Column(Integer, primary_key = True, autoincrement=True)
  ID_Persona = Column(Integer, ForeignKey(('persona.ID_Persona'), ondelete='cascade'))
  ID_Responsabile = Column(Integer, ForeignKey(('dipendente.ID_Dipendente'), ondelete='cascade')) 
  isResponsabile = Column(Integer)
  ID_Orario = Column(Integer, ForeignKey(('orario.ID_Orario'), ondelete='cascade'))
  ID_Stipendio = Column(Integer, ForeignKey(('stipendio.ID_Stipendio'), ondelete='cascade'))
  ID_Categoria = Column(Integer, ForeignKey(('categoria.ID_Categoria'), ondelete='cascade'))
  CateDipeRel = Relationship("Categoria", back_populates="DipeCateRel")
  StipDipeRel = Relationship("Stipendio", back_populates="DipeStipRel")
  OrarDipeRel = Relationship("Orario", back_populates="DipeOrarRel")
  VendDipeRel = Relationship("Vendite", back_populates="DipeVendRel", cascade ="all,delete-orphan")
  PersDipeRel = Relationship("Persona", back_populates="DipePersRel")  
  
class Acquirente(Base): 
  __tablename__ = 'acquirente'
  ID_Acquirente = Column(Integer, primary_key = True, autoincrement=True)
  CartaCredito = Column(String(45))
  PIN = Column(Integer)
  Gradimento = Column(Integer)  
  ID_Persona = Column(Integer, ForeignKey(('persona.ID_Persona'), ondelete='cascade'))  
  PersAcquiRel = Relationship("Persona", back_populates="AcquiPersRel")
  VendAcquiRel = Relationship("Vendite", back_populates="AcquiVendRel")
  
class Vendite(Base): 
  __tablename__ = 'vendite'
  ID_Vendita = Column(Integer, primary_key = True, autoincrement=True)
  TassazioneIVA = Column(Integer)
  PrezzoTotale = Column(Float)
  ScontoProgressivo = Column(Integer)
  ID_Acquirente = Column(Integer, ForeignKey(('acquirente.ID_Acquirente'), ondelete='cascade'))  
  DataVendita = Column(Date)
  ID_Dipendente = Column(Integer, ForeignKey(('dipendente.ID_Dipendente'), ondelete='cascade')) 
  ID_Transazione = Column(String(45))
  DipeVendRel = Relationship("Dipendente", back_populates="VendDipeRel")
  VendutoVendRel = Relationship("Venduto", back_populates="VendVendutoRel", cascade ="all,delete-orphan")
  InviVendRel = Relationship("Inviato", back_populates="VendInviRel", cascade ="all,delete-orphan")
  AcquiVendRel = Relationship("Acquirente", back_populates="VendAcquiRel")

class Venduto(Base): 
  __tablename__ = 'venduto'
  ID_Venduto = Column(Integer, primary_key = True, autoincrement=True)
  ID_Vendita = Column(Integer, ForeignKey(('vendite.ID_Vendita'), ondelete='cascade'))   
  ID_SetPronto = Column(Integer, ForeignKey(('setpronto.ID_SetPronto'), ondelete='cascade')) 
  Prezzo = Column(Float) 
  VendVendutoRel = Relationship("Vendite", back_populates="VendutoVendRel")
  SproVendutoRel = Relationship("SetPronto", back_populates="VendutoSproRel")  

class Spedizione(Base): 
  __tablename__ = 'spedizione'
  ID_Spedizione = Column(Integer, primary_key = True, autoincrement=True)
  ID_Acquirente = Column(Integer)
  TempiSpedizione = Column(Integer) 
  SpeseSpedizione = Column(Float)   
  Giorno = Column(Date) 
  InviSpedRel = Relationship("Inviato", back_populates="SpedInviRel", cascade ="all,delete-orphan")
  
class Inviato(Base): 
  __tablename__ = 'inviato'
  ID_Invio = Column(Integer, primary_key = True, autoincrement=True)
  ID_Vendita = Column(Integer, ForeignKey(('vendite.ID_Vendita'), ondelete='cascade'))
  ID_Spedizione = Column(Integer, ForeignKey(('spedizione.ID_Spedizione'), ondelete='cascade'))
  VendInviRel = Relationship("Vendite", back_populates="InviVendRel")
  SpedInviRel = Relationship("Spedizione", back_populates="InviSpedRel")
  

def creatabella(engine):
  """
  Questa funzione chiede in ingresso i parametri della tabella da creare e poi si interfaccia con il db ricreando la stringa Mysql.
  Se invece non viene specificato S, inserisce il database del Progetto delle altre E-tivity
  """
  from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Time, Float, Date, ForeignKey
  
  sceglicosainserire = input ("Se vuoi inserire una tabella qualsiasi scrivi S altrimenti viene creato il database del progetto: ")
  if (sceglicosainserire == "S"):              #Se si entra qui si è scelto di compilare la tabella manualmente. 
  
              #MANCA LA PARTE FINALE IN CUI LA TABELLA VIENE INSERITA FISICAMENTE SUL DB, FUNZIONA SOLO L'ELSE
                                                                                                                  
    nometabella = input ("\nInserisci il nome della tabella: ")
    numerocampi = input ("Inserisci il numero delle colonne della tabella " + nometabella + ": ")
  
    while (numerocampi.isdigit() == False):         #controlla che il campo del numero delle colonne sia numerico, se non lo è continua a far inserire il dato
      numerocampi = input ("Inserisci il numero delle colonne della tabella " + nometabella + ": ")
    numerocampi = int (numerocampi)
    nomicolonne = []                                #creo due vettori, per il nome delle colonne, e per il tipo di dato  
    tipodatocolonne = []
    notnullcolonne = []
    autoincrementcolonne = []
    indexuniquecolonne = []
    tipipermessi = ["Integer","BigInteger","SmallInteger","Numeric","Float","Boolean","String","Text","Date","DateTime","Time"]
  
    for i in range(0,numerocampi,1):                 #chiede n volte all'utente come si chiama la colonna e il dato da inserire
      acconsentito = "N"
      while (acconsentito != "S"):
        nomicolonne.append (input ("\n1)Inserisci il nome della colonna " + str(i+1) + ": "))   #rimane da controllare il campo nome sia corretto      
        iternumer=1
        for f in tipipermessi:
          print (str(iternumer) + "_" + f)   
          iternumer+=1
 
        tipodatocolonne.append (input ("2)Scegli il tipo di dato tra quelli ammessi elencati: "))
        if ((tipodatocolonne[i].isdigit() == True)and(int(tipodatocolonne[i])>len(tipipermessi))):
          tipodatocolonne[i]="errore"
        while (tipodatocolonne[i].isdigit() == False):      #controlla che il campo del tipo di dato sia numerico, se non lo è continua a far inserire il dato
          cancellaultimoelemento = tipodatocolonne.pop()    #cancella l'ultimo elemento del vettore in quanto avrebbe già appeso il tipo dato sbagliato
          tipodatocolonne.append (input ("Non hai inserito un numero corretto, scegli il tipo di dato tra quelli ammessi elencati: "))
          if ((tipodatocolonne[i].isdigit() == True)and(int(tipodatocolonne[i])>len(tipipermessi))):
            tipodatocolonne[i]="errore"

        notnullcolonne.append (input ("3)La colonna " + nomicolonne[i] + " deve essere NON nulla? specificare S per impedire: \n"))                       #NOTNULL      
        autoincrementcolonne.append (input ("4)La colonna " + nomicolonne[i] + " deve incrementarsi da sola? specificare S per consentire \n"))           #AUTO INCREMENT         
        indexuniquecolonne.append (input ("5)La colonna " + nomicolonne[i] + " è un indice unico? specificare S per abilitarlo \n"))                      #UNIQUE INDEX 
      
        acconsentito = input ("Confermi che la " + str(i+1) + "a colonna " + nomicolonne[i] + " sia di tipo (" + tipipermessi[int(tipodatocolonne[i])-1] + "): S o N ")

    chiaveprimaria = inseriscichiaveprim(nomicolonne , tipipermessi , tipodatocolonne , notnullcolonne , autoincrementcolonne , indexuniquecolonne , numerocampi)
    print ("Chiave Primaria = " + nomicolonne[int(chiaveprimaria)-1])
    
    print ("\n\n!!!!! MANCA LA FUNZIONE CHE EFFETTUA L'EFFETTIVO INSERIMENTO DELLA TABELLA NEL DATABASE !!!!!\n")
    print ("\n\n!!!!! L'idea era di creare una classe, scorrere da 0 al numero dei campi della tabella,\n\
  e per ogni ciclo del for creare una riga <nomecolonna[i]> <tipocolonna[i] etc. \n\
  ma non ho capito come concatenare il ciclo for alla creazione della Classe. Da approfondire in futuro\n")
    
    k=0
    for t in range(0,numerocampi,1): 
      stringaclasseinserimento = ""
        
  else:       
    Base.metadata.create_all(engine)    
  
  return (1)

def inseriscichiaveprim(nomicolonne , tipipermessi , tipodatocolonne , notnullcolonne , autoincrementcolonne , indexuniquecolonne , numerocampi):
  """
  Fa inserire all'utente la chiave primaria, controlla che non ci siano caratteri errati e la restituisce
  """  
  iternumer=1
  print("\n")
  for f in nomicolonne:
    print (iternumer , f , tipipermessi[(int(tipodatocolonne[iternumer-1]))-1], notnullcolonne[iternumer-1], autoincrementcolonne[iternumer-1], indexuniquecolonne[iternumer-1])
    iternumer+=1
  chiaveprimaria = input ("Scegli quale colonna utilizzare come chiave primaria: \n")
  if ((chiaveprimaria.isdigit() == True)and(int(chiaveprimaria)>numerocampi)):
    chiaveprimaria="errore"
    while (chiaveprimaria.isdigit() == False):
      chiaveprimaria = input ("Scegli quale colonna utilizzare come chiave primaria: \n")
      if ((chiaveprimaria.isdigit() == True)and(int(chiaveprimaria)>numerocampi)):
        chiaveprimaria="errore"  
  return (chiaveprimaria)