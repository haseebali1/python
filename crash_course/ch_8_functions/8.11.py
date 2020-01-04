# Messages


def send_messages(messages):
    while messages:
        send_message = messages.pop()
        print ("Sending Message : " + send_message)
        sent_messages.append(send_message)

messages = ["fdkaf sdkjf", "jdweiruo", "nm,xcvdfowife dkfwojvn", "eirocmv"]
sent_messages = []

send_messages(messages[:])

print( f"\nMessages : {messages}" )
print( f"Sent Messages : {sent_messages}" )
