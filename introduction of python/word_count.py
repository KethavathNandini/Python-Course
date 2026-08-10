words = ["India","Usa","Aus","Ireland","japan","Iran"]
count = 0
i_words = []
for w in words:
    if w.startswith("I"):
        count = count + 1
        i_words.append(w)
print(count)
print(i_words)

user = {
    "name" : "samantha",
    "id" :30300,
    "password":"gsdsjkhfk",
    "account":"454gf",
    "country":"universe"

}
sensitive = ["password", "account","nk"]

for i in sensitive:
    if i in user:
        user.pop(i)

print(user)


# game
print("Welcome to the number guessing game . we have a nuber that needs to be guessed. you have 10 chances. ")
print("the secret number is between 1 to 50")
secret_num = 28
attempts = 10
for i in range(1,11):
    print(f"you have {attempts} attempts!")
    number = int(input("Enter your guess: "))
    if number == secret_num:
        print("congrats, your guess is correct!")
        break
    else:
        if number < secret_num:
            higher_lower = "higher"
            print(f"your guess is wrong! try {higher_lower} number")
        else:
            higher_lower = "lower"
        print(f"your guess is wrong! try {higher_lower} number")
    attempts -=1