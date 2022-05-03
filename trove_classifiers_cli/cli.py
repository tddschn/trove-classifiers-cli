#!/usr/bin/env python3

from trove_classifiers import classifiers
# classifiers: A set containing classifiers (as strings). Useful for determining membership.


def main() -> None:
    c_l = list(classifiers)
    c_l.sort()
    print('\n'.join(c_l))


if __name__ == '__main__':
    main()
