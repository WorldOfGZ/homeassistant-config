"""      https://github.com/WorldOfGZ/homeassistant-config                 """

"""  Ce script créé deux sensors pour afficher les jours fériés            """
"""  aujourd'hui et demain, ainsi qu'un sensor binaire si aujourd'hui      """
"""  est férié.                                                            """          

"""  Les entités jours férié seront indisponible si le jour n'est pas      """
"""  férié                                                                 """
"""  L'entité binaire a un fonctionnement traditionnel true/balse          """
"""  Entitées créées :                                                     """
"""    - sensor.jour_ferie                                                 """
"""    - sensor.demain_ferie                                               """
"""    - binary_sensor.estferie                                            """

"""  Nécessite python_script: dans le fichier configuration.yml            """

"""  Le script doit être lancé chaque jour :                               """
"""                                                                        """
""" automation:                                                            """
"""   alias: Refresh jours feries sensors                                  """
"""   trigger:                                                             """
"""     platform: time                                                     """
"""     at: '00:00:01'                                                     """
"""   action:                                                              """
"""     service: python_script.jours_feries                                """
"""     data:                                                              """
"""       name: "jours_feries"                                             """

"""  Exemple d'affichage avec la carte auto-entities                      """

"""    - type: custom:auto-entities                                        """
"""      card:                                                             """
"""        type: entities                                                  """
"""        title: "Infos du jour"                                          """
"""        show_header_toggle: false                                       """
"""      filter:                                                           """
"""        include:                                                        """
"""          - entity_id: /_ferie/                                         """
"""        exclude:                                                        """
"""          - state: "unavailable"                                        """

"""  Ce script est basé sur le projet :                                    """
"""  https://pon.fr/home-assistant-infos-du-jour-et-du-lendemain/          """
"""  Cependant les calculs sont faux sur certaines années.                 """
"""  Ce script propose de corriger les problèmes constatés                 """

"""  Modification faites sur le code original :                            """
"""    - Suppression des lignes de code non utilisées                      """
"""    - Correction du calcul du lendemain (faux si changement de mois)    """
"""    - Correction du calcul des jours relatifs à Paques                  """


"""                    Dates aujourd'hui et demain                         """
today = datetime.datetime.now().date()
tomorrow = today + datetime.timedelta(hours = 24)


"""                     Calcul des jours fériés                            """

#Calcule la date de Paques
def datepaques(an):
    a=an//100
    b=an%100
    c=(3*(a+25))//4
    d=(3*(a+25))%4
    e=(8*(a+11))//25
    f=(5*a+b)%19
    g=(19*f+c-e)%30
    h=(f+11*g)//319
    j=(60*(5-d)+b)//4
    k=(60*(5-d)+b)%4
    m=(2*j-k-g+h)%7
    n=(g-h+m+114)//31
    p=(g-h+m+114)%31
    jour=p+1
    mois=n
    return datetime.date(an, mois, jour)

#Liste des jours fériés
def listejoursferies(an):
    F = []  # =liste des dates des jours feries en date-liste d=[j,m,a]
    L = []  # =liste des libelles du jour ferie
    #Calcul des dattes pour les relatifs à Paques
    date_paques = datepaques(today.year)
    date_lundipaques = date_paques + datetime.timedelta(hours = 24) #+1jour
    date_ascension = date_paques + datetime.timedelta(hours = 24*39) #+39jour
    date_pentecote = date_paques + datetime.timedelta(hours = 24*49) #+49jour
    date_lundipentecote = date_paques + datetime.timedelta(hours = 24*50) #+49jour

    #dp = datepaques(an)
    #jdp,mdp,adp = dp

    # Jour de l'an
    d = [1,1,an]
    F.append(d)
    L.append(u"Jour de l'an")

    # # Jour de test
    # d = [2,11,an]
    # F.append(d)
    # L.append(u"Jour de papoo")

    # # Jour de test
    # d = [3,11,an]
    # F.append(d)
    # L.append(u"Jour de papoo1")
    
    # Dimanche de Paques
    d = [date_paques.day,date_paques.month,date_paques.year]
    F.append(d)
    L.append(u"Dimanche de Pâques")

    # Lundi de Paques
    d = [date_lundipaques.day,date_lundipaques.month,date_lundipaques.year]
    F.append(d)
    L.append(u"Lundi de Pâques")

    # Fête du travail
    d = [1,5,an]
    F.append(d)
    L.append(u"Fête du travail")

    # Victoire des allies 1945
    d = [8,5,an]
    F.append(d)
    L.append(u"Victoire des alliés 1945")

    # Jeudi de l'Ascension
    d = [date_ascension.day,date_ascension.month,date_ascension.year]
    F.append(d)
    L.append(u"Jeudi de l'Ascension")

    # Dimanche de Pentecote
    d = [date_pentecote.day,date_pentecote.month,date_pentecote.year]
    F.append(d)
    L.append(u"Pentecôte")

    # Lundi de Pentecote
    d = [date_lundipentecote.day,date_lundipentecote.month,date_lundipentecote.year]
    F.append(d)
    L.append(u"Lundi de Pentecôte")

    # Fete Nationale
    d = [14,7,an]
    F.append(d)
    L.append(u"Fête Nationale")

    # Assomption
    d = [15,8,an]
    F.append(d)
    L.append(u"Assomption")

    # Toussaint
    d = [1,11,an]
    F.append(d)
    L.append(u"Toussaint")

    # Armistice 1918
    d = [11,11,an]
    F.append(d)
    L.append(u"Armistice 1918")

    # Jour de Noel
    d = [25,12,an]
    F.append(d)
    L.append(u"Jour de Noël")

    return F, L

def estferie(d):
    """estferie(d): => dit si une date d=[j,m,a] donnée est fériée France
      si la date est fériée, renvoie son libellé
      sinon, renvoie "unavailable" afin de masquer le sensor"""
    j,m,a = d
    F,L = listejoursferies(a)
    for i in range(0, len(F)):
        if j==F[i][0] and m==F[i][1] and a==F[i][2]:
            return L[i]
    return "unavailable" 

def ferie(d):
    """estferie(d): => dit si une date d=[j,m,a] donnée est fériée France
      si la date est fériée, renvoie son libellé
      sinon, renvoie "unavailable" afin de masquer le sensor"""
    j,m,a = d
    F,L = listejoursferies(a)
    for i in range(0, len(F)):
        if j==F[i][0] and m==F[i][1] and a==F[i][2]:
            return "on"
    return "off"

"""La syntaxe est hass.states.set(entity_id, state, {dict of attributes}) """
"""Creation des entités """
hass.states.set("sensor.jour_ferie" , estferie([today.day,today.month,today.year]) ,
  {
    "icon" : "mdi:creation" ,
    "friendly_name" : "Férié aujourd'hui"
  }
)

hass.states.set("sensor.demain_ferie" , estferie([tomorrow.day,tomorrow.month,tomorrow.year]),
  {
    "icon" : "mdi:creation" ,
    "friendly_name" : "Férié demain"
  }
)
hass.states.set("binary_sensor.estferie" , ferie([today.day,today.month,today.year]),
  {
    "icon" : "mdi:creation" ,
    "friendly_name" : "Férié"
  }
)

