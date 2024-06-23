from pyspark.sql import SparkSession
from pyspark.sql.functions import col, date_format, from_unixtime
from datetime import datetime

# Initialisation de SparkSession
spark = SparkSession.builder.appName("TraitementTousAvocados").getOrCreate()

try:
    # Récupérer la liste des fichiers dans le répertoire /stagging_avocado
    chemin_hdfs = "hdfs:///stagging_avocado/"
    fs = spark._jvm.org.apache.hadoop.fs.FileSystem.get(spark._jsc.hadoopConfiguration())
    liste_statuts_fichiers = fs.listStatus(spark._jvm.org.apache.hadoop.fs.Path(chemin_hdfs))
    fichiers = [fichier.getPath().getName() for fichier in liste_statuts_fichiers if fichier.isFile()]

    for nom_fichier in fichiers:
        # Lire chaque fichier CSV
        df = spark.read.csv(f"hdfs:///stagging_avocado/{nom_fichier}", header=True, inferSchema=True)

        # Si la colonne 'date' est de type bigint, nous devons la convertir en string
        df = df.withColumn("date_str", from_unixtime(col("date").cast("long"), "yyyy-MM-dd"))

        # Extraction des colonnes 'jour' et 'mois' à partir de la colonne 'date_str'
        df = df.withColumn('jour', date_format(col('date_str'), 'dd')) \
               .withColumn('mois', date_format(col('date_str'), 'MM'))

        # Définir le nom du nouveau fichier CSV
        temps_actuel = datetime.now().strftime("%Y%m%d%H%M")
        nouveau_nom_fichier = f"avocado_nettoye_{temps_actuel}.csv"

        # Sauvegarde du nouveau DataFrame dans un fichier CSV
        df.write.csv(f"hdfs:///refine_avocado/{nouveau_nom_fichier}", mode="overwrite", header=True)

        # Suppression du fichier original de /stagging_avocado
        fs.delete(spark._jvm.org.apache.hadoop.fs.Path(f"hdfs:///stagging_avocado/{nom_fichier}"), True)

except Exception as e:
    print(f"Erreur rencontrée : {str(e)}")

finally:
    # Arrêt de la session Spark
    spark.stop()
