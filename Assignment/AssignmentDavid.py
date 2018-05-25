
# A function that reads the file called follows.txt, splits the lines into users and create a dictionary with user as
# key and the value as a list of the users he/she follows, an empty list that later is filled with each tweets for
# every user, the length of how many users he/she follows, a count for how many tweets each user has, a count for how
# many times each user is quoted and a count for how many tweets each user can see.

def ReadFollowingFile(dictionary, file):

    # The for loop reads through the whole file and divide it into users by splitting it for each space.
    for line in file:
        users = line.split(' ')
        # \n is replaced with nothing to clean up the array of newline character.
        users[-1] = users[-1].replace('\n', '')
        # Populate the dictionary.
        dictionary[users[0]] = [users[1:], [], len(users[1:]), 0, 0, 0]

    return dictionary

# This function reads the file called stream.txt and seperate each line into a user and a tweet. It checks if the
# tweet is a RT or DM, and enter all tweets into the dictionary for each user. It also counts the amount of tweets
# each user has, how many times each user has been retweeted and how many tweets each user can see.

def ReadStreamFile(dictionary, file):
    tweets = []
    count = 0

    # This for loop splits the words for every space in each line.
    for line in file:
        count += 1
        tweets = line.split(' ')
        # \n is replaced with nothing to clean up the array of newline character.
        tweets[-1] = tweets[-1].replace('\n', '')

        # This code checks if the tweet is a RT or DM. It then enter the tweets for every user into the dictionary
        if tweets[1] == "RT" or tweets[1] == "DM":
            tempList = [str(tweets[1]), str(tweets[2]), ' '.join(tweets[3:])]
            dictionary[tweets[0]][1].append(tempList)

            # This if statement checks if the tweet is a RT and increment the number for how many times each user
            # has been quoted.
            if tweets[1] == "RT":
                tempString = tweets[2].replace('@', '')
                dictionary[tempString][4] += 1

        # The else statement enters the tweets for every user into the dictionary
        else:
            tempList = [None, ' '.join(tweets[1:])]
            dictionary[tweets[0]][1].append(tempList)

        # If a user is mentioned in a tweet, this loop returns the username without the @ and increment the count for
        # how many tweets each user can see.
        for word in tweets[1:]:
            if '@' in word:
                word = word[1:]
                if word in dictionary.keys():
                    dictionary[word][5] += 1

        # This for loop increment the count for how many tweets each user can see by checking who they follow.
        for key in dictionary.keys():
            if tweets[0] in dictionary[key][0]:
                dictionary[key][5] += 1

    # This for loop increment the number of how many times each user has tweeted, not counting the RT.
    for key in dictionary.keys():
        count = 0
        for tweet in dictionary[key][1]:
            if tweet[0] == None or tweet[0] == "DM":
                count += 1
        dictionary[key][3] = count

    return dictionary


# A function which takes the followfile and streamfile and populate the userDictionary by using the ReadFollowingFile
# and the ReadStreamFile function and enter all the data into one dictionary.

def CreateDictionary(dictionary, followFle, streamFle):
    dictionary = ReadFollowingFile(dictionary, followFle)
    dictionary = ReadStreamFile(dictionary, streamFle)
    return dictionary

# A function which prints the most social user by name sorted in lexicographical order.

def MostSocialUser(dictionary):
    count = 0
    tempList = []

    # A for loop which checks from the userDictionary the number of how many users each user follows and compare it
    # with the count. Everytime the for loop finds a number which is higher than count, that number will become the
    # count. After the loop have gone through the whole dictionary, the count will be the user who follows the most
    # people.
    for key in dictionary.keys():
        if dictionary[key][2] > count:
            count = dictionary[key][2]

    print("The most social user/s are:")

    # If multiple users has the same amount of people they follow, both will be printed as output. The if statement
    # appends the second one to the first one.
    for key in dictionary.keys():
        if dictionary[key][2] == count:
            tempList.append(key)

    # A loop which prints the username of the most social user and sort it in lexicographical order.
    tempList = sorted(tempList)
    for key in tempList:
        print(key)

# A function which prints the top n user/s with the most tweets and how many tweets it has.

def MostTweets(dictionary):
    print("How many of the top tweeters would you like to see?")
    n = int(input())
    tempList = []

    # A for loop which update the tempList and sort the results with those who have the most tweets to those who have
    # the least. It uses the userDictionary value which counts how many tweets each user has.
    for key in dictionary.keys():
        tempList.append(dictionary[key][3])
    tempList = sorted(set(tempList), reverse=True)

    # If the top n user is more than the number of users, this will run.
    if n > len(tempList):
        print("The number you inputted is longer than the list of top tweets. Printing the entire list from most "
              "tweets to least.")

        # This for loop print every user and how many tweets they have from those who have the most til those with
        # the least. If the user doesn't have any tweets, it will not be printed.
        for index in tempList:
            for key in dictionary.keys():
                if dictionary[key][3] == index and index != 0:
                    print(index, key)

    # If the top n user is less than the amount of users, this will run.
    else:
        print("Printing the user/s with the most tweets.")
        count = 0

        # This while loop prints the number of tweets each user has from the most to the least until n is equal to
        # the count.
        while count < n:
            for key in dictionary.keys():
                if dictionary[key][3] == tempList[count] and tempList[count] != 0:
                    print(tempList[count], key)
            count += 1

# A function which prints the top n user/s which has been retweeted the most and how many times that has occured.

def MostQuoted(dictionary):
    print("How many of the top quoted users do you want to see?")
    n = int(input())
    tempList = []

    # A for loop which update the tempList and sort the results with those who have been quoted the most to those who
    # have been quoted the least. It uses the userDictionary value which counts how many times each user has been
    # quoted.
    for key in dictionary.keys():
        tempList.append(dictionary[key][4])
    tempList = sorted(set(tempList), reverse=True)

    # If the top n user is more than the number of users, this will run.
    if n > len(tempList):
        print("The number you inputted is longer than the list of most RTs. Printing the entire list from most "
              "tweets to least.")

        # This for loop print every user and how many times they have been quoted from those who have been the most
        # til those who have been the least. If the user doesn't have any tweets, it will not be printed.
        for index in tempList:
            for key in dictionary.keys():
                if dictionary[key][4] == index and index != 0:
                    print(index, key)

    # If the top n user is less than the amount of users, this will run.
    else:
        print("Printing the users/s with the most RT's.")
        count = 0

        # This while loop prints the number of how many times each user has been qouted from the most to the least
        # until n is equal to the count.
        while count < n:
            for key in dictionary.keys():
                if dictionary[key][4] == tempList[count] and tempList[count] != 0:
                    print(tempList[count], key)
            count += 1

# A function which prints the top n user/s which has can see the most tweets and how many tweets they can see.

def MostSeenTweets(dictionary):
    print("How many users with the most seen tweets do you want to view?")
    n = int(input())
    tempList = []

    # A for loop which update the tempList and sort the results with those who have seen the most tweets to those who
    # have seen the least. It uses the userDictionary value which counts how many tweets each user can see.
    for key in dictionary.keys():
        tempList.append(dictionary[key][5])
    tempList = sorted(set(tempList), reverse=True)

    # If the top n user is more than the number of users, this will run.
    if n > len(tempList):
        print("The number you inputted is longer than the list of most seen tweets. Printing the entire list from "
              "most tweets to least.")

        # This for loop print every user and how many tweets they can see from those who have seen the most til those
        # who can see the least. If the user doesn't have any tweets, it will not be printed.
        for index in tempList:
            for key in dictionary.keys():
                if dictionary[key][5] == index and index != 0:
                    print(index, key)

    # If the top n user is less than the amount of users, this will run.
    else:
        print("Printing the users/s with the most seen tweets.")
        count = 0

        # This while loop prints the number of tweets each user can see from the most to the least until n is equal to
        # the count.
        while count < n:
            for key in dictionary.keys():
                if dictionary[key][5] == tempList[count] and tempList[count] != 0:
                    print(tempList[count], key)
            count += 1


# Open the files that are going to be used.
followingFile = open("large-data-1/follows.txt")
streamFile = open("large-data-1/stream.txt")
# The main structure that we will hold all of the data in.
userDictionary = {}

# This code creates the userDictionary and runs each function sorted by task.
userDictionary = CreateDictionary(userDictionary, followingFile, streamFile)
# Task 1, prints the most social user
MostSocialUser(userDictionary)
# Task 2, after entering the n number the viewer wants to see, this function will give the users with the most tweets.
MostTweets(userDictionary)
# Task 3, after entering the n number the viewer wants to see, this function will give the users who have been quoted
# the most.
MostQuoted(userDictionary)
# Task 4, after entering the n number the viewer wants to see, this function will give the users who have seen the
# most tweets.
MostSeenTweets(userDictionary)

