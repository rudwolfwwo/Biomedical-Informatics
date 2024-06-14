import os
import re
import matplotlib.pyplot as plt


class Tweet:
    def __init__(self,id,date_time,text):
        self.id = id
        self.date_time = date_time
        self.text = text

def load_file(path):
    tweet_list = []
    if not os.path.exists(path):
        print("Error: Shutting down")
        quit()
    with open(path, "r",encoding="utf-8") as file: #"r",encoding="utf-8"
        for text in file.read().split("\n"): #.read().decode("utf-8").split("\n")
            full_tweet = text.split("|")
            if len(full_tweet) < 3:
                print("Error: Shutting down")
                quit()
            tweet = Tweet(full_tweet[0],full_tweet[1],full_tweet[2])
            tweet_list.append(tweet)
    return tweet_list


def summary(tweet_list):
    print("Number of Tweets: ",len(tweet_list))
    first_tweet_date = tweet_list[-1].date_time.split(" ")
    last_tweet_date = tweet_list[0].date_time.split(" ")
    print("First Tweet Date: " + first_tweet_date[3] +
          " " + first_tweet_date[2] + " " + first_tweet_date[1] + " " + first_tweet_date[5])

    print("Last Tweet Date: " + last_tweet_date[3] +
          " " + last_tweet_date[2] + " " + last_tweet_date[1] + " " + last_tweet_date[5])
    sum = 0
    for tweet in tweet_list:
        sum += len(str(tweet.text))
    print("Overall number of characters: ", sum)
    print("Average number of characters per Tweet: ",round(sum/len(tweet_list),2))


def caesar_cipher(tweet_list,shift):
    alphabet_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    alphabet_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    tweet_encoded = []
    for tweet in tweet_list:
        new_tweet = Tweet(tweet.id,tweet.date_time,"")
        for char in tweet.text:
            if char.isupper():
                new_tweet.text += alphabet_upper[(alphabet_upper.index(char) + shift) % len(alphabet_upper)]
            elif char.islower():
                new_tweet.text += alphabet_lower[(alphabet_lower.index(char) + shift) % len(alphabet_lower)]
            else:
                new_tweet.text += char
        tweet_encoded.append(new_tweet)
    return tweet_encoded


def most_freq_word(tweet_list):
    dict = {}
    for tweet in tweet_list:
        text_wo_link = tweet.text.split("http")[0]
        word = "^[A-Za-z]+|[^A-Za-z][A-Za-z]+|[^A-Za-z][A-Za-z]+$"
        most_freq_word = ""
        for w in re.findall(word,text_wo_link):
            extracted_word = re.search("[A-Za-z]+",w).group()
            most_freq_word = extracted_word
            if extracted_word not in dict:
                dict[extracted_word] = 1
            else:
                dict[extracted_word] += 1
        for d in dict:
            if dict[most_freq_word] < dict[d]:
                most_freq_word = d
    return most_freq_word,dict[most_freq_word]


def summary_plot(tweet_list):
    plt.title("Number of Tweets course throughout the day")
    plt.xlabel("Daytime bins")
    plt.ylabel("Number of Tweets")
    hours = []
    for tweet in tweet_list:
        hours.append(int(tweet.date_time.split(" ")[3].split(":")[0]))
    plt.hist(hours,bins=24)

    plt.savefig("tweet_figure.png")
    plt.show()

def save_tweets(path,tweet_list):
    try:
        with open(path,"w",encoding="utf-8") as file:
            for tweet in tweet_list:
                file.write(tweet.id + "|" + tweet.date_time + "|" + tweet.text + "\n")
    except:
        print("Error: Shutting down")
        quit()
