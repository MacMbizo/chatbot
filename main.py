import re
import long_responses as long

# Function that calculates the probability of the right message
def message_probability(user_message, recognised_words, single_response=False, require_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predifined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percentage of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in require_words:
        if word not in user_message:
            has_required_words = False
            break

def get_response(user_input):
    split_message = re.split(r'\s+|{,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

# Testing response system
while True:
    print('Bot:' + get_response(input('You: ')))