""" Contiene funciones básicas para limpiar nuevos mensajes, vectorizarlos...
"""

# ----- IMPORTS -----
from scipy import sparse
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import MinMaxScaler              # Normalización
from nltk.stem import SnowballStemmer                       # Stemming
from nltk.corpus import stopwords

from sklearn.naive_bayes import MultinomialNB


import pandas as pd
import numpy as np
import joblib

import re
import string
import unidecode

import nltk
# Hay que descargarlo.
nltk.download('stopwords')
# ---- EO IMPORTS -----


# ----- Funciones públicas -----
def preprocesamiento_mensaje(msg: str) -> str:
    msg_limpio = __limpiar_texto(msg)
    msg_limpio = __elimina_stopwords(msg_limpio)
    msg_limpio = __stemming(msg_limpio)
    return msg_limpio


# TODO
def extraccion_metadatos(msg: str) -> pd.DataFrame:
    return pd.DataFrame.from_dict({
        'Longitud del mensaje': len(msg),
        'Contiene links?': _tiene_link(msg),
        'Contiene teléfonos?': _tiene_telefono(msg)
    }, orient='index')


def vectoriza_mensaje(msg):
    transformer = TfidfTransformer()
    loaded_vec = CountVectorizer(
        decode_error="replace", vocabulary=_carga_vocabulario_vectorizador())
    tfidf = transformer.fit_transform(
        loaded_vec.fit_transform(np.array([msg])))

    return tfidf


def obtener_prediccion(modelo: MultinomialNB, msg_vect) -> pd.DataFrame:
    return pd.DataFrame(modelo.predict_proba(msg_vect)[0].reshape(1, -1), columns=["Real", "Spam"])
# ----- EO Funciones públicas -----


# Funciones privadas
def __limpiar_texto(x):
    """
    Devuelve el texto en minúsculas, libre de teléfonos, links, signos de puntuación, etc.
    """
    x = x.lower()  # A minúsculas

    # Links
    x = re.sub(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', x)

    # Signos de puntuación, etc.
    x = re.sub('[%s]' % re.escape(string.punctuation), '', x)

    # Saltos de línea
    x = re.sub('\n', '', x)

    # Palabras con números
    x = re.sub('\w*\d\w*', '', x)

    # Teléfonos móviles
    x = re.sub('(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}', '', x)

    # Teléfonos fijos
    x = re.sub('(?:\+?\(?\d{2,3}?\)?\D?)?\d{4}\D?\d{4}', '', x)

    # Unicode to ASCII
    x = unidecode.unidecode(x)

    return x.strip()


# ----- stop words -----
stop_words = stopwords.words('english')

# Añadimos palabras extras detectadas manualmente.
extra_stop = [
    'dont', 'doin', 'rolf', 'u', 'b', 'ure', 'ur', 'im', 'c', 'its'
]
stop_words += extra_stop


def __elimina_stopwords(x):
    return ' '.join(palabra for palabra in x.split(' ') if palabra not in stop_words)
# ----- EO stop words -----


# ----- stemming -----
snowball = SnowballStemmer(language='english')


def __stemming(x):
    return ' '.join(snowball.stem(palabra) for palabra in x.split(' '))
# ----- EO stemming -----


# ----- metadatos -----
def _tiene_link(x):
    """ Evalua un string con regex y devuelve true si contiene un link.
    Regex obtenida de: http://urlregex.com/
    """
    expr = re.compile(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')

    return expr.search(x) != None  # True si tiene links.


def _tiene_telefono(x):
    """ Evalua un string con regex y devuelve true si contiene un número de teléfono.
    Regex obtenida de: https://scripteverything.com/check-phone-numbers-using-regex-in-python-examples/
    """
    expr1 = re.compile(
        r'(?:\+\d{2})?\d{3,4}\D?\d{3}\D?\d{3}')      # Para teléfonos móviles
    expr2 = re.compile(
        r'(?:\+?\(?\d{2,3}?\)?\D?)?\d{4}\D?\d{4}')   # Para fijos

    return (expr1.search(x) != None
            or expr2.search(x) != None)
# ----- EO metadatos -----


# ----- vectorización -----
def _carga_vocabulario_vectorizador():
    return joblib.load('../Data/dataset/vectorizado/vocabulario_vectorizador')
