# -*- coding: utf-8 -*-

import re
#import sys
import csv
import os
import string
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords

def remove_punctuations(text_string):
        #defining a list of special characters to be used for text cleaning
        special_characters = [",",".","'",";","\n", "?", "!", ":", ")", "(", "@", "*", "{", "}", "#",":", "_", "+", "`", "~", "$", "%", "^", "&", "","<",">","=","`","\"","'"] 
        cleaned_string = str(text_string)
        # removing special character
        for ch in special_characters:
            cleaned_string = cleaned_string.replace(ch, "")
            #cleaned_string = cleaned_string.lower()
        return cleaned_string

def remove_stop_words(document):
        pwd = os.getcwd()
        words_file = pwd + "/stop_words.txt"
        stop_word_list = []
        stop_word_list = [word for line in open(words_file, 'r') for word in line.split(",")]
        cleaned_doc = []
        for term in document.split(" "):
            term = remove_punctuations(term)
            if term not in stop_word_list:
                cleaned_doc.append(term)
        return " ".join(cleaned_doc)

def stem(tweet):
    tweet = tweet.split()
    # wnl = WordNetLemmatizer()
    # tweet = [wnl.lemmatize(w) for w in tweet]
    stemmer = SnowballStemmer("english",ignore_stopwords=True)
    tweetr=[]
    for w in tweet:
        try:
          tweetr.append(stemmer.stem(w))  
        except:
          tweetr.append(w)    
    # tweet = [stemmer.stem(w) for w in tweet]
    return " ".join(tweetr)


def lemmatize_verbs(words):
    """Lemmatize verbs in list of tokenized words"""
    lemmatizer = WordNetLemmatizer()
    lemmas = []
    for word in words:
        lemma = lemmatizer.lemmatize(word, pos='v')
        lemmas.append(lemma)
    return "".join(lemmas)

def preprocess(tweet):
    tweet = tweet.replace("#Sarcastic","")           #Removes the sarcasm hashtag
    tweet = tweet.replace("#sarcastic","")
    tweet = tweet.replace("#Sarcasm","")             #Removes the sarcasm hashtag
    tweet = tweet.replace("#sarcasm","")
    tweet = tweet.replace("#not","")
    tweet = re.sub(r"(?<=^|(?<=[^a-zA-Z0-9-_\.]))@([A-Za-z]+[A-Za-z0-9]+)", "", tweet)      #Removes mentions
    tweet = re.sub(r'(https?|ftp)://[^\s/$.?#].[^\s]*', '', tweet, flags=re.MULTILINE)      #Removes URL
    tweet = remove_punctuations(tweet)
    tweet = remove_stop_words(tweet)
#    tweet = stem(tweet)
    tweet = lemmatize_verbs(tweet)
    return tweet


def main():
    #sys.setdefaultencoding('utf8')   => it's usage is discouraged.
    pwd = os.getcwd();
    norm_in = pwd + "/dataset/normal_with_past"
    norm_out = pwd + "/dataset/normal_with_past_PP"
    sarc_in = pwd + "/dataset/sarcastic_with_past"
    sarc_out = pwd + "/dataset/sarcastic_with_past_PP"
    
    # preprocessing normal tweets
    for f in os.listdir(norm_in):
        inputFile = open(os.path.join(norm_in,f),"r")
        outputFile = open(os.path.join(norm_out,f),"w")
        reader=csv.reader(inputFile)
        writer=csv.writer(outputFile)
        for row in reader:
            row[2]=preprocess(row[2])
            writer.writerow(row)
        inputFile.close()
        outputFile.close()

    # preprocessing sarcastic tweets
    for f in os.listdir(sarc_in):
        inputDest = os.path.join(sarc_in,f)
        outputDest = os.path.join(sarc_out,f)
        inputFile = open(inputDest,"r")
        outputFile = open(outputDest,"w")
        reader=csv.reader(inputFile)
        writer=csv.writer(outputFile)
        for row in reader:
            row[2]=preprocess(row[2])
            writer.writerow(row)
        inputFile.close()
        outputFile.close()




if __name__=="__main__":
    main()