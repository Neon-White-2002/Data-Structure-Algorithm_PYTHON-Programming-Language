# DATA-STRUCTURE & ALGORITHM - QUEUE (PYTHON) :

import sys  # PYTHON-MODULE :)

# CLASS (NODE) :
class Node:
    # CONSTRUCTOR (GENERATE, NEW-NODE) :
    def __init__(self, value):
        # NODE-DATA :
        self.data = value
        # NODE-NEXT-POINTER :
        self.next = None

# CLASS (QUEUE) :
class Queue:
    # CONSTRUCTOR (QUEUE) :
    def __init__(self):
        self.first = None
        self.last = None
        # TRACK, QUEUE-LENGTH :
        self.length = 0

    # EN-QUEUE (APPEND-NODE) :
    def enqueue_method(self, value):
        # GENERATE, NEW-NODE :
        add_node = Node(value)

        # CHECK, WEATHER 'QUEUE', IS 'EMPTY' :
        if self.length == 0:
            # SET, 'FIRST & LAST (POINTER)', AS 'NEW-NODE' :
            self.first = add_node
            self.last = add_node
        else:
            # UPDATE, 'NEW-NODE', AS 'LAST-POINTER' :
            self.last.next = add_node
            self.last = add_node

        # INCREMENT-LENGTH :
        self.length += 1

        # DISPLAY, RESULT :
        print("\n\t>>> YA ! 'NEW-NODE' (EN-QUEUE : APPEND) - SUCCESSFULLY...! ;)")

    # DE-QUEUE (REMOVE-NODE) :
    def dequeue_method(self):
        # CHECK, WEATHER 'QUEUE', IS 'EMPTY' :
        if self.length == 0:
            # DISPLAY, RESULT :
            print("\n\t>>> OOPS ! SEEMS LIKE 'QUEUE', IS AL-READY 'EMPTY' :( \n")
            print("\t>>> FIRST : NULL")
            print("\t>>> LAST : NULL")
            print(f"\t>>> LENGTH : {self.length}")
        else:
            # GENERATE, TEMPORARY-NODE :
            deleted_node = self.first

            # SET, 'FIRST-POINTER' :
            self.first = self.first.next
            deleted_node.next = None
            # DECREMENT-LENGTH :
            self.length -= 1

            # NOW, CHECK WEATHER 'QUEUE', IS 'EMPTY' :
            if self.length == 0:
                # THEN, SET 'FIRST & LAST (POINTER)' AS, 'NULL' :
                self.first = None
                self.last = None

            # DISPLAY, RESULT :
            print("\n\t>>> YA ! 'NODE' (DE-QUEUE : REMOVE) - SUCCESSFULLY...! ;) \n" +
                  f"\t>>> DELETED-NODE : {deleted_node.data} \n" +
                  f"\t>>> DELETED-NODE (NEXT-POINTER) : {deleted_node.next}")

    # DISPLAY, 'QUEUE' :
    def display_queue(self):
        # CHECK, WEATHER 'QUEUE', IS 'EMPTY' :
        if self.length == 0:
            print("\n\t>>> OOPS ! SEEMS LIKE 'QUEUE', IS AL-READY 'EMPTY' :( \n")
            print(f"\t>>> FIRST : {self.first}")
            print(f"\t>>> LAST : {self.last}")
            print(f"\t>>> LENGTH : {self.length}")
        else:
            # GENERATE, TEMPORARY-NODE :
            current_node = self.first

            print("\n\t>>> QUEUE : ", end="")
            for i in range(self.length):
                print(f"{current_node.data} -->", end=" ")
                # NEXT-NODE (INCREMENT) :
                current_node = current_node.next

            # SET, 'NULL' (LAST-NEXT : POINTER) :
            print("NULL", end="\n\n")

            # DISPLAY, 'QUEUE (PARAMETER'S)' :
            print(f"\t>>> FIRST : {self.first.data}")
            print(f"\t>>> LAST : {self.last.data}")
            print(f"\t>>> LENGTH : {self.length}")

# MAIN-METHOD :
if __name__ == '__main__':
    # OBJECT, INITIALIZATION (CLASS - QUEUE) :
    queue = Queue()

    # INFINITY-LOOP :
    while True:
        print("\n\t----- WELCOME TO, 'QUEUE (MENU)' ----- \n")
        print("\t>>> PRESS (1) : EN-QUEUE (APPEND-NODE)")
        print("\t>>> PRESS (2) : DE-QUEUE (REMOVE-NODE)")
        print("\t>>> PRESS (3) : DISPLAY, 'QUEUE'")

        # USER-INPUT :
        option = str(input("\n\t>>> ENTER, YOUR CHOICE : "))
        if len(option) == 0:
            print("\n\t>>> OOPS ! SEEMS LIKE U DIDN'T PROVIDE AN 'CHOICE', TRY AGAIN :(")
            sys.exit("\t>>> SOMETHING WENT WRONG, TRY AGAIN !")
        else:
            try:
                # CONVERT, DATA-TYPE (INTEGER) :
                option = int(option)
                # QUEUE-MENU :
                if option == 1:
                    # EN-QUEUE (APPEND-METHOD) :
                    data = str(input("\n\t>>> ENTER 'DATA', U WANT TO 'ADD' : "))
                    # CHECK, WEATHER 'DATA', IS 'EMPTY' :
                    if len(data) == 0:
                        print("\n\t>>> OOPS ! SEEMS LIKE U DIDN'T PROVIDE AN 'DATA', TRY AGAIN :(")
                        sys.exit("\t>>> SOMETHING WENT WRONG, TRY AGAIN !")
                    else:
                        try:
                            # CONVERT, DATA-TYPE (INTEGER) :
                            data = int(data)
                            # EN-QUEUE (FUNCTION) :
                            queue.enqueue_method(data)
                        except ValueError:
                            print("\n\t>>> OOPS ! SEEMS LIKE IT WAS 'IN-VALID' - DATA, TRY AGAIN :(")
                            sys.exit("\t>>> SOMETHING WENT WRONG, TRY AGAIN !")

                elif option == 2:
                    # DISPLAY, 'QUEUE' :
                    queue.display_queue()
                    # DE-QUEUE (REMOVE-NODE) :
                    queue.dequeue_method()

                elif option == 3:
                    # DISPLAY, 'QUEUE' :
                    queue.display_queue()

                else:
                    print("\n\t>>> SORRY, SEEMS LIKE 'WRONG' CHOICE ! :(")

            except ValueError:
                print("\n\t>>> OOPS ! SEEMS LIKE IT WAS 'IN-VALID' CHOICE, TRY AGAIN :(")
                sys.exit("\t>>> SOMETHING WENT WRONG, TRY AGAIN !")
