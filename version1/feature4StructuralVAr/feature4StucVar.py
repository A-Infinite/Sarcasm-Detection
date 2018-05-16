#sarcasm as written form of expression : structural variation
import io
import sys

from nltk.tag import pos_tag
import nltk
import os,csv

def structuralVariations(tweet):    
    words = nltk.tokenize.word_tokenize(tweet)
    tag = pos_tag(words)
    count = 0
    pronounfeatures = [0,0,0,0]
    #intensifierfeatures = [0,0]
    f5 = []
    #lexical density to include nouns, verbs, adjectives, adverbs)
    for li1 in range(len(tag)):
        lexicallist = ['NN','NNS','NNP','NNPS','VB','VBD','VBG','VBN','VBP','VBZ','RB','RBR','RBS','WRB','JJ','JJR','JJS']
        if(tag[li1][1] in lexicallist):
            count+=1
        elif tag[li1][1] == 'PRP': 
        #personal pronoun singular : i,he she,
            pronounfeatures[0] += 1
        elif tag[li1][1] == 'PRP$':
            #possessive pronoun : my,his,hers
            pronounfeatures[1] += 1
        elif tag[li1][1] == 'WP':
            #wh pronoun : who, what
            pronounfeatures[2] += 1
        elif tag[li1][1] == 'WP$':
            #possessive wh pronoun : whose
            pronounfeatures[3] += 1


        #if (tag[li1][0] == "so"):
        #    intensifierfeatures[0] += 1
        #elif tag[li1][0] == "very":
        #    intensifierfeatures[1] += 1
        #elif tag[li1][0] == "too":
        #    intensifierfeatures[1] += 1
        #elif tag[li1][0] == "really":
        #    intensifierfeatures[1] += 1

    lexicaldensity = count / len(words)
    f5 += pronounfeatures
    #f5 += intensifierfeatures
    f5.append(lexicaldensity)
    return f5

def writeFile(folder,csvfile,label):
    ctr =1
    f5 = csv.writer(csvfile,delimiter=",")
    for f in sorted(os.listdir(folder)):
        print(ctr)
        inputFile = open(os.path.join(folder,f),"r")
        reader= list(csv.reader(inputFile))
        tweet = reader[1][2]
        features = structuralVariations(tweet)
        features.append(label)
        f5.writerow(features)
        inputFile.close()
        ctr=ctr+1

def main():
    pwd = os.getcwd()
    norm = pwd + "/../dataset/normal_with_past_PP"
    sarc = pwd + "/../dataset/sarcastic_with_past_PP"
    csvfile = open("feature4StrucVar.csv","a")
    writeFile(norm,csvfile,0)
    writeFile(sarc,csvfile,1)
    csvfile.close()


if __name__=="__main__":
    main()
