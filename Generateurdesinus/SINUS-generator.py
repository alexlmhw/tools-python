import numpy as np
from scipy.io import wavfile
import os

# Paramètres du signal
duree = 10  # Durée en secondes
F1 = 500  # Fréquence en Hz
F2 = 5000  # Fréquence en Hz
F3 = 10000  # Fréquence en Hz
amplitude = 0.5  # Amplitude du signal

# Générer le signal audio
temps = np.linspace(0, duree, int(duree * 32000), endpoint=False)  # Échantillonnage à 32 kHz
S1 = amplitude * np.sin(2 * np.pi * F1 * temps)
S2 = amplitude * np.sin(2 * np.pi * F2 * temps)
S3 = amplitude * np.sin(2 * np.pi * F3 * temps)
signal = S1+S2+S3

# Créer un répertoire pour stocker le fichier MP3
if not os.path.exists("output"):
    os.mkdir("output")

# Sauvegarder le signal en tant que fichier WAV
wavfile.write("output/signal.wav", 32000, signal.astype(np.float32))

# Convertir le fichier WAV en MP3 en utilisant un logiciel tiers, comme FFmpeg
# Assurez-vous d'avoir FFmpeg installé sur votre système et accessible via la ligne de commande.
# Vous pouvez convertir le fichier en utilisant la commande suivante :
# ffmpeg -i output/signal.wav -b:a 192K -vn output/signal.mp3