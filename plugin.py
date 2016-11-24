###
# Copyright (c) 2016, Pierre-Yves Kerbrat
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import random



class SC(callbacks.Plugin):
    """Manage Star Craft games
    callgame: Call for a new game on the channel.
                      People need to declare themself if they
                      want to take part
    wannaplay [name]: People willing to take part in next game use this command
    who: list already registered player
    team: select teams from the list of registered players"""
    pass

    players = []
    team1 = []
    team2 = []

    def __init__(self, irc):
        self.__parent = super(SC, self)
        self.__parent.__init__(irc)
        self.rng = random.Random()   # create our rng
        self.rng.seed()   # automatically seeds with current time

    def help(self, irc, msg, args):
        irc.reply("Star Craft game manager:")
        irc.reply("callgame: reset and call for a new game")
        irc.reply("wannaplay [name]: use this command to indicate you (or specified name)  want to play in next game")
        irc.reply("who: list already registered player")
        irc.reply("team: pick teams at random")
    help = wrap(help)

    def callgame(self, irc, msg, args):
        self.players = []
        self.team1 = []
        self.team2 = []
        irc.reply("A new game will start soon, please register with wannaplay command")
    callgame = wrap(callgame)

    def wannaplay(self, irc, msg, args, player):
        if (player):
            self.players.append(player)
            irc.reply(player + " is registered for next game");
        else:
            self.players.append(msg.nick)
            irc.reply(msg.nick + " is registered for next game");
    wannaplay = wrap(wannaplay, [additional('text')])

    def who(self, irc, msg, args):
        irc.reply("Already registered = " + utils.str.commaAndify(self.players))
    who = wrap(who)


    def team(self, irc, msg, args):
        if (len(self.players) % 2):
            self.players.append('cpu')
        l = len(self.players) / 2
        random.shuffle(self.players)
        self.team1 = [ self.players[i] for i in range(l)]
        self.team2 = [ self.players[i] for i in range(l, len(self.players))]
        irc.reply("Selected teams are:")
        irc.reply("Team 1 = " + utils.str.commaAndify(team1))
        irc.reply("Team 2 = " + utils.str.commaAndify(team2))
    team = wrap(team)

Class = SC


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
