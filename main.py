"""
Name: Julia Anantchenko
Class: 1026A - Computer Science Fundamentals I
Teacher: Michael A. Bauer
Date: November 13th 2019
Program Description: Analyzes Twitter information.
"""

# import statement
from sentiment_analysis import compute_tweets

# prompts user for tweet and key file names
tweet = input("What is the name of the tweet file?")
keyword = input("What is the name of the keyword file?")

# computes results
results = compute_tweets(tweet, keyword)

# prints Eastern data
print("\nEASTERN:")
print("Happiness Score:", results[0][0])
print("Number of Tweets with Keywords:", results[0][1])
print("Total Number of Tweets in Timezone:", results[0][2])

# prints Central data
print("\nCENTRAL:")
print("Happiness Score:", results[1][0])
print("Number of Tweets with Keywords:", results[1][1])
print("Total Number of Tweets in Timezone:", results[1][2])

# prints Mountain data
print("\nMOUNTAIN:")
print("Happiness Score:", results[2][0])
print("Number of Tweets with Keywords:", results[2][1])
print("Total Number of Tweets in Timezone:", results[2][2])

# prints Pacific data
print("\nPACIFIC:")
print("Happiness Score:", results[3][0])
print("Number of Tweets with Keywords:", results[3][1])
print("Total Number of Tweets in Timezone:", results[3][2])
