def summarize(text, length=80):
    return text[:length] + "..." if len(text) > length else text
