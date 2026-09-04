<<<<<<< HEAD
# bot.py
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from spellchecker import SpellChecker
from donnees import donnees_entrainement, reponses

# Correcteur orthographique
correcteur = SpellChecker(language="fr")


def corriger_phrase(phrase):
    mots = phrase.split()
    mots_corriges = []
    for mot in mots:
        correction = correcteur.correction(mot)
        mots_corriges.append(correction if correction else mot)
    return " ".join(mots_corriges)


# Préparation des données pour le modèle
X = []
y = []

for intention, phrases in donnees_entrainement.items():
    for phrase in phrases:
        X.append(phrase)
        y.append(intention)

# Vectorisation et entraînement
vectoriseur = TfidfVectorizer()
X_vectorise = vectoriseur.fit_transform(X)

modele = MultinomialNB()
modele.fit(X_vectorise, y)

SEUIL_CONFIANCE = 0.35


def repondre(phrase_utilisateur):
    phrase_corrigee = corriger_phrase(phrase_utilisateur)
    phrase_vectorisee = vectoriseur.transform([phrase_corrigee])

    probabilites = modele.predict_proba(phrase_vectorisee)[0]
    meilleure_intention = modele.classes_[probabilites.argmax()]
    confiance = probabilites.max()

    if confiance < SEUIL_CONFIANCE:
        meilleure_intention = "inconnu"

    reponse_choisie = random.choice(reponses[meilleure_intention])
=======
# bot.py
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from spellchecker import SpellChecker
from donnees import donnees_entrainement, reponses

# Correcteur orthographique
correcteur = SpellChecker(language="fr")


def corriger_phrase(phrase):
    mots = phrase.split()
    mots_corriges = []
    for mot in mots:
        correction = correcteur.correction(mot)
        mots_corriges.append(correction if correction else mot)
    return " ".join(mots_corriges)


# Préparation des données pour le modèle
X = []
y = []

for intention, phrases in donnees_entrainement.items():
    for phrase in phrases:
        X.append(phrase)
        y.append(intention)

# Vectorisation et entraînement
vectoriseur = TfidfVectorizer()
X_vectorise = vectoriseur.fit_transform(X)

modele = MultinomialNB()
modele.fit(X_vectorise, y)

SEUIL_CONFIANCE = 0.35


def repondre(phrase_utilisateur):
    phrase_corrigee = corriger_phrase(phrase_utilisateur)
    phrase_vectorisee = vectoriseur.transform([phrase_corrigee])

    probabilites = modele.predict_proba(phrase_vectorisee)[0]
    meilleure_intention = modele.classes_[probabilites.argmax()]
    confiance = probabilites.max()

    if confiance < SEUIL_CONFIANCE:
        meilleure_intention = "inconnu"

    reponse_choisie = random.choice(reponses[meilleure_intention])
>>>>>>> c28d3c9d8d1eb8ad704793ee4cedca9b5342313c
    return meilleure_intention, confiance, reponse_choisie