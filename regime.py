import pandas as pd
import re

class Aliment:
    def __init__(self, name, infos_nutr):
        self.name = name
        self.infos_nutr = infos_nutr

class Recette:
    def __init__(self, name):
        self.name = name
    
    def ingredients(self, dict):
        self.dict = dict
    
    def ajouter_ingredients(self, personnes=1):
        for ingredient in self.dict.keys():
            ajouter_aliment(jour, repas, ingredient, self.dict[ingredient]*personnes)
    
    def liste_ingrédients(self, ingr):
        self.ingr = ingr

    def préparation(self, prep):
        self.prep = prep
    
    def imprimer_liste_ingrédients(self):
        print(self.ingr)

    def imprimer_préparation(self):
        print(self.prep)

aliments = []

def ajouter_aliment(jour, repas, aliment, quantité):
    infos_aliment = [jour, repas]
    infos_aliment.append(aliment.name)
    infos_aliment.append(quantité)
    chiffres = re.compile("\d*\.?\d+")
    infos_nutr = chiffres.findall(aliment.infos_nutr)
    for i in infos_nutr: 
        j = float(i)
        infos_aliment.append(j)
    aliments.append(infos_aliment)

#region Aliments

# Féculents
chapelure = Aliment('Everyday Chapelure 400 g', '''Énergie kcal349 kcal
    Total graisses1.7 g
    Graisses saturées0.2 g
    Total glucides69.6 g
    Sucres3.8 g
    Fibres alimentaires4.7 g
    Protéines11.5 g
    Sel1 g''')

farine = Aliment('Everyday Farine de blé pour préparations variées 1 kg', '''Énergie kcal348 kcal
    Total graisses1.1 g
    Graisses saturées0.2 g
    Total glucides72 g
    Sucres1.1 g
    Fibres alimentaires3.5 g
    Protéines11 g
    Sel< 0.01 g''')

patate_douce = Aliment('BONI patate douce (vrac)', '''Énergie kcal86 kcal
    Total graisses0.1 g
    Graisses saturées0 g
    Total glucides20 g
    Sucres4.2 g
    Fibres alimentaires3 g
    Protéines1.6 g
    Sel0 g ''')

pâtes = Aliment('Boni Selection Farfalle 500 g', '''Énergie kcal370 kcal
    Total graisses1.5 g
    Graisses saturées0.3 g
    Total glucides75 g
    Sucres3 g
    Fibres alimentaires3 g
    Protéines13 g
    Sel0.03 g''')

riz = Aliment('Boni Selection Riz basmati parfumé - ne colle pas 4 sachets-cuisson 500 g', '''Énergie kcal349 kcal
    Total graisses0.8 g
    Graisses saturées0.2 g
    Total glucides77 g
    Sucres< 0.5 g
    Fibres alimentaires1.1 g
    Protéines5 g
    Sel0.03 g ''')



# Fruits et légumes
amandes = Aliment("Boni Selection Amandes 250 g", '''Énergie kcal592 kcal
    Total graisses49 g
    Graisses saturées3.7 g
    Total glucides9.5 g
    Sucres3.9 g
    Fibres alimentaires12 g
    Protéines21 g
    Sel< 0.01 g''')

avocat = Aliment('Boni Selection Avocats 5 pièces ± 750 g', '''Énergie kcal160 kcal
    Total graisses15 g
    Graisses saturées2.1 g
    Total glucides9 g
    Sucres0.7 g
    Fibres alimentaires7 g
    Protéines2 g
    Sel0 g ''')

champignons = Aliment('Boni Selection - Champignons - 100 pourcents culture belge - 300 g', '''
    Énergie kcal19 kcal
    Total graisses0.4 g
    Graisses saturées0 g
    Total glucides0.6 g
    Sucres0 g
    Fibres alimentaires2.1 g
    Protéines2.2 g
    Sel0.01 g ''')

lait_coco = Aliment('Boni Selection Lait de coco 400 ml', '''Énergie kcal167 kcal
    Total graisses18 g
    Graisses saturées16 g
    Total glucides1.8 g
    Sucres1.8 g
    Fibres alimentaires0 g
    Protéines0 g
    Sel0.08 g''')

oignons = Aliment('Boni Selection Oignons 2,5 kg', '''Énergie kcal40 kcal
    Total graisses0.1 g
    Graisses saturées< 0 g
    Total glucides9 g
    Sucres4.2 g
    Fibres alimentaires1.7 g
    Protéines1.1 g
    Sel0 g''')

noix = Aliment("Boni Selection Cerneaux de noix 200 g", '''Énergie kcal689 kcal
    Total graisses65 g
    Graisses saturées6.1 g
    Total glucides7 g
    Sucres2.6 g
    Fibres alimentaires6.7 g
    Protéines15 g
    Sel< 0.01 g''')

noix_de_pécan = Aliment("Boni Selection Noix de pécan grillées 200 g", '''Énergie kcal742 kcal
    Total graisses74 g
    Graisses saturées6.3 g
    Total glucides4.2 g
    Sucres4.1 g
    Fibres alimentaires9.4 g
    Protéines9.5 g
    Sel< 0.01 g''')

sauce_tomate = Aliment('Base tomatée pour pizza Elvea Tetra 250g', '''Énergie kcal36 kcal
    Total graisses0.2 g
    Graisses saturées0 g
    Total glucides5.2 g
    Sucres4.5 g
    Fibres alimentaires3 g
    Protéines1.9 g
    Sel0.38 g''')

tomates_en_morceaux = Aliment('Boni Selection Tomates concassées 400 g', '''Énergie kcal33 kcal
    Total graisses0 g
    Graisses saturées0 g
    Total glucides5.3 g
    Sucres4.3 g
    Fibres alimentaires2.1 g
    Protéines1.9 g
    Sel0.02 g''')



# Légumineuses
haricots_blancs = Aliment('Boni Selection Haricots blancs 400 g', '''Énergie kcal100 kcal
    Total graisses0.8 g
    Graisses saturées< 0.1 g
    Total glucides12 g
    Sucres0.7 g
    Fibres alimentaires7.5 g
    Protéines7.4 g
    Sel0.32 g''')

haricots_noirs = Aliment('Boni Selection Haricots noirs 200 g', '''Énergie kcal104 kcal
    Total graisses0.8 g
    Graisses saturées< 0.1 g
    Total glucides< 14 g
    Sucres< 0.5 g
    Fibres alimentaires5.5 g
    Protéines8 g
    Sel0.3 g''')

pois_chiches = Aliment('BIOITALIA Pois chiches biologiques', ''' Énergie kcal163 kcal
    Total graisses2 g
    Graisses saturées0.2 g
    Total glucides25.2 g
    Sucres3 g
    Fibres alimentaires6.9 g
    Protéines7.6 g
    Sel0.17 g''')



# Produits laitiers
fromage_râpé = Aliment('Everyday Emmental 500 g', '''Énergie kcal286 kcal
    Total graisses20 g
    Graisses saturées7.9 g
    Total glucides0 g
    Sucres0 g
    Fibres alimentaires0 g
    Protéines27 g
    Sel1.2 g ''')

yaourt_grecque = Aliment("Boni Selection Yaourt à la Grecque entier nature 10 % m.g. 1 kg", '''
    Énergie kcal121 kcal
    Total graisses10 g
    Graisses saturées6.2 g
    Total glucides4.3 g
    Sucres3.6 g
    Fibres alimentaires0 g
    Protéines3.5 g
    Sel0.1 g    ''')



# Graisses
huile_colza = Aliment('HUILE DE COLZA VDM 15X1L', '''Énergie kcal828 kcal
    Total graisses92 g
    Graisses saturées7 g
    Total glucides0 g
    Sucres0 g
    Fibres alimentaires0 g
    Protéines0 g
    Sel0 g''')

huile_olive = Aliment('', '''Énergie kcal900 kcal
    Total graisses100 g
    Graisses saturées14 g
    Total glucides0 g
    Sucres0 g
    Fibres alimentaires0 g
    Protéines0 g
    Sel0 g ''')

huile_tournesol = Aliment('Boni Selection Bio Huile de tournesol 75 cl', '''Énergie kcal900 kcal
    Total graisses100 g
    Graisses saturées12 g
    Total glucides0 g
    Sucres0 g
    Fibres alimentaires0 g
    Protéines0 g
    Sel0 g''')



# Viandes



# Produits de la mer



# Sucreries/autres
kelloggs = Aliment("Kellogg's EXTRA Milk Chocolate 500g", '''Énergie kcal484 kcal
    Total graisses22 g
    Graisses saturées12 g
    Total glucides62 g
    Sucres25 g
    Fibres alimentaires4.9 g
    Protéines7 g
    Sel0.68 g''')

vermicelles_chocolat = Aliment("Boni Selection Vermicelles chocolat noir 600 g", '''
    Énergie kcal446 kcal
    Total graisses15 g
    Graisses saturées9 g
    Total glucides69 g
    Sucres66 g
    Fibres alimentaires6.3 g
    Protéines4.8 g
    Sel0.35 g
    ''')

whey = Aliment("Decathlon WHEY PROTEINE ISOLATE CHOCO 900G", '''Énergie kcal377 kcal
    Total graisses3.8 g
    Graisses saturées2.2 g
    Total glucides5 g
    Sucres3.3 g
    Fibres alimentaires1.3 g
    Protéines80 g
    Sel1.1 g''')



#endregion

#region Recettes
One_Pot_Vegan_Swedish_Meatball_Pasta = Recette('One-Pot Vegan Swedish "Meatball" Pasta')
One_Pot_Vegan_Swedish_Meatball_Pasta.ingredients({champignons: 28.125, haricots_blancs: 53.125, oignons: 15, chapelure: 7.5, huile_colza: 5.625, lait_coco: 50, farine: 3.75, pâtes: 50})
One_Pot_Vegan_Swedish_Meatball_Pasta.liste_ingrédients("""Ingredients

    for 8 servings

    Meatballs

        8 oz cremini mushroom (225 g), finely chopped
        15 oz cannellini bean (425 g), 1 can, drained and rinsed
        1 small yellow onion, finely chopped
        1 ¼ cups panko breadcrumbs (60 g)
        ½ cup fresh parsley (20 g), finely chopped
        3 cloves garlic, minced
        1 teaspoon dried rosemary
        1 teaspoon vegan worcestershire
        1 tablespoon soy sauce
        ¼ teaspoon ground nutmeg
        ½ teaspoon liquid smoke
        1 teaspoon salt
        1 teaspoon pepper

    Gravy

        3 tablespoons canola oil
        3 cups vegetable broth (720 mL)
        14 oz full-fat coconut milk (395 mL), 1 can
        1 tablespoon vegan worcestershire
        salt, to taste
        pepper, to taste
        ¼ cup all-purpose flour (30 g)
        4 cups bow tie pasta (400 g), or pasta of choice
        fresh parsley, for ganish)""")
One_Pot_Vegan_Swedish_Meatball_Pasta.préparation("""
  Preparation

    In a large bowl, combine the mushrooms, beans, onion, bread crumbs, parsley, garlic, dried rosemary, Worcestershire sauce, soy sauce, nutmeg, liquid smoke, salt, and pepper. Mix well with a fork, mashing the beans a bit to form a paste.
    Heat the canola oil in a large pot over medium-high heat.
    Roll the “meatball” mixture and into golf ball-sized balls. Place the balls in the pot and cook for 1 minute on each side until browned.
    Add the vegetable broth, coconut milk, Worcestershire sauce, salt, pepper, and flour, and gently stir until evenly combined.
    Bring the liquid to a boil, then add the pasta. Stir constantly until the pasta is cooked and the liquid has reduced to a sauce that coats the noodles and meatballs, 7-8 minutes.
    Garnish with parsley.
    Enjoy!  
 """)

One_Pot_Enchilada_Rice = Recette('One-Pot Enchilada Rice')
One_Pot_Enchilada_Rice.ingredients({huile_olive: 4, oignons: 10, riz: 75, haricots_noirs: 42.5, sauce_tomate: 65, fromage_râpé: 12.5, avocat: 75})
One_Pot_Enchilada_Rice.liste_ingrédients("""Ingredients

    for 4 servings

        1 tablespoon oil
        1 tablespoon minced garlic, minced
        ½ cup red onion (75 g), chopped
        1 cup bell pepper (100 g), chopped
        1 cup tomato (200 g), chopped
        3 cups water (720 mL)
        1 ½ cups rice (300 g)
        1 cup black beans (170 g)
        1 tablespoon fresh cilantro, chopped
        1 cup tomato sauce (260 g)
        1 teaspoon chili powder
        1 teaspoon cumin
        1 teaspoon salt
        1 teaspoon pepper
        ½ cup shredded cheese (50 g), optional
        ½ avocado, cubed, for garnish""")
One_Pot_Enchilada_Rice.préparation("""
  Preparation

    Preheat oven to 400ºF (200ºC).
    Put oil in a cast-iron skillet over medium heat. Add garlic and onion to skillet and stir until garlic is slightly golden and onion has softened.
    Add pepper and sauté 2-3 minutes or until peppers have softened.
    Add tomatoes and sauté 1 minute.
    Remove sauteed vegetables and set aside.
    Pour water into the skillet and wait for it to come to a boil.
    Add rice and stir for 12-15 minutes until rice is fluffier but still slightly tender.
    Make a circle in the center of the rice and add your sautéed vegetables and black beans to the skillet and mix.
    Add cilantro, tomato sauce, chili powder, cumin, salt, and pepper, and stir.
    Add cheese on top (optional).
    Bake in a preheated oven for 20-25 minutes.
    Allow to cool for 5 minutes.
    Garnish with cilantro and avocado (optional).
    Enjoy! 
 """)

Curry_de_pois_chiches_et_patates_douces = Recette('Curry de pois chiches et patates douces')
Curry_de_pois_chiches_et_patates_douces.ingredients({huile_tournesol: 7.5, patate_douce: 150, oignons: 50, pois_chiches: 200, tomates_en_morceaux: 200, lait_coco: 125, riz: 85})
Curry_de_pois_chiches_et_patates_douces.liste_ingrédients("""cfr HelloFresh""")
Curry_de_pois_chiches_et_patates_douces.préparation("""  cfr HelloFresh  """)

Chakchouka = Recette('Chakchouka')
Chakchouka.ingredients({haricots_blancs: 200, patate_douce: 150, oignons: 50, pois_chiches: 200, tomates_en_morceaux: 200, lait_coco: 125, riz: 85})
Chakchouka.liste_ingrédients("""cfr HelloFresh""")
Chakchouka.préparation("""  cfr HelloFresh  """)

#endregion

#region Lundi
jour = "Lundi"

repas = "Déjeuner"
ajouter_aliment(jour, repas, yaourt_grecque, 200)
ajouter_aliment(jour, repas, vermicelles_chocolat, 20)
ajouter_aliment(jour, repas, kelloggs, 60)
ajouter_aliment(jour, repas, amandes, 10)
ajouter_aliment(jour, repas, noix, 10)
ajouter_aliment(jour, repas, noix_de_pécan, 10)
ajouter_aliment(jour, repas, whey, 30)

repas = "Collation"
# Jus de fruits à déterminer

repas = "Dîner"

repas = "Goûter"
ajouter_aliment(jour, repas, whey, 30)
#Autre idée??? Cfr Pilou...

repas = "Souper"
One_Pot_Vegan_Swedish_Meatball_Pasta.ajouter_ingredients(3)

#endregion

#region Mardi
jour = "Mardi"

repas = "Déjeuner"
ajouter_aliment(jour, repas, yaourt_grecque, 200)
ajouter_aliment(jour, repas, vermicelles_chocolat, 20)
ajouter_aliment(jour, repas, kelloggs, 60)
ajouter_aliment(jour, repas, amandes, 10)
ajouter_aliment(jour, repas, noix, 10)
ajouter_aliment(jour, repas, noix_de_pécan, 10)
ajouter_aliment(jour, repas, whey, 30)

repas = "Collation"
# Jus de fruits à déterminer

repas = "Dîner"

repas = "Goûter"
ajouter_aliment(jour, repas, whey, 30)
#Autre idée??? Cfr Pilou...

repas = "Souper"
One_Pot_Enchilada_Rice.ajouter_ingredients(3)

#endregion

#region Mercredi
jour = "Mercredi"

repas = "Déjeuner"
ajouter_aliment(jour, repas, yaourt_grecque, 200)
ajouter_aliment(jour, repas, vermicelles_chocolat, 20)
ajouter_aliment(jour, repas, kelloggs, 60)
ajouter_aliment(jour, repas, amandes, 10)
ajouter_aliment(jour, repas, noix, 10)
ajouter_aliment(jour, repas, noix_de_pécan, 10)
ajouter_aliment(jour, repas, whey, 30)

repas = "Collation"
# Jus de fruits à déterminer

repas = "Dîner"

repas = "Goûter"
ajouter_aliment(jour, repas, whey, 30)
#Autre idée??? Cfr Pilou...

repas = "Souper"
Curry_de_pois_chiches_et_patates_douces.ajouter_ingredients(2)

#endregion

#region Jeudi
jour = "Jeudi"

repas = "Déjeuner"
ajouter_aliment(jour, repas, yaourt_grecque, 200)
ajouter_aliment(jour, repas, vermicelles_chocolat, 20)
ajouter_aliment(jour, repas, kelloggs, 60)
ajouter_aliment(jour, repas, amandes, 10)
ajouter_aliment(jour, repas, noix, 10)
ajouter_aliment(jour, repas, noix_de_pécan, 10)
ajouter_aliment(jour, repas, whey, 30)

repas = "Collation"
# Jus de fruits à déterminer

repas = "Dîner"

repas = "Goûter"
ajouter_aliment(jour, repas, whey, 30)
#Autre idée??? Cfr Pilou...

repas = "Souper"
One_Pot_Vegan_Swedish_Meatball_Pasta.ajouter_ingredients(3)

#endregion

#region Vendredi
jour = "Vendredi"

repas = "Déjeuner"
ajouter_aliment(jour, repas, yaourt_grecque, 200)
ajouter_aliment(jour, repas, vermicelles_chocolat, 20)
ajouter_aliment(jour, repas, kelloggs, 60)
ajouter_aliment(jour, repas, amandes, 10)
ajouter_aliment(jour, repas, noix, 10)
ajouter_aliment(jour, repas, noix_de_pécan, 10)
ajouter_aliment(jour, repas, whey, 30)

repas = "Collation"
# Jus de fruits à déterminer

repas = "Dîner"

repas = "Goûter"
ajouter_aliment(jour, repas, whey, 30)
#Autre idée??? Cfr Pilou...

repas = "Souper"
One_Pot_Vegan_Swedish_Meatball_Pasta.ajouter_ingredients(3)

#endregion

#region Samedi
jour = "Samedi"

repas = "Déjeuner"
ajouter_aliment(jour, repas, yaourt_grecque, 200)
ajouter_aliment(jour, repas, vermicelles_chocolat, 20)
ajouter_aliment(jour, repas, kelloggs, 60)
ajouter_aliment(jour, repas, amandes, 10)
ajouter_aliment(jour, repas, noix, 10)
ajouter_aliment(jour, repas, noix_de_pécan, 10)
ajouter_aliment(jour, repas, whey, 30)

repas = "Collation"
# Jus de fruits à déterminer

repas = "Dîner"

repas = "Goûter"
ajouter_aliment(jour, repas, whey, 30)
#Autre idée??? Cfr Pilou...

repas = "Souper"
One_Pot_Vegan_Swedish_Meatball_Pasta.ajouter_ingredients(3)

#endregion

#region Dimanche
jour = "Dimanche"

repas = "Déjeuner"
ajouter_aliment(jour, repas, yaourt_grecque, 200)
ajouter_aliment(jour, repas, vermicelles_chocolat, 20)
ajouter_aliment(jour, repas, kelloggs, 60)
ajouter_aliment(jour, repas, amandes, 10)
ajouter_aliment(jour, repas, noix, 10)
ajouter_aliment(jour, repas, noix_de_pécan, 10)
ajouter_aliment(jour, repas, whey, 30)

repas = "Collation"
# Jus de fruits à déterminer

repas = "Dîner"

repas = "Goûter"
ajouter_aliment(jour, repas, whey, 30)
#Autre idée??? Cfr Pilou...

repas = "Souper"
One_Pot_Vegan_Swedish_Meatball_Pasta.ajouter_ingredients(3)

#endregion

liste_jours = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche']
liste_repas = ['Déjeuner', 'Collation', 'Dîner', 'Goûter', 'Souper']
liste_infos_nutr = ['Energie', 'Total graisses', 'Graisses saturées', 'Total glucides', 'Sucres', 'Fibres alimentaires', 'Protéines', 'Sel']

régime = pd.DataFrame(aliments, columns = ['Jour', 'Repas', 'Aliment', 'Quantité (g)', 'Énergie/100g (kcal)', 'Total graisses/100g (g)', 'Graisses saturées/100g (g)', 'Total glucides/100g (g)', 'Sucres/100g (g)', 'Fibres alimentaires/100g (g)', 'Protéines/100g (g)', 'Sel/100g (g)'])
régime['Energie'] = régime['Quantité (g)'] * régime['Énergie/100g (kcal)'] / 100
régime['Total graisses'] = régime['Quantité (g)'] * régime['Total graisses/100g (g)'] / 100
régime['Graisses saturées'] = régime['Quantité (g)'] * régime['Graisses saturées/100g (g)'] / 100
régime['Total glucides'] = régime['Quantité (g)'] * régime['Total glucides/100g (g)'] / 100
régime['Sucres'] = régime['Quantité (g)'] * régime['Sucres/100g (g)'] / 100
régime['Fibres alimentaires'] = régime['Quantité (g)'] * régime['Fibres alimentaires/100g (g)'] / 100
régime['Protéines'] = régime['Quantité (g)'] * régime['Protéines/100g (g)'] / 100
régime['Sel'] = régime['Quantité (g)'] * régime['Sel/100g (g)'] / 100
print(régime)

tableaux_par_jour = []
for jour in liste_jours: 
    tableaux_par_jour.append(régime[régime['Jour'] == jour]) 

def obtenir_les_infos_nutritionnelles_par_repas():
    jour = input("Quel jour sommes-nous?").lower().capitalize()
    while not jour in liste_jours:
        jour = input("Entre un jour valide: ")
    index_jour = liste_jours.index(jour)

    repas = input("Quel repas veux-tu examiner?").lower().capitalize()
    while not repas in liste_repas:
        repas = input("Entre un repas valide: ")

    info_nutr = input("""Quelle information nutritionnelle veux-tu avoir?
    Entre 'Energie', 'Total graisses', 'Graisses saturées', 'Total glucides', 'Sucres', 'Fibres alimentaires', 'Protéines', ou 'Sel'
    """).lower().capitalize()
    while not info_nutr in liste_infos_nutr:
        info_nutr = input("Entre un item valide: ")

    if info_nutr == 'Energie':
        print("Tu auras {} kcal pour le {} du {}".format(str(tableaux_par_jour[index_jour][tableaux_par_jour[index_jour]['Repas'] == repas][info_nutr].sum()), repas.lower(), jour.lower()))
    else:
        print("Tu auras {} g de {} pour le {} du {}".format(str(tableaux_par_jour[index_jour][tableaux_par_jour[index_jour]['Repas'] == repas][info_nutr].sum()), info_nutr.lower(), repas.lower(), jour.lower()))

def obtenir_les_infos_nutritionnelles_par_jour():
    jour = input("Quel jour sommes-nous?").lower().capitalize()
    while not jour in liste_jours:
        jour = input("Entre un jour valide: ")
    index_jour = liste_jours.index(jour)

    info_nutr = input("""Quelle information nutritionnelle veux-tu avoir?
    Entre 'Energie', 'Total graisses', 'Graisses saturées', 'Total glucides', 'Sucres', 'Fibres alimentaires', 'Protéines', ou 'Sel'
    """).lower().capitalize()
    while not info_nutr in liste_infos_nutr:
        info_nutr = input("Entre un item valide: ")

    if info_nutr == 'Energie':
        print("Tu auras {} kcal le {}".format(str(tableaux_par_jour[index_jour][info_nutr].sum()), jour.lower()))
    else:
        print("Tu auras {} g de {} le {}".format(str(tableaux_par_jour[index_jour][info_nutr].sum()), info_nutr.lower(), jour.lower()))

#obtenir_les_infos_nutritionnelles_par_repas()


