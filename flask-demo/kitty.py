from wsgiref.simple_server import make_server

def hello(env, say_somthing):
    say_somthing("200 OK", [("Content-Type", "text/html")])

    path = env["PATH_INFO"]
    if path == "/meow":
        return [b"<h1> Meow! </h1>"]

    return [b"<h1> Hello WSGI!</h1>"]

if __name__ == "__main__":
    port = 9527
    web_server = make_server(host = "", port = port, app = hello)

    print(f"SEerving on port {port}...")
    web_server.serve_forever()