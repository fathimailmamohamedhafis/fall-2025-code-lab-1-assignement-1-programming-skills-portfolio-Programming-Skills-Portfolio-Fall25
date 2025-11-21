
question = { 
    'france': 'paris',
    'germany':'berlin',
    'Norway': 'oslo',
    'belgium':'brussels',
    'spain':'madrid',
    'greece': 'athens',
    'portugal':'lisbon',
    'italy': 'Rome',
    'sweden':'stockholm',
    'netherland':'amsterdan'}


for country, capital in question.items():# takes a specific country and capital
    answer= input (f"what is the capital of {country}?").lower().strip()
    if answer == capital.lower():
        print("correct")
    else:
        print ("wrong")

