# In this program I will try to solve the problem
# Our goal is to maximize the score while respecting the maximum weight of the phone

Music = [
    {"Title": "Led Zeppelin - Whole Lotta Love", "Score": 2, "Weight": 40},
    {"Title": "Magma - Retrovision (je suis revenu de l'univers)", "Score": 5, "Weight": 52},
    {"Title": "The Manhattan Project - Goodbye Pork Pie Hat (live)", "Score": 1, "Weight": 27},
    {"Title": "Jaco Pastorius - The Chicken (live)", "Score": 2, "Weight": 68},
    {"Title": "Steve Ray Vaughan - Little Wing", "Score": 3, "Weight": 80},
    {"Title": "Lynyrd SKynyrd - Free Bird (live)", "Score": 5, "Weight": 62},
    {"Title": "Genesis - Back In NYC", "Score": 2, "Weight": 63},
    {"Title": "The Who - I Can See For Miles", "Score": 3, "Weight": 53},
    {"Title": "Jean-Luc Ponty - Jig (live)", "Score": 1, "Weight": 56},
    {"Title": "David Bowie - Space Oddity", "Score": 1, "Weight": 59}
]

Capacity = 500 # MB

X = [0] * len(Music)

def SumScores(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i] * Music[i]["Score"]
    return sum

def SumWeights(x):
    sum = 0
    for i in range(len(x)):
        sum += x[i] * Music[i]["Weight"]
    return sum

def Display(x):
    # We display the total value as well as the total weight and X
    print("Total value: ", SumScores(x))
    print("Total weight: ", SumWeights(x))
    print("X: ", x)

# We will try to solve the problem with a greedy algorithm
# We will sort the music according to their score in relation to their weight
# We will take the most profitable music first
# We will add them to our backpack as long as the capacity is not exceeded

def BestMusic():
    Music.sort(key=lambda x: x["Score"] / x["Weight"], reverse=True)
    x = [0] * len(Music)
    weight = 0
    for i in range(len(Music)):
        if weight + Music[i]["Weight"] <= Capacity:
            x[i] = 1
            weight += Music[i]["Weight"]
    return x

X = BestMusic()

Display(X)