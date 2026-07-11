#!/usr/bin/python3
print('''
      = == = == = == = == = ==
      WELCOME TO THE TOOLKIT!!
      = == = == = == = == = ==
        1. Add a Note
        2. View Notes
        3. Delete a Note
        4. Exit
        '''
)

while True:
        nbr = int(input('Enter your choice number: '))
        if nbr == 4:
                print('''
                = == = == = == = ==
                THANK YOU! 
                APPLICATION CLOSED
                = == = == = == = ==
                ''')
                break
        
        if 1 <= nbr <= 3:
                if nbr == 1:
                        print('''
                        = == = == = == = ==
                        ADD YOUR NOTES
                        = == = == = == = ==
                        ''')
                elif nbr == 2:
                        print('''
                        = == = == = == = ==
                        My Notes
                        = == = == = == = ==
                        ''')
                else:
                        print('''
                        = == = == = == = ==
                        DELETE A NOTE
                        = == = == = == = ==
                        ''')
        else:
                print('The number you entered is not a choice. Try again')