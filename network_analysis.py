from collections import deque

graph = {}

# To add a particular user
def add_user(graph, user):
    if user not in graph:
        graph[user] = []
        print(f"The user {user} has been added to network.")
    else:
        print(f"The user {user} already exists.")

# To add friend
def add_friend(graph, user1, user2):
    if user1 not in graph:
        add_user(graph, user1)
    if user2 not in graph:
        add_user(graph, user2)

    if user2 not in graph[user1]:
        graph[user1].append(user2)
    if user1 not in graph[user2]:
        graph[user2].append(user1)
    print(f"{user1} and {user2} have been added as friends!")

# To view network
def view_network(graph):
    if not graph:
        print("Your network is empty.")
    else:
        print("Below is your current social network:")
        for user, friends in graph.items():
            if friends:
                print(f"{user}: {', '.join(friends)}")
            else:
                print("Sorry you have no friends yet.")

def shortest_path(graph, start, goal):
    if start not in graph or goal not in graph:
        print("Seems like these users have no connection.")

    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

def recommend_friends(graph, user):
    if user not in graph:
        print(f"User '{user}' does not exist.")
        return []

    friends = set(graph[user])
    recommendations = set()

    for friend in friends:
        friends_of_friend = set(graph.get(friend, []))
        recommendations.update(friends_of_friend - friends - {user})

    return list(recommendations)


print("Welcome to your social network analysis.")
while True:
    options = ["Add user", "Add friend", "View your network", "View your shortest path", "Your recommended friends",
              "Exit"]

    for index, option in enumerate(options):
        print(f"{index + 1}. {option}")
    choice = input("What would you like to do?")

    if choice == "1":
        name = input("Enter user name: ")
        add_user(graph, name)
    elif choice == "2":
        user1 = input("Enter the name of the first user: ")
        user2 = input("Enter the name of the second user: ")
        add_friend(graph, user1, user2)
    elif choice == "3":
        view_network(graph)
    elif choice == "4":
        start = input("Enter start user: ")
        goal = input("Enter goal user: ")
        path = shortest_path(graph, start, goal)
        if path:
            print("Shortest path:", " -> ".join(path))
        else:
            print("No path found.")
    elif choice == "5":
        user = input("Enter username: ")
        recs = recommend_friends(graph, user)
        if recs:
            print("Friend recommendations:", ", ".join(recs))
        else:
            print("No recommendations found.")
    elif choice == "6":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
