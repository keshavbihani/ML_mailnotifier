from cleansing1 import *
from mailsnotifier import *
import pynotify

#used to notify is the mail is more related to my workplace
def sendmessage(title, message):

    pynotify.init("Test")

    notice = pynotify.Notification(title, message)

    notice.show()

    return

#self implemented bayes classifier to clasify between workplace mail and spam mail
def classify(mes, training_set, prior=0.5, c=3.7e-4):

    msg_terms = removestop(mes)

    msg_prob = 1

    for term_data in msg_terms:

        if term_data in training_set:

            msg_prob *= training_set[term_data]

        else:

            msg_prob *= c

    return msg_prob * prior




def checkforspam():

    mail_msg = getmailbody()

    spam_prob = classify(mail_msg[1], spam_training_set, 0.2)

    ham_prob = classify(mail_msg[1], ham_training_set, 0.8)

    if spam_prob > ham_prob:

       print('classified as SPAM.')
    else:

        sendmessage(mail_msg[0],mail_msg[1])

    return 1;


#p=checkforspam('need to complete this task')