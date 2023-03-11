import random

print('Welcome to Heshmat!')

greetings = ['Hello!', 'What"s up?', 'Howdy!', 'Greetings!']
goodbyes = ['Bye', 'Goodbye', 'See you later!', 'See you soon']

# Define some keywords and their corresponding responses
keywords = ['music', 'pet', 'book', 'game']
responses = ['Music is so relaxing!', 'Dogs are man\'s bestfriend!', 'I know about a lot of books', 'I like to play video games']

# Ask the user for their name
user_name = input('What is your name? ')
print(f'Nice to meet you, {user_name}!')

while True:
    user_input = input('Say something (or type "bye" to quit): ')
    user_input = user_input.lower()

    # Check if the user wants to quit the program
    if user_input in goodbyes or user_input == 'bye':
        print(random.choice(goodbyes))
        print(f'Goodbye, {user_name}!')
        break
    
    # Check if any of the keywords are in the user's input
    found_keyword = False
    for i, keyword in enumerate(keywords):
        if keyword in user_input:
            print(f'Heshmat: {responses[i]}')
            found_keyword = True
            break
            
    # If no keyword was found, ask the user for a new one
    if not found_keyword:
        new_keyword = input("I'm not sure how to respond. What keyword should I respond to? ")
        
        # Add the new keyword and its corresponding response to the list
        keywords.append(new_keyword)
        new_response = input(f"How should I respond to '{new_keyword}'? ")
        responses.append(new_response)

print('Thanks for chatting with me!')

