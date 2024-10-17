def cleanup (text):
    text = text.lower() 
    punctuation = '''!()-[]{};:'"\\,<>./?@#$%^&*_~''' #use double back slash, one for the checking, and one for the escaping

    for char in text:
        if char in punctuation:
            text = text.replace(char, "")
    return text

def text_to_unique_words (text):
    words = text.split()

    # Create a list to hold unique words
    sorted_words = []

    for word in words:
        if word in sorted_words:
            continue
        sorted_words.append(word)

    sorted_words.sort() #sort alphabatically

     # Print each word on a new line
    for word in sorted_words:
        print(word)

text1 = "Hello world, hello again"
text1 = cleanup(text1)
text_to_unique_words(text1)