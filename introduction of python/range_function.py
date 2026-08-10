# for i in range(10,20,2):
#     print(i)


scores = [2, 1, 3, 58, 89, 56, 90, 3, 22, 3, 4, 6]
summ = 0
for i in range(len(scores)):
    summ = summ + scores[i]
# sum() function
# summ = sum(scores)
print(f"total score is {summ}")

highest = scores[0]  # assuming first value is highest
for i in scores:
    if i > highest:
        highest = i
# max()
# highest = max(scores)
print(f"highest score is {highest}")

lowest = scores[0]  # assuming first value is lowest
for i in scores:
    if i < lowest:
        lowest = i
# min()
# lowest = min(scores)
print(f"lowest score is {lowest}")