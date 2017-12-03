## 1. Overview ##

data = open('movie_metadata.csv', 'r').read().split('\n')
movie_data = [data_line.split(',') for data_line in data]
print(movie_data[:5])

## 3. Writing Our Own Functions ##

def get_movie_names(movie_data):
    movie_names = [item[0] for item in movie_data]
    return movie_names

movie_names = get_movie_names(movie_data)
print(movie_names[:5])

## 4. Functions with Multiple Return Paths ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(movie):
    if movie[-2]=='USA':
        return True
    else:
        return False
    
wonder_woman_usa = is_usa(wonder_woman)

## 5. Functions with Multiple Arguments ##

wonder_woman = ['Wonder Woman','Patty Jenkins','Color',141,'Gal Gadot','English','USA',2017]

def is_usa(input_lst):
    if input_lst[6] == "USA":
        return True
    else:
        return False
    
def index_equal_str(lst, index, string):
    if lst[index] == string:
        return True
    else:
        return False
    
wonder_woman_in_color = index_equal_str(wonder_woman, 2, 'Color')
print(wonder_woman_in_color)

## 6. Optional Arguments ##

def index_equals_str(input_lst,index,input_str):
    if input_lst[index] == input_str:
        return True
    else:
        return False
def counter(input_lst,header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        num_elt = num_elt + 1
    return num_elt

def feature_counter(movie_data, index, input_str, header_row = False):
    if header_row == True:
        movie_data = movie_data[1:]
    movie_feature = [movie for movie in movie_data if movie[index] == input_str]
    return len(movie_feature)

num_of_us_movies = feature_counter(movie_data, -2, 'USA', header_row = True)
        

## 7. Calling a Function inside another Function ##

def feature_counter(input_lst,index, input_str, header_row = False):
    num_elt = 0
    if header_row == True:
        input_lst = input_lst[1:len(input_lst)]
    for each in input_lst:
        if each[index] == input_str:
            num_elt = num_elt + 1
    return num_elt

def summary_statistics(movie_data):
    num_japan_films = feature_counter(movie_data, -2, 'Japan', header_row = True)
    num_color_films = feature_counter(movie_data, 2, 'Color', header_row = True)
    num_films_in_english = feature_counter(movie_data, -3, 'English', header_row = True)
    summary = { 'japan_films': num_japan_films, 
                'color_films': num_color_films,
                'films_in_english': num_films_in_english }
    return summary

summary = summary_statistics(movie_data)
    