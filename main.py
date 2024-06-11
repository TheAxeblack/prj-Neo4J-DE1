"""
Fichier comportant les éléments demandés pour le projet Neo4J
"""

# Import des bibliothèques nécessaires
from neo4j import GraphDatabase

URI="localhost:7687"
AUTH=("neo4j", "motdepasse")

# TODO : Faire le projet

# On créé le client pour pouvoir interagir avec la base de données
with GraphDatabase.driver(URI, auth=AUTH) as driver:
    # On vérifie que la connexion est bien établie
    driver.verify_connectivity()
    # Création des noeuds
    # Création des entreprises
    #  CREATE (e:Enterprise {name: "Casino", activity:"Grande distribution", description:"Blabla ...", size:"55000"})
    #CREATE (e:Enterprise {name:"EDF", activity:"Energie", description:"Blabla ...", size:"10000"})
    #CREATE (e:Enterprise {name:"Caisse d'épargne", activity:"Finance", description:"Blabla ...", size:"37800"})
    #CREATE (e:Enterprise {name:"Ubisoft", activity:"Jeux-vidéo", description:"Blabla ...", size:"15000"})
    # CREATE (e:Enterprise {name:"Caisse d'épargne", activity:"Finance", description:"Blabla ...", size:"37800"})
    
    # Création des utilisateurs
    # CREATE (u:User {name: "Mathis", surname:"Lécuyer", description:"C'est Mathis", skills:"Bronze 2 LOL, C++, BigQuery"})
    # CREATE (u:User {name: "Enzo", surname:"Caruso", description:"C'est Enzo", skills:"Bash, Rocket League"})
    # CREATE (u:User {name: "Hicham", surname:"Aïdel", description:"C'est Hicham", skills:"League of Legends, VBA, SQL server"})
    