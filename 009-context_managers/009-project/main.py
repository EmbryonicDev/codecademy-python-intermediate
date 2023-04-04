from contextlib import contextmanager
# from print_checkpoint import *

# Write your code below:


@contextmanager
def generic(card_type, sender, receiver):
    card_file = open(card_type, 'r')
    order = open(f"{sender}_generic.txt", 'w')

    try:
        order.write(
            f"Dear {receiver}\n\n{card_file.read()}\n\nSincerely, {sender}\n")
        yield order
    finally:
        card_file.close()
        order.close()

# Checkpoint 7 - 10


class Personalized:
    def __init__(self, sender, receiver):
        self.sender = sender
        self.receiver = receiver
        self.order = open(f"{sender}_personalized.txt", 'w')

    def __enter__(self):
        print(f"Opening {self.sender}'s card")
        self.order.write(f"Dear {self.receiver}\n \n")
        return self.order

    def __exit__(self, exc_type, exc_value, Traceback):
        print('closing off card')
        self.order.write(f"\n \nSincerely {self.sender}")
        self.order.close()


# Checkpoint 5
# print_checkpoint(5)
with generic('thankyou_card.txt', 'Mwenda', 'Amanda') as x:
    print('Card Generated!')

# Checkpoint 6
# print_checkpoint(6)
with open('Mwenda_generic.txt', 'r') as file:
    print(file.read())


# Checkpoint 11
# print_checkpoint(11)
# new_order =
with Personalized("John", 'Michael') as order:
    order.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.")

# Checkpoint 12
# print_checkpoint(12)
sender = 'Josiah'
with generic('happy_bday.txt', sender, 'Remy') as generic_card:
    print('Personalized card printed')
    with Personalized(sender, 'Esther') as personal_card:
        personal_card.write("Happy Birthday!! I love you to the moon and back. Even though you're a pain sometimes, you're a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You're getting old!")
