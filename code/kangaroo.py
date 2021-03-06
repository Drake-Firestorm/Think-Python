class Kangaroo:
    def __init__(self, name, contents=[]):
        """Initialize the pouch contents.

        name: string
        contents: initial pouch contents.
        """
        # The problem is the default value for contents.
        # Default values get evaluated ONCE, when the function
        # is defined; they don't get evaluated again when the
        # function is called.

        # In this case that means that when __init__ is defined,
        # [] gets evaluated and contents gets a reference to
        # an empty list.

        # After that, every Kangaroo that gets the default
        # value gets a reference to THE SAME list.  If any
        # Kangaroo modifies this shared list, they all see
        # the change.

        # The next version of __init__ shows an idiomatic way
        # to avoid this problem.
        self.name = name
        self.pouch_contents = contents

    def __init__(self, name, contents=None):
        """Initialize the pouch contents.

        name: string
        contents: initial pouch contents.
        """
        # In this version, the default value is None.  When
        # __init__ runs, it checks the value of contents and,
        # if necessary, creates a new empty list.  That way,
        # every Kangaroo that gets the default value gets a
        # reference to a different list.

        # As a general rule, you should avoid using a mutable
        # object as a default value, unless you really know
        # what you are doing.
        self.name = name
        if contents == None:
            contents = []
        self.pouch_contents = contents

    def put_in_pouch(self, obj):
        self.pouch_contents.append(obj)

    def __str__(self):
        li = [self.name + " has pouch contents:"]
        for item in self.pouch_contents:
            s = '\t' + repr(item)
            li.append(s)
        return "\n".join(li)


if __name__ == "__main__":
    kanga = Kangaroo('Kanga')
    roo = Kangaroo('Roo')
    kanga.put_in_pouch('wallet')
    kanga.put_in_pouch('car keys')
    kanga.put_in_pouch(roo)

    print(kanga)
    print(roo)
