def summarize(text, length=100):
    return text[:length] + "..." if len(text) > length else text
