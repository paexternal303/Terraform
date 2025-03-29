def summarize(text, length=80):
    return text[:length].rstrip() + "..." if len(text) > length else text
   
