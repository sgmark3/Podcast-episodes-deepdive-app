#!/usr/bin/env python

import csv
import pickle
import gensim
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

file = open('model/health_episodes_lda_model_umass.pkl','rb')
health_lda_model = pickle.load(file)
file.close()

file = open('model/sports_episodes_lda_model_umass.pkl','rb')
sports_lda_model = pickle.load(file)
file.close()

file = open('model/religion_episodes_lda_model_umass.pkl','rb')
religion_lda_model = pickle.load(file)
file.close()

file = open('model/invest_episodes_lda_model_umass.pkl','rb')
invest_lda_model = pickle.load(file)
file.close()

file = open('model/crime_episodes_lda_model_umass.pkl','rb')
crime_lda_model = pickle.load(file)
file.close()

file = open('model/nature_episodes_lda_model_umass.pkl','rb')
nature_lda_model = pickle.load(file)
file.close()

file = open('model/all_genres_lda_model_30_umass.pkl','rb')
nature_lda_model = pickle.load(file)
file.close()

df_health = pd.read_csv('data/health.csv')
df_sports = pd.read_csv('data/sports.csv')
df_religion = pd.read_csv('data/religion.csv')
df_invest = pd.read_csv('data/invest.csv')
df_crime = pd.read_csv('data/crime.csv')
df_nature = pd.read_csv('data/nature.csv')
df_allgenres = pd.read_csv('data/all_genres_umass.csv')

# Select a genre
select = st.sidebar.selectbox('Select a podcast genre',['Sports & Games','Health & Fitness','Religion & Christianity','Stocks & Investing','Crime & Conspiracies','Nature & Climate','All genres'])

d = {'Sports & Games':['https://www.dropbox.com/s/lc699tc3v1d7ei9/sports_umass.html?dl=0',\
                       df_sports,\
                       {k:sports_lda_model.show_topic(k,topn=15) for k in range(sports_lda_model.num_topics)}],\
     'Health & Fitness':['https://www.dropbox.com/s/p7vtixk357ozow0/health_umass.html?dl=0',\
                       df_health,  
                       {k:health_lda_model.show_topic(k,topn=15) for k in range(health_lda_model.num_topics)}],\
     'Religion & Christianity':['https://www.dropbox.com/s/yn8v4gkwrfdyrn9/religion_umass.html?dl=0',\
                       df_religion,\
                       {k:religion_lda_model.show_topic(k,topn=15) for k in range(religion_lda_model.num_topics)}],\
     'Stocks & Investing':['https://www.dropbox.com/s/pm69uxl19m3jtxj/invest_umass.html?dl=0',\
                       df_invest,\
                       {k:invest_lda_model.show_topic(k,topn=15) for k in range(invest_lda_model.num_topics)}],
     'Crime & Conspiracies':['https://www.dropbox.com/s/efnqucd0xz4cevg/crime_umass.html?dl=0',\
                       df_crime,\
                       {k:crime_lda_model.show_topic(k,topn=15) for k in range(crime_lda_model.num_topics)}],
     'Nature & Climate':['https://www.dropbox.com/s/36w54cu85cadaca/nature_umass.html?dl=0',\
                       df_nature,\
                       {k:nature_lda_model.show_topic(k,topn=15) for k in range(nature_lda_model.num_topics)}],
     'All genres':['https://www.dropbox.com/s/80i0qqt1cibcdj3/all_genres_30_umass.html?dl=0',\
                       df_allgenres,\
                       {k:nature_lda_model.show_topic(k,topn=15) for k in range(nature_lda_model.num_topics)}]}

# load the word2vec model
file = open('model/word2vec.pkl','rb')
model = pickle.load(file)
file.close()

# setting up the dashboard
keywords = st.text_input('Enter a keyword here','football, nfl')

words = keywords.split(', ')

try:
    similar_words = [[item[0] for item in model.wv.most_similar(word,topn=10)] for word in words]
    bigrams=[]
    for pair in combinations(words,2):
        bigrams.append(pair[0]+'_'+pair[1])
    similar_words.append(bigrams+words)
except KeyError as ke:
    st.markdown('Specify a different set of keywords')

topics_terms={}
percentage={}
weighted_sum={}
for key,val in d[select][2].items():
    topics_terms[key]=[x[0] for x in val]
    percentage[key]=[x[1] for x in val]
    weighted_sum[key]=0
    for entry in similar_words:
        for word in entry:
            for i,w in enumerate(topics_terms[key]):
                if word==w:
                    weighted_sum[key]+=percentage[key][i]

link = d[select][0]
st.write(f'A 2D visualization of the topics and their terms distribution [link]({link})')

episode_length = st.sidebar.selectbox('Choose a duration window for the episodes (in mins)',['5-15','15-30','30-45','45-60','60-60<'])
l = int(episode_length.split('-')[0])
if episode_length.split('-')[1]=='60<':
    u=1000
else:
    u=int(episode_length.split('-')[1])
            
topic, score = sorted(weighted_sum.items(),key=(lambda x: x[1]),reverse=True)[0]

if score > 0:
    st.bar_chart(pd.DataFrame(percentage[topic],columns=[f'Topic-{topic}'],index=topics_terms[topic]))
    df = d[select][1]
    recommendations = df[(df['Dominant topic']==topic)&(df['Episode duration (in mins)']<u)&(df['Episode duration (in mins)']>=l)][['Podcast name','Episode name','Episode duration (in mins)','Description of the episode','url of the podcast episodes']]
    recommendations = recommendations.reset_index()
    st.table(recommendations[['Podcast name','Episode name','Episode duration (in mins)','url of the podcast episodes']])
    with st.expander("See descriptions of the episodes"):
        st.table(recommendations[['Description of the episode']])
else:
    st.write('No topic found. Please enter a different set of keywords')
    
