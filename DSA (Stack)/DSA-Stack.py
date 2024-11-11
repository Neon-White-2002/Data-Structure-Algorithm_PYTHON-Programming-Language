# DSA-STACK (PYTHON) :

import sys  # PYTHON-MODULE

# CLASS-NODE :
class Node:
    # CLASS-NODE (CONSTRUCTOR) :
    def __init__(self, value):
        self.data = value
        self.next = None

# CLASS 'STACK' :
class stack:
    # CLASS-STACK (CONSTRUCTOR) :
    def __init__(self):
        # STACK-PARAMETER :
        self.top = None
        self.bottom = None
        # STACK (HEIGHT & LENGTH) :
        self.height = 0
        self.length = 0

    """
        # Data-Structure & Algorithm (STACK) :
            :-> PUSH-METHOD
            :-> POP-METHOD
            :-> DISPLAY, STACK
    """

    # PUSH-METHOD (APPEND-NODE) :
    def push_method(self, value):
        # GENERATE, NEW-NODE :
        new_node = Node(value)
        # STORE, RESULT :
        result = None

        # CHECK, WEATHER 'STACK', IS FULL OR NOT :
        if self.height == self.length:
            result = ("\n\t>>> SORRY, SEEMS LIKE 'STACK', IS 'FULL' !" +
                      f"\n\t>>> STACK-LENGTH : {self.length}")
        # CHECK, WEATHER 'STACK-HEIGHT', IS 'EMPTY' OR NOT :
        elif self.height == 0:
            # SET, 'TOP & BOTTOM', TO NEW-NODE :
            self.top = new_node
            # BOTTOM, WILL REMAIN 'STATIC (NEW-NODE)' :
            self.bottom = new_node
            # INCREMENT-LENGTH :
            self.height += 1

            # UPDATE, RESULT :
            result = "\n\t>>> YA ! 'NEW-NODE' (PUSH) - SUCCESSFULLY, IN 'STACK'"
        else:
            # PREPEND-NODE :
            new_node.next = self.top
            # UPDATE, 'TOP-POINTER' :
            self.top = new_node
            # INCREMENT-LENGTH :
            self.height += 1

            # UPDATE, RESULT :
            result = "\n\t>>> YA ! 'NEW-NODE' (PUSH), WAS SUCCESSFULLY, IN 'STACK'"

        # DISPLAY, RESULT :
        print(f"{result}")

    # POP-METHOD (REMOVE-NODE) :
    def pop_method(self):
        # CHECK, WEATHER 'STACK', IS 'EMPTY' OR NOT :
        if self.height == 0:
            print("\n\t>>> SORRY, SEEMS LIKE 'STACK', IS 'EMPTY' NOTHING TO 'POP' !")
            print("\t>>> TOP : -1")
            print("\t>>> BOTTOM : -1")
            print(f"\t>>> HEIGHT : {self.height}")
        else:
            # GENERATE, TEMPORARY-NODE :
            temporary_node = None

            # REMOVE-NODE (LAST-POSITION) :
            temporary_node = self.top
            # UPDATE, 'TOP-POINTER' & DELETE-NODE :
            self.top = self.top.next
            temporary_node.next = None
            # DECREMENT-LENGTH :
            self.height -= 1
            # DISPLAY, RESULT :
            print("\n\t>>> YA ! 'NODE', WAS (POP) - SUCCESSFULLY, FROM 'STACK'" +
                  f"\n\t>>> DELETED-NODE : {temporary_node.data}" +
                  f"\n\t>>> DELETED-NODE (NEXT) : {temporary_node.next}")

            # CHECK, WEATHER 'HEIGHT', IS 'ZERO (0)' OR NOT, OF 'STACK' :
            if self.height == 0:
                # SET, 'TOP & BOTTOM' TO, 'NULL' :
                self.top = None
                self.bottom = None

    # DISPLAY, STACK :
    def display_stack(self):
        # CHECK, WEATHER 'STACK', IS 'EMPTY' OR NOT :
        if self.height == 0:
            print("\n\t>>> OOPS ! SEEMS LIKE 'STACK', IS 'EMPTY' \n")
            print(f"\t>>> TOP : {self.top}")
            print(f"\t>>> BOTTOM : {self.bottom}")
            print(f"\t>>> HEIGHT : {self.height}")
        else:
            # TEMPORARY-NODE :
            current_node = self.top

            print("\n\t>>> STACK : ", end="")
            for i in range(self.height):
                print(f"{current_node.data} --> ", end="")
                # NEXT-NODE (INCREMENT) :
                current_node = current_node.next
            # PRINT (NULL) :
            print(f"NULL", end="\n\n")

            # DISPLAY, 'STACK (PARAMETER'S)' :
            print(f"\t>>> TOP : {self.top.data}")
            print(f"\t>>> BOTTOM : {self.bottom.data}")
            print(f"\t>>> HEIGHT : {self.height}")


if __name__ == '__main__':
    # OBJECT, (INITIALIZATION), OF CLASS 'STACK' :
    dsa_stack = stack()

    # HERE, WE WILL SET 'HEIGHT' OF 'STACK' :
    height = str(input("\n\t>>> ENTER, 'HEIGHT (LENGTH)', OF 'STACK' : "))
    if len(height) == 0:
        print("\n\t>>> OOPS ! SEEM LIKE U DIDN'T PROVIDE 'HEIGHT', FOR 'STACK'")
        sys.exit("\t>>> SOMETHING WENT WRONG, TRY AGAIN !")
    else:
        try:
            # CONVERT, DATA-TYPE (INTEGER) :
            height = int(height)
            # SET, 'HEIGHT' :
            dsa_stack.length = height
        except ValueError:
            print("\n\t>>> SORRY, SEEMS LIKE U DIDN'T PROVIDE AN 'VALID-HEIGHT' !")
            sys.exit("\t>>> SOMETHING WENT WRONG, TRY AGAIN !")

    # INFINITY-LOOP (STACK-MENU) :
    while True:
        print("\n\t----- WELCOME TO, 'DSA-STACK' - MENU ----- \n")
        print("\t>>> PRESS (1) : PUSH-METHOD (APPEND-NODE)")
        print("\t>>> PRESS (2) : POP-METHOD (REMOVE-NODE)")
        print("\t>>> PRESS (3) : DISPLAY, 'DSA-STACK'")

        # USER-CHOICE :
        choice = str(input("\n\t>>> ENTER, YOUR 'CHOICE' : "))
        # CHECK, WEATHER 'HEIGHT', IS PROVIDED OR NOT :
        if len(choice) == 0:
            print("\n\t>>> OOPS ! SEEM LIKE U DIDN'T PROVIDE 'CHOICE'")
            sys.exit("\t>>> SOMETHING WENT WRONG, TRY AGAIN !")
        else:
            try:
                # CONVERT, DATA-TYPE (INTEGER) :
                choice = int(choice)
                # STACK-MENU :
                if choice == 1:
                    # PUSH-METHOD :
                    data = str(input("\n\t>>> ENTER, 'DATA' U WANT TO 'PUSH' : "))
                    if len(data) == 0:
                        print("\n\t>>> OOPS ! SEEM LIKE U DIDN'T PROVIDE 'DATA', FOR 'STACK'")
                        sys.exit("\t>>> SOMETHING WENT WRONG, TRY AGAIN !")
                    else:
                        try:
                            # CONVERT, DATA-TYPE (INTEGER) :
                            data = int(data)
                            # PUSH-METHOD (FUNCTION) :
                            dsa_stack.push_method(data)
                        except ValueError:
                            print("\n\t>>> SORRY, SEEMS LIKE U DIDN'T PROVIDE AN 'VALID-DATA' !")
                            sys.exit("\t>>> SOMETHING WENT WRONG, TRY AGAIN !")

                elif choice == 2:
                    # DISPLAY, 'STACK' :
                    dsa_stack.display_stack()
                    # POP-METHOD :
                    dsa_stack.pop_method()

                elif choice == 3:
                    # DISPLAY, 'STACK' :
                    dsa_stack.display_stack()

                else:
                    print("\n\t>>> SORRY, SEEM LIKE, U HAVE CHOSEN 'WRONG-OPTION', TRY AGAIN !")
            except ValueError:
                print("\n\t>>> SORRY, SEEMS LIKE U DIDN'T PROVIDE AN 'VALID-CHOICE' !")
                sys.exit("\t>>> SOMETHING WENT WRONG, TRY AGAIN !")
