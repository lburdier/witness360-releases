"""Exemple de script witness360 : toute la chaîne sur chaque plan, de l'import à l'export Blender.

Lancer :
  - dans l'appli : Fichier > Exécuter un script… (remplissez d'abord CAMERA_360 et PLANS ci-dessous) ;
  - ou en ligne de commande :
      witness360 --script exemple_chaine_complete.py CAMERA_360 PLAN [PLAN…] [--quitter]
    (Mac : /Applications/witness360.app/Contents/MacOS/witness360 --script …)

L'objet w360 est fourni par l'appli (voir le guide, F12, partie Scripts).
"""
import os

# ---------------------------------------------------------------- à remplir (ou passer en arguments)
CAMERA_360 = ""            # fichier .insv d'origine (jamais stabilisé) ou vidéo 360 équirectangulaire
PLANS = []                 # rushes de la caméra ou montage (découpé en plans à l'import)
SORTIE = ""                # dossier de sortie ; vide : dossier « witness360 » à côté du fichier 360
IMAGE_HDRI = None          # image du plan pour l'HDRI ; None : la mieux calée par le solve
# ----------------------------------------------------------------

if ARGS:                                             # noqa: F821 (fourni par l'appli)
    CAMERA_360, PLANS = ARGS[0], ARGS[1:]            # noqa: F821
if not CAMERA_360 or not PLANS:
    raise ErreurScript("Indiquez la caméra 360 et les plans (en haut du script, ou en arguments).")  # noqa: F821

w360.nouveau()                                                                  # noqa: F821
if SORTIE:
    w360.sortie(SORTIE)                                                         # noqa: F821
w360.importer(CAMERA_360, *PLANS)                                               # noqa: F821
w360.synchroniser()                                                             # noqa: F821

echecs = []
for p in w360.plans:                                                            # noqa: F821
    w360.etape(p["nom"])                                                        # noqa: F821
    try:
        w360.metadonnees(p)                                                     # noqa: F821
        w360.auto_track(p)                                                      # noqa: F821
        if w360.synchro(p):                                                     # noqa: F821
            w360.mesurer_objectif(p)                                            # noqa: F821
        w360.resoudre(p)                                                        # noqa: F821
        w360.nettoyer(p)                                                        # noqa: F821
        if w360.synchro(p):                                                     # noqa: F821
            w360.hdri(p, image=IMAGE_HDRI)                                      # noqa: F821
        w360.exporter(p)                                                        # noqa: F821
    except ErreurScript as e:                                                   # noqa: F821
        w360.log("ÉCHEC %s : %s" % (p["nom"], e))                               # noqa: F821
        echecs.append(p["nom"])

projet = w360.enregistrer()                                                     # noqa: F821
w360.bilan(os.path.splitext(projet)[0] + "_bilan.json")                         # noqa: F821
if echecs:
    raise ErreurScript("Plans en échec : %s (voir la console)." % ", ".join(echecs))  # noqa: F821
