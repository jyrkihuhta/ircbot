#!/bin/bash
# You need git and docker
git clone https://github.com/abusesa/idiokit
docker build -t ircbot .
docker run -d --rm --name IRCbot01 ircbot --cc-nick bot1_efnet --whois-host irc.du.se
docker run -d --rm --name IRCbot02 ircbot --cc-nick bot2_dalnet --whois-host SERENITY.IX.US.DAL.NET
docker run -d --rm --name IRCbot03 ircbot --cc-nick bot3_quakenet --whois-host dreamhack.se.quakenet.org
docker run -d --rm --name IRCbot04 ircbot --cc-nick bot4_ircnet --whois-host irc.lut.fi
