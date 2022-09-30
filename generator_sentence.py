from doctest import IGNORE_EXCEPTION_DETAIL
import random
from numpy.testing import IgnoreException
import pandas as pd

cities = pd.read_csv('data/cities.csv' , encoding='utf8')
cities_name = cities['name']
df_new = pd.DataFrame(columns=['tag','sentence'])
df_french2 = pd.read_csv("data/sentence_language.csv")
df_french = pd.read_csv("data/sentence_language.csv")
df_french2 = df_french2[df_french2.Language == 'French']
df_french = df_french[df_french.Language == 'French']
df_random_sentence = pd.concat([df_french2, df_french],ignore_index=True)
random_sentence = df_random_sentence['Text']

i = 0
j = len(cities_name) - 1
k = len(random_sentence) - 1

while i < len(cities_name):
    print(i, '/',j)
    new_row = {'tag':'command','sentence': f'Recherche le trajet pour aller à {cities_name[random.randint(0,j)]} à partir de {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Cherche le trajet pour aller à {cities_name[random.randint(0,j)]} à partir de {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Je souhaite partir à {cities_name[random.randint(0,j)]} depuis {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Je souhaite voyager à {cities_name[random.randint(0,j)]} depuis {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Je veux voyager à {cities_name[random.randint(0,j)]} en partant de {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Recherche le trajet pour aller à {cities_name[random.randint(0,j)]} en partant de {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Cherche le trajet pour aller à {cities_name[random.randint(0,j)]} en partant de {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Je souhaite partir à {cities_name[random.randint(0,j)]} en partant de {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Je souhaite voyager à {cities_name[random.randint(0,j)]} en partant de {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Recherche le trajet entre {cities_name[random.randint(0,j)]} et {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Cherche le trajet entre {cities_name[random.randint(0,j)]} et {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Je souhaite aller de {cities_name[random.randint(0,j)]} à {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Je souhaite voyager de {cities_name[random.randint(0,j)]} à {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Je veux voyager de {cities_name[random.randint(0,j)]} à {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Je veux aller de {cities_name[random.randint(0,j)]} à {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Recherche le trajet de {cities_name[random.randint(0,j)]} et {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Cherche le trajet de {cities_name[random.randint(0,j)]} et {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Je souhaite aller de {cities_name[random.randint(0,j)]} à {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Recherche le voyage de {cities_name[random.randint(0,j)]} et {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Cherche le voyage de {cities_name[random.randint(0,j)]} et {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'command','sentence': f'Je souhaite voyager entre {cities_name[random.randint(0,j)]} à {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': f'Quelle est la ville la plus grande entre {cities_name[random.randint(0,j)]} et {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': f'Quelle est la ville la plus petite entre {cities_name[random.randint(0,j)]} et {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': f'Quelle ville est la plus polluée entre {cities_name[random.randint(0,j)]} et {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': f'Recherche la distance entre {cities_name[random.randint(0,j)]} et {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': f'Quelle est la distance entre {cities_name[random.randint(0,j)]} et {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': f'Recherche sur google la ville {cities_name[random.randint(0,j)]} pour voyager'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': f'Cherche sur youtube des vidéos de {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': random_sentence[random.randint(0,k)] + " Recherche"}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': random_sentence[random.randint(0,k)] + " Cherche"}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': random_sentence[random.randint(0,k)]  + " souhaite"}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': random_sentence[random.randint(0,k)]  + " voyager"}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': random_sentence[random.randint(0,k)]  + " trajet"}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': random_sentence[random.randint(0,k)]  + " voyage"}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': random_sentence[random.randint(0,k)]  + " partie"}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': random_sentence[random.randint(0,k)]  + " aller"}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': random_sentence[random.randint(0,k)] + f' {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': random_sentence[random.randint(0,k)] + f' {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': random_sentence[random.randint(0,k)] + f' {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': random_sentence[random.randint(0,k)] + f' {cities_name[random.randint(0,j)]}'}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': random_sentence[random.randint(0,k)]}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    new_row = {'tag':'not_command','sentence': random_sentence[random.randint(0,k)]}
    df_tmp = pd.DataFrame(new_row, index=[0])
    df_new = pd.concat([df_new, df_tmp])
    i += 1

df_new.to_csv('model/data_sentence_train.csv')