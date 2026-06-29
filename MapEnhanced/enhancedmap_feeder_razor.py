# RazorEnhanced - PHASE 2 (real solution)
# Sends live player stats to EnhancedMap over loopback UDP every 250ms.
# EnhancedMap must have statsudpport = 47600 (default) and be running.
#
# Datagram (must match StatsFeedSnapshot.TryParse):
#   hits|maxhits|stam|maxstam|mana|maxmana|poisoned|yellowhits|paralyzed|hidden
#   6 ints + 4 flags (0/1).
#
# RE API used (verified against player-data-and-functions.txt):
#   Player.Hits/HitsMax, Player.Stam/StamMax, Player.Mana/ManaMax,
#   Player.Poisoned, Player.YellowHits, Player.Paralized, Player.Visible

from System.Net.Sockets import UdpClient
from System.Text import Encoding

PORT = 47600

udp = UdpClient()
udp.Connect("127.0.0.1", PORT)
Misc.SendMessage("EM feeder (RazorEnhanced) -> 127.0.0.1:" + str(PORT), 68)


def flag(b):
    return "1" if b else "0"


while True:
    line = "%d|%d|%d|%d|%d|%d|%s|%s|%s|%s" % (
        Player.Hits, Player.HitsMax,
        Player.Stam, Player.StamMax,
        Player.Mana, Player.ManaMax,
        flag(Player.Poisoned),
        flag(Player.YellowHits),
        flag(Player.Paralized),
        flag(not Player.Visible),
    )
    data = Encoding.UTF8.GetBytes(line)
    udp.Send(data, data.Length)
    Misc.Pause(250)
