from sys import argv

script, user_name = argv
promt = '> '

print(f"hi {user_name}, i'm the {script} script.")
print("i'd like to ask you some questions.")

print(f"Do you like me {user_name}?")
likes = input(promt)

print(f"where do you live {user_name}?")
lives = input(promt)

print("what type of computer do you have?")
computer = input(promt)

print(f"""alright, so you said {likes} about liking me.
you live in {lives}. not sure where that is.
and you have a {computer} computer. nice.""")