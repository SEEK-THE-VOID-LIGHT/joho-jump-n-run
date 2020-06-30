#leveldata

print("loaded level module with code 1")
# ------------------
# ==> reference:
# o -> normal block
# O -> normal block withour 'grass'
# q -> normal wood block
# Q -> wood structure block
# x -> structure block
# S -> start block
# E -> end block
# W -> win block
# ------------------
# default = [  "....................",
#             "....................",
#             "....................",
#             "....................",
#             "....................",
#             "....................",
#             "....................",
#             "....................",
#             "....................",
#             "....................",
#             "....................",
#             "....................",
#             "....................",
#             "....................",
#             "S...................",
#             "oooooooooooooooooooo"]
seconds_left = [8,11,8,8,6,11,9]
level = [[  "....................",
            "....................",
            "......oo.........oEo",
            "o.....xx........oxox",
            "x.....xx........xxxx",
            "x.....xx.....o..xxxx",
            "xooo..xx.....x..xxxx",
            "xxxx..xx.....x..xxxx",
            "xxxx..xx.....x..xxxx",
            "xxxx..oo.....x..xxxx",
            "xxxx..xx.....x..xxxx",
            "xxxx..xx.....x..xxxx",
            "xxxx.ooooo...x..xxxx",
            "xxxx.xxxxx..xxx.xxxx",
            "xxxxSxxxxx.xxxxxxxxx",
            "oooooooooooooooooooo"],

        [   "....................",
            ".o.ooooooooo........",
            ".O.Oxxxxxxxx........",
            ".O.Oxx..............",
            ".O.Ox.......o.......",
            ".O.Ox.......x.......",
            ".O.Ox.......x.......",
            ".O.Ox......ox.......",
            ".O.Ox......xx.......",
            ".O.Oooooo..xx.......",
            ".O.OExxxO..xo.......",
            ".OxOxxxxO..xx.......",
            "oOxOoooxO..xx..o....",
            "OxxxxxxxO..xx..x....",
            "OxxxxxxxO..xx..x.S..",
            "OoooooooOooooooooooo"],

        [   "E...................",
            "....................",
            "....................",
            "oo..................",
            "xx..................",
            "xxooo...............",
            "xxxxx...............",
            "xxxxx...............",
            "xxxxxoo...oo...oo...",
            "xxxxxxx...xx...xx...",
            "xxxxxxx...xx...xx...",
            "xxxxxxx...xx...xxoo.",
            "xxxxxxx...xx..ooxxx.",
            "xxxxxxx...xoo.xxxxx.",
            "xxxxxxx.S.xxx.xxxxx.",
            "oooooooooooooooooooo"],
            
        [    "...........x........",
            "...........x........",
            "...........x........",
            "...........E.......o",
            "...................x",
            "...................x",
            "..................ox",
            "..................xx",
            "................o.xx",
            "................x.xx",
            "..o...o...o...o.x.xx",
            "..x...x...x...x.x.xx",
            ".ox...x...x...x.x.xx",
            ".xx...x...x...x.x.xx",
            "Sxx...x...x...x.x.xx",
            "oooooooooooooooooooo"],
            
        [   "....................",
            "....................",
            "....................",
            "....................",
            "....o...............",
            ".o..x.........xx.xx.",
            ".x..x.........xx.xx.",
            ".x..x...........E...",
            "ox..x.........x...x.",
            "xx..x..........xxx..",
            "xx..x...............",
            "xo..x.o....o........",
            "xx..x.x....x........",
            "xx..x.x....x........",
            "xx..x.x.S..xo.......",
            "oooooooooooooooooooo"],

        [   ".oooooo.............",
            ".O....Oo............",
            ".OS...Ox....o...o...",
            ".Oooo.O....ox...x..o",
            ".x..O.O...oxx...x..x",
            "..x.O.O..oxxx...x..x",
            "...xO.O.oxxxx...x.ox",
            "...xO.Ooxxxxx...x.xx",
            "...xO.Oxxxxxx...o.xx",
            "...xO.....xxx...x.xx",
            "...xO......xx.o.x.xx",
            "...xOoo.....x.x.x.xx",
            "...xxxxo....o.x.x.xx",
            "...xxWxxo...x.x.x.xx",
            "...xxxxxxoo.x.x.x.xx",
            "oooooooooOOooooooooo"],

        [   "....................",
            ".q.......W..........",
            ".Q....qqqq..........",
            ".Q....QQQQ..........",
            "qQ...QQ.............",
            "QQ..QQ..............",
            "QQ.QQ...............",
            "QqQQ................",
            "QQ............q.....",
            "QQ............Q..q..",
            "qQ............Q..Q..",
            "Qq.qq..q......Q..Q..",
            "QQ.QQ..Q......Q..Qq.",
            "QQQQQQ.Q......Q..QQ.",
            "QQQQQQQQ......Q..QQS",
            "oooooooooooooooooooo"]]