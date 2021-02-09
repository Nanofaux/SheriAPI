# -*- coding: utf-8 -*-

"""
The MIT License (MIT)
Copyright (c) 2021 Nanofaux
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

from enum import Enum

"""
Honestly I know enums for this kinda stuff isn't the *most* useful however for one I do like the idea
that you can see all of the applicable endpoints, and also I thought it would be fun & interesting to use 
them. After all, who cares anyway xD it's just a lil' API wrapper I made for a furry bot on discord lol. 
"""


class _SharedEnum(Enum):
    """ For inheritance-testing purposes. """
    pass


class FreeEndpoint(_SharedEnum):
    """ Free endpoints (No token required). """
    Bunny = 0
    Cat = 1
    Deer = 2
    Fox = 3
    Goat = 4
    Horse = 5
    Husky = 6
    Lion = 7
    Mur = 8
    Nature = 9
    Pig = 10
    RPanda = 11
    Shiba = 12
    Snek = 13
    Snep = 14
    Tiger = 15
    Turkey = 16
    Turtle = 17
    Wolves = 18
    Yeen = 19
    Yiff = 20


class SFWEndpoint(_SharedEnum):
    """ SFW Endpoints. """
    Ban = 21
    BellyRub = 22
    Blep = 23
    Boop = 24
    Cry = 25
    Cuddle = 26
    Hold = 27
    Hug = 28
    Kick = 29
    Kiss = 30
    Lick = 31
    Maws = 32
    Pat = 33
    Paws = 34
    Pokemon = 35
    Proposal = 36
    TrickOrTreat = 38

    # New
    Cheese = 104


class NSFWEndpoint(_SharedEnum):
    """ NSFW Endpoints. """
    # While this is technically a free endpoint, it's also an NSFW endpoint so ehh just put it in here too, right?
    Yiff = 20

    SixtyNine = 39
    Anal = 40
    Bang = 41
    Bisexual = 42
    Boob = 43
    BoobWank = 44
    Booty = 45
    Christmas = 46
    Cumflation = 47
    Cuntboy = 48
    Dick = 49
    DickWank = 50
    DickOrgy = 51
    DP = 52
    FBound = 53
    FCreampie = 54
    FemboyPresentation = 55
    Finger = 56
    FPresentation = 57
    FSeduce = 58
    FSolo = 59
    FTease = 60
    Futabang = 61
    Gay = 62
    GIF = 63
    Impregnated = 64
    Lesbian = 65
    MBound = 66
    MCreampie = 67
    MPresentation = 68
    MSeduce = 69
    MSolo = 70
    MTease = 71
    NBoop = 72
    NBrony = 73
    NBulge = 74
    NComics = 75
    NCuddle = 76
    NFemboy = 77
    NFuta = 78
    NGroup = 79
    NHold = 80
    NHug = 81
    NKiss = 82
    NLick = 83
    NPats = 84
    NPokemon = 85
    NProtogen = 86
    NSeduce = 87
    NSFWSelfies = 88
    NSolo = 89
    NSpank = 90
    NTease = 91
    NTrap = 92
    Pawjob = 93
    Petplay = 94
    Pregnant = 95
    Pussy = 96
    PussyEating = 97
    Ride = 98
    Smash = 99
    Suck = 100
    Tentacles = 101
    Toys = 102
    Vore = 103
