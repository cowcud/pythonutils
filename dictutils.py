# Convert dict {k:v} into array of [k,v]'s
def dict_to_array(dict,np=None):
    """Converts dict {k:v} into array of [k,v]'s.

    Parameters
    ----------

    dict:       dictionary
        dict to convert.
        
    np:
                If require numpy array result, pass imported numpy module.

    Returns
    ----------

    array of arrays [[k1,v1],[k2,v2]...]
    """
    
    res = ([[z[0],z[1]] for z in zip(dict.keys(),dict.values())])
    if(np):
        res = np.array(res)
        
    return res

def dict_to_keys_values_arrays(dict,np=None):
    """Converts dict {k:v} into dict with {'src':list of keys, 'trg':list of values}.

    Parameters
    ----------

    dict:       dictionary
        dict to convert.

    Returns
    ----------

    dictionary {'src':[k1,k2,k3...], 'trg':[v1,v2,v3...]}
    """
    kv = dict_to_array(dict,np)
    return {
        "keys": kv[:,0],
        "values": kv[:,1]
    }
    
def swap_dict_keys_values(dict):
    """Converts dict {k:v} into dict {v:k} i.e. reverses keys and values.

    Parameters
    ----------

    dict:       dictionary
        dict to convert {k:v}.

    Returns
    ----------

    dictionary {v:k}
    """
    flip_dict = {v:k for k,v in dict.items()}
    return flip_dict