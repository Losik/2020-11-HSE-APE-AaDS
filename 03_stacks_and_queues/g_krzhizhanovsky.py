n = int(input())

# Scores contain following structure
#   scores[:n - 1] - opponent's cores
#   scores[n - 1]  - or score
#   scores[n]      - dummy cell for convenience
scores = list(map(int, input().split()))
scores.append(0)

# We use list here because we want to be able to traverse
# values in increasing order. Values of other players  are
# limited by 100 and we are going to try 101 max so we create
# a list of 102 element not to get an IndexError
values_count = [0] * 102
# Maps value to some (only one) player that named this vaue
values_owner = {}
values = []

for i, value in enumerate(map(int, input().split())):
    values.append(value)
    values_owner[value] = i
    values_count[value] += 1

# Number of playes with less amount of points
best_reverse_place = 0
# Minimim value we reached our best result with
best_value = 1

# Traversing all possible values for my next move. It can
# make a difference if we either prevent someone from winning
# this round or win this round ourselves.
#
# In the first case we have to traverse values up till 100
# cause according to statement our opponent name values up
# till 100
#
# In the second case there's no point in getting more than 101
# point cause according to statement have already earned 100 points
# max.
for our_value in range(1, 102):

    # Changin values_count fo chosen value
    values_count[our_value] += 1

    # Determining the winner. It is possible that noone
    # gets any points. In this case all points will be
    # assigned to a dummy player that we've artificially added
    # in the beginning
    winner = n
    for value in range(1, 102):
        if values_count[value] == 1:
            # If therer is no owner for a value this is because
            # we updated count but not oowners (would not be easily
            # reversible).
            winner = values_owner.get(value, n - 1)
            # Assigning the winner his points
            scores[winner] += value
            break

    # We are n-1'st player
    reverse_place = sum(1 for i in range(n - 1) if scores[i] < scores[n - 1])
    if reverse_place > best_reverse_place:
        best_reverse_place = reverse_place
        best_value = our_value

    # Rolling back ourr updates
    scores[winner] -= value
    values_count[our_value] -= 1

print(best_value)
