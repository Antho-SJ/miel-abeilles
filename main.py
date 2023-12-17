# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 11:06:18 2023

@author: St-Jean
"""
import matplotlib.pyplot as plt
import random as rd
from beehive import Abeille
import pandas as pd
import numpy as np
import warnings

warnings.filterwarnings("ignore")


#On génère le champ de fleurs sur un graphe
fleurs = [(796,310),(774,130),(116,69),(908,534),(708,99),(444,428),(220,307),(501,287),(345,560),(628,311),(901,639),(436,619),(938,646),(45,549),(837,787),(328,489),(278,434),(704,995),(101,482),(921,964),(493,970),(494,898),(929,389),(730,742),(528,794),(371,429),(98,711),(724,631),(573,903),(964,726),(213,639),(549,329),(684,273),(273,105),(897,324),(508,31),(758,405),(862,361),(898,898),(2,897),(951,209),(189,739),(602,68),(437,601),(330,410),(3,517),(643,404),(875,407),(761,772),(276,666)]

df = pd.DataFrame()

#Création de la ruche initiale à 100 abeilles
Liste_abeille_score = []
Liste_genes_abeille_gen1 = []
for i in range(1,101):
    genes_abeille_gen1 = rd.sample(fleurs, len(fleurs))
    Liste_genes_abeille_gen1.append(genes_abeille_gen1)
    abeille = Abeille(genes=genes_abeille_gen1)
    abeille.calculer_fitness()
    Liste_abeille_score.append(f"Fitness_abeille_{i}: {abeille.fitness_score}")
    
Liste_score=abeille.classement_abeille(Liste_abeille_score)
moyenne = sum(Liste_score) / len(Liste_score)
    
df['Gènes'] = Liste_genes_abeille_gen1
df['Fitness'] = Liste_score
df=df.sort_values('Fitness')
del Liste_abeille_score

generation = 0
Liste_moyenne = []
stagnation_count = 0  #Compteur de stagnation
max_stagnation = 10  #Nombre maximal de générations avec stagnation autorisé

while generation < 500 and stagnation_count < max_stagnation:
    df = df.iloc[:50, :]
    df = df.reset_index(drop=True)
    
    #offspring sera une liste de taille 50 contenant le gène des enfants
    offspring = []
    for i in range(0, len(df)-1, 2):
        parent1 = df['Gènes'][i]
        parent2 = df['Gènes'][49-i]

        child1, child2 = Abeille.single_point_crossover(parent1, parent2)

        offspring.append(child1)
        offspring.append(child2)
    
    #Calcul du score des enfants 
    Liste_abeille_score = []
    for i in range(50):
        abeilles_gen2 = Abeille(genes=offspring[i])
        abeilles_gen2.calculer_fitness()
        Liste_abeille_score.append(f"Fitness_abeille_{i+1}: {abeilles_gen2.fitness_score}")
    Liste_score_enfants = abeille.classement_abeille(Liste_abeille_score)
    
    #Création d'un sous dataframe contenant les informations des enfants
    df_offspring = pd.DataFrame()
    df_offspring['Gènes'] = offspring
    df_offspring['Fitness'] = Liste_score_enfants
    
    #On assemble les deux dataframes pour avoir à nouveau 100 abeilles dans la ruche
    df = pd.concat([df_offspring , df])
    df = df.sort_values('Fitness')
    df = df.reset_index(drop=True)
    #Création d'une liste contenant les moyennes d'une génération (qui nous servira par la suite)
    moyenne = df['Fitness'].mean()
    Liste_moyenne.append(moyenne)
    
    #Vérifier la stagnation
    if generation > 0 and moyenne == Liste_moyenne[generation - 1]:
        stagnation_count += 1
    else:
        stagnation_count = 0  #Réinitialiser le compteur si la moyenne change
     
    generation+=1
    
    if stagnation_count == 1:
        print(f"Stagnation commencée à la génération {generation - stagnation_count}")
        df = Abeille.mutation(df)
print(f"Score le plus bas atteint {Liste_moyenne[-1]}")
del Liste_abeille_score
abscisse = np.arange(1, generation+1, 1)
plt.plot(abscisse,Liste_moyenne)
plt.xlabel('Génération')
plt.ylabel('Moyenne fit score')
plt.show()


#Séparer les coordonnées x et y
x_coords, y_coords = zip(*fleurs)

#Tracer toutes les coordonnées en vert
plt.scatter(x_coords, y_coords, color='g')

#Tracer le chemin en rouge et pointillé
ordre_x, ordre_y = zip(*df['Gènes'][0])
plt.plot(ordre_x, ordre_y, linestyle='--', color='orange')

#Ajouter des labels et une légende
plt.xlabel('Coordonnée X')
plt.ylabel('Coordonnée Y')
plt.title('Chemin de la meilleure abeille')

#Afficher le graphique
plt.show()


