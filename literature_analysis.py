import re, csv, os
import pandas as pd
import numpy as np
import nltk
import math
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('white')
from nltk import everygrams, word_tokenize
#import nltk
#nltk.download('punkt')
from collections import Counter

# check if folder exists
results_path = "results/"
if not os.path.isdir(results_path):
    os.makedirs(results_path)

columnnames =['AU','TI','AB','PY']

def convertWOScsv(filename):
    openfile = open(filename, encoding='latin-1')
    sampledata = openfile.read()
    # divide into list of records
    individualrecords = sampledata.split('\n\n')
    databaseofWOS = []
    for recordindividual in individualrecords:
        onefile = {}
        for x in columnnames:
            everyrow = re.compile('\n'+x + ' ' + '((.*?))\n[A-Z][A-Z1]', re.DOTALL)
            rowsdivision = everyrow.search(recordindividual)
            if rowsdivision:
                onefile[x] = rowsdivision.group(1)
        databaseofWOS.append(onefile)
    return databaseofWOS

def massconvertWOS(folder):
    publicationslist = []
    for file in os.listdir(folder):
        if file.endswith('.txt'):
            converttotable = convertWOScsv(folder + '\\' + file)
            publicationslist += converttotable
    publicationslist = pd.DataFrame(publicationslist)
    publicationslist.dropna(how='all', inplace=True)
    publicationslist.reset_index(drop=True, inplace=True)
    #publicationslist['PY'] =publicationslist['PY'].fillna('').replace('', '2019').astype(int)
    #publicationslist['TC'] = publicationslist['TC'].apply(lambda x: int(x.split('\n')[0]))
    return publicationslist

df = massconvertWOS('raw')
#df = df.drop_duplicates('UT').reset_index(drop=True)

print('Number of Articles:', df.shape[0])
df.head()[['TI', 'AU', 'AB', 'PY']]
df.dropna(inplace=True)
df["text"] = df["TI"] + " " + df["AB"]
df["text"] = df["text"].str.lower()
# remove all special characters
df["text"] = df["text"].str.replace('\W', ' ', regex=True)
# remove common words
#df["text"] = df["text"].str.replace(r'\b\w\b', '').str.replace(r'\s+', ' ')
df["text"] = df["text"].str.replace(' s ', ' ', regex=True)
df["text"] = df["text"].str.replace(' a ', ' ', regex=True)
df["text"] = df["text"].str.replace(' an ', ' ', regex=True)
df["text"] = df["text"].str.replace(' the ', ' ', regex=True)
df["text"] = df["text"].str.replace(' by ', ' ', regex=True)
df["text"] = df["text"].str.replace(' in ', ' ', regex=True)
df["text"] = df["text"].str.replace(' of ', ' ', regex=True)
df["text"] = df["text"].str.replace(' and ', ' ', regex=True)
df["text"] = df["text"].str.replace(' to ', ' ', regex=True)
df["text"] = df["text"].str.replace(' with ', ' ', regex=True)
df["text"] = df["text"].str.replace(' for ', ' ', regex=True)
df["text"] = df["text"].str.replace(' which ', ' ', regex=True)
df["text"] = df["text"].str.replace(' from ', ' ', regex=True)
df["text"] = df["text"].str.replace(' at ', ' ', regex=True)
df["text"] = df["text"].str.replace(' or ', ' ', regex=True)
df["text"] = df["text"].str.replace(' on ', ' ', regex=True)
df["text"] = df["text"].str.replace(' as ', ' ', regex=True)
df["text"] = df["text"].str.replace(' is ', ' ', regex=True)
df["text"] = df["text"].str.replace(' are ', ' ', regex=True)
df["text"] = df["text"].str.replace(' was ', ' ', regex=True)
df["text"] = df["text"].str.replace(' were ', ' ', regex=True)
df["text"] = df["text"].str.replace(' can ', ' ', regex=True)
df["text"] = df["text"].str.replace(' be ', ' ', regex=True)
df["text"] = df["text"].str.replace(' we ', ' ', regex=True)
df["text"] = df["text"].str.replace(' this ', ' ', regex=True)
# remove plurals
df["text"] = df["text"].str.replace(' laws ', ' law ', regex=True)
df["text"] = df["text"].str.replace(' rules ', ' rule ', regex=True)
df["text"] = df["text"].str.replace(' relationships ', ' relationship ', regex=True)
df["text"] = df["text"].str.replace(' regularities ', ' regularity ', regex=True)
df["text"] = df["text"].str.replace(' theories ', ' theory ', regex=True)

#plot over time
#df.groupby('PY').size().plot(kind='bar')
#plt.show()

# count how often certain words (e.g. law) are either in title or abstract
count = pd.DataFrame()
count["word"] = ["law", "rule", "relationship", "regularity", "theory", "functional relationship"]
count["abstract"] = ""
count["title"] = ""
count["abstit"] = ""
for i in range(len(count)):
    count["abstract"][i] = df['AB'].str.contains(count["word"][i], case=False).sum()
    count["title"][i] = df['TI'].str.contains(count["word"][i], case=False).sum()
    count["abstit"][i] = (df['AB'].str.contains(count["word"][i], case=False)|df['TI'].str.contains(count["word"][i], case=False)).sum()
print(count)

# count how often certain combinations of words (e.g. Darcy's law) are either in title or abstract
for c in count["word"]:
    tokens = df['text'].apply(lambda y: [' '.join(ng) for ng in everygrams(word_tokenize(y), 2, 3)]).to_frame()
    #abstract_strings["AB"][45]
    flat_list = []
    for sublist in list(tokens['text']):
        for item in sublist:
            flat_list.append(item)
    filtered_strings = [k for k in flat_list if c in k]
    word_dist = nltk.FreqDist(filtered_strings)
    most_common_words = pd.DataFrame(word_dist.most_common(1000), columns=['Word', 'Frequency'])
    print(most_common_words)
    all_words = pd.DataFrame(filtered_strings)

    # save to file
    most_common_words.to_csv(r'results/most_common_words_'+c+'.csv', index=False)
    all_words.to_csv(r'results/all_words_'+c+'.csv', index=False)


# count how often certain relationship between x and y appears
c="relationship between"
tokens = df['text'].apply(lambda y: [' '.join(ng) for ng in everygrams(word_tokenize(y), 4, 8)]).to_frame()
#abstract_strings["AB"][45]
flat_list = []
for sublist in list(tokens['text']):
    for item in sublist:
        flat_list.append(item)
filtered_strings = [k for k in flat_list if c in k]
word_dist = nltk.FreqDist(filtered_strings)
most_common_words = pd.DataFrame(word_dist.most_common(1000), columns=['Word', 'Frequency'])
print(most_common_words)
all_words = pd.DataFrame(filtered_strings)

# save to file
most_common_words.to_csv(r'results/most_common_words_'+c+'.csv', index=False)
all_words.to_csv(r'results/all_words_'+c+'.csv', index=False)


# manually pick most common words...

# plot results
