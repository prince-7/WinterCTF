from Crypto.Util.number import inverse
from Crypto.PublicKey import RSA
from Crypto.Util.number import *
import os
import binascii
c=16411916528191625268306376343416284046371378706677425453398880382491760005254791709313190311768690571528831422036503270643548618028109870557250232764055237722687680038449744825070345031141263008561223892414661860041541488377676967786740769629073420215918230890247566339971772516923300331101780065988770608882

e=65537
p=9459087979866534301854579339627517281880871857987098205400542290909533812510627152878341353678910479880680875722839306063829321130837210213784261581387173
q=9896984395151566492448748862139262345387297785144637332499966426571398040295087125558780121504834847289828037371643927199404615218623314326851473129699891
n=93616446129104844955059483483752992293153041554713362995577944006733118927583779842204030356971478350811041915377930951956502012771774841082614054554770815187292742308840790006593450752603958942439357309303946472001330045884858387830491605420241505583373355116186785494805020828753183916934302977232966898143

phi= (p-1)*(q-1)

d=inverse(e,phi)

m=pow(c, d, n)

print (binascii.unhexlify(hex(m)[2:-1]))
#this also works 
print ((hex(m)[2:-1]).decode('hex'))
#WinterCTF{Jus7_s1mpl3_RSA}