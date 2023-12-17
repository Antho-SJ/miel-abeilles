# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 11:09:47 2023

@author: St-Jean
"""
import math
import random as rd

class Abeille:
    def __init__(self, genes):
        self.genes = genes  #Liste de déplacements entre les fleurs
        self.index_gene = 0
        self.fitness_score = 0


    def calculer_fitness(self):
        d_1 = math.sqrt((500-self.genes[0][0])**2+(500-self.genes[0][1])**2)
        fitness = d_1

        for i in range(len(self.genes)-1):
            distance = math.sqrt((self.genes[i][0]-self.genes[i+1][0])**2+(self.genes[i][1]-self.genes[i+1][1])**2)
            fitness += distance
        self.fitness_score = fitness
          
    def classement_abeille(self,element):
        Liste_finale=[]
        for i in element:
            liste_temp=i.split(':')
            Liste_finale.append(float(liste_temp[1]))
        return Liste_finale
    
    #Fonction de croisement (Single-Point Crossover)
    def single_point_crossover(parent1, parent2):
        #Choisissez un point de croisement aléatoire
        crossover_point = rd.randint(1, len(parent1) - 1)

        #Effectue le croisement
        child1 = parent1[:crossover_point] + [t for t in parent2 if t not in parent1[:crossover_point]]
        child2 = parent2[:crossover_point] + [t for t in parent1 if t not in parent2[:crossover_point]]

        #Ajouter des tuples manquants pour maintenir la taille à 50
        while len(child1) < 50:
            remaining_tuples = [t for t in parent2 if t not in child1]
            child1.append(rd.choice(remaining_tuples))

        while len(child2) < 50:
            remaining_tuples = [t for t in parent1 if t not in child2]
            child2.append(rd.choice(remaining_tuples))

        return child1, child2
    
    
    def calculer_fitness_score(genes):
        d_1 = math.sqrt((500-genes[0][0])**2+(500-genes[0][1])**2)
        fitness = d_1

        for i in range(len(genes)-1):
            distance = math.sqrt((genes[i][0]-genes[i+1][0])**2+(genes[i][1]-genes[i+1][1])**2)
            fitness += distance
        return fitness
    
    def mutation(df):
        nbr_individu_muté = rd.randint(9,15)

        #Générer x nombres aléatoires distincts entre 0 et 49
        nombres_random = rd.sample(range(100), nbr_individu_muté)
        nombres_random.sort()
        
        for i in range(len(nombres_random)):
            tuple1 = rd.randint(0, 49)
            tuple2 = rd.randint(0, 49)
            temp = df['Gènes'].iloc[nombres_random[i]][tuple1]
            df['Gènes'].iloc[nombres_random[i]][tuple1] = df['Gènes'].iloc[nombres_random[i]][tuple2]
            df['Gènes'].iloc[nombres_random[i]][tuple2] = temp
            df['Fitness'][i] = Abeille.calculer_fitness_score(df['Gènes'][i])
        return df
    
    
    
            
        
        
            
            
        