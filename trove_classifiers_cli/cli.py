#!/usr/bin/env python3
"""
Author : Xinyuan Chen <45612704+tddschn@users.noreply.github.com>
Date   : 2022-05-03
Purpose: Why not?
"""

import argparse
from trove_classifiers import classifiers

# classifiers: A set containing classifiers (as strings). Useful for determining membership.


def add_indentation(classifiers: list[str]) -> list[str]:
    res = []
    for c in classifiers:
        res.append('\t' * (c.count('::') - 1) + c)
    return res


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='CLI for PyPI Trove Classifiers',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('match',
                        metavar='MATCH',
                        nargs='*',
                        help='String(s) to search for',
                        default=[None])

    # parser.add_argument('-a',
    #                     '--arg',
    #                     help='A named string argument',
    #                     metavar='str',
    #                     type=str,
    #                     default='')

    parser.add_argument('-I',
                        '--case',
                        help='Perform case sensitive matching.',
                        action='store_true')

    # parser.add_argument('-f',
    #                     '--file',
    #                     help='A readable file',
    #                     metavar='FILE',
    #                     type=argparse.FileType('rt'),
    #                     default=None)

    parser.add_argument('-q',
                        '--quoted-list',
                        help='Output a quoted list',
                        action='store_true')

    parser.add_argument('-t',
                        '--tree',
                        help='Format output as a tree',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    # from icecream import ic
    # ic(args)
    match = args.match
    case = args.case
    quoted_list = args.quoted_list
    tree = args.tree

    c_l = list(classifiers)
    c_l.sort()
    if match != [None]:
        if case:
            c_l = [c for c in c_l if any(m in c for m in match)]
        else:
            match_lower = [m.lower() for m in match]
            c_l = [c for c in c_l if any(m in c.lower() for m in match_lower)]
    if quoted_list:
        print('\n'.join(['"{}",'.format(c) for c in c_l]))
    else:
        if tree:
            c_l = add_indentation(c_l)
        print('\n'.join(c_l))


if __name__ == '__main__':
    main()
