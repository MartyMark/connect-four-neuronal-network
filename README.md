# connect-four-neuronal-network

TO-DO:

- Wenn Ki spielt → Spiele aufnehmen zum Lernen
- In AWS Deployen und Continues Integration

###Getting Started

**Service starten**

    Terminal -> ./start 

Postman

![img.png](doc/postman_predict_post.png)

**Model trainieren** 

    Terminal -> python3 src/train_command.py

**Model testen** 

    Terminal -> python3 src/test_command.py

###Schnittstellen:

**Zug vorhersagen**

TO-DO: Doku → Wie wird Schnittstelle benutzt

- Datensatz sieht wie folgt aus: [(1,[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,-1]]), (1,[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,0,0,0,0,0,-1]])]
- Ein Array aus Tupel → Jedes Tupel besteht, dem Wert (links) der gewonnen hat, und dem Board zu dem Spielzug (rechts)