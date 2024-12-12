puzzle_input=""".......b..........................................
.A....s...................3V...P....I.............
..s.........b........v.P..................z.......
.p..........A..uS.l...........................8...
.......B...i...................z...............8..
.............s..........E.......m........J........
.c............L...k.P........E....................
........b.....................a...................
.m.s.....V....l....u...S..........O.............8.
...B..............L..1Dm...S....u.z...............
......A......3...e....f..a........................
...................3.......I...............6.....8
....v..l...................5..........I...........
...v........k.0......5..P....z....................
.....A....................VJ...T.......D..........
.i..B..............L......W...........5...........
...........p.....k............u.D..IX.............
...c.......k..........VG.D.........W..............
......i.c.....G....W........5....jJ...............
...........l........................J....E........
..........E..G..t.................................
........i........h.................a....O........C
......K..t.L........m...W......0..j...........2...
................1.......j..0.......gC..M....2.....
.........K............3...........M........U...g..
..K.......p.....G.c...................q.....6.T...
..................1h...............M..C...6f......
............tj..h.......................f.........
....................Y.h............O.........6.C..
...........K....X....t......MfY..O....Q...........
..............p.......0.................g.........
..............n...............g...................
....a..................................wQq.H.2....
.o..................................v.....H..7.2..
........N1..........F.......q....Yw.........H.....
...n..d....H..F....................Y.......e......
...................d..............................
..y....N.....d..Z......9..........................
.N......T.n................497....................
.y....o....Z.........x.............T.............Q
.......y...X.........9..................7....Q....
...............F......................e...........
.n...............F.Z..........................e...
......................9U..............w...........
o.......y...................4.U...................
..x..............X.........w..4.............7.....
.......oZ...d.....................x...............
.............qU...................................
..................................................
.................................................."""


# puzzle_input="""............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............"""

import re
from collections import *
from dataclasses import dataclass
from operator import add, sub

@dataclass
class Vec:
    r: int
    c: int
    
    def __add__(self, other):
        return Vec(self.r + other.r, self.c + other.c)
    def __sub__(self, other):
        return self + - other
    def __neg__(self):
        return Vec(-self.r, -self.c)
    def __mul__(self, scalar):
        return Vec(scalar*self.r, scalar*self.c)
    def __hash__(self):
        return hash((self.r, self.c))
    def __eq__(self, other):
        return isinstance(other, Vec) and self.r == other.r and self.c == other.c
    def within_bounds(self, rows, cols):
        return self.r >= 0 and self.r < rows and self.c >= 0 and self.c < cols


    
def part1():
    ant_locs = defaultdict(list)
    lines = puzzle_input.split("\n")
    n, m = len(lines), len(lines[0])
    regex = r"[^.]"
    for i, line in enumerate(lines):
        for match in re.finditer(regex, line):
            ant_locs[match.group()].append(Vec(i, match.start()))
    
    def generate_antinodes(ant1, ant2):
        return [ant2 + ant2 - ant1]
    antinodes = set()
    for ant, locs in ant_locs.items():
        for loc1 in locs:
            for loc2 in locs:
                if loc1 == loc2:
                    continue
                for antinode in generate_antinodes(loc1, loc2):
                    if antinode.within_bounds(n, m):
                        antinodes.add(antinode)
    
    print(len(antinodes))
        

def part2():
    ant_locs = defaultdict(list)
    lines = puzzle_input.split("\n")
    n_rows, n_cols = len(lines), len(lines[0])
    regex = r"[^.]"
    for i, line in enumerate(lines):
        for match in re.finditer(regex, line):
            ant_locs[match.group()].append(Vec(i, match.start()))
    
    def generate_antinodes(ant1, ant2):
        diff = ant2 - ant1
        antinodes = set()
        for ant in [ant1, ant2]:
            for op in [add, sub]:
                for n in range(max(n_rows, n_cols)):
                    if not (cand:=op(ant, diff*n)).within_bounds(n_rows, n_cols):
                        break
                    antinodes.add(cand)
        return antinodes
    antinodes = set()
    for ant, locs in ant_locs.items():
        for j, loc1 in enumerate(locs):
            for loc2 in locs[j+1:]:
                for antinode in generate_antinodes(loc1, loc2):
                    if antinode.within_bounds(n_rows, n_cols):
                        antinodes.add(antinode)
    
    print(len(antinodes))
    
    
    
    
    
part1()
    
part2()