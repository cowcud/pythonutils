pad_token = '<pad>'
unk_token = '<unk>'
sos_token = '<s>'
eos_token = '</s>'

special_tokens = [pad_token, unk_token, sos_token, eos_token]

def create_special_tokens():
    """Create 'special' tokens for embedding e.g. padding, unknown, sequence start/end.

    Parameters
    ----------
    None.
    
    Returns
    ----------

    dictionary ({special_token_name: special_token_id})
    """
    word2Id=dict([(x,i) for i, x in enumerate(special_tokens)])
    return word2Id

# Get 'special' token IDs (pad, start/end of sequence)
def get_special_token_ids(word2id,token_names):
    """Get ID of token from word2id dictionary (or ID of <unk> token or token not found).

    Parameters
    ----------
    word2id:        dictionary
        Word (token) to ID (number) mapping.

    token_names:    list of strings
        Special token names to look up in word2id mapping.
    
    Returns
    ----------

    tuple of list of ints (Token IDs)
    """
    token_values = []
    for t in token_names:
        try:
            token_var = t + '_token'
            token_value = eval(token_var)
        except:
            token_value = unk_token
        
        token_values.append(token_value)
    
    token_ids = [word2id[x] for x in token_values]
    return(tuple(token_ids))
 
def get_word2id(word2id,token):
    """Get ID of token from word2id dictionary (or ID of <unk> token or token not found).

    Parameters
    ----------
    word2id:        dictionary
        Word (token) to ID (number) mapping.

    token:          string
        Token to look up in word2id mapping.
    
    Returns
    ----------

    int (Token ID)
    """
    if(token in word2id):
        return word2id[token]
    else:
        return word2id['<unk>']

def get_word2ids_from_tokens(word2id,tokens):
    """Get ID of tokens from word2id dictionary for all tokens in some previously tokenized text.

    Parameters
    ----------

    word2id:              dictionary
        Word (token) to ID (number) mapping.

    tokens:       list of strings
        Tokens to look up in word2id mapping.

    Returns
    ----------

    list of ints (Token IDs)
    """
    return [get_word2id(word2id,x) for x in tokens]
    
def get_word2ids_from_token_lists(word2id,token_lists):
    """Process lists of tokens. For each list, get ID of tokens from word2id dictionary 
    for all tokens in the list. Return a corresponding list of lists of token IDs.

    Parameters
    ----------

    word2id:              dictionary
        Word (token) to ID (number) mapping.

    token_lists:       list of list of strings
        Token lists to look up in word2id mapping.

    Returns
    ----------

    list of ints (Token IDs)
    """
    return [get_word2ids_from_tokens(word2id,x) for x in token_lists]