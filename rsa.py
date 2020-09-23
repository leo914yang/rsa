# -*- coding: utf-8 -*-
from gcd import ext_gcd
from exponentiation import exp_mode
# 生成公鑰私鑰，p、q為兩個超大質數


def gen_key(p, q):
    n = p * q
    fy = (p - 1) * (q - 1)  # 計算與n互質的整數個數 尤拉函式
    e = 3889  # 選取e   一般選取65537
    # generate d
    a = e
    b = fy
    r, x, y = ext_gcd(a, b)
    #print(x)  # 計算出的x不能是負數，如果是負數，說明p、q、e選取失敗，一般情況下e選取65537
    d = x
    # 返回：   公鑰     私鑰
    return (n, e), (n, d)


# 加密 m是被加密的資訊 加密成為c
def encrypt(m, pubkey):
    n = pubkey[0]
    e = pubkey[1]
    c = exp_mode(m, e, n)
    return c


# 解密 c是密文，解密為明文m
def decrypt(c, selfkey):
    n = selfkey[0]
    d = selfkey[1]
    m = exp_mode(c, d, n)
    return m


if __name__ == "__main__":
    '''公鑰私鑰中用到的兩個大質數p,q'''
    p = 106697219132480173106064317148705638676529121742557567770857687729397446898790451577487723991083173010242416863238099716044775658681981821407922722052778958942891831033512463262741053961681512908218003840408526915629689432111480588966800949428079015682624591636010678691927285321708935076221951173426894836169
    q = 144819424465842307806353672547344125290716753535239658417883828941232509622838692761917211806963011168822281666033695157426515864265527046213326145174398018859056439431422867957079149967592078894410082695714160599647180947207504108618794637872261572262805565517756922288320779308895819726074229154002310375209
    '''生成公鑰私鑰'''
    pubkey, selfkey = gen_key(p, q)
    '''需要被加密的資訊轉化成數字，長度小於祕鑰n的長度，如果資訊長度大於n的長度，那麼分段進行加密，分段解密即可。'''
    m = 111111111113215555555555555555555555351646443215646514564444444444444856458465684454885641684486468464861486846646846411614816416486416468488464843781273152173157815781578155783512518318251837152851781538578251782517853872511783512851835182518218725178315782583158518218578325782378251827157821587315783251825178231578111115715782583251783158725178351782531851231538715872517832157823158753178215831523151515151515151515151515151515151515151515151515782315781582518731528152
    print("加密前明文", m)
    '''資訊加密'''
    c = encrypt(m, pubkey)
    print("加密後密文:", c)
    '''資訊解密'''
    d = decrypt(c, selfkey)
    print("解密後明文", d)
    if m == d:
        print("成功!!")
    else:
        print("失敗!!!")
