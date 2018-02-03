#!/usr/bin/python3
import csv
import random

'''
1,000 most popular movies on IMDB in the last 10 years,
Reccomend good ones you haven't seen based on ones you have.
1-1000
'''

'''
Compute alignment.
Store dictionary in JSON.
Key is userID, Value is dictionary of film PKs to star ratings.
key list of dicts, not interested in: pks, dict (seen, ratings),
'''

film_file = open('IMDB-Movie-Data.csv')
film_reader = csv.reader(film_file)
films = list(film_reader)

header = films[0]

for i in range(1,10):
    print(films[i][0:2])
    

class User():
    #Films for this dataset are referenced by rank, it's PK.
    def __init__(self, um = [i for i in range(1,1001)], wns = [], wds = [], sn = {}):
        self.id = random.getrandbits(32) #Unique ID (PK for account) [TEMPORARY]
        self.unmarked = um #All films by rank (PK)
        self.wont_see = wns
        self.would_see = wds
        self.seen = sn

    def swiped_left(self, film):
        #Swiped left, film User does not want to see
        swiped_film = self.unmarked.index(film)
        wont_see = self.unmarked.pop(swiped_film)
        self.wont_see.append(wont_see)
        
    def swiped_right(self, film):
        #Swiped left, film User does want to see
        swiped_film = self.unmarked.index(film)
        would_see = self.unmarked.pop(swiped_film)
        self.would_see.append(would_see)

    def seen_rate(self, film, rating):
        #user has seen and will give a rating.
        if type(rating) != int and i in range(1,6):
            raise ValueError(rating,'rating must be INT (1-5 stars)')
        seen_film = self.unmarked.index(film)
        seen = self.unmarked.pop(seen_film)
        self.seen[seen] = rating

me = User()
        
me.swiped_left(1)
print(me.wont_see)

me.swiped_right(2)
print(me.would_see)

me.seen_rate(3,5)
print(me.seen)

def create_user():
    user = User()
    for i in range(250):
        #Mark roughly 250 random films in line with IMDB's meta score
        seen = user.unmarked.pop(random.choice(user.unmarked))
        if len(films[seen][11]) < 1:
            continue
        rating = int(films[seen][11]) + 19
        rating //= 20
        print(films[seen][11],rating)
        #print(films[seen])

    print(len(user.unmarked))
tom = create_user()
        
            
        
        
        
