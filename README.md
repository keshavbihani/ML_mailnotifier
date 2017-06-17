# machinelearning_mailnotifier
This a desktop application which has used various techiques like nlp,machine learning,python etc .

Purpose of this project is to create a desktop notification app which will notify only those mails which are regarding my workplace rest all are not been notified to the user.

firstly i need to find a data best suitable for my classifier. so i find dataset from http://csmining.org/index.php/enron-spam-datasets.html which contained dataset for both ham and spam mails

The data is not good formt that classifier can learn and perform classification.So first i need to preprocess the data so that which can be best used for classifier.Cleansing1.py do all nlp processing using nltk libraby and nltk_data.Certain operations such as tokenization and stop word removal performed on that.Nedd to remove certain more characters to classify it based on workplace data or not

Then i implemented my own naive bayes classifier to give prediction in classifier.py.Which give pretty good prediction but need some more work.

regulartrigger.py file to search for latest mail updated mailbox and based on that mail data has been classified and notified.


