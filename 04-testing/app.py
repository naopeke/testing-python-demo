from blog import Blog
MENU_PROMPT = 'Enter "c" to create a blog, "l" to list blogs, "r" to read one, "p" to create a post, or "q" to quit: '
POST_TEMPLATE = '''
--- {} ---

{}

'''
blogs = dict() # blogs = {} blogs = set() // blog_name: Blog object blogsという名前の空の辞書を作成しています。辞書はキーと値のペアを保存するデータ構造です。


def menu():
    # show the user the available blogs
    # let the user make a choice
    # do something with that choice
    # eventually exit

    print_blogs()
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection == 'c':
            ask_create_blog()
        elif selection == 'l':
            print_blogs()
        elif selection == 'r':
            ask_read_blog()
        elif selection == 'p':
            ask_create_post()
        selection = input(MENU_PROMPT)


def print_blogs():
    # print the available blogs この関数は、利用可能なブログを表示するためのものです。
    for key, blog in blogs.items(): # [(blog_name, Blog), (blog_name, Blog)] blogs辞書の中身を一つずつ取り出しています。
        print(blog)
        print('- {}'.format(blog))

def ask_create_blog():
    title = input('Enter your blog title: ')
    author = input('Enter your name: ')
    blogs[title] = Blog(title, author)

def ask_read_blog():
    title = input('Enter the blg title you want to read: ')
    print_posts(blogs[title])

def print_posts(blog):
    for post in blog.posts:
        print_post(post)

def print_post(post):
    print(POST_TEMPLATE.format(post.title, post.content))

def ask_create_post():
    pass