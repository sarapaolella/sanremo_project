import pandas as pd

new_entries = []

def add(year, artist, song, position, category="Campioni"):
    new_entries.append([year, artist, song, position, category])

# ===== 1990 =====
add(1990, "Pooh", "Uomini soli", 1)
add(1990, "Toto Cutugno", "Gli amori", 2)
add(1990, "Amedeo Minghi & Mietta", "Vattene amore", 3)
for a,s in [("Anna Oxa","Donna con te"),("Marcella & Gianni Bella","Verso l'ignoto"),
            ("Mia Martini","La nevicata del '56"),("Mango","Tu... si"),
            ("Francesco Salvi","A"),("Caterina Caselli","Bisognerebbe non pensare che a te"),
            ("Riccardo Fogli","Ma quale amore"),("Sandro Giacobbe","Io vorrei"),
            ("Paola Turci","Ringrazio Dio"),("Milva","Sono felice"),
            ("Grazia Di Michele","Io e mio padre"),("Lena Biolcati","Amori"),
            ("Peppino di Capri","Evviva Maria"),("Mino Reitano","Vorrei"),
            ("Christian","Amore"),("Ricchi e Poveri","Buona giornata"),
            ("Eugenio Bennato & Tony Esposito","Novecento aufwiedersehen")]:
    add(1990, a, s, "NF")
add(1990, "Marco Masini", "Disperato", 1, "Giovani")
add(1990, "Franco Fasano", "Vieni a stare qui", 2, "Giovani")
add(1990, "Gianluca Guidi", "Secondo te", 3, "Giovani")
for a,s in [("Armando De Razza","La lambada strofinera"),("Rosalinda Celentano","L'eta dell'oro"),
            ("Dario Gai","Noi che non diciamo mai mai"),("Silvia Mezzanotte","Sarai grande"),
            ("Future","Ti diro"),("Beppe De Francia & Bea Giannini","Una storia da raccontare"),
            ("Lijao","Un cielo che si muove"),("Lipstick","Che donne saremo"),
            ("Rose Crisci","Favolando"),("Elite","Malinconia d'ottobre"),
            ("Proxima","Oh dolce amor!"),("Maurizio Della Rosa","Per curiosita"),
            ("Sergio Laccone","Sbandamenti")]:
    add(1990, a, s, "NF", "Giovani")

# ===== 1991 =====
add(1991, "Riccardo Cocciante", "Se stiamo insieme", 1)
add(1991, "Renato Zero", "Spalle al muro", 2)
add(1991, "Marco Masini", "Perche lo fai", 3)
add(1991, "Umberto Tozzi", "Gli altri siamo noi", 4)
add(1991, "Pierangelo Bertoli ft. Tazenda", "Spunta la Luna dal monte", 5)
add(1991, "Amedeo Minghi", "Nene", 6)
add(1991, "Mietta", "Dubbi no", 7)
add(1991, "Al Bano e Romina Power", "Oggi sposi", 8)
add(1991, "Riccardo Fogli", "Io ti prego di ascoltare", 9)
add(1991, "Raf", "Oggi un Dio non ho", 10)
add(1991, "Enzo Jannacci", "La fotografia", 11)
add(1991, "Fiordaliso", "Il mare piu grande che c'e", 12)
add(1991, "Sabrina Salerno & Jo Squillo", "Siamo donne", 13)
add(1991, "Ladri di Biciclette", "Sbatti ben su del Be Bop", 14)
add(1991, "Eduardo De Crescenzo", "E la musica va", 15)
add(1991, "Grazia Di Michele", "Se io fossi un uomo", 16)
add(1991, "Rossana Casale", "Terra", 17)
add(1991, "Loredana Berte", "In questa citta", 18)
add(1991, "Gianni Bella", "La fila degli oleandri", 19)
add(1991, "Mariella Nava", "Gli uomini", 20)
add(1991, "Paolo Vallesi", "Le persone inutili", 1, "Giovani")
add(1991, "Irene Fargo", "La donna di Ibsen", 2, "Giovani")
add(1991, "Rita Forte", "E soltanto una canzone", 3, "Giovani")
for a,s in [("Fandango","Che grossa nostalgia"),("Compilations","Donne del 2000"),
            ("Bungaro, Marco Conidi & Rosario Di Bella","E noi qui"),
            ("Patrizia Bulgari","Giselle"),("Marco Carena","Serenata"),
            ("Gitano","Tamure"),("Paola De Mas","Notte di periferia"),
            ("Stefania La Fauci","Caramba"),("Rudy Marra","Gaetano"),
            ("Gianni Mazza","Il lazzo"),("Timoria","L'uomo che ride"),
            ("Giovanni Nuti","Non e poesia"),("Dario Gai","Sorelle d'Italia")]:
    add(1991, a, s, "NF", "Giovani")

# ===== 1992 =====
add(1992, "Luca Barbarossa", "Portami a ballare", 1)
add(1992, "Mia Martini", "Gli uomini non cambiano", 2)
add(1992, "Paolo Vallesi", "La forza della vita", 3)
add(1992, "Pierangelo Bertoli", "Italia d'oro", 4)
add(1992, "Massimo Ranieri", "Ti penso", 5)
add(1992, "Matia Bazar", "Piccoli giganti", 6)
add(1992, "Flavia Fortunato & Franco Fasano", "Per niente al mondo", 7)
add(1992, "Tazenda", "Pitzinnos in sa gherra", 8)
add(1992, "Fausto Leali", "Perche", 9)
add(1992, "Riccardo Fogli", "In una notte cosi", 10)
add(1992, "Michele Zarrillo", "Strade di Roma", 11)
add(1992, "Mariella Nava", "Mendicante", 12)
add(1992, "Drupi", "Un uomo in piu", 13)
add(1992, "Peppino di Capri & Pietra Montecorvino", "Favola blues", 14)
add(1992, "New Trolls", "Quelli come noi", 15)
for a,s in [("Ricchi e Poveri","Cosi lontani"),("Scialpi","E una nanna"),
            ("Lina Sastri","Femmene 'e mare"),("Paolo Mengoli","Io ti daro"),
            ("Pupo","La mia preghiera"),("Mino Reitano","Ma ti sei chiesto mai"),
            ("Nuova Compagnia di Canto Popolare","Pe' dispietto"),
            ("Giorgio Faletti & Orietta Berti","Rumba di tango"),
            ("Formula 3","Un frammento rosa")]:
    add(1992, a, s, "NF")
add(1992, "Aleandro Baldi & Francesca Alotta", "Non amarmi", 1, "Giovani")
add(1992, "Irene Fargo", "Come una Turandot", 2, "Giovani")
add(1992, "Alessandro Bono ft. Andrea Mingardi", "Con un amico vicino", 3, "Giovani")
for a,s in [("Lorenzo Zecchino","Che ne sai della notte"),("Patrizia Bulgari","Amica di scuola"),
            ("Alessandro Canino","Brutta"),("Rita Forte","Non e colpa di nessuno"),
            ("Massimo Modugno","Uomo allo specchio"),("Statuto","Abbiamo vinto il Festival di Sanremo"),
            ("Tosca","Cosa fara Dio di me"),("Bracco Di Graci","Datemi per favore"),
            ("Aida Satta Flores","Io scappo via"),("Gatto Panceri","L'amore va oltre"),
            ("Stefano Polo","Piccola Africa"),("Andrea Monteforte","Principessa scalza"),
            ("Tomato","Sai cosa sento per te"),("Giampaolo Bertuzzi","Un altro mondo nell'universo"),
            ("Aeroplanitaliani","Zitti zitti")]:
    add(1992, a, s, "NF", "Giovani")

# ===== 1993 =====
add(1993, "Enrico Ruggeri", "Mistero", 1)
add(1993, "Cristiano De Andre", "Dietro la porta", 2)
add(1993, "Rossana Casale & Grazia Di Michele", "Gli amori diversi", 3)
add(1993, "Matia Bazar", "Dedicato a te", 4)
add(1993, "Renato Zero", "Ave Maria", 5)
add(1993, "Mietta & I Ragazzi di Via Meda", "Figli di chi", 6)
add(1993, "Paola Turci", "Stato di calma apparente", 7)
add(1993, "Biagio Antonacci", "Non so piu a chi credere", 8)
add(1993, "Amedeo Minghi", "Notte bella, magnifica", 9)
add(1993, "Francesca Alotta", "Un anno di noi", 10)
add(1993, "Andrea Mingardi", "Sogno", 11)
add(1993, "Roberto Murolo", "L'Italia e bella", 12)
add(1993, "Tullio De Piscopo", "Qui gatta ci cova", 13)
add(1993, "Loredana Berte & Mia Martini", "Stiamo come stiamo", 14)
add(1993, "Nino Buonocore", "Una canzone d'amore", 15)
for a,s in [("Jo Squillo","Balla italiano"),("Ladri di Biciclette ft. Tony Esposito","Cambiamo musica"),
            ("Maurizio Vandelli, Dik Dik & I Camaleonti","Come passa il tempo"),
            ("Francesco Salvi","Dammi 1 bacio"),("Peppino Gagliardi","L'alba"),
            ("Peppino di Capri","La voce delle stelle"),("Schola Cantorum","Sulla strada del mare"),
            ("Alessandro Canino","Tu tu tu tu"),("Milva","Uomini addosso")]:
    add(1993, a, s, "NF")
add(1993, "Laura Pausini", "La solitudine", 1, "Giovani")
add(1993, "Gerardina Trovato", "Ma non ho piu la mia citta", 2, "Giovani")
add(1993, "Nek", "In te", 3, "Giovani")
for a,s in [("Bracco Di Graci","Guardia o ladro"),("Erminio Sinni","L'amore vero"),
            ("Rosario Di Bella","Non volevo"),("Marco Conidi","Non e tardi"),
            ("Fandango","Non ci prenderanno mai"),("Tony Blescia","Quello che non siamo"),
            ("Angela Baraldi","A piedi nudi"),("Leo Leandro","Caramella"),
            ("Antonella Bucci","Il mare delle nuvole"),("Clio","Non dire mai"),
            ("Maria Grazia Impero","Tu con la mia amica")]:
    add(1993, a, s, "NF", "Giovani")

# ===== 1994 =====
add(1994, "Aleandro Baldi", "Passera", 1)
add(1994, "Giorgio Faletti", "Signor tenente", 2)
add(1994, "Laura Pausini", "Strani amori", 3)
add(1994, "Gerardina Trovato", "Non e un film", 4)
add(1994, "Michele Zarrillo", "Cinque giorni", 5)
add(1994, "Enzo Jannacci & Paolo Rossi", "I soliti accordi", 6)
add(1994, "Ivan Graziani", "Maledette malelingue", 7)
add(1994, "Andrea Mingardi", "Amare amare", 8)
add(1994, "Marco Armani", "Esser duri", 9)
add(1994, "Donatella Rettore", "Di notte specialmente", 10)
add(1994, "Mariella Nava", "Terra mia", 11)
add(1994, "Formula 3", "La casa dell'imperatore", 12)
add(1994, "Loredana Berte", "Amici non ne ho", 13)
add(1994, "Alessandro Canino", "Crescerai", 14)
add(1994, "Francesco Salvi", "Statento", 15)
add(1994, "Alessandro Bono", "Oppure no", 16)
add(1994, "Claudia Mori", "Se mi ami", 17)
add(1994, "Carlo Marrale", "L'ascensore", 18)
add(1994, "Squadra Italia", "Una vecchia canzone italiana", 19)
add(1994, "Franco Califano", "Napoli", 20)
add(1994, "Andrea Bocelli", "Il mare calmo della sera", 1, "Giovani")
add(1994, "Antonella Arancio", "Ricordi del cuore", 2, "Giovani")
add(1994, "Danilo Amerio", "Quelli come noi", 3, "Giovani")
for a,s in [("Irene Grandi","Fuori"),("Valeria Visconti","Cosi vivrai"),
            ("Lighea","Possiamo realizzare i nostri sogni"),("Giorgia","E poi"),
            ("Francesca Schiavo","Il mondo e qui"),("Silvia Cecchetti","Il mondo dove va"),
            ("Gio Di Tonno","Senti uomo"),("Paola Angeli","Cuore cuore"),
            ("Simona D'Alessio","E solo un giorno nero"),("Baraonna","I giardini d'Alhambra"),
            ("Daniela Colace","Io e il mio amico Neal"),("Franz Campi","Ma che sarei"),
            ("Joe Barbieri","Non spegnere i tuoi occhi"),("Paideja","Propiziu ventu"),
            ("Daniele Fossati","Senza un dolore")]:
    add(1994, a, s, "NF", "Giovani")

# ===== 1995 =====
add(1995, "Giorgia", "Come saprei", 1)
add(1995, "Gianni Morandi & Barbara Cola", "In amore", 2)
add(1995, "Spagna", "Gente come noi", 3)
add(1995, "Andrea Bocelli", "Con te partiro", 4)
add(1995, "Fiorello", "Finalmente tu", 5)
for i,(a,s) in enumerate([("Danilo Amerio","Bisogno d'amore"),("Lighea","Rivoglio la mia vita"),
            ("883","Senza averti qui"),("Antonella Arancio","Piu di cosi"),
            ("Lorella Cuccarini","Un altro amore no"),("Mango","Dove vai"),
            ("Giorgio Faletti","L'assurdo mestiere"),
            ("Peppino di Capri, Gigi Proietti & Stefano Palatresi","Ma che ne sai"),
            ("Gigliola Cinquetti","Giovane vecchio cuore"),("Massimo Ranieri","La vestaglia"),
            ("Drupi","Voglio una donna"),("Toto Cutugno","Voglio andare a vivere in campagna"),
            ("Sabina Guzzanti & La Riserva Indiana","Troppo sole"),
            ("Loredana Berte","ANGELI & angeli"),("Patty Pravo","I giorni dell'armonia")], 6):
    add(1995, a, s, i)
for a,s in [("Francesca Schiavo","Amore e guerra"),("Valeria Visconti","E con te"),
            ("Gio Di Tonno","Padre e padrone")]:
    add(1995, a, s, "NF")
add(1995, "Neri per Caso", "Le ragazze", 1, "Giovani")
add(1995, "Massimo Di Cataldo", "Che sara di me", 2, "Giovani")
add(1995, "Gigi Finizio", "Lo specchio dei pensieri", 3, "Giovani")
for a,s in [("Rossella Marcone","Un posto al sole"),("Dhamm","Ho bisogno di te"),
            ("Gianluca Grignani","Destinazione Paradiso"),("Raffaella Cavalli","Sentimento"),
            ("Fedele Boccassini","Le foglie"),("Mara","Dentro di me"),
            ("Daniele Silvestri","L'uomo col megafono"),("Prefisso","Chi piu ne ha"),
            ("Rock Galileo","Le cose di ieri"),("Gloria","Le voci di dentro"),
            ("Deco","Monica"),("Flavia Astolfi","Per amore"),
            ("Fabrizio Consoli","Quando saprai")]:
    add(1995, a, s, "NF", "Giovani")

# ===== 1996 =====
for i,(a,s) in enumerate([("Ron & Tosca","Vorrei incontrarti fra cent'anni"),
    ("Elio e le Storie Tese","La terra dei cachi"),("Giorgia","Strano il mio destino"),
    ("Spagna","E io penso a te"),("Neri per Caso","Mai piu sola"),
    ("Massimo Di Cataldo","Se adesso te ne vai"),("Albano Carrisi","E la mia vita"),
    ("Aleandro Baldi ft. Marco Guerzoni","Soli al bar"),("Amedeo Minghi","Cantare e d'amore"),
    ("Paola Turci","Volo cosi"),("Michele Zarrillo","L'elefante e la farfalla"),
    ("Luca Barbarossa","Il ragazzo con la chitarra"),("Federico Salvatore","Sulla porta"),
    ("Rossella Marcone","Una vita migliore"),("Enrico Ruggeri","L'amore e un attimo"),
    ("Raffaella Cavalli","Saro"),("Gigi Finizio","Solo lei"),
    ("Paolo Vallesi","Non andare via"),("Riccardo Fogli","Romanzo"),
    ("New Trolls & Umberto Bindi","Letti")], 1):
    add(1996, a, s, i)
for a,s in [("Dhamm","Ama"),("Mara","Non e amore"),("Fedele Boccassini","Non scherzare dai")]:
    add(1996, a, s, "NF")
add(1996, "Syria", "Non ci sto", 1, "Giovani")
add(1996, "Adriana Ruocco", "Saro bellissima", 2, "Giovani")
add(1996, "Marina Rei", "Al di la di questi anni", 3, "Giovani")
for a,s in [("O.R.O.","Quando ti senti sola"),("Silvia Salemi","Quando il cuore"),
            ("Jalisse","Liberami"),("Olivia","Sottovoce"),("Carmen Consoli","Amore di plastica"),
            ("Petra Magoni","E ci sei"),("Camilla","Zerotretresette"),
            ("Alessandro Errico","Il grido del silenzio"),("Leandro Barsotti","Lasciarsi amare"),
            ("Alessandro Mara","Ci saro"),("Maurizio Lauzi","Un po' di tempo")]:
    add(1996, a, s, "NF", "Giovani")

# ===== 1997 =====
for i,(a,s) in enumerate([("Jalisse","Fiumi di parole"),("Anna Oxa","Storie"),
    ("Syria","Sei tu"),("Silvia Salemi","A casa di Luca"),("Fausto Leali","Non ami che te"),
    ("O.R.O.","Padre Nostro"),("Nek","Laura non c'e"),
    ("Patty Pravo","...E dimmi che non vuoi morire"),("Massimo Ranieri","Ti parlero d'amore"),
    ("Tosca","Nel respiro piu grande"),("Francesco Baccini","Senza tu"),
    ("Dirotta su Cuba","E andata cosi"),("Marina Rei","Dentro me"),
    ("Albano Carrisi","Verso il sole"),("Cattivi Pensieri","Quello che sento"),
    ("Pitura Freska","Papa nero"),("Toto Cutugno","Faccia pulita"),
    ("Ragazzi Italiani","Vero amore"),("New Trolls ft. Greta","Alianti liberi"),
    ("Loredana Berte","Luna")], 1):
    add(1997, a, s, i)
for a,s in [("Alessandro Mara","Attimi"),("Camilla","Come ti tradirei"),
            ("Carmen Consoli","Confusa e felice"),("Alessandro Errico","E pensero al tuo viso..."),
            ("Leandro Barsotti","Fragolina"),("Maurizio Lauzi","Il capo dei giocattoli"),
            ("Olivia","Quando viene sera"),("Adriana Ruocco","Uguali uguali"),
            ("Petra Magoni","Voglio un Dio")]:
    add(1997, a, s, "NF")
add(1997, "Paola e Chiara", "Amici come prima", 1, "Giovani")
for a,s in [("Niccolo Fabi","Capelli"),("Alex Baroni","Cambiare"),("Domino","Io senza te"),
            ("MikiMix","E la notte se ne va"),("Tony Blescia","E ti sento"),
            ("Vito Marletta","Innamorarsi e"),("Randy Roberts","No stop"),
            ("Paolo Carta","Non si puo dire mai... mai!"),("Massimo Caggiano","Ora che ci sei"),
            ("D.O.C. Rock","Secolo crudele"),("Luca Lombardi","Sonia dice di no")]:
    add(1997, a, s, "NF", "Giovani")

# ===== 1998 =====
for i,(a,s) in enumerate([("Annalisa Minetti","Senza te o con te"),
    ("Antonella Ruggiero","Amore lontanissimo"),("Lisa","Sempre"),
    ("Paola Turci","Solo come me"),("Silvia Salemi","Pathos"),
    ("Mango ft. Zenima","Luce"),("Luca Sepe","Un po' di te"),
    ("Niccolo Fabi","Lasciarsi un giorno a Roma"),("Ron","Un porto nel vento"),
    ("Andrea Mingardi","Canto per te"),("Alex Baroni","Sei tu o lei"),
    ("Spagna","E che mai sara"),("Piccola Orchestra Avion Travel","Dormi e sogna"),
    ("Sergio Caputo","Flamingo"),("Nuova Compagnia di Canto Popolare","Sotto il velo del cielo"),
    ("Paola e Chiara","Per te"),("Enzo Jannacci","Quando un musicista ride")], 1):
    add(1998, a, s, i)
for a,s in [("Paola Folli","Ascoltami"),("Percentonetto","Come il sole"),
            ("Costa","Compagna segreta"),("Taglia 42","Con il naso in su"),
            ("Alessandro Pitoni","Dimmi dov'e la strada per il paradiso"),
            ("Nitti e Agnello","I ragazzi innamorati"),("Luciferme","Il soffio"),
            ("Serena C","Quante volte sei"),("Eramo & Passavanti","Senza confini"),
            ("Federico Straga","Siamo noi"),("Liliana Tamberi","Un graffio in piu")]:
    add(1998, a, s, "NF", "Giovani")

# ===== 1999 =====
for i,(a,s) in enumerate([("Anna Oxa","Senza pieta"),("Antonella Ruggiero","Non ti dimentico"),
    ("Mariella Nava","Cosi e la vita"),("Enzo Gragnaniello & Ornella Vanoni","Alberi"),
    ("Stadio","Lo zaino"),("Albano Carrisi","Ancora in volo"),
    ("Marina Rei","Un inverno da baciare"),("Nino D'Angelo","Senza giacca e cravatta"),
    ("Daniele Silvestri","Aria"),("Nada","Guardami negli occhi"),
    ("Eugenio Finardi","Amami Lara"),("Gatto Panceri","Dove dov'e"),
    ("Gianluca Grignani","Il giorno perfetto"),("Massimo Di Cataldo","Come sei bella")], 1):
    add(1999, a, s, i)
add(1999, "Alex Britti", "Oggi sono io", 1, "Giovani")
add(1999, "Filippa Giordano", "Un giorno in piu", 2, "Giovani")
add(1999, "Leda Battisti", "Un fiume in piena", 3, "Giovani")
for a,s in [("Arianna","C'e che ti amo"),("Daniele Groff","Adesso"),
            ("Elena Cataneo","Nessuno puo fermare questo tempo"),
            ("Francesca Chiara","Ti amo che strano"),("Max Gazze","Una musica puo fare"),
            ("Allegra","Puoi fidarti di me"),("Soerba","Noi non ci capiamo"),
            ("Quintorigo","Rospo"),("Boris","Little Darling"),
            ("Dr. Livingstone","Al centro del mondo"),("Irene Lamedica","Quando lei non c'e")]:
    add(1999, a, s, "NF", "Giovani")

# ===== 2000 =====
for i,(a,s) in enumerate([("Piccola Orchestra Avion Travel","Sentimento"),
    ("Irene Grandi","La tua ragazza sempre"),("Gianni Morandi","Innamorato"),
    ("Max Gazze","Il timido ubriaco"),("Samuele Bersani","Replay"),
    ("Gerardina Trovato","Gechi e vampiri"),("Carmen Consoli","In bianco e nero"),
    ("Matia Bazar","Brivido caldo"),("Alice","Il giorno dell'indipendenza"),
    ("Gigi D'Alessio","Non dirgli mai"),("Subsonica","Tutti i miei sbagli"),
    ("Spagna","Con il tuo nome"),("Mietta","Fare l'amore"),
    ("Mariella Nava & Amedeo Minghi","Futuro come te"),
    ("Marco Masini","Raccontami di te"),("Umberto Tozzi","Un'altra vita")], 1):
    add(2000, a, s, i)
add(2000, "Jenny B", "Semplice sai", 1, "Giovani")
add(2000, "Tiromancino & Riccardo Sinigallia", "Strade", 2, "Giovani")
add(2000, "Luna", "Cronaca", 3, "Giovani")
for a,s in [("Andrea Miro","La canzone del perdono"),("Davide De Marinis","Chiedi quello che vuoi"),
            ("Alfonso Maria Parente","Che giorno sara"),("Lythium","Noel"),
            ("Enrico Sognato","E io ci penso ancora"),("Marjorie Biondo","Le margherite"),
            ("Erredieffe","Ognuno per se"),("Claudio Fiori","Fai la tua vita"),
            ("B.A.U.","Ogni ora"),("Fabrizio Moro","Un giorno senza fine"),
            ("Joe Barbieri","Non ci piove"),("Alessio Bonomo","La croce"),
            ("Laura Falcinelli","Uomo davvero"),("Moltheni","Nutriente"),
            ("Andrea Mazzacavallo","Nord-est")]:
    add(2000, a, s, "NF", "Giovani")

# ===== 2001 =====
for i,(a,s) in enumerate([("Elisa","Luce (Tramonti a nord est)"),
    ("Giorgia","Di sole e d'azzurro"),("Matia Bazar","Questa nostra grande storia d'amore"),
    ("Michele Zarrillo","L'acrobata"),("Paola Turci","Saluto l'inverno"),
    ("Jenny B","Anche tu"),("Alex Britti","Sono contento"),
    ("Gigi D'Alessio","Tu che ne sai"),("Fabio Concato","Ciao Ninin"),
    ("Anna Oxa","L'eterno movimento"),("Peppino di Capri","Piovera"),
    ("Gianni Bella","Il profumo del mare"),("Syria","Fantasticamenteamore"),
    ("Sottotono","Mezze verita"),("Quintorigo","Bentivoglio Angelina"),
    ("Bluvertigo","L'assenzio")], 1):
    add(2001, a, s, i)
add(2001, "Gazosa", "Stai con me (Forever)", 1, "Giovani")
for a,s in [("Moses","Maggie"),("Francesco & Giada","Turuturu"),
            ("Principe e Socio M.","Targato NA"),("Carlotta","Promessa"),
            ("Francesco Renga","Raccontami"),("Paolo Meneguzzi","Ed io non ci sto piu"),
            ("Carlito","Emily"),("XSense","Luna"),("Roberto Angelini","Il Signor Domani"),
            ("Sara 6","Bocca"),("Velvet","Nascosto dietro un vetro"),
            ("Stefano Ligi","Battiti"),("Riky Anelli","Ho vinto un viaggio"),
            ("Pincapallina","Quando io"),("Isola Song","Grazie")]:
    add(2001, a, s, "NF", "Giovani")

# ===== 2002 =====
for i,(a,s) in enumerate([("Matia Bazar","Messaggio d'amore"),("Alexia","Dimmi come..."),
    ("Gino Paoli","Un altro amore"),("Fausto Leali & Luisa Corna","Ora che ho bisogno di te"),
    ("Enrico Ruggeri","Primavera a Sarajevo"),("Mariella Nava","Il cuore mio"),
    ("Filippa Giordano","Amarti si"),("Francesco Renga","Tracce di te"),
    ("Fiordaliso","Accidenti a te"),("Gazosa","Ogni giorno di piu"),
    ("Michele Zarrillo","Gli angeli"),("Gianluca Grignani","Lacrime dalla Luna"),
    ("Alessandro Safina","Del perduto amore"),("Daniele Silvestri","Saliro"),
    ("Nino D'Angelo","Mari"),("Patty Pravo","L'immenso"),
    ("Loredana Berte","Dimmi che mi ami"),("Mino Reitano","La mia canzone"),
    ("Lollipop","Batte forte"),("Timoria","Casa mia")], 1):
    add(2002, a, s, i)
add(2002, "Anna Tatangelo", "Doppiamente fragili", 1, "Giovani")
for a,s in [("Valentina Giovagnini","Il passo silenzioso della neve"),
            ("Simone Patrizi","Se poi mi chiami"),("Gianni Fiorellino","Ricomincerei"),
            ("Archinue","La marcia dei santi"),("78 Bit","Fotografia"),
            ("Marco Morandi","Che ne so"),("Botero","Siamo treni"),
            ("Andrea Febo","All'infinito"),("Daniele Vit","Non finira"),
            ("Plastico 6","Fruscio"),("La Sintesi","Ho mangiato la mia ragazza"),
            ("Giuliodorme","Odore"),("Offside","Quando una ragazza c'e"),
            ("Dual Gang","Sara la primavera"),("Giacomo Celentano","You And Me")]:
    add(2002, a, s, "NF", "Giovani")

# ===== 2003 =====
for i,(a,s) in enumerate([("Alexia","Per dire di no"),("Alex Britti","7000 caffe"),
    ("Sergio Cammariere","Tutto quello che un uomo"),("Enrico Ruggeri & Andrea Miro","Nessuno tocchi Caino"),
    ("Syria","L'amore e"),("Lisa","Oceano"),("Giuni Russo","Moriro d'amore"),
    ("Silvia Salemi","Nel cuore delle donne"),("Antonella Ruggiero","Di un amore"),
    ("Luca Barbarossa","Fortuna"),("Nino D'Angelo","'A storia 'e nisciuno"),
    ("Cristiano De Andre","Un giorno nuovo"),("Fausto Leali","Eri tu"),
    ("Anna Oxa","Cambiero"),("Eiffel 65","Quelli che non hanno eta"),
    ("Bobby Solo & Little Tony","Non si cresce mai"),
    ("Anna Tatangelo & Federico Straga","Volere volare"),("Negrita","Tonight"),
    ("Amedeo Minghi","Sara una canzone"),("Iva Zanicchi","Fossi un tango")], 1):
    add(2003, a, s, i)
add(2003, "Dolcenera", "Siamo tutti la fuori", 1, "Giovani")
for a,s in [("Alina","Un piccolo amore"),("Zurawski","Lei che"),
            ("Verdiana","Chi sei non lo so"),("Gianni Fiorellino","Bastava un niente"),
            ("Daniele Stefani","Chiaraluna"),("Patrizia Laquidara","Lividi e fiori"),
            ("Elsa Lila","Valeria"),("Roberto Giglio","Cento cose"),
            ("Jacqueline M. Ferry","Vicina e lontana"),("Daniela Pedali","Vorrei"),
            ("Manuela Zanier","Amami"),("Allunati","Chiama di notte"),
            ("Marco Fasano","E gia"),("Maria Pia & SuperZoo","Tre fragole"),
            ("Filippo Merola","Mi sento libero")]:
    add(2003, a, s, "NF", "Giovani")

# ===== 2004 (single competition) =====
for i,(a,s) in enumerate([("Marco Masini","L'uomo volante"),("Mario Rosini","Sei la vita mia"),
    ("Linda","Aria, sole, terra e mare"),("Paolo Meneguzzi","Guardami negli occhi"),
    ("Bungaro","Guardastelle"),("Massimo Modugno ft. Gipsy Kings","Quando l'aria mi sfiora"),
    ("Stefano Picchi","Generale Kamikaze"),("Morris Albert & Mietta","Cuore"),
    ("Neffa","Le ore piccole"),("Mario Venuti","Crudele"),
    ("DJ Francesco","Era bellissimo"),("Simone","E stato tanto tempo fa"),
    ("DB Boulevard ft. Bill Wyman","Bastera"),("Andrea Mingardi & The Blues Brothers Band","E la musica"),
    ("Omar Pedrini","Lavoro inutile"),("Daniele Groff","Sei un miracolo"),
    ("Adriano Pappalardo","Nessun consiglio"),("Veruska","Un angelo legato a un palo"),
    ("Andre","Il nostro amore"),("Danny Losito ft. Las Ketchup","Single"),
    ("Pacifico","Solo un sogno"),("Piotta","Ladro di te")], 1):
    add(2004, a, s, i)

# ===== 2005 =====
add(2005, "Francesco Renga", "Angelo", 1)
add(2005, "Gigi D'Alessio", "L'amore che non c'e", 2)
add(2005, "Marco Masini", "Nel mondo dei sogni", 3)
for a,s in [("Paolo Meneguzzi","Non capiva che l'amavo"),("Umberto Tozzi","Le parole"),
            ("Antonella Ruggiero","Echi d'infinito"),("Alexia","Da grande"),
            ("Anna Tatangelo","Ragazza di periferia"),("Marina Rei","Fammi entrare"),
            ("Paola e Chiara","A modo mio"),
            ("Nicky Nicolai & Stefano Di Battista Jazz Quartet","Che mistero e l'amore"),
            ("Le Vibrazioni","Ovunque andro"),("Matia Bazar","Grido d'amore"),
            ("DJ Francesco Band","Francesca"),("Velvet","Dovevo dirti molte cose"),
            ("Toto Cutugno ft. Annalisa Minetti","Come noi nessuno al mondo"),
            ("Marcella Bella","Uomo bastardo"),("Peppino di Capri","La panchina"),
            ("Nicola Arigliano","Colpevole"),("Franco Califano","Non escludo il ritorno")]:
    add(2005, a, s, "NF")
add(2005, "Laura Bono", "Non credo nei miracoli", 1, "Giovani")
for a,s in [("La Differenza","Che faro"),("Veronica Ventavoli","L'immaginario"),
            ("Max De Angelis","Sono qui per questo"),("Equ","L'idea"),
            ("Giovanna D'Angi","Fammi respirare"),("Sabrina Guida","Vorrei"),
            ("Concido","Ci vuole k..."),("Moda","Riesci a innamorarmi"),
            ("Enrico Boccadoro","Dov'e la terra capitano?"),
            ("Christian Lo Zito","Segui il tuo cuore"),("Negramaro","Mentre tutto scorre")]:
    add(2005, a, s, "NF", "Giovani")

# ===== 2006 =====
add(2006, "Povia", "Vorrei avere il becco", 1)
for a,s in [("Alex Britti","...solo con te"),("Ron","L'uomo delle stelle"),
            ("Michele Zarrillo","L'alfabeto degli amanti"),("Luca Dirisio","Spariro"),
            ("Gianluca Grignani","Liberi di sognare"),("Dolcenera","Com'e straordinaria la vita"),
            ("Anna Tatangelo","Essere una donna"),("Nicky Nicolai","Lei ha la notte"),
            ("Spagna","Noi non possiamo cambiare"),("Simona Bencini","Tempesta"),
            ("Anna Oxa","Processo a me stessa"),("Nomadi","Dove si va"),
            ("Zero Assoluto","Svegliarsi la mattina"),
            ("Noa, Carlo Fava & Solis String Quartet","Un discorso in generale"),
            ("Mario Venuti & Arancia Sonora","Un altro posto nel mondo"),
            ("Sugarfree","Solo lei mi da"),
            ("I Ragazzi di Scampia & Gigi Finizio","Musica e speranza")]:
    add(2006, a, s, "NF")
add(2006, "Riccardo Maffoni", "Sole negli occhi", 1, "Giovani")
add(2006, "Simone Cristicchi", "Che bella gente", "NF", "Giovani")
for a,s in [("Monia Russo","Un mondo senza parole"),("Helena Hellwig","Di luna morirei"),
            ("L'Aura","Irraggiungibile"),("Tiziano Orecchio","Preda innocente"),
            ("Virginio","Davvero"),("Deasonika","Non dimentico piu"),
            ("Antonello","Capiro crescerai"),("Ameba4","Rido... forse mi sbaglio"),
            ("Ivan Segreto","Con un gesto"),("Andrea Ori","Nel tuo mare")]:
    add(2006, a, s, "NF", "Giovani")

# ===== 2007 =====
for i,(a,s) in enumerate([("Simone Cristicchi","Ti regalero una rosa"),
    ("Albano","Nel perdono"),("Piero Mazzocchetti","Schiavo d'amore"),
    ("Daniele Silvestri","La paranza"),("Mango","Chissa se nevica"),
    ("Paolo Meneguzzi","Musica"),("Tosca","Il terzo fuochista"),
    ("Francesco Facchinetti & Roby Facchinetti","Vivere normale"),
    ("Zero Assoluto","Appena prima di partire"),("Antonella Ruggiero","Canzone fra le guerre")], 1):
    add(2007, a, s, i)
for a,s in [("Nada","Luna in piena"),("Paolo Rossi","In Italia si sta male"),
            ("Velvet","Tutto da rifare"),("Johnny Dorelli","Meglio cosi"),
            ("Amalia Gre","Amami per sempre"),("Marcella Bella & Gianni Bella","Forever (Per sempre)"),
            ("Fabio Concato","Oltre il giardino"),("Leda Battisti","Senza me ti pentirai"),
            ("Stadio","Guardami"),("Milva","The Show Must Go On")]:
    add(2007, a, s, "NF")
add(2007, "Fabrizio Moro", "Pensa", 1, "Giovani")
add(2007, "Stefano Centomo", "Bivio", 2, "Giovani")
add(2007, "Pquadro", "Malinconiche sere", 3, "Giovani")
for a,s in [("Marco Baroni","L'immagine che ho di te"),("Sara Galimberti","Amore ritrovato"),
            ("Elsa Lila","Il senso della vita"),("Romina Falconi","Ama"),
            ("Jasmine","La vita subito"),("Mariangela","Ninna nanna"),
            ("Khorachane","La ballata di Gino"),("Grandi Animali Marini","Napoleone Azzurro"),
            ("Patrizio Bau","Peccati di gola"),("FSC","Non piangere"),
            ("Pier Cortese","Non ho tempo")]:
    add(2007, a, s, "NF", "Giovani")

# ===== 2008 =====
for i,(a,s) in enumerate([("Gio Di Tonno & Lola Ponce","Colpo di fulmine"),
    ("Anna Tatangelo","Il mio amico"),("Fabrizio Moro","Eppure mi hai cambiato la vita"),
    ("Toto Cutugno","Un falco chiuso in gabbia"),("Tiromancino","Il rubacuori"),
    ("Paolo Meneguzzi","Grande"),("Finley","Ricordi"),
    ("Gianluca Grignani","Cammina nel sole"),("Little Tony","Non finisce qui")], 1):
    add(2008, a, s, i)
for a,s in [("Max Gazze","Il solito sesso"),("Tricarico","Vita tranquilla"),
            ("Sergio Cammariere","L'amore non si spiega"),("Eugenio Bennato","Grande sud"),
            ("L'Aura","Basta!"),("Amedeo Minghi","Cammina cammina"),
            ("Mario Venuti","A ferro e fuoco"),("Frankie Hi-NRG MC","Rivoluzione"),
            ("Michele Zarrillo","L'ultimo film insieme"),("Mietta","Baciami adesso"),
            ("Loredana Berte","Musica e parole")]:
    add(2008, a, s, "NF")
add(2008, "Sonohra", "L'amore", 1, "Giovani")
add(2008, "La Scelta", "Il nostro tempo", 2, "Giovani")
add(2008, "Jacopo Troiani", "Ho bisogno di sentirmi dire ti voglio bene", 3, "Giovani")
for a,s in [("Milagro","Domani"),("Frank Head","Para para ra rara"),
            ("Valerio Sanzotta","Novecento"),("Giua","Tanto non vengo"),
            ("Ariel","Ribelle"),("Andrea Bonomo","Anna"),
            ("Melody Fall","Ascoltami"),("Daniele Battaglia","Voce nel vento"),
            ("Rosario Morisco","Signorsi"),("Francesco Rapetti","Come un'amante"),
            ("Valeria Vaglio","Ore ed ore")]:
    add(2008, a, s, "NF", "Giovani")

# ===== 2009 =====
add(2009, "Marco Carta", "La forza mia", 1)
add(2009, "Sal Da Vinci", "Non riesco a farti innamorare", 2)
add(2009, "Povia", "Luca era gay", 3)
add(2009, "Marco Masini", "L'Italia", 4)
add(2009, "Patty Pravo", "E io verro un giorno la", 5)
add(2009, "Francesco Renga", "Uomo senza eta", 6)
add(2009, "Alexia & Mario Lavezzi", "Biancaneve", 7)
add(2009, "Fausto Leali", "Una piccola parte di te", 8)
add(2009, "Albano", "L'amore e sempre amore", 9)
for a,s in [("Dolcenera","Il mio amore unico"),("Pupo, Paolo Belli & Youssou N'Dour","L'opportunita"),
            ("Gemelli Diversi","Vivi per un miracolo"),("Nicky Nicolai & Stefano Di Battista","Piu sole"),
            ("Francesco Tricarico","Il bosco delle fragole"),("Afterhours","Il paese e reale"),
            ("Iva Zanicchi","Ti voglio senza amore")]:
    add(2009, a, s, "NF")
add(2009, "Arisa", "Sincerita", 1, "Giovani")
for a,s in [("Malika Ayane","Come foglie"),("Irene Fornaciari","Spiove il sole"),
            ("Simona Molinari","Egocentrica"),("Filippo Perbellini","Cuore senza cuore"),
            ("Silvia Aprile","Un desiderio arrivera"),("Karima Ammar","Come in ogni ora"),
            ("Chiara Canzian","Prova a dire il mio nome"),("Iskra Menarini","Quasi amore"),
            ("Barbara Gilbo","Che ne sai di me")]:
    add(2009, a, s, "NF", "Giovani")

# Read existing CSV and merge
df_old = pd.read_csv('lista_canzoni_sanremo.csv')
print(f"Existing CSV: {len(df_old)} rows")

df_new = pd.DataFrame(new_entries, columns=['year','artist','song','position','category'])
print(f"New entries: {len(df_new)} rows for years {sorted(df_new['year'].unique())}")

overlap = set(df_old['year'].unique()) & set(df_new['year'].unique())
if overlap:
    print(f"WARNING: Year overlap detected: {overlap}")

df_all = pd.concat([df_old, df_new], ignore_index=True)
df_all = df_all.sort_values('year')
df_all.to_csv('lista_canzoni_sanremo.csv', index=False)
print(f"Final CSV: {len(df_all)} rows")

for y in range(1990, 2010):
    n = len(df_all[df_all['year'] == y])
    print(f"  {y}: {n} songs")
