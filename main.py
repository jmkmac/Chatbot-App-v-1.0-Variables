# Virtual Chatbot to check in patients at a Hospital
print('Hello Welcome to the Hospital Virtual Check In!')
print('\n')
# Question to collects patient information
name = input('Who am I speaking with?:')
print('Hello', name)
print('\n')
age = int(input('What is your age?:'))
# Age on Mars Calculation
martian = age / 1.88
print(name,
      f'Did you know your age on the planet Mars would be {martian:.2f}?\n')
sex = input('Do you identify as Male, Female or Other?:')
print(name, 'You Identify as a', sex, '\n')
# Address information
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
