try_again = "y"
while try_again =="y":

    class SocialNetwork:
        def __init__(self):
            self.file_name = ""
            self.social_NW = {}
            self.common_friends = {}

    class File_Handler:
        def __init__(self, social_network):
            self.social_network = social_network

        def open_file(self):
            while True:
                self.social_network.file_name = input("Enter a file name: ")
                if self.social_network.file_name.lower() == "n":
                    exit()
                try:
                    with open(self.social_network.file_name, 'r') as f:
                        file_contents = f.read()
                        print(file_contents)
                        print()
                        lines = file_contents.split('\n')
                        for i in range(1, len(lines)):
                            line = lines[i].strip().split()
                            if line:
                                for j in range(len(line)):
                                    self.social_network.social_NW[line[j]] = self.social_network.social_NW.get(line[j], [])
                                    for k in range(len(line)):
                                        if j != k:
                                            self.social_network.social_NW[line[j]].append(line[k])
                        display_dictionary = input("Do you want to display the social network (y/n)? ")
                        if display_dictionary.lower() == "y":
                            for name, friend_list in self.social_network.social_NW.items():
                                if len(friend_list) > 0:
                                    print(name + " -> " + ", ".join(friend_list))
                                else:
                                    print(name + " -> ")
                        else:
                            exit()
                        # calculate common friends
                        for name in self.social_network.social_NW.keys():
                            self.social_network.common_friends[name] = [0] * len(self.social_network.social_NW)
                            for friend in self.social_network.social_NW[name]:
                                if friend in self.social_network.social_NW.keys():
                                    index = list(self.social_network.social_NW.keys()).index(friend)
                                    self.social_network.common_friends[name][index] += 1
                        display_common_friends = input("Do you want to display the common friend count (y/n)? ")
                        if display_common_friends.lower() == "y":
                            for name, common_friends in self.social_network.common_friends.items():
                                print(name + " -> " + str(common_friends))
                        else:
                            exit()

                        break
                except FileNotFoundError:
                    print("Error: File not found. Please enter a valid file name or press n to exit.")

    network = SocialNetwork()
    filehandler = File_Handler(network)
    filehandler.open_file()

    class Friendship(SocialNetwork):
        def __init__(self, social_network):
            super().__init__()
            self.social_network = social_network

        def suggest_friends(self):
            while True:
                name = input("Enter a member name to suggest friends: ")
                if name.lower() == 'n':
                    break
                if name not in self.social_network.social_NW.keys():
                    print("Error: Invalid member name. Please enter a valid name.")
                else:
                    suggested_friends = []
                    for friend in self.social_network.social_NW[name]:
                        for mutual_friend in self.social_network.social_NW[friend]:
                            if mutual_friend != name and mutual_friend not in self.social_network.social_NW[name] \
                                    and mutual_friend in self.social_network.social_NW.keys():
                                suggested_friends.append(mutual_friend)
                    suggested_friends = list(set(suggested_friends))
                    if suggested_friends:
                        print(name + " -> " + ", ".join(suggested_friends))
                    else:
                        print(name + " -> No suggested friends.")
                next_user = input("Do you want to suggest friends for another user? (y/n)")
                if next_user.lower() == 'n':
                    break

        def display_friends_count(self):
            while True:
                user_input = input("Do you want to display how many friends a member has? (y/n)")
                if user_input.lower() == 'n':
                    break
                elif user_input.lower() == 'y':
                    name = input("Enter the member's name: ")
                    if name not in self.social_network.social_NW.keys():
                        print("Error: Invalid member name. Please enter a valid name.")
                    else:
                        friends_count = len(self.social_network.social_NW[name])
                        print(name + " has " + str(friends_count) + " friend(s).")
                else:
                    print("Invalid input. Please enter y or n.")

        def least_friends(self):
            friend_count = {}
            for name, common_friends in self.social_network.common_friends.items():
                if sum(common_friends) > 0:
                    friend_count[name] = sum(common_friends)
            min_friend_count = min(friend_count.values())
            least_friends_users = [user for user, count in friend_count.items() if count == min_friend_count]
            display_least_friends = input("Do you want to display the users with the least friends (y/n)? ")
            if display_least_friends.lower() == "y":
                return "Users with least friends are: " + ", ".join(least_friends_users)
            else:
                return "ok"

        def zero_friends(self):
            friend_count = {}
            for name, common_friends in self.social_network.common_friends.items():
                friend_count[name] = sum(common_friends)
            zero_friends_users = [user for user, count in friend_count.items() if count == 0]
            display_zero_friends = input("Do you want to display the users with zero friends (y/n)? ")
            if display_zero_friends.lower() == "y":
                print("Users with zero friends are: " + ", ".join(zero_friends_users))

        def display_friends_of_friends(self):
            while True:
                name = input("Enter the name of the user to display friends of friends or type n: ")
                if name.lower() == 'n':
                    break
                else:
                    friends_of_friends = set()
                    for friend in self.social_network.social_NW[name]:
                        friends_of_friends = friends_of_friends.union(self.social_network.social_NW[friend])
                    friends_of_friends.discard(name)
                    for friend in self.social_network.social_NW[name]:
                        friends_of_friends.discard(friend)
                    if len(friends_of_friends) == 0:
                        print(f"{name} has no friends of friends")
                    else:
                        print(f"{name}'s friends of friends are: " + ', '.join(friends_of_friends))

    # create Friendship object and call suggest_friends method
    friendship = Friendship(network)
    friendship.suggest_friends()
    friendship.display_friends_count()
    least_friends_user = friendship.least_friends()
    print(least_friends_user)
    friendship.zero_friends()
    friendship.display_friends_of_friends()
    try_again = input("Do you want to try another social network ? (y/n)")



