import pickle
import joblib
import pandas as pd
from sentence_transformers import SentenceTransformer
from Tools.clean import nlp_pipeline

encoder = SentenceTransformer('all-MiniLM-L6-v2')

#chargement du modèle et de la selection
model=joblib.load(filename='scoring_model.pkl')
select=joblib.load(filename='select_variable.pkl')

def predict():
    """
    Recupere le commentaire depuis le fichier excel gestion_de_projet_formulaire.xlsm dans la feuille Input que vous devez créer dans votre machine avec un chemin adapté de type C:/Users/name/Documents/
    Renvoie le score de positivité du commentaire dans un fichier excel output_model.xlsx dans la feuille Output que vous devez créer dans votre machine avec un chemin adapté de type C:/Users/name/Documents/NLP/.

    Note: la fonction utilise la fonction nlp_pipeline, l'encoder de texte, la selection de modèle et le modèle de classifiacation,
    :return:

    Exemple:
        Recuperation : "I love it this game. I only play that since my purchase in 2012, I'm statisfied !"
        Sortie: 0.9
    """
    # Asking the user to type a review
    review = pd.read_excel(r"C:/Users/grace/Documents/gestion_de_projet_formulaire.xlsm", sheet_name="Input")

    review = str(review.dtypes)

    review = nlp_pipeline(review)

    embeddings = encoder.encode(review)

    embeddings = embeddings.reshape(1, 384)

    embeddings = pd.DataFrame(embeddings)

    embeddings = select.transform(embeddings[embeddings.columns[:384]])

    prediction = model.predict_proba(embeddings)

    output = pd.DataFrame(prediction)

    output = round(output[1], 2)

    output.to_excel(r"C:/Users/grace/Documents/NLP/output_model.xlsx", sheet_name='Output', index=False)

