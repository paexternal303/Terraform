from blog.models import BlogPost

def render_post(post: BlogPost):
    return f"<h1>{post.title}</h1><h4>By {post.author}</h4><p>{post.content}</p>"
