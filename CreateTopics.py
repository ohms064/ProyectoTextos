import lda
import numpy as np
from Parser2 import parser
from index import *
from counter import countDocs
"""
parser(encode="cp1252")
decoding, code = createIndexMap(encode="cp1252")
createIndexFiles(encode="cp1252", coding=code)
del code #Borramos code para liberar memoria
vocabs = np.array(list(decoding.keys()))
del decoding
"""
numWords, numDocs = countDocs(encode="cp1252")
np.ndarray((numDocs, 1000000), int)