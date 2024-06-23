from pyspark.sql import SparkSession
import os

spark = SparkSession.builder.appName("AvocadoVolumeCalculation").getOrCreate()
try:
    # répertoire contenant les fichiers
    input_dir = "hdfs:///raw_avocado/"
    # Liste tous les fichiers
    files = spark._jvm.org.apache.hadoop.fs.FileSystem.get(spark._jsc.hadoopConfiguration()).listStatus(
        spark._jvm.org.apache.hadoop.fs.Path(input_dir))
    csv_files = [file.getPath().getName() for file in files if file.getPath().getName().endswith('.csv')]

    # # Lecture du fichier CSV depuis HDFS Boucle sur chaque fichier CSV trouvé
    for csv_file in csv_files:
        df = spark.read.csv(os.path.join(input_dir, csv_file), header=True, inferSchema=True)

        # Calcul de la somme du volume pour chaque fichier
        sum_volume = df.groupBy().sum("Volume").collect()[0][0]

        # Insertion des résultats dans la table Hive 'avocado_volume_tracking'
        spark.sql(f"INSERT INTO TP_MASTER.avocado_volume_tracking VALUES ('{csv_file}', {sum_volume})")

        # Écriture des résultats dans un nouveau fichier CSV dans /stagging_avocado
        output_path = f"hdfs:///stagging_avocado/{csv_file}"
        df.write.csv(output_path, mode="overwrite", header=True)
        print(f"Le fichier {csv_file} a été traité avec succès.")

finally:
    spark.stop()

