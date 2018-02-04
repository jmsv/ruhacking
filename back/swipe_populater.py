#!/usr/bin/python3
import csv
import random
import copy
import json
import urllib
import re

'''
NO ID SYSTEM, AM USING RANDOM INTS AS PKs FOR POEPLE
'''

'''
To demo, could rate in rank order to make alignment more likely
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


class User():
    #Films for this dataset are referenced by rank, it's PK.
    def __init__(self, um = [i for i in range(1,1001)], wns = [], wds = [], sn = {}):
        self.id = random.getrandbits(32) #Unique ID (PK for account) [TEMPORARY]
        self.unmarked = copy.deepcopy(um) #All films by rank (PK)
        self.wont_see = copy.deepcopy(wns)
        self.would_see = copy.deepcopy(wds)
        self.seen = copy.deepcopy(sn)

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

def create_intellectual_user():
    #*me, an intellectual* -- ratings aline with IMDB ratings
    user = User()
    for i in range(250):
        #Mark roughly 250 random films in line with IMDB's meta score
        seen = random.choice(user.unmarked)
        if len(films[seen][11]) < 1:
            continue
        rating = int(films[seen][11]) + 19
        rating //= 20
        user.seen_rate(seen,rating)
        #print(films[seen])
    return user

def create_bogus_user():
    #Random markings for films
    user = User()
    for i in range(250):
        #Mark roughly 250 random films in line with IMDB's meta score
        seen = random.choice(user.unmarked)
        if len(films[seen][11]) < 1:
            continue
        rating = random.randint(1,5)
        user.seen_rate(seen,rating)
        #print(films[seen])
    return user

def alignment(user1, user2):
    #The more you align the better, 0-1 scale 1 is they agree perfectly, 0 is complete disagreement.
    #print('First user has rated',str(len(user1.seen)),'films.')
    #print('Second user has rated',str(len(user2.seen)),'films.')
    u1seen = set(user1.seen)
    u2seen = set(user2.seen)
    bothseen =  list(u1seen.intersection(u2seen))
    bs_pop = len(bothseen)
    print('Intersection: ',bs_pop)
    total = 0
    for film in bothseen:
        total += abs(user1.seen[film] - user2.seen[film])
    total /= bs_pop
    alignment = 4 - total
    alignment/= 4
    return alignment

def trailer(film):
    search = films[film][1] + ' trailer'
    query_string = urllib.parse.urlencode({"search_query" : search })
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return ("http://www.youtube.com/watch?v=" + search_results[0])

def get_aligned_recs(user, aligned_user):
    #find all films for user (that they haven't seen) that aligned user has seen, sorted by rating.
    #So far returns 5 stars then 4 stars.
    already_seen = set(user.seen)
    aligned_seen = set(aligned_user.seen)
    bothseen =  list(already_seen.intersection(aligned_seen))
    #print(bothseen)
    aligned_seen = list(aligned_seen)
    short_list = [i for i in aligned_seen if i not in bothseen]
    #print(len(short_list))
    five_star = [film for film in short_list if aligned_user.seen[film] == 5]
    #print(len(five_star))
    four_star = [film for film in short_list if aligned_user.seen[film] == 4]
    #print(len(four_star))
    return five_star + four_star

def json_film_by_no(fn):
    #fn = film_number, RETURNS JSON
    #Take a filmID and return name, description, IMDB rating, trailerURL, genre, length, actors
    #length is in minutes
    f = films[fn]
    film = {'Title':f[1], 'Genre':f[2], 'Description':f[3], 'Cast':f[5], 'Year':f[6],
            'Length': f[7], 'TrailerURL': trailer(fn)}
    return json.dumps(film)

def user_to_json(user):
    #turn a user into json.
    u = user
    preJSON = {'unmarked':u.unmarked, 'wont_see': u.wont_see,
               'would_see': u.would_see, 'seen': u.seen}
    return json.dumps(preJSON)

def json_to_user(jds):
    #oppositte of above funciton, turns json into user object.
    #jds =jsondumps
    ud = json.loads(jds)
    #um = [i for i in range(1,1001)], wns = [], wds = [], sn = {}
    this_user = User(um = ud['unmarked'], wns = ud['wont_see'],
                     wds = ud['would_see'], sn = ud['seen'])
    return this_user
    

#Test shit         
##dick = create_bogus_user()
##harry = create_intellectual_user()
##get_aligned_recs(dick,harry)
##h = user_to_json(harry)
