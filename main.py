# -*- coding: utf-8 -*-
import os
from pathlib import Path
from physics import QuantumSimulator
from visualizer import LorentzVisualizer

def main():
    # 1. Configuration des chemins
    STEPS = 200
    FRAMES = 100
    FILENAME = 'LorentzQ_video.mp4'
    
    # Détection automatique du dossier Téléchargements de l'utilisateur
    download_path = Path.home() / "Downloads" / FILENAME
    
    # 2. Init modules
    sim = QuantumSimulator(taux_erreur=0.025)
    viz = LorentzVisualizer(steps=STEPS)
    
    # 3. Création de l'animation
    print("🚀 Initialisation de la simulation LorentzQ...")
    ani = viz.animate(sim, frames=FRAMES)

    # 4. Sauvegarde
    try:
        print(f"🎬 Encodage en cours... Cible : {download_path}")
        
        # On enregistre directement au chemin du dossier Téléchargements
        ani.save(str(download_path), writer='ffmpeg', fps=20)
        
        print(f"✅ Terminé ! Vidéo disponible ici : {download_path}")
            
    except Exception as e:
        print(f"⚠️ Erreur FFMPEG : {e}")
        # Repli sur le format GIF dans les téléchargements si FFMPEG échoue
        gif_path = download_path.with_suffix('.gif')
        print(f"🔄 Tentative de sauvegarde en GIF : {gif_path}")
        ani.save(str(gif_path), writer='pillow', fps=20)

if __name__ == "__main__":
    main()