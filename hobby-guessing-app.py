print("Title of program: Hobby Guessing Game")
print()
print("Welcome to the hobby guessing game! Please answer the following questions truthfully and we'll try to guess what you like to do :)")
print("Please respond with a number 1 - 5, where 1 is strongly disagree and 5 is strongly agree.")
print()

craft1 = input("I enjoy building and fixing things.")

craft2 = input("Paint and colours make me happy.")

craft3 = input("I find joy in making new things.")

cooking1 = input("I like experimenting with different flavours.")

cooking2 = input("I often help my mother/father in preparing meals.")

cooking3 = input("I know how different combinations of ingredients can create unique tastes")

music1 = input("I play a musical instrument well.")

music2 = input("I find joy in harmonies and melodies.")

music3 = input("I find the sounds of instruments beautiful.")

dancing1 = input("Music makes me want to move about.")

dancing2 = input("I like learning different dances.")

dancing3 = input("I enjoy creating choreography for different songs.")

singing1 = input("I enjoy singing in the shower.")

singing2 = input("I feel like singing along whenever I hear songs that I know being played.")

singing3 = input("Singing makes me feel euphoric.")

craft_final = int(craft1) + int(craft2) + int(craft3)
cooking_final = int(cooking1) + int(cooking2) + int(cooking3)
music_final = int(music1)+ int(music2) + int(music3)
dancing_final = int(dancing1) + int(dancing2) + int(dancing3)

print()

if craft_final > cooking_final and craft_final > music_final and craft_final > dancing_final> singing_final:
  print("We think that you like craft work!")
elif cooking_final > music_final and cooking_final > dancing_final > singing_final:
  print("We think that you enjoy cooking!")
elif music_final > dancing_final > singing_final:
  print("We think that you enjoy playing musical instruments!")
eif dancing_final > singing_final:
  print("We think that your hobby is dancing!")
else:
  print("We think that your hooby is singing!")
