#!/usr/bin/python3
nbr = int(input('''
      = == = == = == = == = ==
      WELCOME TO THE TOOLKIT!!
      = == = == = == = == = ==
        1. Add a Note
        2. View Notes
        3. Delete a Note
        4. Search Notes
        5. Exit
        
        Choose a number: '''
)
)

while nbr < 1 or nbr > 5:
        print('The number you entered is not an option. Try again.')
        nbr = int(input('''
      = == = == = == = == = ==
      WELCOME TO THE TOOLKIT!!
      = == = == = == = == = ==
        1. Add a Note
        2. View Notes
        3. Delete a Note
        4. Search Notes
        5. Exit
        
        Choose a number: '''
)
)

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
elif nbr == 3:
        print('''
              = == = == = == = ==
                DELETE A NOTE
              = == = == = == = ==
              ''')
elif nbr == 4:
        print('''
              = == = == = == = ==
               Search for Notes
              = == = == = == = ==
              ''')
else:
        print('''
              = == = == = == = ==
              THANK YOU! 
              APPLICATION CLOSED
              = == = == = == = ==
              ''')