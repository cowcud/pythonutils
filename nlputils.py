import re

def tokenize_text(text,lang='en',nltk=None):
    """Tries to extract tokens from given text for given language.

    Parameters
    ----------

    text:       string
        Text to tokenize.

    lang:       string, optional
        ISO language code e.g. 'en'.

    nltk:       module reference, optional
        If prefer to use nltk module, reference for module.

    Returns
    ----------

    list of strings (tokens identified in text)
    """
    if(lang=='en'):
        # If nltk is available, use that
        if(nltk):
            return nltk.word_tokenize(text)
        # Otherwise, just split on whitespace (after removing punctuation)
        else:
            punc_free_text = re.sub(r'[,;.]','',text)
            return [x.strip().lower() for x in re.split(r'\s*',punc_free_text)]
    else:
        # For other languages, for now nothing special
        return list(text)

def tokenize_text_blocks(text_blocks,lang='en',nltk=None):
    """Tries to extract tokens from given text blocks for given language and return
    corresponding blocks of tokens.

    Parameters
    ----------

    text_blocks:       list of strings
        Text blocks to tokenize.

    lang:       string, optional
        ISO language code e.g. 'en'.

    nltk:       module reference, optional
        If prefer to use nltk module, reference for module.

    Returns
    ----------

    list of strings (tokens identified in text)
    """
    token_blocks = [tokenize_text(t,lang,nltk) for t in text_blocks]
    return token_blocks
        
def get_unique_tokens_in_text_blocks(text_blocks,lang="en",nltk=None):
    """Get unique tokens in input sentences.

    Parameters
    ----------

    text_blocks:       list of strings
        Text_blocks to process.

    lang:       string, optional
        ISO language code e.g. 'en'.

    nltk:       module reference, optional
        If prefer to use nltk module to tokenize the sentences, reference for module.

    Returns
    ----------

    list of strings (unique tokens identified in text blocks)
    """
    token_blocks = tokenize_text_blocks(text_blocks)
    return list(set([t for l in token_blocks for t in l]))