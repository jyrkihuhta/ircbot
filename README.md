== INSTALLATION AND USAGE ==

The bot is a very simple idiokit application. It uses two IRC servers: one for C&C and one for WHOIS. The C&C channel is filtered for the !whois command and the replies from the target WHOIS server is piped to the C&C as PRIVMSG.

Example,
14:03 <@AWdawd> !whois root
14:03 < bot1_freenode> No such nick/channel
14:03 < bot3_quakenet> ~exgehfdrq rmeclhltx.users.quakenet.org * exgehfdrq
14:03 < bot3_quakenet> *.quakenet.org QuakeNet IRC Server

Default values for the C&C and WHOIS IRC server configurations are in server_configs.py, but you can also use command line argumants to override them.

=== Dependencies ===

git clone https://github.com/abusesa/idiokit

=== Docker ===

docker build -t ircbot .
docker run -it --rm --name IRCbot03 ircbot --cc-nick bot3_quakenet --whois-host dreamhack.se.quakenet.org

=== Naked ===

cd idiokit
sudo python setup.py install
cd ..
python ircbot.py --cc-nick bot3_quakenet --whois-host dreamhack.se.quakenet.org

