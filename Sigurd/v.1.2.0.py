# For å jobbe med første del av notatboken trenger vi disse bibliotekene
import math
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

# Først setter vi lengder og vinkler:
theta1 = 30     # Vinkel mellom positiv x-akse og "overarm" i grader
l1 = 60        # Lengde til overarm (f. eks. i meter)
theta2 = 30   # Vinkel mellom overarm og underarm i grader
l2 = 50        # Lengde til underarm (bruk samme lengde-enhet som for l1).

# Funksjoner som inngår i utregning med homogene koordinater

np.set_printoptions(formatter={'float_kind': "{: .6f}".format})

def M_rotasjon2D(theta):
# Funksjon som definerer en homogen rotasjonsmatrise (3x3) for to romlige dimensjoner.
# I såkalte homogene koordinater bruker vi en ekstra dimensjon (slik at en homogen 3x3-matrise beskriver
# en tranformasjon i to romlige dimensjoner).
# Den ekstra koordinaten gjør det bl.a. mulig å beskrive forflytning ved matrisemultiplikasjon.
# Theta skal oppgis i grader.
    c = np.cos(theta*np.pi/180)
    s = np.sin(theta*np.pi/180)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1]])

def M_translasjon2D(x,y):
# Homogen translasjonsmatrise (3x3) for to romlige dimensjoner.
    return np.array([[1, 0, x], [0, 1, y], [0, 0, 1]])

def konkatener(Mliste):
# Funksjon som multipliserer alle matrisene i Mliste. Mliste er altså en liste av homogene
# transformasjonsmatriser (bortsatt fra posA som er en homogen kolonnevektor - se nederst)
    svar = 1
    for M in reversed(Mliste):
        svar = np.dot(M, svar)
    return svar