def lookup(obj):
    """Return a list of available attributes and methods of an object.

    This function retrieves the names of all attributes and methods of the 
    given object, including those inherited from its class hierarchy.
    """
    return dir(obj)

