import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import pickle5 as pickle




# Fonction création du model
def create_model(data):
    X = data.drop(["diagnosis"],axis = 1)
    y = data["diagnosis"]
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    X_train , X_test, y_train, y_test = train_test_split(
        X,y,test_size=0.2, random_state=42
    )

    #entrainement du model
    model = LogisticRegression()
    model.fit(X_train,y_train)


    #test le model
    y_pred = model.predict(X_test)
    print('Accuracy of our model', accuracy_score(y_test,y_pred))
    print('Classification report: \n', classification_report(y_test, y_pred))
    return scaler, model


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
    model, scaler = create_model(data)
    with open("model/model.pkl","wb") as f:
        pickle.dump(model,f)
    with open("model/scaler.pkl","wb") as f:
        pickle.dump(scaler, f)
    

    return

if __name__ == '__main__':
    main()