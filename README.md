# homeassistant-config
> [!WARNING]
> Ce dépot est en cours de construction !
> 
Ce dépot regroupe une partie de la configuration de mon installation Home Assistant.
Il sera mis à jour en fonction de la pertinence des informations à partager.

## Packages
> [!TIP]
> Nécessite de déclarer `packages: !include_dir_named packages` sous `homeassistant:` dans le fichier `configuration.yml`

### Météo
Permet de récupérer les alertes météo l'API de Météo France. 
Les cartes d'alertes aujourd'hui et demain sont également récupérées pour pouvoir être affichées dans une card
Un sensor additionnel plus facile utiliser dans les cards est également créé selon le retour de l'API 

### Speedtest
Permet de réaliser des speedtest en CLI 
Trois sensors sont créés à partir du résultat pour faciliter le traitement dans une card (graphique par exemple)

### Vacances scolaires
Permet de récupérer sur l'API de l'éducation nationale les prochaines vacances. 
Deux binary sensors déduisent ensuite si on est actuellement en vacances ou non pour aujourd'hui et demain.

## Scripts Python
> [!TIP]
> Nécessite de déclarer `python_script:` dans le fichier `configuration.yml`

### Jours Fériés
Permet de créer 2 sensors (nom du jour férié aujourd'hui et demain) et 1 sensor binaire (jour férié aujourd'hui) pour la gestion plus facile des jours fériés dans les automation.
Le script doit être lancé une fois par jour. Les entités créées permettent de conditionner des automations le jour même ou d'anticiper certaines en cas de jour férié le lendemain.
