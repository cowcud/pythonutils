import re

## tokenization (if you are using different language, you would need to tokenize differently)
def tokenize_text(text,lang='en',nltk=None):
    """Converts all elements of list to lower case.

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

def get_unique_tokens_in_sentences(sents,lang="en",nltk=None):
    """Get unique tokens in input sentences.

    Parameters
    ----------

    sents:       list of strings
        Sentences to process.

    lang:       string, optional
        ISO language code e.g. 'en'.

    nltk:       module reference, optional
        If prefer to use nltk module to tokenize the sentences, reference for module.

    Returns
    ----------

    list of strings (unique tokens identified in sentences)
    """
    sent_tokens = [tokenize_text(s,lang) for s in sents]
    return list(set([t for l in sent_tokens for t in l]))