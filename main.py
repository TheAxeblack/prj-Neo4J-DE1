"""
Fichier comportant les éléments demandés pour le projet Neo4J
"""

# Import des bibliothèques nécessaires
from neo4j import GraphDatabase

URI = "localhost:7687"  # Adresse de la base de données
AUTH = ("neo4j", "motdepasse")  # Identifiants de connexion

# On crée le client pour pouvoir interagir avec la base de données
with GraphDatabase.driver(URI, auth=AUTH) as driver:
    # On vérifie que la connexion est bien établie
    driver.verify_connectivity()

    # Création des nœuds
    # Création des entreprises du LinkedIn-like
    driver.execute_query(
        "CREATE (e:Enterprise {name: $name, activity:$activity, description:$description, size:$size})",
        name="Casino",  # Nom de l'entreprise
        activity="Grande distribution",  # Secteur d'activité de l'entreprise
        description="Blabla ...",  # On peut mettre une description de l'entreprise
        size=50000,  # On précise la taille de l'entreprise (nombre d'employés)
        database_="neo4j"  # On précise la base de données à utiliser
    )

    driver.execute_query(
        "CREATE (e:Enterprise {name: $name, activity:$activity, description:$description, size:$size})",
        name="EDF",
        activity="Energie",
        description="Blabla ...",
        size=10000,
        database_="neo4j")

    driver.execute_query(
        "CREATE (e:Enterprise {name: $name, activity:$activity, description:$description, size:$size})",
        name="Caisse d'épargne",
        activity="Finance",
        description="Blabla ...",
        size=37800,
        database_="neo4j")

    driver.execute_query(
        "CREATE (e:Enterprise {name: $name, activity:$activity, description:$description, size:$size})",
        name="Ubisoft",
        activity="Jeux-vidéo",
        description="Blabla ...",
        size=15000,
        database_="neo4j")

    driver.execute_query(
        "CREATE (e:Enterprise {name: $name, activity:$activity, description:$description, size:$size})",
        name="Caisse d'épargne",
        activity="Finance",
        description="Blabla ...",
        size=37800,
        database_="neo4j")

    # Affichage des entreprises précédemment créées
    records, summary, keys = driver.execute_query("MATCH (e:Enterprise) RETURN e", database_="neo4j")
    for record in records:
        print(record.data())

    # Création des utilisateurs du LinkedIn-like on passe par un dict pour les données
    # CREATE (u:User {name: "Mathis", surname:"Lécuyer", description:"C'est Mathis", skills:"Bronze 2 LOL, C++, BigQuery"})
    user1 = {
        "name": "Mathis",
        "surname": "Lécuyer",
        "description": "C'est Mathis",
        "skills": {
            "Bronze 2 LOL",
            "C++",
            "BigQuery"
        }
    }
    driver.execute_query(
        "CREATE (u:User {name: $name, surname:$surname, description:$description, skills:$skills})",
        parameters_=user1,
        database_="neo4j", )

    # CREATE (u:User {name: "Enzo", surname:"Caruso", description:"C'est Enzo", skills:"Bash, Rocket League"})
    # CREATE (u:User {name: "Hicham", surname:"Aïdel", description:"C'est Hicham", skills:"League of Legends, VBA, SQL server"})
