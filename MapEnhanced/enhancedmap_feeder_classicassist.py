# ClassicAssist - PHASE 2 (real solution)
# Sends live player stats to EnhancedMap over loopback UDP every 250ms.
# EnhancedMap must have statsudpport = 47600 (default) and be running.
#
# Datagram (must match StatsFeedSnapshot.TryParse):
#   hits|maxhits|stam|maxstam|mana|maxmana|poisoned|yellowhits|paralyzed|hidden
#   6 ints + 4 flags (0/1).
#
# ClassicAssist Player API (verified against the ClassicAssist Macro Commands wiki):
#   Player.Hits/MaxHits, Player.Stam/MaxStam, Player.Mana/MaxMana,
#   Player.Poisoned, Player.YellowHits, Player.Paralyzed, Player.Hidden
# Delay + socket use .NET primitives (guaranteed under IronPython).

from System.Net.Sockets import UdpClient
from System.Text import Encoding
from System.Threading import Thread

PORT = 47600

udp = UdpClient()
udp.Connect("127.0.0.1", PORT)


def flag(b):
    return "1" if b else "0"


while True:
    line = "%d|%d|%d|%d|%d|%d|%s|%s|%s|%s" % (
        Player.Hits, Player.MaxHits,
        Player.Stam, Player.MaxStam,
        Player.Mana, Player.MaxMana,
        flag(Player.Poisoned),
        flag(Player.YellowHits),
        flag(Player.Paralyzed),
        flag(Player.Hidden),
    )
    data = Encoding.UTF8.GetBytes(line)
    udp.Send(data, data.Length)
    Thread.Sleep(250)
