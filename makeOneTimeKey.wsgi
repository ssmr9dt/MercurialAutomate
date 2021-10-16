import random
import string

def application(environ, start_response):
        start_response("200 OK", [("Content-Type", "text/html")])
        key = get_random_string(32)
        f = open("/var/www/Programs/key.txt", "wt")
        f.write(key)
        f.close()
        return [key.encode("utf-8")]

def get_random_string(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        return result_str
