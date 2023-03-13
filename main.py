# Adding Sentinel Loops 3/13/2023
# Virtual Chatbot to check in patients at a Hospital
start = int(input('Would you like to start your check-in process? Press (1) for Yes & (2) for No:\n'))

while start == 1: # Loop that will exit program or allow user to fill out check in information
  
  print('Hello Welcome to the Hospital Virtual Check In!')
  print('\n')
  
# Get name of Patients
  name = input('Who am I speaking with?:')
  print('Hello', name)
  print('\n')

# How you identify loop
  print('Hello tell us how you identify?')
  sex = int(input('Do you identify as a (1):Male, (2):Female or (3):Martian?:'))
  print('\n')
  while sex > 3:
      #print('Hello tell us how you identify?')
      sex = int(input('Do you identify as a (1):Male, (2):Female or (3):Martian?:'))
  
  if sex == 1:
      print(name, 'You Identify as a Male.')
      print('\n')
      age = int(input('What is your age?:'))
      print(name, 'you are', age, 'years old.')
  else:
    if sex == 2:
      print(name, 'you identify as a Female.')
      print('\n')
      age = int(input('What is your age?:'))
      print(name, 'you are', age, 'years old.')
    else:
      # Martian Age and Fare to get back from Mars
      if sex == 3:
        print(name, 'you identify as a Martian!')
        print('\n')    
        age = int(input('What is your age?:'))
        martian_age = age / 1.88  #Martian age calculation
        if age <= 12:
          print(name,f'Did you know your age on the planet Mars would be {martian_age:.0f} years old!')
          print('If you want to travel back to Mars your fare would be $5,000!')
          print('\n')
        elif age >= 19 and age <= 65:
          print(name,f'Did you know your age on the planet Mars would be {martian_age:.0f} years old!')
          print('If you want to travel back to Mars your fare would be $10,000!')
          print('\n')
        else:
          print(name,f'Did you know your age on the planet Mars would be {martian_age:.0f} years old!')
          print('If you want to travel back to Mars your fare would be $7,000!')
          print('\n')
        
      #Address information
      house_number = int(input('What is your house number?:'))
      street = input('What is your street name?:')
      city = input('What City do you live?:')
      state = input('What State do you ive?:')
      zip = int(input('What is your zip code?:'))
      print(name, 'you live at:', house_number,
      street, city, state, zip)
      print('\n')

  
    #Exit Chatbot
    print('Thank you', name,'for entering your patient information.  Please have a sit and we will be with you shortly.\n')
    

# Quit Application Function
quit('Thank you now exiting check-in')
