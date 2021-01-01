from nltk.chat.util import Chat, reflections
pairs = [
    [
        r"hi|hey there",
        ["hello","HII"]
    ],
    [
        r"hello my self (.*) and you",
        ["hello my self chatty and i am a robot"]
    ],
    [
        r"what is your name",
        ["my self chatty and i am a robot"]
    ],
    [
        r"quit|bye",
        ['BYE BYE TAKE CARE']
    ]
]
def chatty():
    print("Hi i am chatty")
    chat = Chat(pairs , reflections)
    chat.converse()
if __name__ == "__main__":
    chatty()
