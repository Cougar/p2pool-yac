from p2pool.bitcoin import networks
from p2pool.util import math

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

nets = dict(
    yacoin=math.Object(
        PARENT=networks.nets['yacoin'],
        SHARE_PERIOD=10, # seconds
        CHAIN_LENGTH=12*60*60//10, # shares
        REAL_CHAIN_LENGTH=12*60*60//10, # shares
        TARGET_LOOKBEHIND=30, # shares
        SPREAD=10, # blocks
        IDENTIFIER='ff38e5b9e7923ff'.decode('hex'),
        PREFIX='ff06c3a24ee74ff'.decode('hex'),
        P2P_PORT=12579,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=8336,
        BOOTSTRAP_ADDRS='rav3n.dtdns.net'.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: v >= 60004,
    ),

    yacoin_testnet=math.Object(
        PARENT=networks.nets['yacoin_testnet'],
        SHARE_PERIOD=3, # seconds
        CHAIN_LENGTH=20*60//3, # shares
        REAL_CHAIN_LENGTH=20*60//3, # shares
        TARGET_LOOKBEHIND=200, # shares
        SPREAD=12, # blocks
        IDENTIFIER='e037d5b8c7923510'.decode('hex'),
        PREFIX='7208c1a54ef649b0'.decode('hex'),
        P2P_PORT=19777,
        MIN_TARGET=0,
        MAX_TARGET=2**256//2**20 - 1,
        PERSIST=False,
        WORKER_PORT=18336,
        BOOTSTRAP_ADDRS=' '.split(' '),
        ANNOUNCE_CHANNEL='#p2pool-alt',
        VERSION_CHECK=lambda v: v >= 60004,
    ),
)
for net_name, net in nets.iteritems():
    net.NAME = net_name
