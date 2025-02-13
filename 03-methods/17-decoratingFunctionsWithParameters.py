import functools

user = {"username": "jose", "access_level": "guest"}

# *arg（可変長位置引数）
# *arg は 任意の数の位置引数 を受け取ることができる。
# ここでは panel の値が *arg のタプル内に入る。

# **kwargs（可変長キーワード引数）
# **kwargs は 任意の数のキーワード引数 を受け取ることができる。
# 例えば、もし get_admin_password が panel="admin", user="jose" のような呼び出しを許可していたら、user="jose" は kwargs に格納される。

# *arg, **kwargs の役割
# デコレーターはどんな関数にも適用できるようにするため、引数を固定せず *arg, **kwargs を使っている。
# func(*arg, **kwargs) の形で元の関数 (get_admin_password) を呼び出すことで、デコレーターが関数のパラメータ構造を変更せずに処理を追加できる。

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*arg, **kwargs):
        if user["access_level"] == "admin":
            return func(*arg, **kwargs)
        else:
            return f"No admin permissions for {user['username']}"
    return secure_function

@make_secure
def get_admin_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

print(get_admin_password("billing"))
