file = open("dummy-data-1/follows.txt")

user_dict = {}

# A for loop that reads in users into a dictionary where the username is the key and the value is their tweeting information

for line in file:
    users = line.split(" ")
    user_dict[users[0].replace("\n","")] = [users[1:], [], len(users[1:]), 0]
    for i in range(0, len(user_dict[users[0].replace("\n","")][0])):
        user_dict[users[0].replace("\n","")][0][i] = user_dict[users[0].replace("\n","")][0][i].replace("\n","")

stream = open("dummy-data-1/stream.txt")

for line in stream:
    tweets = line.split(" ")
    if tweets[1] != "RT" and tweets[1] != "DM":
        str = ' '.join(tweets[1:])
        user_dict[tweets[0].replace("\n","")][1].append(str)


for user in user_dict.keys():
    user_dict[user][3] = len(user_dict[user][1])







