# homeassistant-config
> [!WARNING]
> Ce dépot est en cours de construction !
> 
Ce dépot regroupe une partie de la configuration de mon installation Home Assistant.
Il sera mis à jour en fonction de la pertinence des informations à partager.

## Packages
> [!TIP]
> Nécessite de déclarer `packages: !include_dir_named packages` sous `homeassistant:` dans le fichier `configuration.yml`

## Scripts Python
> [!TIP]
> Nécessite de déclarer `python_script:` dans le fichier `configuration.yml`

### Jours Fériés
Permet de créer 2 sensors (nom du jour férié aujourd'hui et demain) et 1 sensor binaire (jour férié aujourd'hui) pour la gestion plus facile des jours fériés dans les automation.
Le script doit être lancé une fois par jour. Les entités créées permettent de conditionner des automations le jour même ou d'anticiper certaines en cas de jour férié le lendemain.
