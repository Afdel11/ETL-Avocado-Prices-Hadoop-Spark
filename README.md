# 🥑 Pipeline Big Data pour l'Analyse des Marchés d'Avocats

**Une solution complète de traitement de données pour l'analyse du marché des avocats utilisant l'écosystème Hadoop**

![Architecture du Pipeline](media/pipeline_arch.png) *Diagramme d'architecture exemple*

## 📌 Aperçu du Projet
Ce projet implémente une solution Big Data complète pour traiter et analyser les données de marché des avocats depuis des fichiers CSV jusqu'à des insights actionnables. Le pipeline intègre :
- **MySQL** pour le stockage initial des données
- **Apache NiFi** pour l'automatisation de l'ingestion
- **HDFS** pour le stockage distribué
- **Spark** pour la transformation des données
- **Hive** pour les requêtes de type SQL
- **Cron** pour l'orchestration du workflow

## 🛠️ Stack Technique
| Composant       | Technologie Utilisée |
|-----------------|----------------------|
| Ingestion       | Apache NiFi          |
| Stockage        | MySQL, HDFS          |
| Traitement      | PySpark              |
| Data Warehouse  | Hive                 |
| Orchestration   | Cron                 |

## 📂 Étapes du Pipeline
1. **Préparation des Données**
   - Découpage du CSV source en partitions
   - Chargement dans la base MySQL

2. **Ingestion Automatisée**
   - Workflow NiFi extrait les données de MySQL
   - Stockage des fichiers bruts dans HDFS (`/raw_avocado`)

3. **Traitement des Données**
   - Job Spark #1 : Calcule les métriques de volume → Table Hive
   - Job Spark #2 : Enrichit avec des features de date → Stockage HDFS raffiné (`/refine_avocado`)

4. **Analyse**
   - Tables externes Hive pour accès SQL
   - Vues agrégées (ex : `volume_per_month`)

5. **Automatisation**
   - NiFi programmé toutes les 5 minutes
   - Jobs Spark planifiés via Cron

## 🚀 Guide de Démarrage
### Prérequis
- Cluster Hadoop
- MySQL 8.0+
- Apache NiFi
- Spark 3.x
- Hive 3.x

### Installation
```bash
# Cloner le dépôt
git clone https://github.com/votre-repo/avocado-bigdata.git

# Créer les répertoires HDFS
hdfs dfs -mkdir /raw_avocado
hdfs dfs -mkdir /staging_avocado
hdfs dfs -mkdir /refine_avocado
