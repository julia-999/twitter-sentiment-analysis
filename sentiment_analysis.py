"""
Name: Julia Anantchenko
Class: 1026A - Computer Science Fundamentals I
Teacher: Michael A. Bauer
Date: November 13th 2019
Program Description: Performs simple sentiment analysis on Twitter data.
"""

# import statement
from string import punctuation

# constants for location coordinates provided by assignment
TOP_LAT = 49.189787
BOT_LAT = 24.660845
P1_LONG = -67.444574
P3_LONG = -87.518395
P5_LONG = -101.998892
P7_LONG = -115.236428
P9_LONG = -125.242264

# list for the keywords
key_rows = []


# function run by main, computes the data
def compute_tweets(tweet_file, keyword_file):

    # opens files, returns empty list if there is an error
    try:
        tweet = open(tweet_file, "r", encoding="utf-8")
        key = open(keyword_file, "r", encoding="utf-8")
    except IOError:
        print("File cannot be found.")
        return [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)]

    # lists for tweets of each location
    eastern = []
    central = []
    mountain = []
    pacific = []

    # adds entries to a list which consist of the keywords and their appropriate scores
    for line in key:
        key_rows.append(line.strip().split(","))

    # for loop that sorts the tweet into the appropriate location
    for line in tweet:

        # creates a list of each word in the line
        tweet_words = line.split()

        # removes the punctuation from the ends of each word
        for i in range(len(tweet_words)):
            tweet_words[i] = tweet_words[i].lower().strip("[,]")
            if i > 1:
                tweet_words[i] = tweet_words[i].lower().strip(punctuation)

        # determines the location of the tweet
        location = determine_location(float(tweet_words[0]), float(tweet_words[1]))

        # sorts the tweet in the appropriate list
        if location == "eastern":
            eastern.append(tweet_words)
        elif location == "pacific":
            pacific.append(tweet_words)
        elif location == "central":
            central.append(tweet_words)
        elif location == "mountain":
            mountain.append(tweet_words)

    # calculates data for each location
    eastern_data = calc_loc_totals(eastern)
    central_data = calc_loc_totals(central)
    mountain_data = calc_loc_totals(mountain)
    pacific_data = calc_loc_totals(pacific)

    # closes files
    tweet.close()
    key.close()

    # resets key_rows
    key_rows.clear()

    # returns the data in a list of tuples
    return [eastern_data, central_data, mountain_data, pacific_data]


# counts the total score of keywords in one tweet line
def count_keyword_match(words):

    # variables for sentiment and keywords
    total_sentiment = 0
    num_keywords = 0

    # for loop that compares the key and the tweet
    for i in range(len(words)):
        for j in range(len(key_rows)):

            # checks if they match
            if key_rows[j][0] == words[i]:

                # counts the total score and amount of keywords
                total_sentiment += int(key_rows[j][1])
                num_keywords += 1

    # returns the happiness score if there are keywords
    if num_keywords != 0:
        return total_sentiment/num_keywords

    # returns 0 if no keywords
    return 0


# calculates all of the sentiment data per location: happiness score, total with keywords and total tweets
def calc_loc_totals(loc_lines):

    # variables for tweet data
    count_of_keyword_tweets = 0
    total_happiness_score = 0
    count_of_tweets = len(loc_lines)

    # for loop that counts the total happiness score and amount of keyword tweets
    for i in range(count_of_tweets):
        score = count_keyword_match(loc_lines[i])
        if score != 0:
            count_of_keyword_tweets += 1
            total_happiness_score += score

    # calculates the average score and returns the data
    if count_of_keyword_tweets != 0:
        return total_happiness_score/count_of_keyword_tweets, count_of_keyword_tweets, count_of_tweets

    # returns 0 for the average if no keyword tweets to prevent dividing by 0 error
    return 0, 0, count_of_tweets


# determines the location of the tweet
def determine_location(lat, long):

    # finds location based on coordinates
    if BOT_LAT <= lat <= TOP_LAT:
        if P1_LONG >= long > P3_LONG:
            return "eastern"
        elif P3_LONG >= long > P5_LONG:
            return "central"
        elif P5_LONG >= long > P7_LONG:
            return "mountain"
        elif P7_LONG >= long >= P9_LONG:
            return "pacific"

    # returns nothing if no location match
    return ""
