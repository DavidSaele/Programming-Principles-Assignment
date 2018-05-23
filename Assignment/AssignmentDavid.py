
def ReadFollowingFile(dictionary, file):
    for line in file:
        users = line.split(' ')
        # Clean up the array of newline character.
        users[-1] = users[-1].replace('\n', '')
        # Populate the dictionary.
        dictionary[users[0]] = [users[1:], [], len(users[1:]), 0, 0, 0]

    return dictionary


def ReadStreamFile(dictionary, file):
    tweets = []
    count = 0
    for line in file:
        count += 1
        tweets = line.split(' ')
        tweets[-1] = tweets[-1].replace('\n', '')

        # This loop gives the user which is mentioned
        for word in tweets[1:]:
            if '@' in word:
                word = word[1:]
                if word in dictionary.keys():
                    dictionary[word][5] += 1

        #This loop is if they are a follower
        for key in dictionary.keys():
            if tweets[0] in dictionary[key][0]:
                dictionary[key][5] += 1

        if tweets[1] == "RT" or tweets[1] == "DM":
            tempList = [str(tweets[1]), str(tweets[2]), ' '.join(tweets[3:])]
            dictionary[tweets[0]][1].append(tempList)
            if tweets[1] == "RT":
                tempString = tweets[2].replace('@', '')
                dictionary[tempString][4] += 1
        else:
            tempList = [None, ' '.join(tweets[1:])]
            dictionary[tweets[0]][1].append(tempList)

    for key in dictionary.keys():
        count = 0
        for tweet in dictionary[key][1]:
            if tweet[0] == None or tweet[0] == "DM":
                count += 1
        dictionary[key][3] = count

    return dictionary


def CreateDictionary(dictionary, followFle, streamFle):
    dictionary = ReadFollowingFile(dictionary, followFle)
    dictionary = ReadStreamFile(dictionary, streamFle)
    return dictionary


def MostSocialUser(dictionary):
    count = 0
    tempList = []
    for key in dictionary.keys():
        if dictionary[key][2] > count:
            count = dictionary[key][2]

    print("The most social user/s are:")
    for key in dictionary.keys():
        if dictionary[key][2] == count:
            tempList.append(key)

    tempList = sorted(tempList)
    for key in tempList:
        print(key)


def MostTweets(dictionary):
    print("How many of the top tweeters would you like to see?")
    num = int(input())
    tempList = []

    for key in dictionary.keys():
        tempList.append(dictionary[key][3])
    tempList = sorted(set(tempList), reverse=True)

    if num > len(tempList):
        print(
            "The number you inputted is longer than the list of top tweets. Printing the entire list from most tweets to least.")
        for index in tempList:
            for key in dictionary.keys():
                if dictionary[key][3] == index and index != 0:
                    print(index, key)
    else:
        print("Printing the user/s with the most tweets.")
        count = 0
        while count < num:
            for key in dictionary.keys():
                if dictionary[key][3] == tempList[count]:
                    print(index, key, "has tweeted", tempList[count], "times.")
            count += 1


def MostQuoted(dictionary):
    print("How many of the top quoted users do you want to see?")
    num = int(input())
    tempList = []

    for key in dictionary.keys():
        tempList.append(dictionary[key][4])
    tempList = sorted(set(tempList), reverse=True)

    if num > len(tempList):
        print(
            "The number you inputted is longer than the list of most RTs. Printing the entire list from most tweets to least.")
        for index in tempList:
            for key in dictionary.keys():
                if dictionary[key][4] == index and index != 0:
                    print(index, key)
    else:
        print("Printing the users/s with the most RT's.")
        count = 0
        while count < num:
            for key in dictionary.keys():
                if dictionary[key][4] == tempList[count]:
                    print(tempList[count], key)
            count += 1


def MostSeenTweets(dictionary):
    print("How many users with the most seen tweets do you want to view?")
    num = int(input())
    tempList = []

    for key in dictionary.keys():
        tempList.append(dictionary[key][5])
    tempList = sorted(set(tempList), reverse=True)

    if num > len(tempList):
        print(
            "The number you inputted is longer than the list of most seen tweets. Printing the entire list from most tweets to least.")
        for index in tempList:
            for key in dictionary.keys():
                if dictionary[key][5] == index:
                    print(index, key)
    else:
        print("Printing the users/s with the most seen tweets.")
        count = 0
        while count < num:
            for key in dictionary.keys():
                if dictionary[key][5] == tempList[count]:
                    print(tempList[count], key)
            count += 1


# Open the files that are going to be used.
followingFile = open("dummy-data-1/follows.txt")
streamFile = open("dummy-data-1/stream.txt")
# The main structure that we will hold all of the data in.
userDictionary = {}

userDictionary = CreateDictionary(userDictionary, followingFile, streamFile)
MostSocialUser(userDictionary)
MostTweets(userDictionary)
MostQuoted(userDictionary)
MostSeenTweets(userDictionary)

# Close the files we were using.
followingFile.close()
streamFile.close()