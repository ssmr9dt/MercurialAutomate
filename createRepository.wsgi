import re
from urllib.parse import parse_qs
import subprocess
from subprocess import PIPE

def application(environ, start_response):
        start_response('200 OK', [('Content-Type', 'text/html')])

        fr = open("/var/www/Programs/key.txt", "rt")
        file_key = fr.read()
        fr.close()

        fr = open("/var/www/Programs/key.txt", "wt")
        fr.close()

        if not file_key:
                return ["error: can't open key file".encode("utf-8")]

        if len(file_key) <= 0:
                return ["error: file_key is 0".encode("utf-8")]

        pattern = "^[0-9a-zA-Z-]+$"

        form = parse_qs(environ.get("QUERY_STRING", ""))

        if "key" not in form:
                return ["error: ".encode("utf-8")]

        if "name" not in form:
                return ["error: ".encode("utf-8")]

        key = form["key"][0]

        if len(key) <= 0:
                return ["error: ".encode("utf-8")]

        name = form["name"][0]

        if len(name) <= 0:
                return ["error: ".encode("utf-8")]

        if not re.match(pattern, name):
                return ["error: Mismatch naming conventions".encode("utf-8")]

        if file_key != key:
                return ["error: Mimatch network flow".encode("utf-8")]

        shell = "/home/netsys/1.createRepository.sh " + name
        proc = subprocess.run(shell, shell=True, stdout=PIPE, stderr=PIPE, text=True)

        if proc.stdout.find("error") >= 0:
                return [proc.stdout.encode("utf-8")]

        return ["success".encode("utf-8")]
