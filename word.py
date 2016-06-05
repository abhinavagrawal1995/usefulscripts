#Because I'm lazy. Simply opens links to vocabulary.com and mnemonic dictionary for the word given as command line argument
import os
import sys
word=sys.argv[1]
os.system("google-chrome http://www.mnemonicdictionary.com/?word="+word)
os.system("google-chrome https://www.vocabulary.com/dictionary/"+word)
