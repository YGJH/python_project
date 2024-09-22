from Crypto.Util.number import *
from sympy import symbols, solve
from gmpy2 import invert , sqrt , iroot
from libnum import nroot

n = 898494207121683242612500440870692449259945659421335241407940200935687503464958544042432583714592993691614170619398392935138999002387400531204263120616745670147932392952562195868792562069944852337309718973548158535055377935463177698990249495313772130479821685311793174922452950614442288437878964843710938077388670902422894477165235101505257760411735564053575469318903906089113620536449653696638797632236144712653203908696778665351511793021320773923213942713397700401388270039920091239405814006668108040597690207944566078892181765934214595257847651711476131415160888911345635186423337201014962963764035863693459382595084900925979485554117114069940567796221874895614465042864172137638955245664291752128593919670733665054061062396719585009214206282312514459400378963609368653857711569850486683217668348904814568672712289782083508668645655476902236546805987111793761021472893206886689668151872183924131737201706113722075840008895322956135657677537227429895243406340343946789448570341484203128015128762717198341114376972691138652870217510657356533164527400185753946563827675924789868862930748289644154859320168315074962017097483850054257068649454298497732162386662700746608087749870832425432356472146477507778719803408295237486791781114763
e = 65537
leak = 1654414018716649853055885367603031772608988025591232371235570760226816079772986421114476626505134350864789309630706802081933588211475038438909255925311850350886494681378331296172326799243471652427663066541699998267951665767635956129469995670031462357820108279028961120782781375361531543030024029958070690435436403229845323373578872052970583146183896267001861881148830803862098833928266268761350901662138572403842379352512458701760665479881748129134900825208952298535783045989352954283582437741809399923730380269971001203517697726973629916507990255513394624851395221512274135242644664483830351716093646671184553680856803968197583842243737647667141566463125021037434480026062029778156154054010489512045145663352534083153896549782401208639813264060537143496797018393923355548583179835812746397832843264413339230778043861304733621969964556176910356970861757658812971936977738044771626097504855153055734821499638178494232920508077788950353310772607044243158924539463475327212386364912076051582211062121166692712763501557195023850322878519473934794152417704687849073178803239363364983918154599122444318383925090438548121589676925986817527011853037899923593014110694282176982156378928944773581174652697321547529574072912682339707346321728
ciph = b'W\x04\x9498x+\x9c%\xcc\x87\xfd\x9e\xe2\x85\xbc\xd1\x85u\x8b\xe1\xfbL\x8d#\x89|\xcb\xf7W\xfb\xb3\t\xf1\xd6|\x0b\xc2\xd3,\xb8\xda\xf5\xe8+\x06\x13^\xd7\x0ft\x88:F\x85\xfc\xe2k\xc2\xcb\x04\xf9sR_\xedi.\xbe@6\x9d\xc2\x97\xac\xd7~\\\xdb\xe81\xf2\xc9&\xdbB"\x81\x19q2\xe2\x19\xe5\xb0\xaa\xd7~>f\x16]\xe8\x0e\x8apl\x99-=\x99lk\x13\xdf\x12u\x86*\x86W^\xa3\x8bs\x9f\xaa<\x05\x9c\xa8\xb4\xbc\x02\x8d\xa3\xee\xc8\xa3BD\nm\x81\x82\x83\xa0\x8b\xdfonuGk\xdbdJ\xe6Z!\xf2l_PR]\xa6\xb3\xbc\x01\xc0\xe7\xa0a\'`\x83\x97\x05\xae+\xabv\x1d@lm?u$\xa88!6\xc3\x07\xc5\xb0\x82\xd4\xef$!\xe3\xaaI\xf4\x0b\xdf\x9f\xff\xfcE\xab\xda(b\x80\xcf~@L_\x16\xc10\x0b\x1a#]\x18\x901\xde\xe7aD\xce\x17\xa3\x9e\xc7\xd0jR_\x8b6\xdfH,srl\xb0\x17\x14Z\xd1\x92\\\x82\xcay6\xbd\x8c\xd0\x0564\xba)\x9f\xa6w\xfb\x8d\xfb\xb3\xc6\x90\x07J\xd3\xc2\x90\xb2\xbe\xe8\xb9\x9d\xcc\xb4\x1b\xc8\xf2\xb3\xe4=\xc2J\x86\xc1\x818X\xa9]q\x8bO\'{\\\xd1au\xa3V\x98\xd8v\x12=\xd2H\xf7\xea\xc9+\x1c\x80y\x97\x11\xbb\xd7\xf0\x01\xacbq\xb4\xf99\x05\x12\x17\xd1\xde\x9e\'\x9f\xf1\xf2\x9c3\x06J\x03"\xcc(4b\xcaX\xd6\xf3\xc0\xa1\x03\x1b\x1f6W\x18\x08\xcb\xb2s%\xb5\xe0\xadz\xd3a\xca\xf0%\xb0\xf8\xe3\x97-\x9d\n\xe2\xfa\x9d\xafd\xb4{i\xe5\xac\x89\x10Sm\xd0L\x98\x0c\xbd\xe6|\xa3G\xdfF\xf9\xb6uf\xb9zz\x045\\\x98\xc7\xf07\x8e\xfb\xf2\x08\x95\xb4\xb1\x83\xc2\x18\x8f\x06\x8aY\xc9\x0e\x94KE\x0e\xa8/O\xa5\xe4s`(\x9b\xde\x81;\x16}\x9cTs.\x02U\xea\x16T\x0e\xc5`\x10\xf3Tp\xdc\xeb,\xa5\xf8\xc4p\x81\x06\x07i\x96\xb8"\x97\x19\x8at\xe5z\x9a\xc4\xb9\x8a'
ciph = bytes_to_long(ciph)

x = n*2 + 2 * n + leak
u = (1+nroot(1 + 4 * x , 2)) // 2
phi = n - u + 1


def egcd(a, b):
    if a==0:
        return (b,0,1)
    else:
        g, x, y = egcd(b % a , a)
        return (g, y-(b//a) * x , x)
def modinv(b, n):
    g, x, _ = egcd(b , n)
    if g==1:
        return x % n

# phi = 18981841105895636526675685852772632158842968216380018810386298633786155635996081803989776444322885832862508871280454015266715098097212762303823817669399277859053310692838636039765017523835850272300243126797277954387477501506925762258179024160726332434715115654485883242651742714579029928789693932848304595300557598771771916885657124686659115500480713168586733334661578825234626810544986999850919797887684002470003670584760754817335881188217827325978672125887105289532163257040782227376007186110000528082717532620633242481591525315400422216875344556182304568224748955706842779081172058234105975321598248746429911195312
tur_phi = 18981841105895636526675685852772632158842968216380018810386298633786155635996081803989776444322885832862508871280454015266715098097212762303823817669399277859053310692838636039765017523835850272300243126797277954387477501506925762258179024160726332434715115654485883242651742714579029928789693932848304595300557598771771916885657124686659115500480713168586733334661578825234626810544986999850919797887684002470003670584760754817335881188217827325978672125887105289532163257040782227376007186110000528082717532620633242481591525315400422216875344556182304568224748955706842779081172058234105975321598248746429911195312
print(phi==tur_phi)
d = modinv(e, phi)
print("d = {}".format(d))
m = pow(ciph , int(d) , n)
print(long_to_bytes(m))