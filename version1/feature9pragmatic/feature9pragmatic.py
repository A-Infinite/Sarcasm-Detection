import re
import os, csv
import nltk 
def get_pragmatic_features(tweet_tokens):
    capitalized_words = user_specific = intensifier = tweet_len_ch = 0
    negations=affirmatives=interjection=punct=0
    for t in tweet_tokens:
        tweet_len_ch += len(t)
        if t.isupper() and len(t) > 1:
            capitalized_words += 1       # count of capitalized words
        if t.startswith("@"):
            user_specific += 1          # count of user mentions
        if t.startswith("#"):
            user_specific += 1          # count-based feature of hashtags used (excluding sarcasm or sarcastic)
        if t.lower().startswith("haha") or re.match('l(o)+l$', t.lower()):
            user_specific += 1          # binary feature marking the presence of laughter
        if t in strong_negations:
            negations += 1           # count-based feature of strong negations
        if t in strong_affirmatives:
            affirmatives += 1           # count-based feature of strong affirmatives
        if t in interjections:
            interjection += 1           # count-based feature of relevant interjections
        if t in intensifiers:
            intensifier += 1           # count-based feature of relevant intensifiers
        if t in punctuation:
            punct += 1          # count-based feature of relevant punctuation signs
#        if t in emoji.UNICODE_EMOJI:
#           user_specific += 1          # count-based feature of emojis
    tweet_len_tokens = len(tweet_tokens)  # get the length of the tweet in tokens
    average_token_length = float(tweet_len_tokens) / max(1.0, float(tweet_len_ch))  # average tweet length
    feature_list = [tweet_len_ch,  tweet_len_tokens,  average_token_length, capitalized_words, user_specific, negations, affirmatives, interjection,  intensifier, punct]
    #print(feature_list)
    return feature_list



strong_affirmatives = ["yes", "yeah", "always", "all", "any", "every", "everybody", "everywhere", "ever"]
strong_negations = ["no", "not", "never", "none" "n't", "nothing", "neither", "nobody", "nowhere"]

punctuation = ["?", "!", "..."]

interjections = ["oh", "hey", "wow", "aha", "aham", "aw", "bam", "blah", "bingo", "boo", "bravo",
                 "cheers", "congratulations", "congrats", "duh", "eh", "gee", "gosh", "hey", "hmm",
                 "huh", "hurray", "oh", "oh dear", "oh my", "oh well", "oops", "ouch", "ow", "phew",
                 "shh", "uh", "uh-huh", "mhm", "ugh", "well", "wow", "woah", "yeah", "yep", "yikes", "yo"]

intensifiers = ["amazingly", "astoundingly", "awful", "bare", "bloody", "crazy", "dreadfully",
                "colossally", "especially", "exceptionally", "excessively", "extremely",
                "extraordinarily", "fantastically", "frightfully", "fucking", "fully", "hella",
                "holy", "incredibly", "insanely", "literally", "mightily", "moderately", "most",
                "outrageously", "phenomenally", "precious", "quite", "radically", "rather",
                "really", "remarkably", "right", "sick", "strikingly", "super", "supremely",
                "surprisingly", "terribly", "terrifically", "too", "totally", "uncommonly",
                "unusually", "veritable", "very", "wicked", "so" , "very"]

def writeFile(folder, csvfile,label):
    outfile = csv.writer(csvfile,delimiter=",")
    ctr=1
    for f in sorted(os.listdir(folder)):
    	print(ctr)
    	inputFile = open(os.path.join(folder,f),"r")
    	reader = list(csv.reader(inputFile))
    	#print(reader)
    	tweet = reader[1][2]
    	tweet =tweet.strip()
    	tokenizer = nltk.tokenize.TreebankWordTokenizer()
    	tweet_tokens=tokenizer.tokenize(tweet)
    	print(tweet_tokens)
    	feature_list=get_pragmatic_features(tweet_tokens)
    	feature_list.append(label)
    	outfile.writerow(feature_list)
    	ctr=ctr+1

def main():
    pwd = os.getcwd()
    norm = pwd + "/../newdatasetForF9/normal_with_past_PP"
    sarc = pwd + "/../newdatasetForF9/sarcastic_with_past_PP"
    csvfile = open("feature9pragmatic.csv","a")
    writeFile(norm,csvfile,0)
    writeFile(sarc,csvfile,1)
    csvfile.close()


if __name__=="__main__":
    main()