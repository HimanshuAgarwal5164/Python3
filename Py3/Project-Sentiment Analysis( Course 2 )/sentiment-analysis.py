'''
Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is.
You will create a csv file, which contains columns for the-
                                                            Number of Retweets,
                                                            Number of Replies,
                                                            Positive Score (which is how many happy words are in the tweet),
                                                            Negative Score (which is how many angry words are in the tweet),
                                                            Net Score for each tweet.
At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.
'''


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(s):
    s1=""
    for x in s:
        if x not in punctuation_chars:
            s1=s1+x
    return s1

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(s):
    s=strip_punctuation(s)
    words=s.split()
    c=0
    for x in words:
        if x.lower() in positive_words:
            c=c+1
    return c

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(s):
    s=strip_punctuation(s)
    words=s.split()
    c=0
    for x in words:
        if x.lower() in negative_words:
            c=c+1
    return c

fhand=open('project_twitter_data.csv','r')
l1=fhand.readlines()
lines=l1[1:]
fhand.close()
fhand2=open('resulting_data.csv','w')
fhand2.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score\n')
for line in lines:
    line=line.strip()
    l=line.split(',')
    text=l[0]
    text=strip_punctuation(text)
    retweets=(l[1])
    replies=(l[2])
    pos=get_pos(text)
    neg=get_neg(text)
    net=pos-neg
    s=retweets+', '+replies+', '+str(pos)+', '+str(neg)+', '+str(net)+'\n'
    fhand2.write(s)
fhand2.close()


