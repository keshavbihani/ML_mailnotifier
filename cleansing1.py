from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from os import listdir
from os.path import isfile, join
"""
nlp techniques used to clean data and make data a good readable for computer to
use it as a learning in my machine learning algorithm
"""

spamPath="G:\data\spam\\"
hamPath="G:\data\ham\\"
stopword=stopwords.words('english')
#print(stopword)

#used to clean not required words from the training data to check for result
def removestop(data):
    list=set(word_tokenize(data.replace('=\\n', '').lower()))

   # print(len(list))

    finallist=[word for word in list if word not in stopword and (word.isalpha() and word not in ('http','www','Subject: '))]

 #   print(len(finallist))

    return finallist

#extract mails from all text files based
def getData(allmails):

    maildata=''

    with open(allmails,'r',encoding="Latin-1") as data:

        for line in data:

            maildata+=line

    return maildata


def form_training_data(path):
    finaldict={}

    allmails=[]
    for mails in listdir(path):

        if isfile(join(path,mails)):

           allmails.append(mails)
    final_set=[]

    for mail in allmails:

        all_data_from_mail=getData(path+mail)

        #print(all_data_from_mail)

        final_set=removestop(all_data_from_mail)
        #generate a frequency distribution of all mails based in both ham and spam classes
        for str in final_set:

            if str not in finaldict:

                finaldict[str]=1

            else:

                finaldict[str]= finaldict[str] + 1


    return finaldict



spam_training_set = form_training_data(spamPath)

ham_training_set = form_training_data(hamPath)
