#if/else statements applied to Chatbot 2/22/2023
#Virtual Chatbot to check in patients at a Hospital
print('Hello Welcome to the Hospital Virtual Check In!')
print('\n')

#Question to collects patient information
name = input('Who am I speaking with?:')
print('Hello', name)
print('\n')

#How do you Identify sequence structure with the martian age and fare decision structure 
sex1 = '1'
sex2 = '2'
sex3 = '3'
sex = input('Do you identify as (1):Male, (2):Female or (3):Martian?:')
if sex == sex1:
  print(name,'You Identify as a Male.\n')
  age = int(input('What is your age?:'))
  print(name,'you are',age,'years old.\n')
else:
  if sex == sex2:
    print(name,'you identify as a Female.\n')
    age = int(input('What is your age?:'))
    print(name,'you are',age,'years old.\n')
  else:
    if sex == sex3:
      print(name,'you identify as a Martian!\n')
      age = int(input('What is your age?:'))
      martian_age = age / 1.88 #Martian age calculation
      if age <=12:
        print(name,f'Did you know your age on the planet Mars would be {martian_age:.0f} years old!') 
        print('If you want to travel back to Mars your fare would be $5,000!')
      elif age >=19 and age <=65:
        print(name,f'Did you know your age on the planet Mars would be {martian_age:.0f} years old!')
        print('If you want to travel back to Mars your fare would be $10,000!')
      else:
        print(name,f'Did you know your age on the planet Mars would be {martian_age:.0f} years old!')
        print('If you want to travel back to Mars your fare would be $7,000!')
    if sex > sex3:
      print('Please pick a number that corralates to how you identify!')
    else:
      print('\n')
      
#Address information
house_number = int(input('What is your house number?:'))
street = input('What is your street name?:')
city = input('What City do you live?:')
state = input('What State do you ive?:')
zip = int(input('What is your zip code?:'))
print(name, 'you live at:', house_number, street, city, state, zip)
print('\n')
print(
  'Thank you', name,
  'for entering your patient information.  Please have a sit and we will be with you shortly.'
)
