class Person:

    def __init__(self, name='N/A', birth_date='N/A', death_date=""):
        self.__name = name
        self.__birth_date = birth_date
        self.__death_date = death_date
        self.__parent = None
        self.__children = []

    def add_child(self, person):
        person.__parent = self
        self.__children.append(person)

    def delete_child(self, name):
        for person in self.__children:
            if person.__name == name:
                self.__children.remove(person)

    def get_age(self):
        birth_year = self.__birth_date[0:4]
        birth_month = self.__birth_date[5:7]
        birth_day = self.__birth_date[8:]
        death_year = self.__death_date[0:4]
        death_month = self.__death_date[5:7]
        death_day = self.__death_date[8:]
        year_difference = int(death_year) - int(birth_year)
        month_difference = int(death_month) - int(birth_month)
        day_difference = int(death_day) - int(birth_day)

        if month_difference > 0:
            return year_difference

        elif month_difference == 0 and day_difference >= 0:
            return year_difference

        else:
            return year_difference - 1

    def get_birth_date(self):
        return self.__birth_date

    def get_child(self, name):
        for person in self.__children:

            if person.__name == name:
                return person

    def get_children(self):
        return self.__children

    def get_death_date(self):
        return self.__death_date

    def get_name(self):
        return self.__name

    def get_parent(self):
        return self.__parent

    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date
        return self.__birth_date

    def set_death_date(self, death_date):
        self.__death_date = death_date
        return self.__death_date

    def set_name(self, name):
        self.__name = name
        return self.__name

    def set_parent(self, parent):
        self.__parent = parent
        return self.__parent

    def __str__(self):
        death_symbol = ""
        death_date = ""
        age_text = ""

        if self.__death_date != "":
            death_symbol = " ✝"
            death_date = self.__death_date
            age = self.get_age()
            age_text = " (" + str(age) + ")"

        text = self.__name + " *" + self.__birth_date + death_symbol + death_date + age_text
        return text

    def __eq__(self, other):

        if isinstance(other, Person):

            if other.__name == self.__name:

                if self.__birth_date[0:7] == other.__birth_date[0:7] and \
                        self.__death_date[0:7] == other.__death_date[0:7]:

                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


def header(current_person):
    """
      prints header and gets option from user

        Parameters:
          current_person: the current person in the system(for header, getting
           info from current person, making changes to current person, and relatives)

        Returns:
          option

        """
    # Start of statements for the header function

    print("------------------------------------------------------")
    print(current_person)
    print("------------------------------------------------------")
    print(" 1) Edit name                 6) Print statistics")
    print(" 2) Edit date of birth        7) Print children")
    print(" 3) Edit date of death        8) Print grandchildren")
    print(" 4) Add a child               9) Print aunts/uncles")
    print(" 5) Delete a child           10) Print cousins")
    print()
    print("11) Enter child's family     12) Enter parent's family")
    print()
    option = int(input("Select option (or 0 to exit): "))
    print()
    return option


def option_0():
    """
      exits the program

        """
    # Start of statements for the header function
    print()
    exit()


def option_1(current_person):
    """
      changes name of current_person

        Parameters:
          current_person: the current person in the system(for header, getting
           info from current person, making changes to current person, and relatives)

        """
    # Start of statements for the option_1 function
    new_name = input("Enter name: ")

    while new_name == "":
        new_name = input("ERROR: No name entered, try again: ")

    print()

    current_person.set_name(new_name)


def option_2(current_person):
    """
      changes birthday of current_person from user input

        Parameters:
          current_person: the current person in the system(for header, getting
           info from current person, making changes to current person, and relatives)

        """
    # Start of statements for the option_2 function
    new_birth_date = input("Enter date of birth: ")
    b_d_test = False

    while not b_d_test:

        if len(new_birth_date) == 10:

            if new_birth_date[0:4].isnumeric() and new_birth_date[5:7].isnumeric():

                if new_birth_date[8:].isnumeric and new_birth_date[4] == "-" and new_birth_date[7] == "-":

                    b_d_test = True
        else:
            new_birth_date = input("ERROR: Must follow 1970-01-01 format, try again: ")

    current_person.set_birth_date(new_birth_date)
    print()


def option_3(current_person):
    """
      changes death_date of current_person from user input

        Parameters:
          current_person: the current person in the system(for header, getting
           info from current person, making changes to current person, and relatives)

        """
    # Start of statements for the option_3 function
    new_death_date = input("Enter date of death: ")
    d_d_test = False

    while not d_d_test:

        if len(new_death_date) == 10:

            if new_death_date[0:4].isnumeric() and new_death_date[5:7].isnumeric():

                if new_death_date[8:].isnumeric and new_death_date[4] == "-" and new_death_date[7] == "-":

                    d_d_test = True
        else:
            new_death_date = input("ERROR: Must follow 1970-01-01 format, try again: ")

    current_person.set_death_date(new_death_date)
    print()


def option_4(current_person):
    """
      adds a child from user input (name, birthday)

        Parameters:
          current_person: the current person in the system(for header, getting
           info from current person, making changes to current person, and relatives)

        """
    # Start of statements for the option_4 function
    child_name = input("Enter name: ")

    while child_name == "":
        child_name = input("ERROR: No name entered, try again: ")

    child_dob = input("Enter date of birth: ")
    c_dob_test = False

    while not c_dob_test:

        if len(child_dob) == 10:

            if child_dob[0:4].isnumeric() and child_dob[5:7].isnumeric():

                if child_dob[8:].isnumeric and child_dob[4] == "-" and child_dob[7] == "-":

                    c_dob_test = True
        else:
            child_dob = input("ERROR: Must follow 1970-01-01 format, try again: ")

    current_person_1 = Person(child_name, child_dob)

    children = current_person.get_children()
    check = True

    for child in children:

        if current_person_1.__eq__(child):

            print("ERROR: Child with same name, and year and month of birth already exists.")
            check = False

    if check:

        current_person.add_child(current_person_1)

    print()


def option_5(current_person):
    """
      deletes a child from user input

        Parameters:
          current_person: the current person in the system(for header, getting
           info from current person, making changes to current person, and relatives)

        """
    # Start of statements for the option_5 function
    list_of_children = current_person.get_children()

    if not list_of_children:

        print("No children found for " + str(current_person.get_name()) + ".")
        print()

    else:
        counter = 1

        for child in list_of_children:

            print(str(counter) + ") " + str(child.get_name()))
            counter += 1

        delete_choice = int(input("Select a child (or 0 to go back to main menu): "))
        print()

        if delete_choice == 0:

            print("Returning to main menu.")
            print()

        else:

            child = list_of_children[delete_choice - 1]
            child_name = child.get_name()
            print(str(child.get_name()) + " deleted.")
            current_person.delete_child(child_name)
            print()


def option_6(current_person):
    """
      prints statistics on children and grandchildren of current_person

        Parameters:
          current_person: the current person in the system(for header, getting
           info from current person, making changes to current person, and relatives)

        """
    # Start of statements for the option_6 function
    children_list = current_person.get_children()
    total_grandchildren = 0

    for child in children_list:

        num_children_for_child = len(child.get_children())
        total_grandchildren += int(num_children_for_child)

    print("Number of children: " + str(len(children_list)))
    print("Number of grandchildren: " + str(total_grandchildren))
    print()


def option_7(current_person):
    """
      prints children of current_person

        Parameters:
          current_person: the current person in the system(for header, getting
           info from current person, making changes to current person, and relatives)

        """
    # Start of statements for the option_7 function
    list_of_children = current_person.get_children()

    if not list_of_children:
        print("No children found for " + str(current_person.get_name()) + ".")
        print()

    else:
        print("Children of " + str(current_person.get_name()) + ":")

        for child in list_of_children:

            print("- ", end="")
            print(child)

        print()


def option_8(current_person):
    """
      prints grandchildren of current_person

        Parameters:
          current_person: the current person in the system(for header, getting
           info from current person, making changes to current person, and relatives)

        """
    # Start of statements for the option_8 function
    children_list = current_person.get_children()
    grandchildren_list = []

    for child in children_list:

        grandchildren = child.get_children()

        for grandchild in grandchildren:

            grandchildren_list.append(grandchild)

    if not grandchildren_list:

        print("No grandchildren found for " + str(current_person.get_name()) + ".")

    else:
        print("Grandchildren of " + str(current_person.get_name()) + ":")

        for grandchild in grandchildren_list:

            print("- ", end="")
            print(grandchild)

    print()


def option_9(current_person):
    """
     prints aunts and uncles of current_person

        Parameters:
          current_person: the current person in the system(for header, getting
           info from current person, making changes to current person, and relatives)

        """
    # Start of statements for the option_9 function
    parent_a = current_person.get_parent()

    if parent_a is None:
        print("No aunts and uncles found for " + str(current_person.get_name()) + ".")

    else:
        grand_parent = parent_a.get_parent()

        if grand_parent is None:
            print("No aunts and uncles found for " + str(current_person.get_name()) + ".")

        else:

            list_of_aunts_and_uncles = grand_parent.get_children()
            list_of_aunts_and_uncles.remove(parent_a)

            if not list_of_aunts_and_uncles:
                print("No aunts and uncles found for " + str(current_person.get_name()) + ".")

            else:
                print("Aunts and uncles of " + str(current_person.get_name()) + ":")

                for person in list_of_aunts_and_uncles:

                    print("- ", end="")
                    print(person)
    print()


def option_10(current_person):
    """
      prints cousins of current_person

        Parameters:
          current_person: the current person in the system(for header, getting
           info from current person, making changes to current person, and relatives)

        """
    # Start of statements for the option_10 function
    parent_a = current_person.get_parent()

    if parent_a is None:
        print("No cousins found for " + str(current_person.get_name()) + ".")

    else:

        grand_parent = parent_a.get_parent()

        if grand_parent is None:
            print("No cousins found for " + str(current_person.get_name()) + ".")

        else:
            list_of_aunts_and_uncles = grand_parent.get_children()

            if not list_of_aunts_and_uncles:
                print("No cousins found for " + str(current_person.get_name()) + ".")

            else:
                cousins = []

                if parent_a in list_of_aunts_and_uncles:

                    list_of_aunts_and_uncles.remove(parent_a)

                for person in list_of_aunts_and_uncles:

                    children = person.get_children()

                    for child in children:
                        cousins.append(child)

                if not cousins:

                    print("No cousins found for " + str(current_person.get_name()) + ".")

                else:

                    print("Cousins of " + str(current_person.get_name()) + ":")

                    for cousin in cousins:

                        print("- ", end="")
                        print(cousin)
    print()


def option_11(current_person):
    """
      enters child's family

        Parameters:
          current_person: the current person in the system(for header, getting
           info from current person, making changes to current person, and relatives)

        Returns:
          current_person

        """
    # Start of statements for the option_11 function
    list_of_children = current_person.get_children()
    current_person = current_person

    if not list_of_children:

        print("No children found for " + str(current_person.get_name()) + ".")
        print()

    else:
        counter = 1
        for child in list_of_children:

            print(str(counter) + ") " + str(child.get_name()))
            counter += 1

        new_user = int(input("Select a child (or 0 to go back to main menu): "))
        print()

        if new_user == 0:

            print("Returning to main menu.")
            print()

        else:
            new_current_person = list_of_children[new_user - 1]
            print("Entering family of " + str(new_current_person.get_name()) + ".")
            current_person = new_current_person
            print()

    return current_person


def option_12(current_person):
    """
      enters parent's family

        Parameters:
          current_person: the current person in the system(for header, getting
           info from current person, making changes to current person, and relatives)

        Returns:
          current_person

        """
    # Start of statements for the option_12 function
    current_person = current_person
    parent = current_person.get_parent()

    if parent is None:

        print("No parent found for " + str(current_person.get_name()) + ".")
        print()

    else:

        print("Entering family of " + str(parent.get_name()) + ".")
        current_person = parent
        print()

    return current_person


def main():

    current_person = Person('John Doe', '1960-01-15', '2020-01-15')
    option = ""

    while option != 0:

        option = header(current_person)

        if option == 0:
            option_0()

        elif option == 1:
            option_1(current_person)

        elif option == 2:
            option_2(current_person)

        elif option == 3:
            option_3(current_person)

        elif option == 4:
            option_4(current_person)

        elif option == 5:
            option_5(current_person)

        elif option == 7:
            option_7(current_person)

        elif option == 11:
            current_person = option_11(current_person)

        elif option == 12:
            current_person = option_12(current_person)

        elif option == 6:
            option_6(current_person)

        elif option == 8:
            option_8(current_person)

        elif option == 9:
            option_9(current_person)

        elif option == 10:
            option_10(current_person)


if __name__ == '__main__':
    main()
