#------------------------------------------------------------------------------#
""" Information:
Possible tests: [load_file, summary, caesar_cipher, most_freq_word, summary_plot, save_tweets]
Example call: python grader.py --input NYThealth_tweets.txt --test caesar_cipher

If you want to use the grade for testing, be aware that the PA_TweetAnalyzer
script have to be located in the same directory as the grader.
"""
import os.path

#------------------------------------------------------------------------------#
# Import PA_TweetAnalyzer
import PA_TweetAnalyzer as api
#from PA_TweetAnalyzer import load_file
# Import libraries
import argparse
import importlib
import unidecode

##-----------------------------------##
##           Preprocessing           ##
##-----------------------------------##
# Implement Argument Parser
parser = argparse.ArgumentParser(description="Grader for the Tweet Analyzer")
# Add arguments to the Argument Parser
parser.add_argument("--db", action="store", dest="db", type=str,
                    default="NYThealth_tweets.txt")
parser.add_argument("--test", action="store", dest="test", type=str,
                    default="load_file")
# Parse arguments
args = parser.parse_args()



# Load database
db = api.load_file(args.db)

# Define an output function for Tweets
def output(tweet_list):
    for tweet in tweet_list:
        print(str(tweet.id) + "\t" + str(tweet.date_time) + "\t" + str(tweet.text))

##-----------------------------------##
##              Checks               ##
##-----------------------------------##
# Check file loading function
if args.test == "load_file":
    output(db)

# Check summary function
elif args.test == "summary":
    api.summary(db[10:1234])

# Check caesar cipher function
elif args.test == "caesar_cipher":
    for i in range(501, 1980):
        # Remove accents for simplification
        tweet_orginal_text = db[i].text
        db[i].text = unidecode.unidecode(db[i].text)
        db[i].text = db[i].text.replace("'", "")
        db[i].text = db[i].text.replace("’", "")
        # Perform caesar cipher testing
        shift = i % 26
        text_original = db[i].text
        # Encode a tweet list with the single tweet i
        tweet_encoded = api.caesar_cipher([db[i]], shift)[0]
        text_encoded = tweet_encoded.text
        # Decode again the same tweet with the negative shift
        tweet_decoded = api.caesar_cipher([tweet_encoded], -shift)[0]
        text_decoded = tweet_decoded.text
        # Output results
        print("Original: " + text_original)
        print("Encoded: " + text_encoded)
        print("Decoded: " + text_decoded)
        print("Is original and decoded the same: " + str(text_original == text_decoded))
        # Add accents again to original tweet text
        db[i].text = tweet_orginal_text

# Check most frequent word function
elif args.test == "most_freq_word":
    subset_db = db[10:900]
    word, freq = api.most_freq_word(subset_db)
    print("Most frequent word: " + "'" + word + "'")
    print("Frequency: " + str(freq))

# Check summary plot function
elif args.test == "summary_plot":
    api.summary_plot(db)

# Check save tweets function
elif args.test == "save_tweets":
    api.save_tweets("tweet_db.txt", db[104:1714])
    with open("tweet_db.txt", "r", encoding="utf-8") as reader:
        txt = reader.read()
        print(txt)
