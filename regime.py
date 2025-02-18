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

farine = Aliment('Everyday Farine de blé pour préparations variées 1 kg', '''Énergie kcal301 kcal
    Total graisses7.6 g
    Graisses saturées0.6 g
    Total glucides49 g
    Sucres2.8 g
    Fibres alimentaires3.4 g
    Protéines7.9 g
    Sel1.3 g''')

pain_naan = Aliment('Boni Selection Pain naan ail et coriandre 2 pièces 240 g', '''Énergie kcal348 kcal
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

tortilla_chips = Aliment('Boni Selection Original chips 200 g', '''Énergie kcal472 kcal
    Total graisses20 g
    Graisses saturées2 g
    Total glucides64 g
    Sucres0.8 g
    Fibres alimentaires4 g
    Protéines6.6 g
    Sel0.9 g''')

# Fruits et légumes
abricot = Aliment("Abricot 45g", '''Énergie kcal45 kcal
    Total graisses0 g
    Graisses saturées0 g
    Total glucides9 g
    Sucres6.7 g
    Fibres alimentaires1.7 g
    Protéines0 g
    Sel< 0.01 g''')

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

banane = Aliment('Bananes', '''Énergie kcal89 kcal
    Total graisses0.3 g
    Graisses saturées0.1 g
    Total glucides23 g
    Sucres12 g
    Fibres alimentaires2.6 g
    Protéines1.1 g
    Sel0 g ''')

citron = Aliment('Citron', '''Énergie kcal27 kcal
    Total graisses0 g
    Graisses saturées0 g
    Total glucides1.6 g
    Sucres0.8 g
    Fibres alimentaires0 g
    Protéines0 g
    Sel0 g''')

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

mandarine = Aliment('Mandarine', '''Énergie kcal47 kcal
    Total graisses0 g
    Graisses saturées0 g
    Total glucides9.2 g
    Sucres8.6 g
    Fibres alimentaires1.7 g
    Protéines1 g
    Sel0 g''')

nectar_abricot = Aliment("Nectar d'abricot CARREFOUR SELECTION ", '''Énergie kcal47 kcal
    Total graisses0 g
    Graisses saturées0 g
    Total glucides11 g
    Sucres10 g
    Fibres alimentaires0.5 g
    Protéines0 g
    Sel< 0.01 g''')

noix = Aliment("Boni Selection Cerneaux de noix 200 g", '''Énergie kcal689 kcal
    Total graisses65 g
    Graisses saturées6.1 g
    Total glucides7 g
    Sucres2.6 g
    Fibres alimentaires6.7 g
    Protéines15 g
    Sel< 0.01 g''')

noix_de_cajou = Aliment("Boni Selection Noix de cajou nature 250 g", '''Énergie kcal581 kcal
    Total graisses44 g
    Graisses saturées7.8 g
    Total glucides27 g
    Sucres5.9 g
    Fibres alimentaires3.3 g
    Protéines18 g
    Sel0.03 g''')

noix_de_coco_flocons = Aliment("Flocons de noix de coco", '''Total graisses65 g
    Graisses saturées57 g
    Total glucides7.4 g
    Sucres7.4 g
    Fibres alimentaires16 g
    Protéines7 g
    Sel0.1 g''')

noix_de_pécan = Aliment("Boni Selection Noix de pécan grillées 200 g", '''Énergie kcal742 kcal
    Total graisses74 g
    Graisses saturées6.3 g
    Total glucides4.2 g
    Sucres4.1 g
    Fibres alimentaires9.4 g
    Protéines9.5 g
    Sel< 0.01 g''')

oignons = Aliment('Boni Selection Oignons 2,5 kg', '''Énergie kcal40 kcal
    Total graisses0.1 g
    Graisses saturées< 0 g
    Total glucides9 g
    Sucres4.2 g
    Fibres alimentaires1.7 g
    Protéines1.1 g
    Sel0 g''')

poivron = Aliment('poivrons rouges', '''Énergie kcal35 kcal
    Total graisses0 g
    Graisses saturées0 g
    Total glucides6 g
    Sucres4.8 g
    Fibres alimentaires3.2 g
    Protéines1 g
    Sel0 g''')

sauce_tomate = Aliment('Base tomatée pour pizza Elvea Tetra 250g', '''Énergie kcal36 kcal
    Total graisses0.2 g
    Graisses saturées0 g
    Total glucides5.2 g
    Sucres4.5 g
    Fibres alimentaires3 g
    Protéines1.9 g
    Sel0.38 g''')

tomates_concassées_oignons = Aliment('Boni Selection Bio Tomates concassées au basilic et à loignon 500 g', '''Énergie kcal39 kcal
    Total graisses< 0.5 g
    Graisses saturées0 g
    Total glucides6.8 g
    Sucres6.4 g
    Fibres alimentaires1.7 g
    Protéines1.6 g
    Sel0.83 g''')

tomates_concentré = Aliment('Boni Selection Double concentré de tomates 28-30 % 140 g', '''Énergie kcal96 kcal
    Total graisses0.3 g
    Graisses saturées0.1 g
    Total glucides16.5 g
    Sucres16.5 g
    Fibres alimentaires4.2 g
    Protéines4.8 g
    Sel0.4 g''')

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

lentilles = Aliment('Boni Selection Lentilles noires 500 g', '''Énergie kcal375 kcal
    Total graisses1.1 g
    Graisses saturées0.2 g
    Total glucides60 g
    Sucres2 g
    Fibres alimentaires11 g
    Protéines26 g
    Sel0.02 g''')

pois_chiches = Aliment('BIOITALIA Pois chiches biologiques', ''' Énergie kcal163 kcal
    Total graisses2 g
    Graisses saturées0.2 g
    Total glucides25.2 g
    Sucres3 g
    Fibres alimentaires6.9 g
    Protéines7.6 g
    Sel0.17 g''')



# Produits laitiers
feta = Aliment('KOLIOS feta 200g', '''Énergie kcal310 kcal
    Total graisses26 g
    Graisses saturées18.5 g
    Total glucides2.1 g
    Sucres0.2 g
    Protéines17 g
    Sel1.2 g''')

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

yaourt_vanille = Aliment("Boni Selection Yaourt à la Grecque vanille 4 pièces 600 g", '''
    Énergie kcal126 kcal
    Total graisses7.3 g
    Graisses saturées4.7 g
    Total glucides13 g
    Sucres12 g
    Fibres alimentaires0 g
    Protéines2.5 g
    Sel0.1 g''')


# Graisses
beurre_amandes = Aliment("Delhaize 100 beurre d'amandes", '''Énergie kcal630 kcal
    Total graisses53 g
    Graisses saturées4.4 g
    Total glucides6.2 g
    Sucres4 g
    Fibres alimentaires8.6 g
    Protéines27 g
    Sel0 g''')

huile_colza = Aliment('HUILE DE COLZA VDM 15X1L', '''Énergie kcal828 kcal
    Total graisses92 g
    Graisses saturées7 g
    Total glucides0 g
    Sucres0 g
    Fibres alimentaires0 g
    Protéines0 g
    Sel0 g''')

huile_olive = Aliment('Huile Olive', '''Énergie kcal900 kcal
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

miel = Aliment("Miel", '''Énergie kcal320 kcal
    Total graisses0.1 g
    Graisses saturées0 g
    Total glucides79.3 g
    Sucres79.3 g
    Protéines0.5 g
    Sel0.015 g''')

oeuf = Aliment("Boni Selection Bio Oeufs de poules élevées en plein air L 6 pièces", '''Énergie kcal155 kcal
    Total graisses11 g
    Graisses saturées3.3 g
    Total glucides1.1 g
    Sucres1.1 g
    Fibres alimentaires0 g
    Protéines13 g
    Sel0.12 g''')

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
Chakchouka.ingredients({haricots_blancs: 150, poivron: 75, tomates_concassées_oignons: 150, feta: 25, oeuf: 120, tortilla_chips: 100, huile_olive: 15})
Chakchouka.liste_ingrédients("""cfr HelloFresh""")
Chakchouka.préparation("""  cfr HelloFresh  """)

Dahl = Recette('Dahl')
Dahl.ingredients({oignons: 50, patate_douce: 75, tomates_concentré: 75, lait_coco: 125, lentilles: 37.5, pain_naan: 120, huile_olive: 15})
Dahl.liste_ingrédients("""cfr HelloFresh""")
Dahl.préparation("""  cfr HelloFresh  """)

Riz_jaune_et_curry_dépinards = Recette("Riz jaune et curry d'épinards à la noix de coco")
Riz_jaune_et_curry_dépinards.ingredients({oignons: 50, riz: 85, noix_de_cajou: 10, noix_de_coco_flocons: 5, lait_coco: 50, oeuf: 60, huile_olive: 15, huile_tournesol: 7.5})
Riz_jaune_et_curry_dépinards.liste_ingrédients("""cfr HelloFresh""")
Riz_jaune_et_curry_dépinards.préparation("""  cfr HelloFresh  """)

#endregion

#region Smoothies

smoothie_banana = Recette("Smoothie banana")
smoothie_banana.ingredients({banane: 240, yaourt_vanille: 300, miel: 10})
smoothie_banana.liste_ingrédients("""cfr feuille 1""")
smoothie_banana.préparation("""cfr feuille 1""")

smoothie_tangerine_honey = Recette("Smoothie tangerine-honey")
smoothie_tangerine_honey.ingredients({mandarine: 200, citron: 240, miel: 60})
smoothie_tangerine_honey.liste_ingrédients("""cfr feuille 13""")
smoothie_tangerine_honey.préparation("""cfr feuille 13""")

smoothie_apricot_almond = Recette("Smoothie apricot-almond")
smoothie_apricot_almond.ingredients({nectar_abricot: 360, yaourt_vanille: 120, beurre_amandes: 30})
smoothie_apricot_almond.liste_ingrédients("""cfr feuille 14""")
smoothie_apricot_almond.préparation("""cfr feuille 14""")

smoothie_banana = Recette("Smoothie banana")
smoothie_banana.ingredients({banane: 240, yaourt_vanille: 300, miel: 10})
smoothie_banana.liste_ingrédients("""cfr feuille 17""")
smoothie_banana.préparation("""cfr feuille 17""")

smoothie_banana = Recette("Smoothie banana")
smoothie_banana.ingredients({banane: 240, yaourt_vanille: 300, miel: 10})
smoothie_banana.liste_ingrédients("""cfr feuille 34""")
smoothie_banana.préparation("""cfr feuille 34""")

smoothie_banana = Recette("Smoothie banana")
smoothie_banana.ingredients({banane: 240, yaourt_vanille: 300, miel: 10})
smoothie_banana.liste_ingrédients("""cfr feuille 38""")
smoothie_banana.préparation("""cfr feuille 38""")

smoothie_banana = Recette("Smoothie banana")
smoothie_banana.ingredients({banane: 240, yaourt_vanille: 300, miel: 10})
smoothie_banana.liste_ingrédients("""cfr feuille 40""")
smoothie_banana.préparation("""cfr feuille 40""")

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
One_Pot_Vegan_Swedish_Meatball_Pasta.ajouter_ingredients(2)

repas = "Goûter"
ajouter_aliment(jour, repas, whey, 30)
#Autre idée??? Cfr Pilou...

repas = "Souper"
One_Pot_Vegan_Swedish_Meatball_Pasta.ajouter_ingredients(2)

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
One_Pot_Enchilada_Rice.ajouter_ingredients(1)

repas = "Goûter"
ajouter_aliment(jour, repas, whey, 30)
#Autre idée??? Cfr Pilou...

repas = "Souper"
One_Pot_Enchilada_Rice.ajouter_ingredients(2)

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
Curry_de_pois_chiches_et_patates_douces.ajouter_ingredients(0.5)

repas = "Goûter"
ajouter_aliment(jour, repas, whey, 30)
#Autre idée??? Cfr Pilou...

repas = "Souper"
Curry_de_pois_chiches_et_patates_douces.ajouter_ingredients(1)

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
Chakchouka.ajouter_ingredients(0.5)

repas = "Goûter"
ajouter_aliment(jour, repas, whey, 30)
#Autre idée??? Cfr Pilou...

repas = "Souper"
Chakchouka.ajouter_ingredients(1)

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
Dahl.ajouter_ingredients(0.5)

repas = "Goûter"
ajouter_aliment(jour, repas, whey, 30)
#Autre idée??? Cfr Pilou...

repas = "Souper"
Dahl.ajouter_ingredients(1)

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
Riz_jaune_et_curry_dépinards.ajouter_ingredients(1)

repas = "Goûter"
ajouter_aliment(jour, repas, whey, 30)
#Autre idée??? Cfr Pilou...

repas = "Souper"
Riz_jaune_et_curry_dépinards.ajouter_ingredients(1)

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
One_Pot_Vegan_Swedish_Meatball_Pasta.ajouter_ingredients(2)

repas = "Goûter"
ajouter_aliment(jour, repas, whey, 30)
#Autre idée??? Cfr Pilou...

repas = "Souper"
One_Pot_Vegan_Swedish_Meatball_Pasta.ajouter_ingredients(2)

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

liste_courses = régime.groupby('Aliment').sum()
print(liste_courses)


def obtenir_les_infos_nutritionnelles():
    type_info = int(input("""Veux-tu connaître les informations nutritionnelles par 1) jour ou 2) repas?
    Entre 1 ou 2: """))
    while not type_info in [1,2]:
        type_info = input("Entre 1 ou 2: ")
    
    if type_info == 1:
        obtenir_les_infos_nutritionnelles_par_jour()
    elif type_info == 2:
        obtenir_les_infos_nutritionnelles_par_repas()

def obtenir_les_infos_nutritionnelles_par_repas():
    jour = input("Quel jour sommes-nous?").lower().capitalize()
    while not jour in liste_jours:
        jour = input("Entre un jour valide: ").lower().capitalize()
    index_jour = liste_jours.index(jour)

    repas = input("Quel repas veux-tu examiner?").lower().capitalize()
    while not repas in liste_repas:
        repas = input("Entre un repas valide: ").lower().capitalize()

    info_nutr = input("""Quelle information nutritionnelle veux-tu avoir?
    Entre 'Energie', 'Total graisses', 'Graisses saturées', 'Total glucides', 'Sucres', 'Fibres alimentaires', 'Protéines', ou 'Sel'
    """).lower().capitalize()
    while not info_nutr in liste_infos_nutr:
        info_nutr = input("Entre un item valide: ").lower().capitalize()

    if info_nutr == 'Energie':
        print("Tu auras {} kcal pour le {} du {}".format(str(tableaux_par_jour[index_jour][tableaux_par_jour[index_jour]['Repas'] == repas][info_nutr].sum()), repas.lower(), jour.lower()))
    else:
        print("Tu auras {} g de {} pour le {} du {}".format(str(tableaux_par_jour[index_jour][tableaux_par_jour[index_jour]['Repas'] == repas][info_nutr].sum()), info_nutr.lower(), repas.lower(), jour.lower()))

def obtenir_les_infos_nutritionnelles_par_jour():
    jour = input("Quel jour sommes-nous?").lower().capitalize()
    while not jour in liste_jours:
        jour = input("Entre un jour valide: ").lower().capitalize()
    index_jour = liste_jours.index(jour)

    info_nutr = input("""Quelle information nutritionnelle veux-tu avoir?
    Entre 'Energie', 'Total graisses', 'Graisses saturées', 'Total glucides', 'Sucres', 'Fibres alimentaires', 'Protéines', ou 'Sel'
    """).lower().capitalize()
    while not info_nutr in liste_infos_nutr:
        info_nutr = input("Entre un item valide: ").lower().capitalize()

    if info_nutr == 'Energie':
        print("Tu auras {} kcal le {}".format(str(tableaux_par_jour[index_jour][info_nutr].sum()), jour.lower()))
    else:
        print("Tu auras {} g de {} le {}".format(str(tableaux_par_jour[index_jour][info_nutr].sum()), info_nutr.lower(), jour.lower()))

#obtenir_les_infos_nutritionnelles()

#régime.to_excel(r'..\..\régime.xlsx', index = False)

for i in tableaux_par_jour:
    print(i['Jour'].head(1))
    print(i['Protéines'].sum())
    print(i['Energie'].sum())
    



