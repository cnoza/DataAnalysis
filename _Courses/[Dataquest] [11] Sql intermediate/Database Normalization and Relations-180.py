## 4. Querying a normalized database ##

# This was already done but I include it for reference
# import sqlite3
# conn = sqlite3.connect('academy_awards.db')
query = ''' 
    select ceremonies.year, nominations.movie from nominations
    inner join ceremonies 
    on nominations.ceremony_id == ceremonies.id
    where nominations.nominee == 'Natalie Portman'
'''
cursor = conn.cursor()
cursor.execute(query)
portman_movies = cursor.fetchall()
print(portman_movies)

## 7. Join table ##

query1 = '''
    select * from movies_actors limit 5
'''
cursor1 = conn.cursor()
cursor1.execute(query1)
five_join_table = cursor1.fetchall()

query2 = '''
    select * from actors limit 5
'''
cursor2 = conn.cursor()
cursor2.execute(query2)
five_actors = cursor2.fetchall()

query3 = '''
    select * from movies limit 5
'''
cursor3 = conn.cursor()
cursor3.execute(query3)
five_movies = cursor3.fetchall()

print(five_join_table)
print(five_actors)
print(five_movies)

## 9. Querying a many-to-many relation ##

query = '''
    SELECT actors.actor, movies.movie FROM movies
    INNER JOIN movies_actors ON movies.id == movies_actors.movie_id
    INNER JOIN actors ON movies_actors.actor_id == actors.id
    WHERE movies.movie == "The King's Speech";
'''
cursor = conn.cursor()
cursor.execute(query)
kings_actors = cursor.fetchall()
print(kings_actors)

## 10. Practice: querying a many-to-many relation ##

query='''
    select movies.movie, actors.actor from movies
    inner join movies_actors on movies.id == movies_actors.movie_id
    inner join actors on movies_actors.actor_id == actors.id
    where actors.actor = 'Natalie Portman';
'''
cursor = conn.cursor()
cursor.execute(query)
portman_joins = cursor.fetchall()
print(portman_joins)