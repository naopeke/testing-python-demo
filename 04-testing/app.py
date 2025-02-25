blogs = dict() # blogs = {} blogs = set() // blog_name: Blog object blogsという名前の空の辞書を作成しています。辞書はキーと値のペアを保存するデータ構造です。

def menu():
    # show the user the available blogs
    # let the user make a choice
    # do something with that choice
    # eventually exit

    print_blogs()


def print_blogs():
    # print the available blogs この関数は、利用可能なブログを表示するためのものです。
    for key, blog in blogs.items(): # [(blog_name, Blog), (blog_name, Blog)] blogs辞書の中身を一つずつ取り出しています。
        print(blog)
        print('- {}'.format(blog))