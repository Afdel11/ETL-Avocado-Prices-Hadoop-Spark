import pandas as pd

# Lire le fichier avocado
df = pd.read_csv('avocado.csv')

#  taille des sous-fichiers
taille_fichier = len(df) // 5

# Création des sous-fichiers
for i in range(5):
    index_debut = i * taille_fichier
    #inclure le dernier sous-fichier complet
    index_fin = (i + 1) * taille_fichier if i < 4 else len(df)
    df_chunk = df.iloc[index_debut:index_fin]
    df_chunk.to_csv(f'avocado_{i+1}.csv', index=False)
