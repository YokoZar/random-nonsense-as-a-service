#!/usr/bin/env python3
from bottle import route, run
import subprocess
EXEC = "/usr/bin/dadadodo"
TIMEOUT = 5

def validate_sentences(sentences: str):
    try:
        number = int(sentences)
    except:
        return False
    if 1 <= number <= 5:
        return True
    else:
        return False

def run_dada(quote_file, sentences="1"):
    if not validate_sentences(sentences):
        sentences = "1"
    try: 
        out = subprocess.check_output([EXEC] + ["-count", sentences, "-columns", "140"] + [quote_file], 
                                      timeout=TIMEOUT, stderr=subprocess.DEVNULL)
    except subprocess.TimeoutExpired:
        return "### Timeout error ###"
    return out.decode().rstrip()

@route('/oscar')
@route('/oscar/')
@route('/oscar/<number>')
def oscar(number="1"):
    return str(run_dada("oscar.txt", sentences=number))

run(host='localhost', port=80, server="gunicorn")

