#!/usr/bin/env python3

import argparse, os, sys, struct, zlib, struct
from collections import OrderedDict

dialogues: list = [
    # Game Dialogues
    (0x1BC34, 0x1BC69), (0x1BC9C, 0x1BCAF), (0x1BCBD, 0x1BCE1), (0x1BD00, 0x1BD3A), (0x1BD3B, 0x1BD4C),
    (0x1BD50, 0x1BD61), (0x1BD6B, 0x1BD73), (0x1BD9C, 0x1BDB8), (0x1BDC0, 0x1BDCC), (0x1BDD8, 0x1BDF8),
    (0x1BE09, 0x1BE18), (0x1BE3A, 0x1BE4E), (0x1BE53, 0x1BE7A), (0x1BE9B, 0x1BEA6), (0x1BEAF, 0x1BECC),
    (0x1BEDE, 0x1BEFA), (0x1BF26, 0x1BFD6), (0x1BFDA, 0x1C016), (0x1C040, 0x1C097), (0x1C0B4, 0x1C0C8),
    (0x1C0D6, 0x1C11D), (0x1C151, 0x1C165), (0x1C17F, 0x1C1CD), (0x1C1EF, 0x1C211), (0x1C228, 0x1C24C),
    (0x1C261, 0x1C2A0), (0x1C2F6, 0x1C315), (0x1C319, 0x1C326), (0x1C355, 0x1C392), (0x1C396, 0x1C3A9),
    (0x1C3E0, 0x1C3F2), (0x1C40D + 6, 0x1C467), (0x1C49F, 0x1C4A7), (0x1C4A8, 0x1C4C5), (0x1C509, 0x1C52B),
    (0x1C53B, 0x1C57B), (0x1C62F, 0x1C655), (0x1C676, 0x1C71D), (0x1C739, 0x1C75F), (0x1C77F, 0x1C811),
    (0x1C82F, 0x1C8BA), (0x1C8DA, 0x1C8F7), (0x1C8FF, 0x1C94B), (0x1C955, 0x1C962), (0x1C96A, 0x1C98C),
    (0x1C996, 0x1C9A8), (0x1C9C6, 0x1CA30), (0x1CA56, 0x1CACA), (0x1CAE8, 0x1CB08), (0x1CB0C, 0x1CB22),
    (0x1CB2E, 0x1CB4A), (0x1CB4E, 0x1CB5C), (0x1CB68, 0x1CB77), (0x1CB7B, 0x1CB90), (0x1CB9C, 0x1CBBA),
    (0x1CBBE, 0x1CBEE), (0x1CBFD, 0x1CC1D), (0x1CC29, 0x1CC4A), (0x1CC4E, 0x1CC5F), (0x1CC7B, 0x1CC95),
    (0x1CCDB, 0x1CD33), (0x1CE3C, 0x1CE4F), (0x1CE5B, 0x1CE74), (0x1CEA2, 0x1CEB8), (0x1CED4 + 5, 0x1CEE5),
    (0x1D066, 0x1D085), (0x1D0A7, 0x1D0BD), (0x1D0D9, 0x1D111), (0x1D132, 0x1D15D), (0x1D15E, 0x1D1AE),
    (0x1D1D8, 0x1D1E2), (0x1D1F6, 0x1D223), (0x1D242, 0x1D26B), (0x1D6EA, 0x1D71A), (0x1D71E, 0x1D759),
    (0x1D79C, 0x1D7C5), (0x1D7CA, 0x1D7F1), (0x1D7F5, 0x1D81B), (0x1D823, 0x1D857), (0x1D862, 0x1D88E),
    (0x1D88F, 0x1D8A3), (0x1D8A5, 0x1D8BB), (0x1D8BC, 0x1D8D3), (0x1D8D4, 0x1D8FC), (0x1D8FD, 0x1D90F),
    (0x1D910, 0x1D919), (0x1D91A, 0x1D92F), (0x1D930, 0x1D943), (0x1D944, 0x1D958), (0x1D97D, 0x1D9A4),
    (0x1D9A7, 0x1D9BD), (0x1D9BE, 0x1D9D4), (0x1D9D5, 0x1D9DD), (0x1D9DE, 0x1DA51), (0x1DA55, 0x1DA73),
    (0x1DA77, 0x1DA81), (0x1DA92, 0x1DACB), (0x1DADF, 0x1DAEC), (0x1DB22 + 2, 0x1DB95), (0x1DB9F, 0x1DBBF),
    (0x1DBC0, 0x1DBD8), (0x1DBD9, 0x1DBF3), (0x1DBF4, 0x1DC02), (0x1DC21, 0x1DC72), (0x1DC76, 0x1DD2C),
    (0x1DD3A, 0x1DD87), (0x1DDA0, 0x1DDE0), (0x1DDF0, 0x1DE0C), (0x1DE10, 0x1DE4E), (0x1DE58, 0x1DE79),
    (0x1DE7D, 0x1DEAA), (0x1DEBF, 0x1DEDB), (0x1DEDC, 0x1DF00), (0x1DF01, 0x1DF19), (0x1DF1A, 0x1DF2D),
    (0x1DF2E, 0x1DF46), (0x1DF47, 0x1DF55), (0x1DF56, 0x1DF61), (0x1DF62, 0x1DF90), (0x1DF9B, 0x1DFA6),
    (0x1DFA7, 0x1DFD4), (0x1DFD5, 0x1E001), (0x1E003, 0x1E066), (0x1E079, 0x1E09B), (0x1E09C, 0x1E0BD),
    (0x1E0FC, 0x1E11E), (0x1E145, 0x1E1A8), (0x1E1C2, 0x1E1DC), (0x1E1FB, 0x1E264), (0x1E268, 0x1E297),
    (0x1E29B, 0x1E31C), (0x1E320, 0x1E37D), (0x1E383, 0x1E3AE), (0x1E3AF, 0x1E3EA), (0x1E3EB, 0x1E451),
    (0x1E459, 0x1E4B4), (0x1E4BC, 0x1E4E0), (0x1E4FB, 0x1E503), (0x1E50F, 0x1E53F), (0x1E558, 0x1E589),
    (0x1E591, 0x1E5A9), (0x1E5E1, 0x1E615), (0x1E632, 0x1E64A), (0x1E652, 0x1E676), (0x1E677, 0x1E696),
    (0x1E69B, 0x1E6BB), (0x1E6BC, 0x1E6DC), (0x1E6E9, 0x1E75D), (0x1E75E, 0x1E770), (0x1E771, 0x1E787),
    (0x1E789, 0x1E872), (0x1E892, 0x1E8B5), (0x1E8B6, 0x1E8D5), (0x1E8DC, 0x1E905), (0x1E90F, 0x1E91C),
    (0x1E923, 0x1E936), (0x1E93F, 0x1E99E), (0x1E9A4, 0x1E9C5), (0x1E9C8, 0x1E9DD), (0x1E9E8, 0x1E9F7),
    (0x1E9F8, 0x1EA3E), (0x1EA50, 0x1EA66), (0x1EA6A, 0x1EA93), (0x1EADD, 0x1EAFB), (0x1EB36, 0x1EB4F),
    (0x1EB6C, 0x1EB8F), (0x1EB9F, 0x1EBCD), (0x1EBD1, 0x1EBE7), (0x1EC01, 0x1EC67), (0x1EC7C, 0x1ECA9),
    (0x1ECD9, 0x1ECF6), (0x1ED07, 0x1ED26), (0x1ED2C, 0x1ED6B), (0x1ED7B, 0x1ED9D), (0x1ED9E, 0x1EDB1),
    (0x1EDB6, 0x1EDCB), (0x1EDCC, 0x1EDE7), (0x1EDEB, 0x1EE07), (0x1EE08, 0x1EE18), (0x1EE1A, 0x1EE30),
    (0x1EE36, 0x1EE46), (0x1EE4D, 0x1EEC0), (0x1EEF2, 0x1EF12), (0x1EF1A, 0x1EF89), (0x1EF95, 0x1EFBE),
    (0x1EFCD, 0x1EFE2), (0x1EFE3, 0x1F005), (0x1F008, 0x1F090), (0x1F097, 0x1F0AD), (0x1F0AE, 0x1F0CC),
    (0x1F0D2, 0x1F0FC), (0x1F10E, 0x1F157), (0x1F163, 0x1F21A), (0x1F21B, 0x1F22F), (0x1F23B, 0x1F28A),
    (0x1F2B0, 0x1F2D5), (0x1F2D6, 0x1F2E6), (0x1F2EA, 0x1F30C), (0x1F311, 0x1F32F), (0x1F330, 0x1F335),
    (0x1F336, 0x1F358), (0x1F35E, 0x1F393), (0x1F397, 0x1F41F), (0x1F424, 0x1F430), (0x1F431, 0x1F443),
    (0x1F444, 0x1F47E), (0x1F47F, 0x1F4A4), (0x1F4A5, 0x1F4BB), (0x1F4BC, 0x1F4E0), (0x1F51C, 0x1F563),
    (0x1F57A, 0x1F5B9), (0x1F5E3, 0x1F610), (0x1F61E, 0x1F66A), (0x1F66E, 0x1F6AD), (0x1F6D1, 0x1F71C),
    (0x1F73C, 0x1F77F), (0x1F783, 0x1F79A), (0x1F79B, 0x1F7AA), (0x1F830, 0x1F87B), (0x1F891, 0x1F8AF),
    (0x1F8D5, 0x1F9EE), (0x1F9FC, 0x1FA2B), (0x1FA3D, 0x1FA4D), (0x1FA5C, 0x1FAB4), (0x1FAB8, 0x1FAEB),
    (0x1FAF3, 0x1FB16), (0x1FB1E, 0x1FB3D), (0x1FB63, 0x1FB7E), (0x1FB80, 0x1FB8A), (0x1FB97, 0x1FBD2),
    (0x1FBEF, 0x1FBFF), (0x1FC3A, 0x1FC42), (0x1FC4D, 0x1FC64), (0x1FD2D, 0x1FD42), (0x1FD45, 0x1FD80),
    (0x1FDD2, 0x1FDE4), (0x1FE0C, 0x1FE28), (0x1FE43, 0x1FE51), (0x1FE5B, 0x1FE60), (0x1FE61, 0x1FE7C),
    (0x1FE9C, 0x1FEB4), (0x1FEBF, 0x1FED2), (0x1FEE0, 0x1FEE8), (0x1FF0A, 0x1FF2B), (0x1FF34, 0x1FF36),
    (0x1FF37, 0x1FF41),
    # Battle messages
    (0x1D281, 0x1D28C), (0x1D28D, 0x1D29C), (0x1D29D, 0x1D2AB), (0x1D2AC, 0x1D2B7), (0x1D2B8, 0x1D2C7),
    (0x1D2C8, 0x1D2D3), (0x1D2D4, 0x1D2DE), (0x1D2DF, 0x1D2E3), (0x1D2E4, 0x1D2E9), (0x1D2EA, 0x1D2EE),
    (0x1D2EF, 0x1D2F4), (0x1D2F5 + 3, 0x1D315), (0x1D316 + 3, 0x1D330),
    (0x1D331, 0x1D336), (0x1D337, 0x1D33B), (0x1D33C, 0x1D340), (0x1D341, 0x1D347), (0x1D348, 0x1D34D),
    (0x1D34E, 0x1D352), (0x1D353, 0x1D359), (0x1D35A, 0x1D360), (0x1D361, 0x1D369), (0x1D36A, 0x1D36D),
    (0x1D36E, 0x1D371), (0x1D372, 0x1D376), (0x1D377, 0x1D37A), (0x1D37B, 0x1D380), (0x1D381, 0x1D385),
    (0x1D386, 0x1D38B), (0x1D38C, 0x1D391), (0x1D392, 0x1D397), (0x1D398, 0x1D39F), (0x1D3A0, 0x1D3A6),
    (0x1D3A7, 0x1D3AB), (0x1D3AC, 0x1D3B1), (0x1D3B2, 0x1D3BA), (0x1D3BB, 0x1D3C0), (0x1D3C1, 0x1D3C8),
    (0x1D3C9, 0x1D3CE), (0x1D3CF, 0x1D3D2), (0x1D3D3, 0x1D3D6), (0x1D3D7 + 3, 0x1D3E1), (0x1D3E2, 0x1D3EB),
    (0x1D3FF + 3, 0x1D410), (0x1D411 + 3, 0x1D424), (0x1D425, 0x1D42C), (0x1D42D, 0x1D43A), (0x1D43B, 0x1D442),
    (0x1D443, 0x1D446), (0x1D451, 0x1D457), (0x1D458, 0x1D463), (0x1D464, 0x1D46D), (0x1D46E, 0x1D477),
    (0x1D478 + 3, 0x1D483), (0x1D484 + 3, 0x1D48F), (0x1D490, 0x1D49B), (0x1D49C, 0x1D4A6), (0x1D4A7, 0x1D4B1),
    (0x1D4B2, 0x1D4BD), (0x1D4BE + 3, 0x1D4CE), (0x1D4CF, 0x1D4DE), (0x1D4DF, 0x1D4F0), (0x1D4F1, 0x1D4FD),
    (0x1D4FE, 0x1D506), (0x1D507, 0x1D514), (0x1D515, 0x1D529), (0x1D52A + 3, 0x1D538), (0x1D539 + 3, 0x1D54C),
    (0x1D556, 0x1D55E), (0x1D55F, 0x1D56B), (0x1D56C, 0x1D577), (0x1D578, 0x1D582), (0x1D58F, 0x1D599),
    (0x1D59C, 0x1D5AA), (0x1D5AF, 0x1D5B4), (0x1D5B7, 0x1D5C9), (0x1D5DE, 0x1D5E4),
    #
    (0x18776, 0x1877c), # Empty!
    (0x18BF5, 0x18BFc), # How many?
    (0x18C05, 0x18c0a), # Price
    (0x18c13, 0x18c17), # Gold

    (0x1A004, 0x1a016), # Give up? No/Yes
    (0x1A4c2, 0x1A4d0), # Battlefield Round
    (0x1A4F8, 0x1a506), # Already cleaned out!

    (0x1A146, 0x1A14A), # ITEM - BATTLE SUB
    (0x1A246, 0x1A24B), # SPELL - BATTLE SUB

    (0x1B0BE, 0x1b0C4), # BATTLE
    (0x1B0CF, 0x1b0d2), # RUN (1BYTE)
    (0x1B0DD, 0x1b0e4), # CONTROL (1BYTE)

    (0x1b13c, 0x1b140), # ITEM
    (0x1B14B, 0x1b152), # DEFENSE
    (0x1B15D, 0x1b163), # ATTACK
    (0x1B16E, 0x1b173), # SPELL

    (0x1B344, 0x1b348), # LIFE

    (0x1953A, 0x19542), # NEW GAME
    (0x195D9, 0x195e6), # Save completed
    (0x196A4, 0x196aa), # Empty!

    (0x19A65, 0x19a70), # Defense Total
    (0x19AD3, 0x19adb), # Attack Power
    (0x19B0A, 0x19b13) # Defense Power

]

char_tbl: dict = {
    # Special Bytes
    0x01: '<LINE>\n', 0x30: '<SCROLL>\n', 0x31: '\n<SPEAKER1:>\n', 0x32: '\n<SPEAKER2:>\n', 0x35: '<HERONAME>',
    0x36: '<END>',
    # FONT
    0x90: '0', 0x91: '1', 0x92: '2', 0x93: '3', 0x94: '4', 0x95: '5', 0x96: '6', 0x97: '7', 0x98: '8', 0x99: '9',
    0x9A: 'A', 0x9B: 'B', 0x9C: 'C', 0x9D: 'D', 0x9E: 'E', 0x9F: 'F', 0xA0: 'G', 0xA1: 'H', 0xA2: 'I', 0xA3: 'J',
    0xA4: 'K', 0xA5: 'L', 0xA6: 'M', 0xA7: 'N', 0xA8: 'O', 0xA9: 'P', 0xAA: 'Q', 0xAB: 'R', 0xAC: 'S', 0xAD: 'T',
    0xAE: 'U', 0xAF: 'V', 0xB0: 'W', 0xB1: 'X', 0xB2: 'Y', 0xB3: 'Z', 0xB4: 'a', 0xB5: 'b', 0xB6: 'c', 0xB7: 'd',
    0xB8: 'e', 0xB9: 'f', 0xBA: 'g', 0xBB: 'h', 0xBC: 'i', 0xBD: 'j', 0xBE: 'k', 0xBF: 'l', 0xC0: 'm', 0xC1: 'n',
    0xC2: 'o', 0xC3: 'p', 0xC4: 'q', 0xC5: 'r', 0xC6: 's', 0xC7: 't', 0xC8: 'u', 0xC9: 'v', 0xCA: 'w', 0xCB: 'x',
    0xCC: 'y', 0xCD: 'z', 0xCE: '!', 0xCF: '?', 0xD0: ',', 0xD1: '\'', 0xD2: '.', 0xD3: '\u201C', 0xD4: '\u201D',
    0xD5: '."', 0xD6: ';', 0xD7: ':', 0xD8: '…', 0xD9: '/', 0xDA: '-', 0xDB: '&', 0xDC: '>', 0xDD: '%', 0xFF: ' ',
    0xDE: 'È', 0xDF: 'à', 0xE0: 'é', 0xE1: 'è', 0xE2: 'ì', 0xE3: 'ò', 0xE4: 'ù'
}

inv_char_tbl = {v: k for k, v in char_tbl.items()}

mte_tbl: dict = {
    # MTE
    0x3D: 'Crystal', 0x3E: 'Rainbow Road', 0x3F: 'th', 0x40: 'e ', 0x41: 'the ', 0x42: 't ', 0x43: 'ou', 0x44: 'you',
    0x45: 's ', 0x46: 'to ', 0x47: 'in', 0x48: 'ing ', 0x49: 'l ', 0x4A: 'll ', 0x4B: 'er', 0x4C: 'd ', 0x4D: ', ',
    0x4E: '\'s ', 0x4F: 'an', 0x52: 'ight', 0x53: '...', 0x54: 'on', 0x55: 'you ', 0x56: 'en', 0x57: 'ha', 0x58: 'ow',
    0x59: 'y ', 0x5A: 'of ', 0x5B: 'Th', 0x5C: 'or', 0x5D: 'I\'ll ', 0x5E: 'ea', 0x5F: 'is ', 0x60: 'es', 0x63: 'wa',
    0x64: 'again', 0x65: 'st', 0x66: 'I ', 0x67: 've ', 0x68: 'ed ', 0x69: 'om', 0x6A: 'er ', 0x6B: 'p ', 0x6C: 'ack',
    0x6D: 'ust ', 0x6E: '!<END>', 0x6F: '!<LINE>\n', 0x70: 'that ', 0x71: 'prophecy', 0x72: 'o ', 0x73: '.<LINE>\n',
    0x74: '.<END>', 0x75: 'I\'m ', 0x76: 'el', 0x77: 'with ', 0x78: 'a ', 0x79: 'Spencer', 0x7A: 'ma', 0x7B: 'in ',
    0x7C: 'monst', 0x7D: 'k ', 0x7E: '\'t '
}


special_tbl: dict = {
    # Character Speaking
    0x1A00: 'Hero:', 0x1A02: 'Old Man:', 0x1A08: 'Old Man:', 0x1A0A: 'Man in Forest:', 0x1A0B: 'Minotaur:',
    0x1A14: 'Kaeli\'s Mom:', 0x1A15: 'Kaeli:', 0x1A1B: 'Flamerus Rex:', 0x1A1C: 'Phoebe:', 0x1A31: 'Ice Golem:',
    0x1A32: 'Spencer:', 0x1A3B: 'Arion:', 0x1A3C: 'Arion\'s Friend:', 0x1A46: 'Phoebe:', 0x1A4E: 'Hydra:',
    0x1A5B: 'Otto:', 0x1A5C: 'Otto:', 0x1A5F: 'Mac:', 0x1A60: 'Phoebe:', 0x1A7C: 'Phoebe:',
    0x1A81: 'Old Man:', 0x1A82: 'Kaeli:', 0x1A83: 'Kaeli\'s Mom:', 0x1A84: 'Tristam:', 0x1A85: 'Tristam:',
    0x1A86: 'Tristam:', 0x1A87: 'Phoebe:', 0x1A88: 'Sprite:', 0x1A89: 'Sprite:', 0x1A8A: 'Phoebe:',
    0x1A8B: 'Phoebe:', 0x1A8C: 'Phoebe:', 0x1A8D: 'Phoebe:', 0x1A8E: 'Phoebe:', 0x1A8F: 'Tristam:',
    0x1A90: 'Phoebe:', 0x1A91: 'Reuben:', 0x1A92: 'Arion:', 0x1A95: 'Reuben:', 0x1A96: 'Tristam:',
    0x1A97: 'Monster:', 0x1A98: 'Tristam:', 0x1A99: 'Kaeli:', 0x1A9C: 'Kaeli:', 0x1A9D: '???',
    0x1A9E: 'Tristam:', 0x1A9F: 'Spencer:', 0x1AA0: 'Kaeli:', 0x1AA1: 'Reuben:', 0x1AA2: 'Light Crystal:',
    0x1AA4: 'Reuben:', 0x1AA7: 'Crystals:', 0x1AA9: 'Mac:', 0x1AAB: 'Reuben:', 0x1AAC: 'Kaeli:',
    0x1AAD: 'Phoebe:', 0x1AAE: 'Reuben:', 0x1AAF: 'Kaeli\'s Mom:', 0x1AB0: 'Spencer:', 0x1AB1: '???',
    0x1AB2: 'Otto:', 0x1AB3: 'Girl:', 0x1AB4: 'Mac:', 0x1AB5: 'Woman:',
    # Character mentioned
    0x1B00: 'Hero:', 0x1B09: 'Old Man:', 0x1B1C: 'Phoebe:', 0x1B26: 'Kaeli:', 0x1B2E: 'Old Man:',
    0x1B32: 'Spencer:', 0x1B3B: 'Arion:', 0x1B3A: 'Reuben:', 0x1B3F: 'Spencer:', 0x1B4F: 'Tree:',
    0x1B54: 'Dullihan:', 0x1B5B: 'Kaeli:', 0x1B5C: 'Otto:', 0x1B5F: 'Mac:', 0x1B6A: 'Norma:',
    0x1B75: 'Mac:', 0x1B7A: 'Dark King:', 0x1B7E: 'Tristam:', 0x1B81: 'Old Man:', 0x1B82: 'Kaeli:',
    0x1B84: 'Tristam:', 0x1B86: 'Tristam:', 0x1B89: 'Phoebe:', 0x1B91: 'Reuben:', 0x1B94: 'Reuben:',
    0x1B95: 'Reuben:', 0x1B9C: 'Kaeli:', 0x1B9D: 'Reuben:', 0x1BA2: '???', 0x1BA3: '???', 0x1BA5: '???',
    0x1BAA: 'Spencer:', 0x1BDB: 'Kaeli:',
    # Main Characters Names
    0x1D01: 'Kaeli', 0x1D02: 'Tristam', 0x1D03: 'Phoebe', 0x1D04: 'Reuben',
    # Objects
    0x1E00: 'Elixir', 0x1E01: 'Tree Wither', 0x1E02: 'Wakewater', 0x1E03: 'Venus Key', 0x1E04: 'Multi-Key',
    0x1E05: 'Mask', 0x1E06: 'Magic Mirror', 0x1E07: 'Thunder Rock', 0x1E08: 'Captain Cap', 0x1E09: 'Libra Crest',
    0x1E0A: 'Gemini Crest', 0x1E0B: 'Mobius Crest', 0x1E0C: 'Sand Coin', 0x1E0D: 'River Coin', 0x1E0E: 'Sun Coin',
    0x1E0F: 'Sky Coin', 0x1E10: 'Cure Potion', 0x1E11: 'Heal Potion', 0x1E12: 'Seed', 0x1E13: 'Refresher',
    0x1E14: 'Exit', 0x1E15: 'Cure', 0x1E16: 'Heal', 0x1E17: 'Life', 0x1E18: 'Quake', 0x1E19: 'Blizzard',
    0x1E1A: 'Fire', 0x1E1B: 'Aero', 0x1E1C: 'Thunder', 0x1E1D: 'White', 0x1E1E: 'Meteor', 0x1E1F: 'Flare',
    0x1E20: 'Steel Sword', 0x1E21: 'Knight Sword', 0x1E22: 'Excalibur', 0x1E23: 'Axe', 0x1E24: 'Battle Axe',
    0x1E25: 'Giant\'s Axe', 0x1E26: 'Cat Claw', 0x1E27: 'Charm Claw', 0x1E28: 'Dragon Claw', 0x1E29: 'Bomb',
    0x1E2A: 'Jumbo Bomb', 0x1E2B: 'Mega Grenade', 0x1E2C: 'Morning Star', 0x1E2D: 'Bow of Grace',
    0x1E2E: 'Ninja Star', 0x1E2F: 'Steel Helm', 0x1E30: 'Moon Helm', 0x1E31: 'Apollo Helm', 0x1E32: 'Steel Armor',
    0x1E33: 'Noble Armor', 0x1E34: 'Gaia\'s Armor', 0x1E35: 'Relica Armor', 0x1E36: 'Mystic Robe',
    0x1E37: 'Flame Armor', 0x1E38: 'Black Robe', 0x1E39: 'Steel Shield', 0x1E3A: 'Venus Shield',
    0x1E3B: 'Aegis Shield', 0x1E3C: 'Ether Shield', 0x1E3D: 'Charm', 0x1E3E: 'Magic Shield', 0x1E3F: 'Cupid Locket',
    # Weapons/Attacks
    0x1E40: 'Sword', 0x1E41: 'Scimitar', 0x1E42: 'Dragon Cut', 0x1E43: 'Rapier', 0x1E44: 'Axe', 0x1E45: 'Beam',
    0x1E46: 'Bone Missile', 0x1E47: 'Bow & Arrow', 0x1E48: 'Blow Dart', 0x1E49: 'Cure', 0x1E4A: 'Heal',
    0x1E4B: 'Quake', 0x1E4C: 'Blizzard', 0x1E4D: 'Fire', 0x1E4E: 'Thunder', 0x1E4F: 'Reflectant',
    0x1E50: 'Electrapulse', 0x1E51: 'Power Drain', 0x1E52: 'Spark', 0x1E53: 'Iron Nail', 0x1E54: 'Scream',
    0x1E55: 'Quicksand', 0x1E56: 'Doom Gaze', 0x1E57: 'Doom Powder', 0x1E58: 'Cure', 0x1E59: 'Fire Breath',
    0x1E5A: 'Punch', 0x1E5B: 'Kick', 0x1E5C: 'Uppercut', 0x1E5D: 'Stab', 0x1E5E: 'Head Butt', 0x1E5F: 'Body Slam',
    0x1E60: 'Scrunch', 0x1E61: 'Full Nelson', 0x1E62: 'Neck Choke', 0x1E63: 'Dash', 0x1E64: 'Roundhouse',
    0x1E65: 'Choke Up', 0x1E66: 'Stomp Stomp', 0x1E67: 'Mega Punch', 0x1E68: 'Bearhug', 0x1E69: 'Axe Bomber',
    0x1E6A: 'Piledriver', 0x1E6B: 'Sky Attack', 0x1E6C: 'Wraparound', 0x1E6D: 'Dive', 0x1E6E: 'Attach',
    0x1E6F: 'Mucus', 0x1E70: 'Claw', 0x1E71: 'Fang', 0x1E72: 'Beak', 0x1E73: 'Sting', 0x1E74: 'Tail',
    0x1E75: 'Psudopod', 0x1E76: 'Bite', 0x1E77: 'Hydro Acid', 0x1E78: 'Branch', 0x1E79: 'Fin', 0x1E7A: 'Scissor',
    0x1E7B: 'Whip Tongue', 0x1E7C: 'Horn', 0x1E7D: 'Giant Blade', 0x1E7E: 'Headomerang', 0x1E7F: 'Chew Off',
    0x1E80: 'Quake', 0x1E81: 'Flame', 0x1E82: 'Flame Sweep', 0x1E83: 'Fireball', 0x1E84: 'Flame Pillar',
    0x1E85: 'Heatwave', 0x1E86: 'Water Gun', 0x1E87: 'Coldness', 0x1E88: 'Icy Foam', 0x1E89: 'Ice Block',
    0x1E8A: 'Snowstorm', 0x1E8B: 'Whirlwater', 0x1E8C: 'Ice Breath', 0x1E8D: 'Tornado', 0x1E8E: 'Typhoon',
    0x1E8F: 'Hurricane', 0x1E90: 'Thunder', 0x1E91: 'Thunder Beam', 0x1E92: 'Corrode Gas', 0x1E93: 'Doom Dance',
    0x1E94: 'Sonic Boom', 0x1E95: 'Bark', 0x1E96: 'Screechvoice', 0x1E97: 'Para-needle', 0x1E98: 'Para-claw',
    0x1E99: 'Para-snake', 0x1E9A: 'Para-breath', 0x1E9B: 'Poison Sting', 0x1E9C: 'Poison Thorn',
    0x1E9D: 'Rotton Mucus', 0x1E9E: 'Poison Snake', 0x1E9F: 'Poisonbreath', 0x1EA0: 'Blinder', 0x1EA1: 'Blackness',
    0x1EA2: 'Stone Beak', 0x1EA3: 'Gaze', 0x1EA4: 'Stare', 0x1EA5: 'Spooky Laugh', 0x1EA6: 'Riddle',
    0x1EA7: 'Bad Breath', 0x1EA8: 'Body Oder', 0x1EA9: 'Para-stare', 0x1EAA: 'Poison Fluid',
    0x1EAB: 'Poison Flour', 0x1EAC: 'Hypno-sleep', 0x1EAD: 'Lullaby', 0x1EAE: 'Sleep Lure',
    0x1EAF: 'Sleep Powder', 0x1EB0: 'Blind Flash', 0x1EB1: 'Smokescreen', 0x1EB2: 'Muffle', 0x1EB3: 'Silence Song',
    0x1EB4: 'Stone Gas', 0x1EB5: 'Stone Gaze', 0x1EB6: 'Double Sword', 0x1EB7: 'Double Hit', 0x1EB8: 'Triple Fang',
    0x1EB9: 'Double Kick', 0x1EBA: 'Twin Shears', 0x1EBB: 'Three Heads', 0x1EBC: '6 Psudopods', 0x1EBD: 'Snake Head',
    0x1EBE: 'Drain', 0x1EBF: 'Dissolve', 0x1EC0: 'Sucker Stick', 0x1EC1: 'Selfdestruct', 0x1EC2: 'Multiply',
    0x1EC3: 'Para Gas', 0x1EC4: 'Rip Earth', 0x1EC5: 'Stone Block', 0x1EC6: 'Windstorm', 0x1EC7: 'Twin Fang',
    0x1EC8: 'Psychshield', 0x1EC9: 'Psychshield', 0x1ECA: 'Dark Cane', 0x1ECB: 'Dark Saber', 0x1ECC: 'Ice Sword',
    0x1ECD: 'Fire Sword', 0x1ECE: 'Mirror Sword', 0x1ECF: 'Quake Axe', 0x1ED0: 'Cure Arrow', 0x1ED1: 'Lazer',
    0x1ED2: 'Spider Kids', 0x1ED3: 'Silver Web', 0x1ED4: 'Golden Web', 0x1ED5: 'Mega Flare', 0x1ED6: 'Mega White',
    0x1ED7: 'Fire Breath', 0x1ED8: 'Sky Attack', 0x1ED9: 'Piledriver', 0x1EDA: 'Hurricane', 0x1EDB: 'Heatwave',
    0x1EDC: 'BLANK', 0x1EDD: 'Explosive', 0x1EDE: 'Arrow', 0x1EDF: 'Ninja Star',
    # Locations
    0x1F00: 'World', 0x1F01: 'Focus Tower', 0x1F02: 'Hill of Destiny', 0x1F03: 'Level Forest', 0x1F04: 'Foresta',
    0x1F05: 'Kaeli\'s House', 0x1F06: 'Sand Temple', 0x1F07: 'Bone Dungeon', 0x1F08: 'Libra Temple', 0x1F09: 'Aquaria',
    0x1F0A: 'Phoebe\'s House', 0x1F0B: 'Wintry Cave', 0x1F0C: 'Life Temple', 0x1F0D: 'Falls Basin',
    0x1F0E: 'Ice Pyramid', 0x1F0F: 'Spencer\'s Place', 0x1F11: 'Fireburg', 0x1F12: 'Rueben\'s House', 0x1F13: 'Mine',
    0x1F14: 'Sealed Palace', 0x1F15: 'Volcano', 0x1F16: 'Lava Dome', 0x1F17: 'Rope Bridge', 0x1F18: 'Alive Forest',
    0x1F19: 'Giant Tree', 0x1F1A: 'Kaidge Temple', 0x1F1B: 'Windhole Temple', 0x1F1C: 'Mount Gale', 0x1F1D: 'Windia',
    0x1F1E: 'Otto\'s House', 0x1F1F: 'Pazuzu\'s Tower', 0x1F20: 'Light Temple', 0x1F21: 'Ship Dock', 0x1F22: 'Deck',
    0x1F23: 'Mac\'s Ship', 0x1F24: 'Doom Castle',
    # Objects
    0x2000: 'Brownie', 0x2001: 'Mintmint', 0x2002: 'Red Cap', 0x2003: 'Mad Plant', 0x2004: 'Plant Man',
    0x2005: 'Live Oak', 0x2006: 'Slime', 0x2007: 'Jelly', 0x2008: 'Ooze', 0x2009: 'Poison Toad', 0x200A: 'Giant Toad',
    0x200B: 'Mad Toad', 0x200C: 'Basilisk', 0x200D: 'Flazzard', 0x200E: 'Salamand', 0x200F: 'Sand Worm',
    0x2010: 'Land Worm', 0x2011: 'Leech', 0x2012: 'Skeleton', 0x2013: 'Red Bone', 0x2014: 'Skulder', 0x2015: 'Roc',
    0x2016: 'Sparna', 0x2017: 'Garuda', 0x2018: 'Zombie', 0x2019: 'Mummy', 0x201A: 'Desert Hag', 0x201B: 'Water Hag',
    0x201C: 'Ninja', 0x201D: 'Shadow', 0x201E: 'Sphinx', 0x201F: 'Manticor', 0x2020: 'Centaur', 0x2021: 'NiteMare',
    0x2022: 'Stooney Roost', 0x2023: 'Hot Wings', 0x2024: 'Ghost', 0x2025: 'Spector', 0x2026: 'Gather',
    0x2027: 'Beholder', 0x2028: 'Fangpire', 0x2029: 'Vampire', 0x202A: 'Mage', 0x202B: 'Sorcerer',
    0x202C: 'Land Turtle', 0x202D: 'Adamant Turtle', 0x202E: 'Scorpion', 0x202F: 'Snipion', 0x2030: 'Werewolf',
    0x2031: 'Cerberus', 0x2032: 'Edgehog', 0x2033: 'Sting Rat', 0x2034: 'Lamia', 0x2035: 'Chimera', 0x2036: 'Avizzard',
    0x2037: 'Gargoyle', 0x2038: 'Gorgun', 0x2039: 'Minotaur Zombie', 0x203A: 'Phanquid', 0x203B: 'Freezer Crab',
    0x203C: 'Iflyte', 0x203D: 'Stheno', 0x203E: 'Chimera', 0x203F: 'Thanatos', 0x2040: 'Skullrus Rex',
    0x2041: 'Stone Golem', 0x2042: 'Behemoth', 0x2043: 'Minotaur', 0x2044: 'Squidite', 0x2045: 'Snow Crab',
    0x2046: 'Jinn', 0x2047: 'Medusa', 0x2048: 'Gidrah', 0x2049: 'Dullihan', 0x204A: 'Flameosaurus Rex',
    0x204B: 'Ice Golem', 0x204C: 'Dual Headed Hydra', 0x204D: 'Twin Headed Wyvern', 0x204E: 'Pazuzu', 0x204F: 'Zuh',
    0x2050: 'Dark King', 0x2051: 'Demoplay'}

dialogues_to_move: list = [
    '250', '251', '253', '254', '255', '256', '316', '317']

dialogues_to_keep: dict = {
    '11': 0x1BF26 + 3, '236': 0x1C261 + 3, '237': 0x1C413 + 3, '239': 0x1C82F + 3,
    '240': 0x1CA56 + 3, '241': 0x1D9DE + 3, '243': 0x1DC76 + 3}

def main():
    version = 'v0.1'

    desc = 'FFMQtool {} - Final Fantasy Mystic Quest SCRIPT Tool\n'.format(version) + \
           'Created by _Ombra_ of Mumble Translations\n' + \
           'Website: https://mumble.romhacking.it'

    parser = argparse.ArgumentParser(prog='FFMQtool',
                                     formatter_class=argparse.RawDescriptionHelpFormatter,
                                     description=desc)

    commands = parser.add_subparsers(dest='command')

    extract = commands.add_parser('extract', help='extract script or font from ROM')
    extract.add_argument('SCRIPTorFONT', choices=['script', 'font'])
    extract.add_argument('ROM', help='ROM file')

    insert = commands.add_parser('insert', help='extract script or font from ROM')
    insert.add_argument('SCRIPTorFONT', choices=['script', 'font'])
    insert.add_argument('FILE', help='SCRIPT TXT or FONT BIN file')
    insert.add_argument('ROM', help='ROM file')

    args = parser.parse_args()

    # If no argument is passed, show the help
    if args.command is None:
        parser.print_help()
    else:
        # If extract argument is passed, check if file exists and is a file, then extract
        if args.command == 'extract':
            if not os.path.exists(args.ROM) or not os.path.isfile(args.ROM):
                print('\nROM File does not exist')
                exit()

            rom = open(args.ROM, "rb").read()
            # Check validity of ROM
            # check_rom(rom)

            if args.SCRIPTorFONT == 'script':
                do_extract_script(rom)
            else:
                do_extract_font(rom)

        # If insert argument is passed, check if folder exists and is a folder, then insert
        elif args.command == 'insert':

            if not os.path.exists(args.FILE) or not os.path.isfile(args.FILE):
                print('\nSCRIPT of FONT Files do not exist')
                exit()
            elif not os.path.exists(args.ROM) or not os.path.isfile(args.ROM):
                print('\nROM Files do not exist')
                exit()

            rom = open(args.ROM, 'rb+').read()
            # Check validity of ROM
            # check_rom(rom)

            if args.SCRIPTorFONT == 'script':
                script = open(args.FILE, 'r').readlines()
                do_insert_script(args.ROM, args.FILE)
            elif args.SCRIPTorFONT == 'font':
                font = open(args.FILE, 'rb').read()
                do_insert_font(rom, font)


def check_rom(rom):
    # Read ROM name and calculate CRC32
    rom_name = rom[0x7FC0:0x7FD6]
    rom_crc = hex(zlib.crc32(rom) & 0xffffffff)
    # Check if ROM is correct. If it is, continue execution.
    if rom_name != b'FF MYSTIC QUEST       ' or rom_crc != '0x2c52c792':
        print('\nROM file is not correct')
        exit()
    else:
        pass


########################################################################################################################
# EXTRACTOR
########################################################################################################################


def do_extract_script(rom):

    print("\nExtracting {} dialogues...".format(len(dialogues) + 1))
    output = open("dump_eng.txt", "w", encoding="utf-8")
    i = 0

    while i < len(dialogues):
        ofs_start = (dialogues[i])[0]
        ofs_end = (dialogues[i])[1]
        output.write("[BLOCK {}: 0x{:02X} to 0x{:02X}]\n".format(i, ofs_start, ofs_end))
        block: bytes = rom[ofs_start:ofs_end]
        decoded_block = do_decode_block(block)
        output.write(decoded_block + "\n\n")
        i += 1

    output.close()
    print("Extraction completed!")


def do_decode_block(block):
    decoded_block: str = ''
    i = 0

    # Loop bytes
    while i < len(block):
        b1 = block[i]
        b2 = block[i + 1] if i + 1 < len(block) else None
        b3 = block[i + 2] if i + 2 < len(block) else None

        try:
            decoded_block += char_tbl[b1]

        except KeyError:

            if b1 in mte_tbl:
                decoded_block += mte_tbl[b1]

            elif b2 is not None or b3 is not None:
                char: int = (b1 << 8 | b2)

                if b1 in (0x1A, 0x1B) and char in special_tbl:
                    decoded_block += "\n<{:02X} {}>\n".format(char, special_tbl[char])
                    i += 1
                elif b1 in (0x1D, 0x1E, 0x1F, 0x20) and char in special_tbl:
                    decoded_block += special_tbl[char]
                    i += 1
                elif b1 in (0x05, 0x1A, 0x1B, 0x1D, 0x1E, 0x1F, 0x20, 0x2E) and char not in special_tbl:
                    decoded_block += '<{:02X}{:02X}>'.format(b1, b2)
                    i += 1
                elif b1 in (0x03, 0x08, 0x0C, 0x0F, 0x2F):
                    decoded_block += '<{:02X}{:02X}{:02X}>'.format(b1, b2, b3)
                    i += 2
                else:
                    decoded_block += '<{:02X}>'.format(b1)
            else:
                decoded_block += '<{:02X}>'.format(b1)
        i += 1

    # Sanitize decoded_block in case \n is the first char of the decoded block
    if decoded_block[0] == '\n':
        decoded_block = decoded_block[1:]

    return decoded_block


def do_extract_font(rom):
    print("\nExtracting font...")
    output = open("font.bin", "wb")

    # Reading the font from the ROM (4096 bytes)
    font_data: bytes = rom[0x38030:0x39030]

    # Read and organize the pixels in 64 bytes chunks
    i = 0
    while i < len(font_data):
        tiles = 0
        while tiles < 64:
            pixel01: bytes = font_data[i:i + 2]
            pixel23: bytes = font_data[i + 0x040:i + 0x042]
            pixel45: bytes = font_data[i + 0x080:i + 0x082]
            pixel67: bytes = font_data[i + 0x0C0:i + 0x0C2]
            pixel89: bytes = font_data[i + 0x100:i + 0x102]
            pixelAB: bytes = font_data[i + 0x140:i + 0x142]
            pixelCD: bytes = font_data[i + 0x180:i + 0x182]
            pixelEF: bytes = font_data[i + 0x1C0:i + 0x1C2]
            output.write(pixel01 + pixel23 + pixel45 + pixel67 + pixel89 + pixelAB + pixelCD + pixelEF)
            tiles += 2
            i += 2
        i += 448

    output.close()
    print("Extraction completed!")


########################################################################################################################
# INSERTION
########################################################################################################################

def pc2snes_lorom(offset):
    return ((offset * 2) & 0xFF0000) + (offset & 0x7FFF) + 0x8000


def snes2pc_lorom(offset):
    return (int(offset / 2) & 0xFF0000) + (offset & 0xFFFF) - 0x8000

def do_encode_text(text):
    encoded_text = b''
    i = 0
    while i < len(text):
        char = text[i]
        if char == '<':
            char_to_decode = '<'
            while char != '>':
                i += 1
                char = text[i]
                char_to_decode += char
            if char_to_decode == '<LINE>':
                char_to_decode = '<LINE>\n'
            elif char_to_decode == '<SCROLL>':
                char_to_decode = '<SCROLL>\n'
            elif char_to_decode == '<SPEAKER1:>':
                char_to_decode = '\n<SPEAKER1:>\n'
            elif char_to_decode == '<SPEAKER2:>':
                char_to_decode = '\n<SPEAKER2:>\n'
            decoded_char = inv_char_tbl.get(char_to_decode)
            if not decoded_char:
                if ':' in char_to_decode:
                    special_code = char_to_decode.split(' ')[0][1:]
                    special_code_int = int(special_code, 16)
                    if special_tbl.get(special_code_int):
                        encoded_char = struct.pack(">h", special_code_int)
                    else:
                        raise Exception(char_to_decode)
                else:
                    char_to_decode = char_to_decode[1:-1].replace(' ???', '')
                    encoded_char = bytes.fromhex(char_to_decode)
            else:
                encoded_char = struct.pack(">b", decoded_char)
            encoded_text += encoded_char
        else:
            if char != '\n':
                if char == '.':
                    if text[i + 1] == '"':
                        i += 1
                        encoded_text += b'\xd5'
                    else:
                        encoded_char = inv_char_tbl.get(char)
                        encoded_text += bytes([encoded_char])
                else:
                    encoded_char = inv_char_tbl.get(char)
                    if not encoded_char:
                        raise Exception(char)
                    encoded_text += bytes([encoded_char])
        i += 1
    # print(encoded_text)
    return encoded_text

def do_insert_script(rom, script):
    buffer = OrderedDict()
    with open(script, 'r') as f:
        block = ''
        for line in f:
            if '[BLOCK ' in line:
                splitted_line = line.split(' ')
                block = splitted_line[1].replace(':', '')
                offset_from = int(splitted_line[2], 16)
                offset_to = int(splitted_line[4].replace(']\n', ''), 16)
                buffer[block] = ['', [offset_from, offset_to]]
            else:
                buffer[block][0] += line
    index = 0
    table_offset = 0x81000
    old_text_offset = 0x1ff65 # 149 bytes disponibili
    new_text_offset = 0x82000
    with open(rom, 'rb+') as f:
        for block, value in buffer.items():
            # print("BLOCK: " + block)
            if block == '244':
                continue
            [text, offsets] = value
            encoded_text = do_encode_text(text) # codifica il testo
            [offset_from, offset_to] = offsets
            f.seek(offset_from) # vado all'indirizzo del testo originale
            f.write(b'\xf0') # scrivo 0xf0
            f.write(struct.pack('<H', index)) # scrivo l'indice della tabella nel vecchio testo
            index_offset = table_offset + (index * 3) # calcolo l'indirizzo dell'indice della tabella
            f.seek(index_offset) # vado all'indirizzo dell'indice della tabella
            if block in dialogues_to_move:
                new_text_pointer = struct.pack('i', pc2snes_lorom(old_text_offset)) # converto l'indirizzo
            elif block in dialogues_to_keep.keys():
                new_text_pointer = struct.pack('i', pc2snes_lorom(dialogues_to_keep.get(block)))
            else:
                new_text_pointer = struct.pack('i', pc2snes_lorom(new_text_offset)) # converto l'indirizzo
            f.write(new_text_pointer[:3]) # scrivo il puntatore alla posizione del nuovo testo nella tabella
            return_pointer = struct.pack('i', pc2snes_lorom(offset_to)) # converto l'indirizzo di ritorno
            f.write(return_pointer[:3]) # scrivo il puntatore di ritorno al vecchio testo nella tabella
            index += 1 # incremento l'indice
            if block in dialogues_to_move:
                f.seek(old_text_offset) # vado all'indirizzo dove scrivere il testo
            elif block in dialogues_to_keep.keys():
                f.seek(dialogues_to_keep.get(block)) # vado all'indirizzo dove scrivere il testo
            else:
                f.seek(new_text_offset) # vado all'indirizzo dove scrivere il testo
            f.write(encoded_text) # scrivo il testo
            f.write(b'\xf0') # scrivo 0xf0
            f.write(struct.pack('<H', index)) # scrivo l'indice della tabella
            if block in dialogues_to_move:
                old_text_offset = f.tell()
            elif block in dialogues_to_keep.keys():
                pass
            else:
                new_text_offset = f.tell()
            index += 1 # incremento l'indice

def do_insert_font(rom, font):
    print("\nInserting font...")

    # Prepping the compressed data (4096 bytes)
    compressed_font_data: list = [0] * 4096

    output = open('ffmq_new.sfc', 'wb')

    # Read and organize the pixels in 64 bytes chunks
    i = 0
    block = 0
    base = 0
    while i < len(font):
        if i in (0x200, 0x400, 0x600, 0x800, 0xA00, 0xC00, 0xE00):
            block += 0x1C0
        tile = 0
        ofs = 0

        while tile < 16:
            pixel = list(font[i:i + 2])
            compressed_font_data[block+base+ofs:block+base+ofs+2] = pixel
            ofs += 0x40
            tile += 2
            i += 2
        base += 2

    new_rom = list(rom)
    new_rom[0x38030:0x39030] = compressed_font_data

    output.write(bytes(new_rom))
    output.close()

    print("Insertion completed!")


if __name__ == '__main__':
    main()
