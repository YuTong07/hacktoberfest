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

reading1 = input("I can get lost in the story when reading")
reading2 = input("I love spending time reading books")
reading3 = input("I want to write or publish a book of my own in future")

craft_final = int(craft1) + int(craft2) + int(craft3)
cooking_final = int(cooking1) + int(cooking2) + int(cooking3)
music_final = int(music1)+ int(music2) + int(music3)
dancing_final = int(dancing1) + int(dancing2) + int(dancing3)
singing_final = int(singing1) + int(singing2) + int(singing3)
reading_final = int(reading1) + int(reading2) + int(reading3)

if craft_final > cooking_final and craft_final > music_final and craft_final > dancing_final and craft_final > singing_final and craft_final > reading_final:
  print("We think that you like craft work!")
  
if cooking_final > craft_final and cooking_final > music_final and cooking_final > dancing_final and cooking_final > singing_final and cooking_final > reading_final:
  print("We think that you enjoy cooking!")

if music_final > cooking_final and music_final > craft_final and music_final > dancing_final and music_final > singing_final and music_final > reading_final:
  print("We think that you enjoy playing musical instruments!")
  
if dancing_final > craft_final and dancing_final > cooking_final and dancing_final > music_final and dancing_final > singing_final and dancing_final > reading_final:
  print("We think that your hobby is dancing!")
  
if singing_final > craft_final and singing_final > cooking_final and singing_final > music_final and singing_final > dancing_final and singing_final > reading_final:
  print("We think that your hobby is singing!")

if reading_final > craft_final and reading_final > cooking_final and reading_final > music_final and reading_final > dancing_final and reading_final > singing_final:
  print("We think that your hobby is reading!")
