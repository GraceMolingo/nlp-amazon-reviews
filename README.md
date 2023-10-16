# Prédiction d'évaluation des critiques sur Amazon

Remplacez les étoiles en attribuant une note à un commentaire à l'aide de la NLP.

## Introduction
Il arrive que l'avis d'un client ne soit pas clair, qu'un commentaire ne reflète pas l'évaluation (ex. méthode des cinq étoiles). 
Ce phénomène peut s'expliquer par différentes raisons comme le fait que cette méthode de notation dépend de la personnalité du client (une note de 3/5 est-elle une bonne note ou non ?). 
Pour pallier à ces méthodes de notation, nous travaillons sur un moyen d'attribuer une note basée directement sur l'analyse d'un commentaire. 
Ce projet est basé sur l'analyse des sentiments à l'aide du NLP.

## Jeu de données
Pour ce projet, nous utilisons un ensemble de données de critiques Amazon (voir [jmcauley.ucsd.edu](https://jmcauley.ucsd.edu/data/amazon/)). 
Ces critiques sont associées à un système d'évaluation à 5 étoiles.
L'ensemble de données original contient 142,8 millions d'avis et a été divisé par catégories. Les commentaires analysés sont en anglais.
Dans ce projet, nous utilisons une petite partie de l'ensemble de données original. Plus précisément, nous utilisons le fichier suivant qui contient 231 780 observations (sans doublons).


* `amazon_reviews_us_Video_Games.tsv`

## Modèle

### Etape 1 : Data cleaning

Les données collectées peuvent contenir des bruits qui peuvent rendre notre modèle moins efficace. Ici, nous voulons effacer certains caractères inutiles dans les commentaires.
Par exemple, nous n'avons pas besoin d'URL, de chiffres ou de caractères spéciaux. Nous utilisons donc une fonction pour nous en débarrasser. De plus, nous ne voulons pas de contractions (telles que "won't" : "will not").
Nous corrigeons les contractions pour renforcer notre modèle de formation.

### Etape 2 : Encodage du text

L'encodage de texte consiste en la tokenisation des entrées textuelles afin de transformer le texte en données numériques.

Nous utilisons le modèle d'encodage pré-entraîné "all-MiniLM-L6-v2" de [Transformers] (https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). Ce transformateur de phrases vise à cartographier les phrases et les paragraphes dans un espace vectoriel dense de 384 dimensions. 

Les transformateurs automatisent la tokenisation des mots. Il consiste à diviser les chaînes de caractères en listes de sous-chaînes.
Par exemple "The cat is at the window" : ["The", "cat", "is", "at", "the", "window"].

### Etape 3 : Modèle Machine Learning

Le modèle SVM est utilisé pour la classification. Nous implémentons ce modèle avec une précision de ~80%. 
Le classificateur SVM de [scikit learn] (https://scikit-learn.org/stable/modules/svm.html) est efficace dans les espaces à haute dimensionnels. Nous utilisons l'argument de la validation croisée quintuple pour fournir des probabilités sur l'appartenance à une classe.


## Structure

Each files on this repository correspond to a step. 
Le fichier `tools` contient les fichiers suivants : 
- `cleaning` - la fonction de nettoyage des comentaires. 
- `encoding` - encodage des données en numérique avec Transformers.
- `var_selection` - applique une selection des variables.

The folder `classification` contient les fichiers suivants :
- `model` - entraine un classifieur et l'evalue. 
- `predict` - la fonction de prédiction. 

The folder `deployment` ontient les fichiers suivants :
- `application.xlsm` - le fichier contient notre application. Merci d'appuyer sur le bouton launch.
- `output_model.xls` - le fichier enregistre le resultat du modèl, il n'est pas necessaire de l'ouvrir dans notre machine.
- `scoring_model.pkl` - le fichier pickle contient le modèle de scoring.
- `select_vaiable.pkl` - le fichier pickle contient la selection des variables dont nous avons besoin.
Lire help.txt pour plus d'informations.

Le fichier `test` contient les fichiers suivants :
- `test_` - le fichier qui test les fonctions. 

# Avant d'excuter l'application, merci d'etre sûre d'avoir renseigné les bon chemins de tes fichiers excel et python. 
