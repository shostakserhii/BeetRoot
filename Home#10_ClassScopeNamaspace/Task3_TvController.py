channels = ['BBC','Discovery','TV1000']
current = 0
class TvController():

    def __init__(self, channels):
        self.channels = channels

    def first_channel(self):
        global current 
        current = 0
        return channels[0]

    def last_channel(self):
        global current 
        current = 2
        return channels[-1]

    def turn_channel(self,N):
        global current
        current = N - 1
        return channels[N-1]

    def next_channel(self):
        global current
        if current == 2:
            current = 0
            return channels[current] 
        current += 1
        return channels[current]

    def previous_channel(self):
        global current
        current -= 1
        return channels[current]

    def current_channel(self):
        return channels[current]
    
    def is_exist(self):
        N = input("input number or name of the channel: ")
        if 4> N.isdigit() >0:
            return "Exists! you can watch it"
        elif N.isalpha():
            for item in channels:
                if N.upper() == item:
                    return "Exists! you can watch it"
        else:
            return "No results, sorry"

controller = TvController(channels)
print(controller.first_channel())
print(controller.turn_channel(3))
print(controller.next_channel())
print(controller.previous_channel())

while True:
    choice = input(f"""
    We have 3 channels available:
                1:  BBC
                2:  Discovery
                3:  TV1000
            You are now watching {channels[current]} 
    And next operations:
                first channel:      -f
                last channel:       -l
                turn channel:       -t
                next channel:       -n
                previous channel:   -p
                current channel:    -c
                check if channel exists:  -check
                QUIT - q
    """)
    if choice == 'q':
        print("Closing......")
        break
    elif choice.strip().lower() == 'f':
        print(controller.first_channel())
    elif choice.strip().lower() == 'l':
        print(controller.last_channel())
    elif choice.strip().lower() == 't':
        N = input("input number: ")
        print(controller.turn_channel(N))
    elif choice.strip().lower() == 'n':
        print(controller.next_channel())
    elif choice.strip().lower() == 'p':
        print(controller.previous_channel())
    elif choice.strip().lower() == 'c':
        print(channels[current])
    elif choice.strip().lower() == 'check':
        print(controller.is_exist())
    else:
        print("Cannot see what you want, man")
    continue

 