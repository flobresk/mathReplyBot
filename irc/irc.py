import socket


class IRC:
    irc = socket.socket()

    def __init__(self):
        self.irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send(self, chan, msg):
        self.irc.send(("PRIVMSG " + chan + " " + msg + "\r\n").encode())
        print(("PRIVMSG " + chan + " " + msg + "\r\n").encode())

    def connect(self, server, channel, botnick, authCode):
        # defines the socket
        print ("connecting to:" + server)
        self.irc.connect((server, 6667))  # connects to the server
        self.irc.send(
            ("PASS " + authCode + "\r\n").encode())  # user authentication
        self.irc.send(("NICK " + botnick + "\r\n").encode())
        self.irc.send(("JOIN " + channel + "\r\n").encode() ) # join the chan

    def get_text(self):
        text = self.irc.recv(2040)
        #text.decode('utf-8')# receive the text

        if text.find('PING :tmi.twitch.tv'.encode()) != -1:
            self.irc.send(('PONG :tmi.twitch.tv \r\n').encode())
            print("got ping request, sending pong")

        return text