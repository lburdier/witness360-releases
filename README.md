<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/witness360_logo_sombre.png">
    <img src="assets/witness360_logo_clair.png" alt="witness360" width="520">
  </picture>
</p>

# witness360

Tracking caméra aidé par une caméra 360 « témoin » montée sur le rig, livré dans Blender.

Ce dépôt sert à distribuer les versions compilées de witness360 (Windows et Mac). Le code source est dans un dépôt privé.

## Télécharger

Aucune version publiée pour l'instant. La première version compilée (Windows `.exe`, Mac `.app`) sera dans l'onglet
[Releases](../../releases).

## Ce que fait witness360 (prototype 0.1)

1. On glisse le fichier 360 (`.insv`) et les plans du montage (`.mp4`, `.mov`) dans la fenêtre.
2. Chaque plan est retrouvé dans le 360 par le son, avec un contrôle de fiabilité.
3. Les plans sont trackés automatiquement (points suivis image par image).
4. À venir : masques, objectif, solve caméra aidé par le gyroscope du 360, export Blender (`.abc` + HDRI 360).

![Écran d'accueil](captures/01_accueil.png)

## Configuration

- Windows 10 ou 11 (64 bits), ou macOS récent (version minimale précisée à la première sortie).
- Caméra 360 : Insta360 ONE X2, fichiers `.insv` non stabilisés.
