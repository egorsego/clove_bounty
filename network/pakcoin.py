
from clove.network.bitcoin import Bitcoin


class Pakcoin(Bitcoin):
    """
    Class with all the necessary PAK network information based on
    http://www.github.com/pakcoin-project/pakcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'pakcoin'
    symbols = ('PAK', )
    seeds = ('seed.pakcoin.org',)
    port = 7867


class PakcoinTestNet(Pakcoin):
    """
    Class with all the necessary PAK testing network information based on
    http://www.github.com/pakcoin-project/pakcoin/blob/master/src/net.cpp
    (date of access: 02/12/2018)
    """
    name = 'test-pakcoin'
    seeds = ()
    port = 17867
