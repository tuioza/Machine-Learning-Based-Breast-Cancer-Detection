import pandas as pd

def create_model(data):
    X = data.drop(["diagnosis"],axis = 1)
    y = data["diagnosis"]
    return

# Fonction pour nettoyer les données
def clean_data() -> pd.DataFrame:
    # Lecture du fichier CSV
    data: pd.DataFrame = pd.read_csv("data/data.csv")
    
    # Suppression des colonnes 'Unnamed: 32' et 'id'
    data = data.drop(['Unnamed: 32', 'id'], axis=1)
    
    # Mapping des valeurs de la colonne 'diagnosis' de 'M' à 1 et 'B' à 0
    data['diagnosis'] = data['diagnosis'].map({'M': 1, 'B': 0})
    
    return data  # Retourne les données nettoyées au format DataFrame




def main():
    data = clean_data() 
    return

if __name__ == '__main__':
    main()