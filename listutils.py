def convert_list_to_lowercase(list):
    """Converts all elements of list to lower case.

    Parameters
    ----------

    list:       list of strings
        List to convert to lowercase.

    Returns
    ----------

    list of strings (converted to lowercase)
    """
    return [x.lower() for x in list]

def get_longest_list_length(lists):
    """Get length of longest list in list of lists.

    Parameters
    ----------

    list:       list of lists
        Lists to analyse.

    Returns
    ----------

    int (longest list length)
    """
    return max([len(d) for d in lists])

def flatten_list(list):
    """Flatten e.g. [[1,2],[2,3]] -> [1,2,2,3]

    Parameters
    ----------

    list:       list (potentially containing sub-lists)
        List to process.

    Returns
    ----------
    
    list (flattened)
    """
    return [i for t in [v for v in list] for i in t]