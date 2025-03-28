from blog.models import BlogPost
from blog.views import render_post

if __name__ == "__main__":
    post = BlogPost("Hello", "This is a post about AI and tagging systems.")
    print(render_post(post))
