# Object Oriented Programming
# TU856 & TU858
# Semester 1, 2020-21
# Arshad shah
# 11-12-2020

class Document:
    """
    Class to handle file management for file writing.
    Class Document receives the file name at initialisation.
    """

    def __init__(self, file_name):
        self._characters = []
        self._cursor = 0
        self._filename = file_name

    @property
    def charaters(self):
        """
        a getter method to get the characters array

        returns: characters list
        """
        return self._charaters

    @characters.setter
    def set_characters(self,words):
        """
        a setter method for characters

        attributes: strings to insert

        returns: no return
        """
        self._charaters = words

    @property
    def get_cursor(self):
        """
        a getter method to get the cursor position

        returns: cursor position
        """
        return self._cursor

    @cursor.setter
    def set_cursor(self,words):
        """
        a setter method for characters

        attributes: strings to insert

        returns: no return
        """
        self._charaters = words

    def get_filename(self):
        """
        a getter method to get the file name

        returns: name of file
        """
        return self._filename

    def insert(self, character):
        """
        Method inserts a character at the current
        cursor position.
        Argument:
        ---------
        character : str
        the character to insert

        returns: no return
        -------
        """
        self.characters.insert(self.cursor, character)
        self.cursor += 1

    def delete(self):
        """
        Method deletes a character from the current
        cursor position.
        Arguments: none
        Returns: none
        """
        try:
            del self.characters[self.cursor]
        except:
            print("invalid number steps")


    def save(self):
        """
        Method saves all characters in the characters list
        to a file.
        Arguments: none
        Returns: none
        """
        with open(self.filename, 'w') as f:
            f.write(''.join(self.characters))

        print(f"Your file {self.filename} has "
              f"been created.\nPlease check.\n")

    def forward(self, steps):
        """
        Method fowards to a particular position in
        characters [].
        Arguments:
        ----------
        steps: int
            The amount of steps the cursor should be
            pushed forward by

        Returns: none.
        """
        self.cursor += steps

    def backward(self, steps):
        """
        Method backward moves the cursor position to
        that specific location in the characters list.
        Arguments:
        ----------
        steps : int
            The amount of steps to go back

        Returns: none
        """
        self.cursor -= steps

# initialising an object and using the class
doc = Document("lab_t2.txt")
characters = 'fake mews'

for letter in characters:
    doc.insert(letter)

doc.backward(44)
doc.delete()
doc.insert('n')
doc.save()
