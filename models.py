class BlogPost:
    def __init__(self, title, content, author="Unknown", tags=None):
        self.title = title
        self.content = content
        self.author = author
        self.tags = tags or []

    def add_tag(self, tag):
        self.tags.append(tag)
