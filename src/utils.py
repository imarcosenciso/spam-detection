""" Contiene funciones básicas para limpiar nuevos mensajes, vectorizarlos...
"""

# ----- IMPORTS -----
from scipy import sparse
from sklearn.feature_extraction.text import TfidfVectorizer  # Vectorización de strings
from sklearn.preprocessing import MinMaxScaler              # Normalización
from nltk.stem import SnowballStemmer                       # Stemming
from nltk.corpus import stopwords
import pandas as pd
import numpy as np

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
def extraccion_metadatos(msg: str) -> dict:
    return {}
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
