file = open("dummy-data-1/follows.txt")

user_dict = {}

# A for loop that reads in users into a dictionary where the username is the key and the value is their tweeting information

for line in file:
    users = line.split(" ")
    user_dict[users[0].replace("\n","")] = [users[1:], [None, None, []], len(users[1:]), 0]
    for i in range(0, len(user_dict[users[0].replace("\n","")][0])):
        user_dict[users[0].replace("\n","")][0][i] = user_dict[users[0].replace("\n","")][0][i].replace("\n","")

stream = open("dummy-data-1/stream.txt")

for line in stream:
    tweets = line.split(" ")
    if tweets[1] == "RT" or tweets[1] == "DM":
        user_dict[tweets[0].replace("\n","")][1][0] = tweets[1]
        user_dict[tweets[0].replace("\n", "")][1][1] = tweets[2]
        st = ' '.join(tweets[3:])
        user_dict[tweets[0].replace("\n", "")][1][2].append(st)
    else:
        str = ' '.join(tweets[1:])
        user_dict[tweets[0].replace("\n","")][1][2].append(str)


for user in user_dict.keys():
    if user_dict[user][1][0] is not "RT" and user_dict[user][1][0] is not "DM":
        user_dict[user][3] = len(user_dict[user][1][2])

def find_popular(dict, type, n):
    if type == "users":
        following_count_list = []
        for key in dict.keys():
            following_count_list.append(dict[key][2])
            following_count_list = list(set(following_count_list))

        #print("printing users which is following the most")

        pos_count = len(following_count_list) - 1
        counter = n
        while counter != 0:
            for key in dict.keys():
                if dict[key][2] == following_count_list[pos_count]:
                    print("User:", key, "has", following_count_list[pos_count], "followers")
            counter -= 1
            pos_count -= 1

    elif type == "tweets":
        tweet_count_list = []
        for key in dict.keys():
            tweet_count_list.append(dict[key][3])
            tweet_count_list = list(set(tweet_count_list))

        # print("printing users with most tweets")

        pos_count = len(tweet_count_list) - 1
        counter = n
        while counter != 0:
            for key in dict.keys():
                if dict[key][3] == tweet_count_list[pos_count]:
                    print("User:", key, "has", tweet_count_list[pos_count], "tweets")
            counter -= 1
            pos_count -= 1

find_popular(user_dict, "tweets", 2)

