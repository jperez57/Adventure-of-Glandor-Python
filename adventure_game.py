import time

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(3)

def into():
    print_pause("I hear birds and waterfalls?")

    print_pause("You awake in the fields of Glandor")

def fields(items):
    print_pause("You start wondering the field.")
    print_pause("After a few moments, you stumble "
                "apon a frog in a wizards cloak.")
    if "Key" in items:
        print_pause("The frog wizard greets you, has already "
                    "given you the key to the chest of secrets, so there is nothing "
                    "more to do here now.")
    else:
        print_pause("The frog wizard greets you and present you with a key "
                    "to the chest of secrets.")
        items.append("Key")
    print_pause("You continue wondering the fields.")
    adventure(items)
def waterfall(items):
    print_pause("You head toward the sound of a waterfall.")
    print_pause("After a few moments, you find the waterfall and under it "
                "a mysterious cave.")
    if "sword of courage" in items:
        print_pause("The cave and chest is empty.")
        print_pause("There doesn't seem to be much to do here.")
    else:
        print_pause("There is a chest in the center of the cave.")
        if "Key" in items:
            print_pause("You try the key from the frog wizard. "
                        "The chest unlocks and you find the mystical Sword of Courage.")
            items.append("sword of courage")
        else:
            print_pause("The chest is locked."
                        "It looks like you need a key to opeen it.")
    print_pause("You head back to the field.")
    adventure(items)


def swamp(items):
    print_pause("You head toward a dark and terrifying swamp.")
    print_pause("After a few moments, you are startled by "
                "by the ferocious, murderous, legendary dragon of Glandor.")
    if "Key" in items:
        print_pause("Under the Dragon stands the Frog Wizard.")
        print_pause("He yells to you, 'You need the Sword to kill the beast'.")
        if "sword of courage" in items:
            print_pause("Fortunately, you have the Sword of Courage!")
            print_pause("You unsheath the Sword of Courage thrust it into the heart of the beast! "
                        "Thus saving Glandor from utter destruction!")
        else:
            print_pause("The Dragon begins to set the swamp a blaze")
            adventure(items)
    else:
        print_pause("A Frog in a wizard cloak under the Dragon yells")
        print_pause("'hero please take this key you need the ")
        print_pause("Sword of Courage to save Glandor'.")
        adventure(items)


def adventure(items):
    print_pause("Please choose what "
                "action you wish to take:")
    area = input("1. Search through the fields\n"
                  "2. Inspect the waterfall\n"
                  "3. Wander to a terrifying swamp\n")
    if area == '1':
        fields(items)
    elif area == '2':
        waterfall(items)
    elif area == '3':
      swamp(items)

def play_game():
    items = []
    into()
    adventure(items)


play_game()