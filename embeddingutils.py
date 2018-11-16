import numpy as np

pad_token = '<pad>'
unk_token = '<unk>'
sos_token = '<s>'
eos_token = '</s>'

special_tokens = [pad_token, unk_token, sos_token, eos_token]

def initialize_word2id_with_special_tokens():
    """Initialize embedding word2id with 'special' tokens e.g. padding, unknown, sequence start/end.

    Parameters
    ----------
    None.
    
    Returns
    ----------

    dictionary ({special_token_name: special_token_id})
    """
    word2id=dict([(x,i) for i, x in enumerate(special_tokens)])
    return word2id

def add_tokens_to_word2id(word2id,tokens):
    """Add tokens to existing embedding word2id.

    Parameters
    ----------
    word2id:        dictionary
        Word (token) to ID (number) mapping.
    
    tokens:       list of strings
        Tokens to add to word2id mapping.

    Returns
    ----------

    dictionary (updated mapping {special_token_name: special_token_id})
    """
    offset = len(word2id.keys())
    for t in tokens:
        word2id[t] = offset
        offset+=1
    
    return word2id        

def create_word2id_from_tokens(tokens,initialize=False):
    """Create new embedding word2id.

    Parameters
    ----------
    tokens:         list of strings
        Tokens to add to word2id mapping.
    
    initialize:     boolean
        True if want to initialize the word2id with special tokens e.g. pad, sos, eos.
        
    Returns
    ----------

    dictionary (updated mapping {special_token_name: special_token_id})
    """
    word2id = {}
    if(initialize):
        word2id = initialize_word2id_with_special_tokens()
    
    word2id = add_tokens_to_word2id(word2id,tokens)
    return word2id

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
    
def create_random_embedding(embedding_dimension):
    """Create a random embedding of given dimension.

    Parameters
    ----------

    embedding_dimension:              int
        Dimension size e.g. 100, 300.

    Returns
    ----------

    Numpy array of random uniform floats between -1 and 1.
    """
    return np.random.uniform(-1,1,size = (embedding_dimension))
    
def initialize_embedding_matrix(vocab_size,embedding_dimension,dtype=np.float32):
    """Create a random embedding matrix for given vocabulary size and embedding dimension.

    Parameters
    ----------
    vocab_size:             int
        Vocabulary size.

    embedding_dimension:    int
        Dimension size e.g. 100, 300.

    dtype:                  int, optional (default = np.float32)
        Numpy data type.

    Returns
    ----------

    Numpy array of zeros of specified shape and type representing an initialised embedding matrix.
    """
    return np.zeros((vocab_size,embedding_dimension),dtype=dtype)

def populate_random_embedding_matrix(embedding_matrix,offset=0):
    """Populate a random embedding matrix for given vocabulary size and embedding dimension.
    Optionally start from a specific vocabulary offset.

    Parameters
    ----------
    embedding_matrix        Numpy array of vocab_size, embedding_dimension shape
        See initialize_embedding_matrix for details
        
    offset                  int, optional, default = 0
        Start randomising at offset X e.g. vocabulary word #7

    Returns
    ----------

    Randomised embedding matrix (input, but randomised).
    """
    
    vocab_size = embedding_matrix.shape[0] 
    embedding_dimension = embedding_matrix.shape[1]
    for r in range(offset,vocab_size+offset):
        embedding_matrix[r] = create_random_embedding(embedding_dimension)

    return embedding_matrix

def create_random_embedding_matrix(vocab_size,embedding_dimension,dtype=np.float32):
    init_matrix = initialize_embedding_matrix(vocab_size,embedding_dimension,dtype=dtype)
    
    return populate_random_embedding_matrix(init_matrix)