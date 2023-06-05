from server import Server
import dis
import re


class ServerClassVerifier:
    def __init__(self, server_class):
        self.examined_class = server_class
        with open('server_dis.txt', 'w') as f:
            dis.dis(self.examined_class, file=f)

        forbidden = ['connect']
        must_be = ['socket', 'AF_INET', 'SOCK_STREAM']
        with open('server_dis.txt', 'r') as f:
            disasm = f.read()
            for string in forbidden:
                result = re.findall(rf"LOAD_METHOD.*\({string}\)", disasm)
                if result:
                    raise AttributeError(f"class {self.examined_class} should not have {string}: {result}")

            for string in must_be:
                result = re.findall(rf"LOAD_GLOBAL.*\({string}\)", disasm)
                if not result:
                    raise AttributeError(f"class {self.examined_class} should have {string}")

        print(f'{self.examined_class} is valid')


if __name__ == "__main__":
    server_verifier = ServerClassVerifier(Server)
