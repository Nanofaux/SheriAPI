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

from .enums import FreeEndpoint, NSFWEndpoint, SFWEndpoint


def lookup(enum):
    for to_try in free_endpoints, sfw_endpoints, nsfw_endpoints:
        try:
            return list(to_try.keys())[list(to_try.values()).index(enum.value)]
        except ValueError:
            continue


def to_enum(endpoint):
    if endpoint in free_endpoints:
        return FreeEndpoint(free_endpoints[endpoint])
    if endpoint in sfw_endpoints:
        return SFWEndpoint(sfw_endpoints[endpoint])
    if endpoint in nsfw_endpoints:
        return NSFWEndpoint(nsfw_endpoints[endpoint])


free_endpoints = {
    'bunny': 0, 'cat': 1, 'deer': 2, 'fox': 3, 'goat': 4, 'horse': 5, 'husky': 6, 'lion': 7, 'mur': 8, 'nature': 9,
    'pig': 10, 'rpanda': 11, 'shiba': 12, 'snek': 13, 'snep': 14, 'tiger': 15, 'turkey': 16, 'turtle': 17, 'wolves': 18,
    'yeen': 19, 'yiff': 20}

sfw_endpoints = {
    'ban': 21, 'belly_rub': 22, 'blep': 23, 'boop': 24, 'cry': 25, 'cuddle': 26, 'hold': 27, 'hug': 28, 'kick': 29,
    'kiss': 30, 'lick': 31, 'maws': 32, 'pat': 33, 'paws': 34, 'pokemon': 35, 'proposal': 36,
    'trickortreat': 38, 'cheese': 104}

nsfw_endpoints = {
    'yiff': 20, '69': 39, 'anal': 40, 'bang': 41, 'bisexual': 42, 'boob': 43, 'boobwank': 44, 'booty': 45,
    'christmas': 46, 'cumflation': 47, 'cuntboy': 48, 'dick': 49, 'dick_wank': 50, 'dickorgy': 51, 'dp': 52,
    'fbound': 53, 'fcreampie': 54, 'femboypresentation': 55, 'finger': 56, 'fpresentation': 57, 'fseduce': 58,
    'fsolo': 59, 'ftease': 60, 'futabang': 61, 'gay': 62, 'gif': 63, 'impregnated': 64, 'lesbian': 65, 'mbound': 66,
    'mcreampie': 67, 'mpresentation': 68, 'mseduce': 69, 'msolo': 70, 'mtease': 71, 'nboop': 72, 'nbrony': 73,
    'nbulge': 74, 'ncomics': 75, 'ncuddle': 76, 'nfemboy': 77, 'nfuta': 78, 'ngroup': 79, 'nhold': 80, 'nhug': 81,
    'nkiss': 82, 'nlick': 83, 'npats': 84, 'npokemon': 85, 'nprotogen': 86, 'nseduce': 87, 'nsfwselfies': 88,
    'nsolo': 89, 'nspank': 90, 'ntease': 91, 'ntrap': 92, 'pawjob': 93, 'petplay': 94, 'pregnant': 95,
    'pussy': 96, 'pussy_eating': 97, 'ride': 98, 'smash': 99, 'suck': 100, 'tentacles': 101, 'toys': 102, 'vore': 103}
