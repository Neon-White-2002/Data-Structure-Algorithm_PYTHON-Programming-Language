# SINGLE-LINKED-LIST (PYTHON) :

import sys  # PYTHON (PACKAGE), TO 'EXIT'

# CLASS-NODE :
class Node:
    # CONSTRUCTOR (CLASS), NODE :
    def __init__(self, value):
        self.data = value
        self.next = None


# CLASS-SINGLE-LINKED-LIST :
class single_linked_list:
    # CONSTRUCTOR (CLASS), SINGLE-LINKED-LIST :
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    """ => SINGLE-LINKED-LIST (METHOD'S) :
            -> APPEND-NODE
            -> DELETE-NODE
            -> UPDATE-NODE
            -> INSERT-NODE
            -> SEARCH-NODE
            -> REVERSE-LINKED-LIST
            -> DISPLAY-LINKED-LIST
    """

    # APPEND-NODE :
    def append_node(self, value):
        # GENERATE, NEW-NODE :
        add_node = Node(value)

        # CHECK, WEATHER 'HEAD-NODE' IS NULL OR NOT :
        if self.length == 0 or self.head is None:
            # SET, 'HEAD & TAIL (NODE)', TO 'NEW-NODE' :
            self.head = add_node
            self.tail = add_node
        else:
            # SET, 'TAIL-NODE' => NEXT-POINTER, TO 'NEW-NODE' :
            self.tail.next = add_node
            self.tail = add_node
        # INCREMENT, LENGTH :
        self.length += 1

        # DISPLAY, RESULT :
        print("\n\t>>> ----- YA, 'NODE' (APPEND) - SUCCESSFULLY ! -----")

    # DELETE-NODE :
    def delete_node(self, value):
        # TEMPORARY-NODE :
        current_node = self.head
        previous_node = self.head
        # STORE, RESULT :
        result = None
        # STORE, DELETED-NODE :
        deleted_node = None

        # CHECK, WEATHER 'HEAD-NODE', IS NULL OR NOT :
        if self.length == 0 or self.head is None:
            result = "\n\t>>> ----- SORRY, SEEMS LIKE 'LINKED-LIST', IS EMPTY ! -----"
        elif self.head.data == value:
            # STORE, 'HEAD-NODE' :
            deleted_node = self.head

            # UPDATE, HEAD-POINTER :
            self.head = self.head.next
            # DECREMENT, LENGTH :
            self.length -= 1

            # CHECK, WEATHER 'LENGTH', IS 'ZERO' OR NOT :
            if self.length == 0:
                self.head = None
                self.tail = None

            # UPDATE, RESULT :
            deleted_node.next = None
            result = (f"\n\t>>> YA, 'HEAD-NODE' (DELETED) - SUCCESSFULLY ! -----" +
                      f"\n\t>>> DELETED-NODE : {deleted_node.data}" +
                      f"\n\t>>> DELETED-NODE (NEXT-POINTER) : {deleted_node.next}")
        else:
            while current_node is not None:
                # HERE, CHECK, WEATHER 'CURRENT-NODE', IS EQUAL TO 'VALUE' :
                if current_node.data == value:
                    # CHECK, WEATHER 'CURRENT-NODE', IS EQUAL TO 'TAIL-NODE' :
                    if current_node.data == self.tail.data:
                        # UPDATE, 'PREVIOUS-NEXT', TO 'CURRENT-NEXT' :
                        previous_node.next = current_node.next
                        # UPDATE, 'TAIL-NODE' :
                        self.tail = previous_node
                        # DECREMENT, LENGTH :
                        self.length -= 1

                        # UPDATE, RESULT :
                        result = (("\n\t>>> ----- YA, 'TAIL-NODE' (DELETED) - SUCCESSFULLY !" +
                                  f"\n\t>>> DELETED-NODE : {current_node.data}") +
                                  f"\n\t>>> DELETED-NODE (NEXT-POINTER) : {current_node.next}")

                        # STOP, WHILE-LOOP :
                        break
                    else:
                        # UPDATE, 'PREVIOUS-NEXT', TO 'CURRENT-NEXT' :
                        previous_node.next = current_node.next
                        # HERE, UPDATE (CURRENT-NODE) => NEXT-POINTER, TO 'NULL' :
                        current_node.next = None
                        # DECREMENT, LENGTH :
                        self.length -= 1

                        # UPDATE, RESULT :
                        result = (("\n\t>>> ----- YA, 'NODE' (DELETED) - SUCCESSFULLY !" +
                                   f"\n\t>>> DELETED-NODE : {current_node.data}") +
                                  f"\n\t>>> DELETED-NODE (NEXT-POINTER) : {current_node.next}")

                        # STOP, WHILE-LOOP :
                        break
                else:
                    # UPDATE, RESULT :
                    result = "\n\t>>> ----- SORRY, CAN'T FOUND 'NODE' & 'DELETE IT' ! -----"

                # NEXT-POINTER (INCREMENT) :
                previous_node = current_node
                current_node = current_node.next

        # DISPLAY, RESULT :
        print(f"{result}")


    # UPDATE-NODE :
    def update_node(self, old_value, new_value):
        # TEMPORARY-NODE :
        current_node = self.head
        # STORE, RESULT :
        result = None

        # CHECK, WEATHER 'HEAD-NODE', IS NULL OR NOT :
        if self.length == 0 or self.head is None:
            result = "\n\t>>> ----- SORRY, SEEMS LIKE 'LINKED-LIST', IS EMPTY ! -----"
        elif self.head.data == old_value:
            self.head.data = new_value
            result = "\n\t>>> ----- YA, 'HEAD-NODE' (UPDATED) - SUCCESSFULLY ! -----"
        elif self.tail.data == old_value:
            self.tail.data = new_value
            result = "\n\t>>> ----- YA, 'TAIL-NODE' (UPDATED) - SUCCESSFULLY ! -----"
        else:
            while current_node is not None:
                # CHECK, WEATHER CURRENT-NODE, IS EQUAL TO OLD-VALUE :
                if current_node.data == old_value:
                    # THEN, UPDATE CURRENT-NODE (VALUE), TO 'NEW-VALUE' :
                    current_node.data = new_value
                    # UPDATE, RESULT :
                    result = "\n\t>>> ----- YA, 'NODE' (UPDATED) - SUCCESSFULLY ! -----"
                    # STOP, WHILE-LOOP :
                    break
                else:
                    # UPDATE, RESULT (NODE) WAS NOT-FOUND :
                    result = "\n\t>>> ----- SORRY, 'NODE' WAS NOT FOUND & UPDATED ! -----"

                # NEXT-POINTER (INCREMENT) :
                current_node = current_node.next

        # DISPLAY, RESULT :
        print(f"{result}")

    # INSERT-NODE :
    def insert_node(self, index, value):
        # TEMPORARY-NODE :
        current_node = self.head
        previous_node = self.head
        # STORE, RESULT :
        result = None

        # CHECK, WEATHER 'HEAD-NODE', IS EMPTY OR NOT :
        if index < 0 or index >= self.length:
            result = "\n\t>>> ----- SORRY, 'INDEX' IS OUT OF BOUND, TRY AGAIN !"
        elif index == 0:
            # GENERATE, NEW-NODE :
            prepend_node = Node(value)

            # PREPEND-NODE (METHOD) :
            prepend_node.next = self.head
            self.head = prepend_node

            # INCREMENT-LENGTH :
            self.length += 1

            # UPDATE, RESULT :
            result = "\n\t>>> ----- YA, 'NODE' (INSERTED) - SUCCESSFULLY AT 'HEAD-POSITION' ! -----"
        elif index == self.length - 1:
            # GENERATE, NEW-NODE :
            add_node = Node(value)

            # APPEND-NODE :
            self.tail.next = add_node
            self.tail = add_node

            # INCREMENT-LENGTH :
            self.length += 1

            # UPDATE, RESULT :
            result = "\n\t>>> ----- YA, 'NODE' (INSERTED) - SUCCESSFULLY AT 'TAIL-POSITION' ! -----"
        else:
            # GENERATE, NEW-NODE :
            insert_node = Node(value)

            # INSERT-NODE (IN BETWEEN) :
            for i in range(index):
                # HERE, WEILL (INCREMENT) NEXT-POINTER, THEN 'STORE' PREVIOUS-NODE => (CURRENT-NODE ---> PREVIOUS-POINTER) & CURRENT-NODE => (INDEX) :
                previous_node = current_node
                current_node = current_node.next

            # HERE, WE WILL SET : (PREVIOUS-NODE) => NEXT-POINTER, TO 'NEW-NODE' :
            previous_node.next = insert_node
            # THEN, SET 'NEW-NODE' => NEXT-POINTER, TO CURRENT-NODE :
            insert_node.next = current_node
            # INCREMENT-LENGTH :
            self.length += 1

            # UPDATE, RESULT :
            result = f"\n\t>>> ----- YA, 'NODE' (INSERTED) - SUCCESSFULLY AT : '{index}TH' POSITION, IN LINKED-LIST !"

        # DISPLAY, RESULT :
        print(f"{result}")

    # SEARCH-NODE :
    def search_node(self, value):
        # TEMPORARY-NODE :
        current_node = self.head
        # STORE, RESULT :
        result = None
        # COUNTER :
        count = 0

        # CHECK, WEATHER 'HEAD-NODE', IS NULL OR NOT :
        if self.length == 0 or self.head is None:
            result = "\n\t>>> ----- SORRY, SEEMS LIKE 'LINKED-LIST', IS EMPTY ! -----"
        elif self.head.data == value:
            result = f"\n\t>>> ----- YA, 'HEAD-NODE' FOUND AT : 'OTH' POSITION, IN LINKED-LIST ! -----"
        elif self.tail.data == value:
            result = f"\n\t>>> ----- YA, 'TAIL-NODE' FOUND AT : '{self.length}' POSITION, IN LINKED-LIST ! -----"
        else:
            while current_node is not None:
                # CHECK, WEATHER CURRENT-NODE, IS EQUAL TO 'VALUE' :
                if current_node.data == value:
                    # UPDATE, RESULT :
                    result = f"\n\t>>> ----- YA, 'NODE' FOUND AT : '{count + 1}' POSITION, IN LINKED-LIST ! -----"
                    # STOP, WHILE-LOOP :
                    break
                else:
                    # UPDATE, RESULT (NODE) WAS NOT-FOUND :
                    result = "\n\t>>> ----- SORRY, 'NODE' WAS NOT FOUND ! -----"
                # NEXT-POINTER (INCREMENT) :
                current_node = current_node.next
                # INCREMENT, COUNTER :
                count += 1

        # DISPLAY, RESULT :
        print(f"{result}")

    # REVERSE-LINKED-LIST :
    def reverse_linked_list(self):
        # TEMPORARY-NODE'S :
        current_node = self.head    # CURRENT-NODE (HEAD-NODE)
        next_node = current_node.next   # NEXT-NODE (CURRENT-NODE => NEXT-POINTER)
        previous_node = None    # PREVIOUS-NODE (NULL)

        for i in range(self.length):
            # SET, NEXT-NODE TO, CURRENT-NODE (NEXT-POINTER) :
            next_node = current_node.next
            # SET, CURRENT-NODE (NEXT-POINTER) TO, PREVIOUS-NODE :
            current_node.next = previous_node
            # SET, PREVIOUS-NODE TO, CURRENT-NODE :
            previous_node = current_node
            # UPDATE, (INCREMENT) OF : CURRENT-NODE TO, 'NEXT-NODE' :
            current_node = next_node

        # SWAP-NODE'S :
        temporary_node = self.head
        self.head = self.tail
        self.tail = temporary_node

        # DISPLAY, RESULT :
        print("\n\t>>> ----- YA, 'SINGLE-LINKED-LIST' WAS 'REVERSE' - SUCCESSFULLY ! -----")
    # DISPLAY-LINKED-LIST :
    def display_linked_list(self):
        # TEMPORARY-NODE :
        current_node = self.head

        # CHECK, WEATHER 'LINKED-LIST', IS 'EMPTY' OR 'NOT' :
        if self.head is None:
            print("\n\t>>> ----- SORRY, SEEMS LIKE 'SINGLE-LINKED-LIST', IS EMPTY -----")
        else:
            print("\n\t>>> SINGLE-LINKED-LIST : ", end=" ")
            while current_node is not None:
                print(f"{current_node.data} -> ", end="")
                # NEXT-POINTER (INCREMENT) :
                current_node = current_node.next

        # SINGLE-LINKED-LIST (PARAMETER'S) - VALUE :
        if self.head is None:
            print(f"\n\t>>> HEAD-NODE : {self.head}")
            print(f"\t>>> TAIL-NODE : {self.tail}")
            print(f"\t>>> LENGTH : {self.length}")
        else:
            # DISPLAY, (DATA) OF 'HEAD & TAIL' - NODE :
            print(f"\n\n\t>>> HEAD-NODE : {self.head.data}")
            print(f"\t>>> TAIL-NODE : {self.tail.data}")
            print(f"\t>>> LENGTH : {self.length}")


# MAIN-METHOD :
if __name__ == '__main__':
    # OBJECT, OF CLASS (SINGLE-LINKED-LIST) :
    linked_list = single_linked_list()

    # SINGLE-LINKED-LIST (MENU) :
    while True:
        print("\n\t---------- WELCOME TO, SINGLE-LINKED-LIST (MENU) ----------")
        print("\t>>> PRESS (1) : ADD-NODE")
        print("\t>>> PRESS (2) : DELETE-NODE")
        print("\t>>> PRESS (3) : UPDATE-NODE")
        print("\t>>> PRESS (4) : INSERT-NODE")
        print("\t>>> PRESS (5) : SEARCH-NODE")
        print("\t>>> PRESS (6) : REVERSE-LINKED-LIST")
        print("\t>>> PRESS (7) : DISPLAY-LINKED-LIST")

        option = str(input("\n\t>>> ENTER, YOUR OPTION : "))
        try:
            if len(option) == 0:
                print("\n\t>>> ----- PLEASE, PROVIDE AN 'OPTION' ! -----")
                sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
            else:
                option = int(option)
                # LINKED-LIST (OPTION-MENU) :
                if option == 1:
                    # APPEND-NODE (METHOD) :
                    value = str(input("\n\t>>> ENTER, DATA U WANT TO ADD : "))
                    try:
                        if len(value) == 0:
                            print("\n\t>>> ----- PLS, PROVIDE AN 'DATA' -----")
                            sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                        else:
                            # UPDATE, DATA-TYPE (INTEGER) :
                            value = int(value)
                            # APPEND-NODE (FUNCTION) :
                            linked_list.append_node(value)
                    except ValueError:
                        print("\n\t>>> ----- SORRY, WRONG 'DATA OR VALUE', TRY AGAIN ! -----")
                        sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                elif option == 2:
                    # CHECK, WEATHER 'LINKED-LIST', IS EMPTY OR NOT :
                    if linked_list.length == 0 or linked_list.head is None:
                        print("\n\t>>> ----- SORRY, SEEMS LIKE 'SINGLE-LINKED-LIST', IS EMPTY ! -----")
                    else:
                        # DISPLAY, LINKED-LIST :
                        linked_list.display_linked_list()

                        # DELETE-NODE (METHOD) :
                        delete_value = str(input("\n\t>>> ENTER, DATA U WANT TO DELETE : "))
                        try:
                            if len(delete_value) == 0:
                                print("\n\t>>> ----- PLS, PROVIDE AN 'DATA' -----")
                                sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                            else:
                                # UPDATE, DATA-TYPE (INTEGER) :
                                delete_value = int(delete_value)
                                # DELETE-NODE (FUNCTION) :
                                linked_list.delete_node(delete_value)
                        except ValueError:
                            print("\n\t>>> ----- SORRY, WRONG 'DATA OR VALUE', TRY AGAIN ! -----")
                            sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                elif option == 3:
                    # CHECK, WEATHER 'LINKED-LIST', IS EMPTY OR NOT :
                    if linked_list.length == 0 or linked_list.head is None:
                        print("\n\t>>> ----- SORRY, SEEMS LIKE 'SINGLE-LINKED-LIST', IS EMPTY ! -----")
                    else:
                        # DISPLAY, LINKED-LIST :
                        linked_list.display_linked_list()

                        # UPDATE-NODE (METHOD) :
                        old_value = str(input("\n\t>>> ENTER, OLD-VALUE : "))
                        new_value = str(input("\n\t>>> ENTER, NEW-VALUE : "))
                        try:
                            if len(old_value) == 0 or len(new_value) == 0:
                                print("\n\t>>> ----- PLS, PROVIDE AN 'DATA' -----")
                                sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                            else:
                                # UPDATE, DATA-TYPE (INTEGER) :
                                old_value = int(old_value)
                                new_value = int(new_value)
                                # UPDATE-NODE (FUNCTION) :
                                linked_list.update_node(old_value, new_value)
                        except ValueError:
                            print("\n\t>>> ----- SORRY, WRONG 'DATA OR VALUE', TRY AGAIN ! -----")
                            sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                elif option == 4:
                    # CHECK, WEATHER 'LINKED-LIST', IS EMPTY OR NOT :
                    if linked_list.length == 0 or linked_list.head is None:
                        # APPEND-NODE :
                        add_data = str(input("\n\t>>> ENTER, DATA U WANT TO 'INSERT' : "))
                        try:
                            if len(add_data) == 0:
                                print("\n\t>>> ----- PLS, PROVIDE AN 'DATA' -----")
                                sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                            else:
                                # UPDATE, DATA-TYPE (INTEGER) :
                                add_data = int(add_data)
                                # APPEND-NODE (FUNCTION) :
                                linked_list.append_node(add_data)
                        except ValueError:
                            print("\n\t>>> ----- SORRY, WRONG 'DATA OR VALUE', TRY AGAIN ! -----")
                            sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                    else:
                        # DISPLAY, LINKED-LIST :
                        linked_list.display_linked_list()

                        # INSERT-NODE (METHOD) :
                        index = str(input("\n\t>>> ENTER, INDEX : "))
                        insert_value = str(input("\n\t>>> ENTER, DATA U WANT TO INSERT : "))
                        try:
                            if len(insert_value) == 0 or len(index) == 0:
                                print("\n\t>>> ----- PLS, PROVIDE AN 'DATA & INDEX' -----")
                                sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                            else:
                                # UPDATE, DATA-TYPE (INTEGER) :
                                index = int(index)
                                insert_value = int(insert_value)
                                # INSERT-NODE (FUNCTION) :
                                linked_list.insert_node(index, insert_value)
                        except ValueError:
                            print("\n\t>>> ----- SORRY, WRONG 'DATA OR VALUE', TRY AGAIN ! -----")
                            sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                elif option == 5:
                    # CHECK, WEATHER 'LINKED-LIST', IS EMPTY OR NOT :
                    if linked_list.length == 0 or linked_list.head is None:
                        print("\n\t>>> ----- SORRY, SEEMS LIKE 'SINGLE-LINKED-LIST', IS EMPTY ! -----")
                    else:
                        # DISPLAY, LINKED-LIST :
                        linked_list.display_linked_list()

                        # SEARCH-NODE (METHOD) :
                        search_value = str(input("\n\t>>> ENTER, DATA YOU WANT TO SEARCH : "))
                        try:
                            if len(search_value) == 0:
                                print("\n\t>>> ----- PLS, PROVIDE AN 'DATA' -----")
                                sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                            else:
                                # UPDATE, DATA-TYPE (INTEGER) :
                                search_value = int(search_value)
                                # UPDATE-NODE (FUNCTION) :
                                linked_list.search_node(search_value)
                        except ValueError:
                            print("\n\t>>> ----- SORRY, WRONG 'DATA OR VALUE', TRY AGAIN ! -----")
                            sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                elif option == 6:
                    # REVERSE, 'SINGLE-LINKED-LIST' :
                    linked_list.reverse_linked_list()
                elif option == 7:
                    # DISPLAY, LINKED-LIST :
                    linked_list.display_linked_list()
        except ValueError:
            print("\n\t>>> ----- SORRY, WRONG 'DATA OR VALUE', TRY AGAIN ! -----")
            sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
