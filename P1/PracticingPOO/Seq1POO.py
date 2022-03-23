class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases

        print("New sequence created!")

    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        return len(self.strbases)

