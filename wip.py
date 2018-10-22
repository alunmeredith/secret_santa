import random
from typing import List

class Person:
    def __repr__(self):
        return("{}".format(self.name))

    def __str__(self):
        return("{}".format(self.name))

    def __init__(self, name, family, spouse, generation): 
      self.name = name
      self.family = family
      self.possibilities = {}
      self.spouse = spouse
      self.generation = generation
      self.target = None



# Inialise all people in this group.
people = [
    Person("alun", "meredith", "", "young"),
    Person("amy", "cutler", "", "young"),
    Person("steve", "wright", "sandra", "old"),
    Person("sandra", "wright", "steve", "old")
    ]

# Create a map of each person to their possible targets. 
def initalise_targets(person: Person, all_people: list):
    others = all_people.copy()
    #others.remove(person)
    for p in others:
        person.possibilities[p] = 1
    return(person)


initialised_targets = [initalise_targets(person, people) for person in people]


print(initialised_targets)


def samePersonScore(person: Person, target: Person, score): 
    return_value = score
    if (person.name == target.name):
         return_value = score + -999
    return(return_value)

def sameGenerationScore(person: Person, target: Person, score):
    return_value = score
    if(person.generation == target.generation):
        return_value = score + 5 
    return(return_value)

def sameFamilyScore(person: Person, target: Person, score):
    return_value = score
    if(person.family == target.family):
        return_value = score - 10 
    return(return_value)

def spouseScore(person: Person, target: Person, score):
    return_value = score
    if(person.name == target.spouse):
        return_value = score - 20 
    return(return_value)

scores = (samePersonScore, spouseScore, sameFamilyScore, sameGenerationScore)

for score in scores: 
    for person in initialised_targets:
        for target, weight in person.possibilities.items():
            new_weight = score(person, target, weight)
            person.possibilities[target] = new_weight


## Randomly assign targets
def assignTargets(people: List[Person]):
    people_copy = people.copy()
    random.shuffle(people_copy)

    first = people_copy.pop()
    previous = first
    for person in people_copy:
        person.target = previous
        previous = person
    first.target = previous

    people_copy.append(first)
    return(people_copy)

def totalPoints(people: List[Person]):
    for person in people:
        target = person.target
        #a = {v for k, v in person.possibilities.items() if k.name == target}
        res = []
        for k, v in person.possibilities.items():
            if k.name == target:
                res.append[v]
        
        print(res)
        
x = assignTargets(initialised_targets)
totalPoints(initialised_targets)




