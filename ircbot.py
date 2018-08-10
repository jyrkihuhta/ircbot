import idiokit
from server_configs import *
from idiokit.irc import connect
import argparse

WHOIS_REPLIES = ["301", "311", "312", "313", "317", "318", "319", \
                    "326", "327", "330", "338", "377", "378", "379", \
                    "401", "402", "431"]

@idiokit.stream
def issue_commands(channel):
    while True:
        prefix, command, params = yield idiokit.next()
        if command != "PRIVMSG":
            continue

        if not params or params[0] != channel:
            continue

        try:
            splitted = params[1].split()
            issue_command = splitted[0].strip().lower()
        except IndexError:
            continue

        if issue_command == "!whois":
            try:
                target = splitted[1]
            except IndexError:
                continue

            yield idiokit.send("WHOIS", target)

@idiokit.stream
def capture_whois(channel):
    while True:
        prefix, command, params = yield idiokit.next()
        if command in WHOIS_REPLIES:
            yield idiokit.send("PRIVMSG", channel, " ".join(params))

@idiokit.stream
def ircbot(cc_host, cc_port, cc_nick, cc_channel, whois_host, whois_port, whois_nick):
    cc_irc = yield connect(cc_host, cc_port, cc_nick)
    whois_irc = yield connect(whois_host, whois_port, whois_nick)
    yield cc_irc.join(cc_channel)
    yield cc_irc | issue_commands(cc_channel) | whois_irc | capture_whois(cc_channel) | cc_irc

def main():
    parser = argparse.ArgumentParser(description='Run a simple IRCBot (default values are in server_configs.py')
    parser.add_argument('--cc-host', type=str, help='The C&C IRC server host', default=cc_host)
    parser.add_argument('--cc-port', type=str, help='The C&C IRC server port', default=cc_port)
    parser.add_argument('--cc-nick', type=str, help='The C&C IRC server nick', default=cc_nick)
    parser.add_argument('--cc-channel', type=str, help='The C&C nick for your bot', default=cc_channel)
    parser.add_argument('--whois-host', type=str, help='The target IRC server host', default=whois_host)
    parser.add_argument('--whois-port', type=str, help='The target IRC server port', default=whois_port)
    parser.add_argument('--whois-nick', type=str, help='The target IRC server nick', default=whois_nick)

    args = parser.parse_args()
    idiokit.main_loop(ircbot(args.cc_host, args.cc_port, args.cc_nick, args.cc_channel, \
                                args.whois_host, args.whois_port, args.whois_nick))

if __name__ == '__main__':
    main()


