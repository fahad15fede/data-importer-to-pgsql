import re
import long_responses

def msg_probability(user_msg, recognised_words, single_response=False, required_words = []):
    msg_certainty = 0
    has_required_words = True

    #COunts how many words are present in the msg predefined
    for word in user_msg:
        if word in recognised_words:
            msg_certainty +=1
    
    #Calculates the percent of recognised words in a user message
    percentage = float(msg_certainty)/float(len(recognised_words))

    for word in required_words:
        if word not in user_msg:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)

    else:
        return 0


def check_all_messages(msg):
    highest_prob_list = {}

    def response(bot_response, list_of_words,  single_response=False, required_words = []):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = msg_probability(msg, list_of_words, single_response, required_words)
     
    #Responses ------------------------------------------------------------------------------------

    #Greet
    response('Hello!', ['hello', 'hi', 'wassup', 'hey'], single_response=True)
    response('Hey, I\'m  good.', ['Hello, how are you today?', 'wassup, how you doin?', 'hey, how are you?'], single_response=True)



    best_match = max(highest_prob_list, key = highest_prob_list.get)
    # print(highest_prob_list)
    return best_match

def get_response(user_input):
    split_msg = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_msg)

    return response
#Testung the response system 
while True:
    print('Bot:' + get_response(input('You:' )))