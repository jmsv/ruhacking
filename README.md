# ruhacking
University of Reading Hackathon - 20180203

Film recocmendation service which looks for people who think like you and suggests the films they like. Featuring a Tinderfied UI.
Example of methods:
Two users are created and rate films similarly, so the films that 'you' has liked that 'me' has not seen are reccomended.
Also intended to reccomend the optimum film for a group to watch (party of more than 1 where the avg predicted grade would be maximised).

Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from swipe_populater import *
>>> me = User()
>>> you = User()
>>> json_film_by_no(1)
'{"Length": "121", "Year": "2014", "TrailerURL": "http://www.youtube.com/watch?v=d96cjJhvlMA", "Cast": "Chris Pratt, Vin Diesel, Bradley Cooper, Zoe Saldana", "Genre": "Action,Adventure,Sci-Fi", "Description": "A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.", "Title": "Guardians of the Galaxy"}'
>>> me.seen_rate(1,3)
>>> you.seen_rate(1,3)
>>> alignment(me,you)
Intersection:  1
1.0
>>> films[55]
['55', 'The Dark Knight', 'Action,Crime,Drama', 'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the Dark Knight must come to terms with one of the greatest psychological tests of his ability to fight injustice.', 'Christopher Nolan', 'Christian Bale, Heath Ledger, Aaron Eckhart,Michael Caine', '2008', '152', '9', '1791916', '533.32', '82']
>>> me.seen_rate(55,2)
>>> you.seen_rate(55,4)
>>> alignment(me,you)
Intersection:  2
0.75
>>> you.seen_rate(175,5)
>>> you.seen_rate(225,4)
>>> you.seen_rate(250,2)
>>> films[175]
['175', 'Frozen', 'Animation,Adventure,Comedy', 'When the newly crowned Queen Elsa accidentally uses her power to turn things into ice to curse her home in infinite winter, her sister, Anna, teams up with a mountain man, his playful reindeer, and a snowman to change the weather condition.', 'Chris Buck', 'Kristen Bell, Idina Menzel, Jonathan Groff, Josh Gad', '2013', '102', '7.5', '451894', '400.74', '74']
>>> films[225]
['225', "We're the Millers", 'Comedy,Crime', 'A veteran pot dealer creates a fake family as part of his plan to move a huge shipment of weed into the U.S. from Mexico.', 'Rawson Marshall Thurber', 'Jason Sudeikis, Jennifer Aniston, Emma Roberts, Ed Helms', '2013', '110', '7', '334867', '150.37', '44']
>>> films[250]
['250', 'The Intouchables', 'Biography,Comedy,Drama', 'After he becomes a quadriplegic from a paragliding accident, an aristocrat hires a young man from the projects to be his caregiver.', 'Olivier Nakache', 'François Cluzet, Omar Sy, Anne Le Ny, Audrey Fleurot', '2011', '112', '8.6', '557965', '13.18', '57']
>>> get_aligned_recs(me,you)
[175, 225]
