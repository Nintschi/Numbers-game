highest = 10
answer = random.randint(1,highest)
#print(answer) # todo: remove after testing

print("Please guess a number between 1 and {}: ".format(highest))
guess = int(input())

if guess == answer:
    print("jihaaaa right")
else:
    if guess > answer:
        print("...a bit lower")
    if guess < answer:
        print("...a bit higher")
    guess = int(input())
    if guess == answer:
        print("yeah now have it!")
    if guess != answer:
        print("soooory :(")