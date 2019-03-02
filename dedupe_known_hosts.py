from sys import argv
from os import environ


class SshKnownHost():
    def __init__(self, k=None, kt=None, n=None):
        self.key = k
        self.keytype = kt
        self.__names = []
        if n is not None:
            self.names = n

    @property
    def keytype(self):
        return self.__keytype

    @keytype.setter
    def keytype(self, t):
        self.__keytype = t

    @property
    def names(self):
        return ','.join(self.__names)

    @names.setter
    def names(self, n):
        if ',' in n:
            self.__names += n.split(',')
        else:
            self.__names.append(n)

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, k):
        self.__key = k

    def __repr__(self):
        return "{} {} {}".format(self.names, self.keytype, self.key)


def main():
    knownhosts = "{}/.ssh/known_hosts".format(environ['HOME'])
    if len(argv) > 1:
        knownhosts = argv[1]

    knownhosts = open(knownhosts, 'r')
    keysdict = {}

    for n, kt, k in [line.split() for line in knownhosts]:
        if k in keysdict.keys():
            keysdict[k].names = n
        else:
            keysdict[k] = SshKnownHost(k, kt, n)

    for val in keysdict.values():
        print(val)


if __name__ == '__main__':
    main()
