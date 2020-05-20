class TvController():

    channels = ['BBC','Discovery','TV1000']

    def __init__(self, channels = ['BBC','Discovery','TV1000'],channel_number = 0):
        self.channels = channels
        self.channel_number = channel_number
    
    def current_channel(self):
        return self.channels[self.channel_number]

    def first_channel(self):
        self.channel_number = 0
        return self.current_channel()

    def last_channel(self):
        self.channel_number -= 1
        return self.current_channel()

    def turn_channel(self,number):
        if int(number) <= len(self.channels):
            self.channel_number = int(number)-1
            return self.current_channel()
        return "we do not have such channel number. Sorry, bro..."

    def next_channel(self):
        if self.channel_number < len(self.channels)-1:
            self.channel_number +=1
            return self.current_channel()
        self.channel_number = 0
        return self.current_channel()
        

    def previous_channel(self):
        self.channel_number -=1
        return self.current_channel()
    
    def is_exist(self):
        check = input("input number or name of the channel: ").strip()
        if len(self.channels)> check.isdigit()>0:
            return f"Exists! you can watch {self.channels[int(check)-1]}"
        elif check.upper().isalpha():
            for item in self.channels:
                if check.upper() == item:
                    return f"Exists! you can watch it {self.channels.index(check.upper())+1}"
        else:
            return "No results, sorry"

controller = TvController()

while True:
    choice = input(f"""
    We have 3 self.channels available:
                1:  BBC
                2:  Discovery
                3:  TV1000
            You are now watching {TvController.channels} 
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
        print(controller.current_channel())
    elif choice.strip().lower() == 'check':
        print(controller.is_exist())
    else:
        print("Cannot see what you want, man")
    continue

 