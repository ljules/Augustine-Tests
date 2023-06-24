#########################################################
#                                                       #
#   FICHIER DE CONFIGURATION PERSONNALISE AUGUSTINE     #
#                                                       #
#########################################################


# INFORMATIONS GENERALES DU SITE :
# --------------------------------
AUTHOR = 'Prof'
SITENAME = 'Augustine'
SITESUBTITLE = 'Phase de test'
SITEURL = 'https://ljules.github.io/Augustine-Tests'
TIMEZONE = 'Europe/Paris'
DEFAULT_LANG = 'fr'


# CHEMINS POUR LE CONTENU DE DEVELOPPEMENT :
# ------------------------------------------
THEME = 'THEMES/notmyidea_perso'
PATH = 'content'
STATIC_PATHS = ['images']
OUTPUT_PATH = 'docs'    # Attention, pour la publication sur GitHub Pages le dossier doit être "/docs"

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# OPTION DE STRUCTURATION DU SITE :
# ---------------------------------
#DEFAULT_CATEGORY = 'test'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
#MENUITEMS = ( ('Wiki', 'https://fr.wikipedia.org/wiki/Éco-marathon_Shell'))
USE_FOLDER_AS_CATEGORY = True           # Attribution de la catégorie par le dossier parent des articles.      
DELETE_OUTPUT_DIRECTORY = True          # Nettoyage des fichiers de sortie avant génération.
STATIC_CHECK_IF_MODIFIED = True         
SUMMARY_MAX_LENGTH = 50                 # Longueur des résumés des articles
DEFAULT_PAGINATION = 5                  # Nombre d'articles ventilés par page d'une catégorie.


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# OPTION DE PERSONNALISATION DU THEME :
# -------------------------------------
SHOW_ARTICLE_INFO = False            # Activation/désaction des informations (date, auteur, catégorie) des articles.
SHOW_EXTRA = True
SHOW_LOW_FOOTER = True              # Activation/désaction de la partie inférieure du footer.
MESSAGE_LOW_FOOTER = "Site de l'association Tournesol & du projet Augustine - version de juin 2023"


# DONNEES LIEES  A EXTRA :
# ------------------------
# Blogroll
LINKS = (('Lycée Léonard de Vinci', 'https://www.vinci-melun.org'),
          ('Site Shell Eco-Marathon', 'https://www.shellecomarathon.com/'),
          ('Site France Shell Eco-Marathon', 'https://www.shell.fr/energie-innovation/shell-eco-marathon.html'))

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/AugustineShellEco'),
         ('Instagram', 'https://www.instagram.com/team_augustine/'))



