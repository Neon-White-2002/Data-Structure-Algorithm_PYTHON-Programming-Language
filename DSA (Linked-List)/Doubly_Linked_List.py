# DOUBLY-LINKED-LIST (PYTHON) :

import sys  # PYTHON PACKAGE, TO (EXIT) :

# CLASS-NODE :
class Node:
    def __init__(self, value):
        # NODE-DATA :
        self.data = value
        # NODE (NEXT-POINTER) :
        self.next = None
        # NODE (PREVIOUS-POINTER) :
        self.previous = None

# CLASS-DOUBLY-LINKED-LIST :
class doubly_linked_list:
    def __init__(self):
        # DOUBLY-LINKED-LIST (PARAMETER'S) :
        self.head = None
        self.tail = None
        # LENGTH, OF 'LINKED-LIST' :
        self.length = 0

    """
        # 'DOUBLY-LINKED-LIST' (METHOD'S) :
        
        => APPEND-NODE
        => DELETE-NODE
        => UPDATE-NODE
        => INSERT-NODE
        => SEARCH-NODE
        => REVERSE-LINKED-LIST
        => DISPLAY-LINKED-LIST
    """

    # APPEND-NODE :
    def append_node(self, value):
        # GENERATE, NEW-NODE :
        new_node = Node(value)

        # CHECK, WEATHER 'LINKED-LIST', IS EMPTY OR NOT :
        if self.length == 0 or self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            #HERE : SET (TAIL-NODE => NEXT) TO, 'NEW-NODE' :
            self.tail.next = new_node
            # HERE : SET (NEW-NODE => PREVIOUS) TO, 'TAIL-NODE' :
            new_node.previous = self.tail
            # NOW, SET 'TAIL-POINTER' TO, 'NEW-NODE' :
            self.tail = new_node
        # INCREMENT, LENGTH :
        self.length += 1

        # DISPLAY, RESULT :
        print("\n\t>>> ----- YA, 'NEW-NODE' (APPEND) - SUCCESSFULLY ! -----")

    # DELETE-NODE :
    def delete_node(self, value):
        # STORE, RESULT :
        result = None
        # STORE, DELETED-NODE :
        deleted_node = None

        # CHECK, WEATHER 'LINKED-LIST', IS EMPTY OR NOT :
        if self.length == 0 or self.head is None:
            result = "\n\t>>> ----- SORRY, SEEMS LIKE 'DOUBLY-LINKED-LIST', IS 'EMPTY' ! -----"
        # CHECK, WEATHER 'HEAD-NODE (DATA)', IS EQUAL TO 'VALUE' :
        elif self.head.data == value:
            # STORE, 'HEAD', AS 'DELETED-NODE' :
            deleted_node = self.head

            # SET, NEW 'HEAD-POINTER' :
            self.head = self.head.next
            # CHECK, WEATHER 'HEAD-NODE', IS NULL OR NOT :
            if self.head is not None:
                # THEN, SET 'PREVIOUS-POINTER', TO 'NULL' :
                self.head.previous = None

            # DECREMENT-LENGTH :
            self.length -= 1

            # HERE, SET 'HEAD & TAIL (NODE-POINTER)', TO 'NULL' :
            if self.length == 0:
                self.head = None
                self.tail = None

            # UPDATE, RESULT :
            deleted_node.next = None
            deleted_node.previous = None
            result = ("\n\t>>> ----- YA, 'HEAD-NODE' (DELETED & UPDATED) - SUCCESSFULLY ! -----\n" +
                      f"\n\t>>> DELETED-NODE : {deleted_node.data}" +
                      f"\n\t>>> DELETED-NODE (NEXT) : {deleted_node.next}" +
                      f"\n\t>>> DELETED-NODE (PREV) : {deleted_node.previous}")
        # CHECK, WEATHER 'TAIL-NODE (DATA)', IS EQUAL TO 'VALUE' :
        elif self.tail.data == value:
            # STORE, 'TAIL', AS 'DELETED-NODE' :
            deleted_node = self.tail

            # SET, NEW-TAIL-POINTER' :
            self.tail = self.tail.previous
            self.tail.next = None

            # DECREMENT-LENGTH :
            self.length -= 1

            # UPDATE, RESULT :
            deleted_node.next = None
            deleted_node.previous = None
            result = ("\n\t>>> ----- YA, 'TAIL-NODE' (DELETED & UPDATED) - SUCCESSFULLY ! -----\n" +
                      f"\n\t>>> DELETED-NODE : {deleted_node.data}" +
                      f"\n\t>>> DELETED-NODE (NEXT) : {deleted_node.next}" +
                      f"\n\t>>> DELETED-NODE (PREV) : {deleted_node.previous}")
        # HERE, 'DELETE-NODE', IN-BETWEEN 'LINKED-LIST' :
        else:
            # TEMPORARY-NODE :
            current_node = self.head
            # PREVIOUS-NODE (CURRENT-NODE) :
            previous_node = self.head

            for i in range(self.length):
                # CHECK, WEATHER 'CURRENT-NODE', IS EQUAL TO 'VALUE' :
                if current_node.data == value:
                    # HERE, SET : (PREVIOUS-NODE => NEXT-POINTER), TO 'CURRENT-NODE => NEXT-POINTER' :
                    previous_node.next = current_node.next
                    # THEN, SET : (CURRENT-NODE => NEXT-PREVIOUS POINTER), TO 'PREVIOUS-NODE' :
                    current_node.next.previous = previous_node
                    # DECREMENT-LENGTH :
                    self.length -= 1

                    # UPDATE, RESULT :
                    current_node.next = None
                    current_node.previous = None
                    result = ("\n\t>>> ----- YA, 'NODE' (DELETED) - SUCCESSFULLY ! -----\n" +
                              f"\n\t>>> DELETED-NODE : {current_node.data}" +
                              f"\n\t>>> DELETED-NODE (NEXT) : {current_node.next}" +
                              f"\n\t>>> DELETED-NODE (PREV) : {current_node.previous}")

                    # STOP, FOR-LOOP :
                    break
                else:
                    # UPDATE, RESULT :
                    result = "\n\t>>> ----- SORRY, SEEMS LIKE 'NODE' WAS NOT-FOUND, SO IT CAN'T BE 'DELETED' ! -----"

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

        # CHECK, WEATHER 'HEAD-NODE (DATA)', IS EQUAL TO 'OLD-VALUE' :
        if self.head.data == old_value:
            # SET, 'HEAD-NODE (DATA)', TO 'NEW-DATA' :
            self.head.data = new_value
            result = "\n\t>>> ----- YA, 'HEAD-NODE' (UPDATED) - SUCCESSFULLY ! -----"
        # CHECK, WEATHER 'TAIL-NODE (DATA)', IS EQUAL TO 'OLD-VALUE' :
        elif self.tail.data == old_value:
            # SET, 'TAIL-NODE (DATA)', TO 'NEW-DATA' :
            self.tail.data = new_value
            result = "\n\t>>> ----- YA, 'TAIL-NODE' (UPDATED) - SUCCESSFULLY ! -----"
        else:
            # HERE, WE WILL 'UPDATE' IN-BETWEEN (NODE), IN LINKED-LIST :
            for i in range(self.length):
                # CHECK, WEATHER 'CURRENT-NODE (DATA)', IS EQUAL TO 'OLD-DATA' :
                if current_node.data == old_value:
                    # HERE, UPDATE 'CURRENT-NODE (DATA)', TO 'NEW-DATA' :
                    current_node.data = new_value
                    # UPDATE, RESULT :
                    result = "\n\t>>> ----- YA, 'NODE' (UPDATED) - SUCCESSFULLY ! -----"
                    # STOP, FOR-LOOP :
                    break
                else:
                    # UPDATE, RESULT :
                    result = "\n\t>>> ----- SORRY, 'NODE' DIDN'T FOUND, SO IT CAN BE 'UPDATED' ! -----"

                # NEXT-POINTER (INCREMENT) :
                current_node = current_node.next

        # DISPLAY, RESULT :
        print(f"{result}")

    # INSERT-NODE :
    def insert_node(self, index, value):
        # STORE, RESULT :
        result = None

        # CHECK, WEATHER 'INDEX', IS 'OUT-OF-BOUND' OR NOT :
        if index < 0 or index >= self.length:
            result = "\n\t>>> ----- OOPS ! SEEMS LIKE 'INDEX', IS 'OUT-OF-BOUND', TRY AGAIN ! -----"
        # CHECK, WEATHER 'INDEX', IS 'ZERO (0)' :
        elif index == 0:
            # GENERATE, NEW-NODE :
            prepend_node = Node(value)

            # PREPEND-NODE :
            self.head.previous = prepend_node
            prepend_node.next = self.head
            self.head = prepend_node

            # INCREMENT, LENGTH :
            self.length += 1

            # UPDATE, RESULT :
            result = "\n\t>>> ----- YA, 'NODE' (INSERTED) AT : 'HEAD-POSITION' - SUCCESSFULLY ! -----"
        # CHECK, WEATHER 'INDEX', IS 'LENGTH' :
        elif index == self.length - 1:
            # GENERATE, NEW-NODE :
            append_node = Node(value)

            # APPEND-NODE :
            self.tail.next = append_node
            append_node.previous = self.tail
            self.tail = append_node

            # INCREMENT, LENGTH :
            self.length += 1

            # UPDATE, RESULT :
            result = "\n\t>>> ----- YA, 'NODE' (INSERTED) AT : 'TAIL-POSITION' - SUCCESSFULLY ! -----"
        # HERE, WE WILL 'INSERT-NODE', IN-BETWEEN :
        else:
            # TEMPORARY-NODE :
            current_node = self.head
            previous_node = self.head

            # GENERATE, NEW-NODE :
            insert_new_node = Node(value)

            # INSERT-NODE, IN BETWEEN 'LINKED-LIST' :
            for i in range(index):
                # NEXT-POINTER (INCREMENT) :
                previous_node = current_node
                current_node = current_node.next

            # HERE, WE WILL INSERT-NODE :
            previous_node.next = insert_new_node
            insert_new_node.next = current_node
            current_node.previous = insert_new_node
            insert_new_node.previous = previous_node

            # INCREMENT, LENGTH :
            self.length += 1

            # UPDATE, RESULT :
            result = f"\n\t>>> ----- YA, 'NODE' (INSERTED) AT : '{index}' POSITION - SUCCESSFULLY ! -----"

        # DISPLAY, RESULT :
        print(f"{result}")

    # SEARCH-NODE :
    def search_node(self, value):
        # STORE, RESULT :
        result = None
        # COUNTER :
        count = 0

        # CHECK, WEATHER 'HEAD-NODE (DATA)', IS EQUAL TO 'VALUE' :
        if self.head.data == value:
            result = "\n\t>>> ----- YA, 'HEAD-NODE' FOUND AT : 'OTH' POSITION, IN 'DOUBLY-LINKED-LIST' ! -----"
        elif self.tail.data == value:
            result = f"\n\t>>> ----- YA, 'TAIL-NODE' FOUND AT : '{self.length}' POSITION, IN 'DOUBLY-LINKED-LIST ! -----"
        else:
            # TEMPORARY-NODE :
            current_node = self.head

            # HERE, WE WILL 'SEARCH-NODE', IN-BETWEEN 'DOUBLY-LINKED-LIST' :
            for i in range(self.length):
                # CHECK, WEATHER 'CURRENT-NODE (DATA)', IS EQUAL TO 'VALUE' :
                if current_node.data == value:
                    # NODE-FOUND (UPDATE, RESULT) :
                    result = f"\n\t>>> ----- YA, 'NODE' FOUND AT : '{count + 1}' POSITION, IN 'DOUBLY-LINKED-LIST' ! -----"
                    # STOP, FOR-LOOP :
                    break
                else:
                    # UPDATE, RESULT :
                    result = "\n\t>>> ----- SORRY, 'NODE' WAS NOT-FOUND, IN 'DOUBLY-LINKED-LIST' ! -----"

                # NEXT-POINTER (INCREMENT) :
                current_node = current_node.next
                # INCREMENT, COUNTER :
                count += 1

        # DISPLAY, RESULT :
        print(f"{result}")

    # REVERSE, 'DOUBLY-LINKED-LIST' :
    def reverse_doubly_linked_list(self):
        # CHECK, WEATHER 'LINKED-LIST', IS EMPTY OR NOT :
        if self.length == 0 or self.head is None:
            print("\n\t>>> ----- SORRY, SEEMS LIKE 'DOUBLY-LINKED-LIST', IS 'EMPTY' ! -----")
        else:
            # TEMPORARY-NODE :
            current_node = self.head
            # PREVIOUS-NODE (NULL) :
            previous_node = None

            # SWAP : (NEXT & PREVIOUS - POINTER) :
            for i in range(self.length):
                # SET : 'PREVIOUS-NODE', TO 'CURRENT-NODE : NEXT-POINTER' :
                previous_node = current_node.previous
                # SET : 'CURRENT-NODE : NEXT-POINTER', TO 'CURRENT-NODE : PREVIOUS-POINTER' :
                current_node.previous = current_node.next
                # SET : 'CURRENT-NODE : NEXT-POINTER', TO 'PREVIOUS-NODE' :
                current_node.next = previous_node
                # UPDATE : 'CURRENT-NODE', TO 'NEXT-NODE' :
                current_node = current_node.previous

            # SWAP 'HEAD & TAIL (NODE' :
            temp_node = self.head
            self.head = self.tail
            self.tail = temp_node
            # DISPLAY, RESULT :
            print("\n\t>>> YA ! 'DOUBLY-LINKED-LIST', IS 'REVERSED' - SUCCESSFULLY ! -----")


    # DISPLAY, 'DOUBLY-LINKED-LIST' :
    def display_doubly_linked_list(self):
        # CHECK, WEATHER 'LINKED-LIST', IS EMPTY OR NOT :
        if self.length == 0 or self.head is None:
            print("\n\t>>> ----- SORRY, SEEMS LIKE 'DOUBLY-LINKED-LIST', IS 'EMPTY' ! ----- \n")

            # DISPLAY, 'DOUBLY-LINKED-LIST' (PARAMETER'S) :
            print(f"\t>>> HEAD-NODE : {self.head}")
            print(f"\t>>> TAIL-NODE : {self.tail}")
            print(f"\t>>> LENGTH : {self.length}")
        else:
            # TEMPORARY-NODE :
            current_node = self.head

            print("\n\t>>> 'DOUBLY-LINKED-LIST' : ", end="")
            for i in range(self.length):
                print(f"{current_node.data} <-->", end=" ")
                # NEXT-POINTER (INCREMENT) :
                current_node = current_node.next

            # DISPLAY, 'DOUBLY-LINKED-LIST' (PARAMETER'S) :
            print(f"\n\n\t>>> HEAD-NODE : {self.head.data}")
            print(f"\t>>> TAIL-NODE : {self.tail.data}")
            print(f"\t>>> LENGTH : {self.length}")

if __name__ == '__main__':
    # OBJECT, OF CLASS : 'DOUBLY-LINKED-LIST' :
    linked_list = doubly_linked_list()

    while True:
        # DOUBLY-LINKED-LIST (MENU) :
        print("\n\t---------- WELCOME TO, DOUBLY-LINKED-LIST (MENU) ----------", end="\n\n")
        print("\t>>> PRESS (1) : APPEND-NODE")
        print("\t>>> PRESS (2) : DELETE-NODE")
        print("\t>>> PRESS (3) : UPDATE-NODE")
        print("\t>>> PRESS (4) : INSERT-NODE")
        print("\t>>> PRESS (5) : SEARCH-NODE")
        print("\t>>> PRESS (6) : REVERSE-LINKED-LIST")
        print("\t>>> PRESS (7) : DISPLAY-LINKED-LIST")

        # USER-INPUT : (CHOICE) :
        option = str(input("\n\t>>> ENTER, YOUR OPTION : "))
        try:
            if len(option) == 0:
                print("\n\t>>> ----- SORRY, PLEASE PROVIDE AN 'OPTION' ! -----")
                sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
            else:
                # CONVERT, DATA-TYPE (INTEGER) :
                option = int(option)

                # LINKED-LIST (MENU) :
                if option == 1:
                    # APPEND-NODE (METHOD) :
                    add_data = str(input("\n\t>>> ENTER, 'DATA' U WANT TO ADD : "))
                    try:
                        if len(add_data) == 0:
                            print("\n\t>>> ----- OOPS ! SEEMS LIKE YOU DIDN'T PROVIDE AN 'DATA' -----")
                            sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                        else:
                            # CONVERT, DATA-TYPE (INTEGER) :
                            add_data = int(add_data)
                            # APPEND-NODE (FUNCTION) :
                            linked_list.append_node(add_data)
                    except ValueError:
                        print(f"\n\t>>> ----- SORRY, SEEMS LIKE 'IN-VALID' DATA ! {ValueError} -----")
                        sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")

                elif option == 2:
                    # CHECK, WEATHER 'LINKED-LIST', IS EMPTY OR NOT :
                    if linked_list.length == 0 or linked_list.head is None:
                        print("\n\t>>> ----- SORRY, SEEMS LIKE 'DOUBLY-LINKED-LIST', IS 'EMPTY' ! -----")
                    else:
                        # DISPLAY, 'DOUBLY-LINKED-LIST' :
                        linked_list.display_doubly_linked_list()

                        # DELETE-NODE (METHOD) :
                        delete_data = str(input("\n\t>>> ENTER, 'DATA' U WANT TO 'DELETE' : "))
                        try:
                            if len(delete_data) == 0:
                                print("\n\t>>> ----- OOPS ! SEEMS LIKE YOU DIDN'T PROVIDE AN 'DATA' -----")
                                sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                            else:
                                # CONVERT, DATA-TYPE (INTEGER) :
                                delete_data = int(delete_data)
                                # DELETE-NODE (FUNCTION) :
                                linked_list.delete_node(delete_data)
                        except ValueError:
                            print(f"\n\t>>> ----- SORRY, SEEMS LIKE 'IN-VALID' DATA ! {ValueError} -----")
                            sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")

                elif option == 3:
                    # CHECK, WEATHER 'LINKED-LIST', IS EMPTY OR NOT :
                    if linked_list.length == 0 or linked_list.head is None:
                        print("\n\t>>> ----- SORRY, SEEMS LIKE 'DOUBLY-LINKED-LIST', IS 'EMPTY' ! -----")
                    else:
                        # DISPLAY, 'DOUBLY-LINKED-LIST' :
                        linked_list.display_doubly_linked_list()

                        # UPDATE-NODE (METHOD) :
                        old_value = str(input("\n\t>>> ENTER, 'OLD-DATA' : "))
                        new_value = str(input("\n\t>>> ENTER, 'NEW-DATA' : "))
                        try:
                            if len(old_value) == 0 or len(new_value) == 0:
                                print("\n\t>>> ----- OOPS ! SEEMS LIKE YOU DIDN'T PROVIDE AN 'DATA' -----")
                                sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                            else:
                                # CONVERT, DATA-TYPE (INTEGER) :
                                old_value = int(old_value)
                                new_value = int(new_value)
                                # UPDATE-NODE (FUNCTION) :
                                linked_list.update_node(old_value, new_value)
                        except ValueError:
                            print(f"\n\t>>> ----- SORRY, SEEMS LIKE 'IN-VALID' DATA ! {ValueError} -----")
                            sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")

                elif option == 4:
                    # DISPLAY, 'DOUBLY-LINKED-LIST' :
                    linked_list.display_doubly_linked_list()

                    # INSERT-NODE (METHOD) :
                    if linked_list.length == 0 or linked_list.head is None:
                        # HERE, WE WILL 'INSERT-NODE', WHEN 'HEAD & TAIL (NODE)', IS 'NULL' :
                        data = str(input("\n\t>>> ENTER, DATA U WANT TO 'INSERT' : "))
                        try:
                            if len(data) == 0:
                                print("\n\t>>> ----- OOPS ! SEEMS LIKE YOU DIDN'T PROVIDE AN 'DATA' -----")
                                sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                            else:
                                # CONVERT, DATA-TYPE (INTEGER) :
                                data = int(data)
                                # ADD-NODE :
                                linked_list.append_node(data)
                        except ValueError:
                            print(f"\n\t>>> ----- SORRY, SEEMS LIKE 'IN-VALID' DATA ! {ValueError} -----")
                            sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                    else:
                        # HERE, WE WILL 'INSERT-NODE', WHEN 'HEAD & TAIL' ARE NOT 'NULL' OR 'EMPTY' :
                        index = str(input("\n\t>>> ENTER, 'INDEX' : "))
                        insert_data = str(input("\n\t>>> ENTER, 'DATA' U WANT TO 'INSERT' : "))
                        try:
                            if len(index) == 0 or len(insert_data) == 0:
                                print("\n\t>>> ----- OOPS ! SEEMS LIKE YOU DIDN'T PROVIDE AN 'DATA' -----")
                                sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                            else:
                                # CONVERT, DATA-TYPE (INTEGER) :
                                index = int(index)
                                insert_data = int(insert_data)
                                # INSERT-NODE (FUNCTION) :
                                linked_list.insert_node(index, insert_data)
                        except ValueError:
                            print(f"\n\t>>> ----- SORRY, SEEMS LIKE 'IN-VALID' DATA ! {ValueError} -----")
                            sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")

                elif option == 5:
                    # CHECK, WEATHER 'LINKED-LIST', IS EMPTY OR NOT :
                    if linked_list.length == 0 or linked_list.head is None:
                        print("\n\t>>> ----- SORRY, SEEMS LIKE 'DOUBLY-LINKED-LIST', IS 'EMPTY' ! -----")
                    else:
                        # DISPLAY, 'DOUBLY-LINKED-LIST' :
                        linked_list.display_doubly_linked_list()

                        # SEARCH-NODE (METHOD) :
                        search_data = str(input("\n\t>>> ENTER, 'DATA' U WANT TO 'SEARCH' : "))
                        try:
                            if len(search_data) == 0:
                                print("\n\t>>> ----- OOPS ! SEEMS LIKE YOU DIDN'T PROVIDE AN 'DATA' -----")
                                sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
                            else:
                                # CONVERT, DATA-TYPE (INTEGER) :
                                search_data = int(search_data)
                                # SEARCH-NODE (FUNCTION) :
                                linked_list.search_node(search_data)
                        except ValueError:
                            print(f"\n\t>>> ----- SORRY, SEEMS LIKE 'IN-VALID' DATA ! {ValueError} -----")
                            sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")

                elif option == 6:
                    # DISPLAY, 'REVERSE-DOUBLY-LINKED-LIST' :
                    linked_list.reverse_doubly_linked_list()

                elif option == 7:
                    # DISPLAY, 'DOUBLY-LINKED-LIST' :
                    linked_list.display_doubly_linked_list()
        except ValueError:
            print("\n\t>>> ----- OOPS ! SEEMS LIKE NOT 'VALID' DATA OR VALUE ! -----")
            sys.exit("\t>>> ----- SOMETHING WENT WRONG, TRY AGAIN ! -----")
