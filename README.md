# Pipeline Big Data Avocado : Ingestion, Traitement et Analyse avec MySQL, NiFi, Spark et Hive

## Description 
🥑 Pipeline Big Data pour l'Analyse des Prix des Avocats
Ce projet démontre un workflow complet de traitement de données depuis l'ingestion initiale (fichiers CSV) jusqu'à l'analyse avancée, en utilisant une stack Big Data moderne :

MySQL pour le stockage initial,

Apache NiFi pour l'automatisation des flux,

HDFS/Spark pour le traitement distribué,

Hive pour l'analyse SQL et la création de vues agrégées.

🔧 Stack Technique :
MySQL · Apache NiFi · HDFS · PySpark · Hive · Cron

### 🚀 Fonctionnalités Clés :

Ingestion flexible : Chargement de fichiers CSV découpés dans MySQL, puis transfert vers HDFS via NiFi.

Traitement scalable :

Calcul du volume total par fichier avec Spark.

Enrichissement des données (extraction jour/mois depuis la date).

Analyse intelligente :

Création de tables/vues Hive pour requêter les données nettoyées.

Agrégation des volumes par mois (vue volume_per_month).

Automatisation :

Orchestration via cron (exécution périodique des jobs Spark et NiFi).

### 📊 Résultats Concrets :

Optimisation du stockage : Architecture multi-couches (raw → staging → refined).

Monitoring : Logs et vérifications à chaque étape pour garantir l'intégrité des données.
