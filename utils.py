def summarize(text, length=100):
    return text[:length].rstrip() + "..." if len(text) > length else text
