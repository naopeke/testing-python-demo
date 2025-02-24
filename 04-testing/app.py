blogs = dict() # blogs = {} blogs = set() // blog_name: Blog object

def menu():
    # show the user the available blogs
    # let the user make a choice
    # do something with that choice
    # eventually exit

    print_blogs()


def print_blogs():
    # print the available blogs
    for key, blog in blogs.items(): # [(blog_name, Blog), (blog_name, Blog)]
        print(blog)
        print('- {}', format(blog))