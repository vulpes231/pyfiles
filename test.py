# rnadom module shuffle(), randint(=> int), random(=> float), choice(=> single) choice(=> [])
import random

random_mark = random.randint(40, 100)
print(random_mark)

if random_mark <= 50:
    print(f"Scored {random_mark} GRADE D")
elif random_mark <= 70:
    print(f"Scored {random_mark} GRADE C")
elif random_mark <= 85:
    print(f"Scored {random_mark} GRADE B")
else:
    print(f"Scored {random_mark} GRADE A")

# options = ("rock", "paper","scissors")



# random_choice = random.choice(options)

