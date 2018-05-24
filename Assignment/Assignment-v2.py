def PrintDictionary(dictionary):
    for key in dictionary.keys():
        print("Printing information for", key)
        print("Following:")
        print(dictionary[key][0])
        print("Tweets:")
        print(dictionary[key][1])
        print("Count of followed users:")
        print(dictionary[key][2])
        print("Count of tweets:")
        print(dictionary[key][3])
        print("Count of retweets:")
        print(dictionary[key][4])
        print("Count of tweets seen:")
        print(dictionary[key][5])
        print("\n \n \n")

def ReadFollowingFile(dictionary, file):
    for line in file:
        print("Reading follows.txt.")
        users = line.split(' ')
        #Clean up the array of newline character.
        users[-1] = users[-1].replace('\n', '')
        #Populate the dictionary.
        dictionary[users[0]] = [users[1:], [], len(users[1:]), 0, 0, 0]

    return dictionary

def ReadStreamFile(dictionary, file):
    tweets = []
    count = 0
    for line in file:
        print("Reading stream.txt.")
        count += 1
        tweets = line.split(' ')
        tweets[-1] = tweets[-1].replace('\n', '')

        if tweets[1] == "RT" or tweets[1] == "DM":
            tmpLst = [str(tweets[1]), str(tweets[2]), ' '.join(tweets[3:])]
            dictionary[tweets[0]][1].append(tmpLst)
            if tweets[1] == "RT":
                tmpString = tweets[2].replace('@', '')
                dictionary[tmpString][4] += 1
        else:
            tmpLst = [None, ' '.join(tweets[1:])]
            dictionary[tweets[0]][1].append(tmpLst)
#################################################################UPDATED###############################################################################
        if tweets[1] != "DM" and tweets[1] != "RT":
            for key in dictionary.keys():
                if tweets[0] in dictionary[key][0]:
                    dictionary[key][5] += 1
                for word in tweets[1:]:
                    if '@' in word:
                        word = ''.join([i for i in word if i.isalnum()])
                        if word == key:
                            dictionary[key][5] += 1
        elif tweets[1] == "RT":
            for key in dictionary.keys():
                if tweets[0] == dictionary[key][5]:
                    dictionary[key][5] += 1
                for word in tweets[2:]:
                    if '@' in word:
                        word = ''.join([i for i in word if i.isalnum()])
                        if word == key:
                            dictionary[key][5] += 1
        elif tweets[1] == "DM":
            for word in tweets[2:]:
                if '@' in word:
                    word = ''.join([i for i in word if i.isalnum()])    
                    dictionary[word][5] += 1
#################################################################UPDATED###############################################################################
    return dictionary

def CreateDictionary(dictionary, followFle, streamFle):
    dictionary = ReadFollowingFile(dictionary, followFle)
    dictionary = ReadStreamFile(dictionary, streamFle)
    return dictionary

def MostSocialUser(dictionary):
    count = 0
    for key in dictionary.keys():
        if dictionary[key][2] > count:
            count = dictionary[key][2]

    print("The most social user/s are:")
    for key in dictionary.keys():
        if dictionary[key][2] == count:
            print(key)

def MostTweets(dictionary):
    print("How many of the top tweeters would you like to see?")
    num = int(input())
    tmpLst = []
    
    for key in dictionary.keys():
        tmpLst.append(dictionary[key][3])
    tmpLst = sorted(set(tmpLst), reverse=True)

    if num > len(tmpLst):
        print("The number you inputted is longer than the list of top tweets. Printing the entire list from most tweets to least.")
        for index in tmpLst:
            for key in dictionary.keys():
                if dictionary[key][3] == index:
                    print(key)
    else:
        print("Printing the user/s with the most tweets.")
        count = 0
        while count < num:
            for key in dictionary.keys():
                if dictionary[key][3] == tmpLst[count]:
                    print(key, "has tweeted", tmpLst[count], "times.")
            count += 1

def MostQuoted(dictionary):
    print("How many of the top quoted users do you want to see?")
    num = int(input())
    tmpLst = []

    for key in dictionary.keys():
        tmpLst.append(dictionary[key][4])
    tmpLst = sorted(set(tmpLst), reverse=True)

    if num > len(tmpLst):
        print("The number you inputted is longer than the list of most RTs. Printing the entire list from most tweets to least.")
        for index in tmpLst:
            for key in dictionary.keys():
                if dictionary[key][4] == index:
                    print(key, "has been retweeted", index, "times.")
    else:
        print("Printing the users/s with the most RT's.")
        count = 0
        while count < num:
            for key in dictionary.keys():
                if dictionary[key][4] == tmpLst[count]:
                    print(key, "has been retweeted", tmpLst[count], "times.")
            count += 1

def MostSeenTweets(dictionary):
    print("How many users with the most seen tweets do you want to view?")
    num = int(input())
    tmpLst = []

    for key in dictionary.keys():
        tmpLst.append(dictionary[key][5])
    tmpLst = sorted(set(tmpLst), reverse=True)

    if num > len(tmpLst):
        print("The number you inputted is longer than the list of most seen tweets. Printing the entire list from most tweets to least.")
        for index in tmpLst:
            for key in dictionary.keys():
                if dictionary[key][5] == index:
                    print(key, "has seen", index, "tweets.")
    else:
        print("Printing the users/s with the most seen tweets.")
        count = 0
        while count < num:
            for key in dictionary.keys():
                if dictionary[key][5] == tmpLst[count]:
                    print(key, "has seen", tmpLst[count], "tweets.")
            count += 1

#Open the files that are going to be used.
followingFile = open("dummy-data-1/follows.txt", 'r')
streamFile = open("dummy-data-1/stream.txt", 'r')
#The main structure that we will hold all of the data in.
userDictionary = {}

userDictionary = CreateDictionary(userDictionary, followingFile, streamFile)
MostSocialUser(userDictionary)
MostTweets(userDictionary)
MostQuoted(userDictionary)
MostSeenTweets(userDictionary)
# for key in userDictionary.keys():
#     print(key, userDictionary[key][5])

#Close the files we were using.
followingFile.close()
streamFile.close()