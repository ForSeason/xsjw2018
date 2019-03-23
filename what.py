__all__ = ['what']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['canary', 'b64tohex', 'Classic', 'am3', 'bnpClamp', 'bnpInvDigit', 'b64pad', 'am2', 'montMulTo', 'z', 'hex2b64', 'rng_get_byte', 'bnToString', 'bnNegate', 'byte2Hex', 'bnpSquareTo', 'RSADoPublic', 'Arcfour', 'rng_pptr', 'cSqrTo', 'BigInteger', 'nbi', 'bnBitLength', 'RSAEncrypt', 'rng_seed_time', 'am1', 'b64toBA', 'BI_FP', 'b64map', 'cReduce', 'bnCompareTo', 'montSqrTo', 'nbv', 'vv', 'bnModPowInt', 'prng_newstate', 'BI_RM', 'dbits', 'BI_RC', 'linebrk', 'ARC4init', 'rr', 'bnpFromString', 'bnpDLShiftTo', 'rng_pool', 'bnpDivRemTo', 'RSASetPublic', 'bnpFromInt', 'bnAbs', 'bnpRShiftTo', 't', 'SecureRandom', 'rng_state', 'bnpDRShiftTo', 'rng_seed_int', 'bnpIsEven', 'nbits', 'intAt', 'bnMod', 'cRevert', 'bnpLShiftTo', 'pkcs1pad2', 'bnpMultiplyTo', 'j_lm', 'bnpCopyTo', 'Montgomery', 'parseBigInt', 'cMulTo', 'RSAKey', 'rng_psize', 'bnpSubTo', 'int2char', 'cConvert', 'montConvert', 'montRevert', 'montReduce', 'bnpExp', 'ARC4next', 'rng_get_bytes'])
@Js
def PyJsHoisted_b64tohex_(s, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 's':s}, var)
    var.registers(['i', 'slop', 'ret', 'k', 's'])
    var.put('ret', Js(''))
    pass
    var.put('k', Js(0.0))
    pass
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('s').get('length')):
        try:
            if (var.get('s').callprop('charAt', var.get('i'))==var.get('b64pad')):
                break
            var.put('v', var.get('b64map').callprop('indexOf', var.get('s').callprop('charAt', var.get('i'))))
            if (var.get('v')<Js(0.0)):
                continue
            if (var.get('k')==Js(0.0)):
                var.put('ret', var.get('int2char')((var.get('v')>>Js(2.0))), '+')
                var.put('slop', (var.get('v')&Js(3.0)))
                var.put('k', Js(1.0))
            else:
                if (var.get('k')==Js(1.0)):
                    var.put('ret', var.get('int2char')(((var.get('slop')<<Js(2.0))|(var.get('v')>>Js(4.0)))), '+')
                    var.put('slop', (var.get('v')&Js(15)))
                    var.put('k', Js(2.0))
                else:
                    if (var.get('k')==Js(2.0)):
                        var.put('ret', var.get('int2char')(var.get('slop')), '+')
                        var.put('ret', var.get('int2char')((var.get('v')>>Js(2.0))), '+')
                        var.put('slop', (var.get('v')&Js(3.0)))
                        var.put('k', Js(3.0))
                    else:
                        var.put('ret', var.get('int2char')(((var.get('slop')<<Js(2.0))|(var.get('v')>>Js(4.0)))), '+')
                        var.put('ret', var.get('int2char')((var.get('v')&Js(15))), '+')
                        var.put('k', Js(0.0))
        finally:
                var.put('i',Js(var.get('i').to_number())+Js(1))
    if (var.get('k')==Js(1.0)):
        var.put('ret', var.get('int2char')((var.get('slop')<<Js(2.0))), '+')
    return var.get('ret')
PyJsHoisted_b64tohex_.func_name = 'b64tohex'
var.put('b64tohex', PyJsHoisted_b64tohex_)
@Js
def PyJsHoisted_am3_(i, x, w, j, c, n, this, arguments, var=var):
    var = Scope({'x':x, 'w':w, 'i':i, 'n':n, 'c':c, 'arguments':arguments, 'j':j, 'this':this}, var)
    var.registers(['h', 'l', 'i', 'c', 'm', 'j', 'xl', 'xh', 'x', 'w', 'n'])
    var.put('xl', (var.get('x')&Js(16383)))
    var.put('xh', (var.get('x')>>Js(14.0)))
    while (var.put('n',Js(var.get('n').to_number())-Js(1))>=Js(0.0)):
        var.put('l', (var.get(u"this").get(var.get('i'))&Js(16383)))
        var.put('h', (var.get(u"this").get((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)))>>Js(14.0)))
        var.put('m', ((var.get('xh')*var.get('l'))+(var.get('h')*var.get('xl'))))
        var.put('l', ((((var.get('xl')*var.get('l'))+((var.get('m')&Js(16383))<<Js(14.0)))+var.get('w').get(var.get('j')))+var.get('c')))
        var.put('c', (((var.get('l')>>Js(28.0))+(var.get('m')>>Js(14.0)))+(var.get('xh')*var.get('h'))))
        var.get('w').put((var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1)), (var.get('l')&Js(268435455)))
    return var.get('c')
PyJsHoisted_am3_.func_name = 'am3'
var.put('am3', PyJsHoisted_am3_)
@Js
def PyJsHoisted_bnpClamp_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['c'])
    var.put('c', (var.get(u"this").get('s')&var.get(u"this").get('DM')))
    while ((var.get(u"this").get('t')>Js(0.0)) and (var.get(u"this").get((var.get(u"this").get('t')-Js(1.0)))==var.get('c'))):
        var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())-Js(1))
PyJsHoisted_bnpClamp_.func_name = 'bnpClamp'
var.put('bnpClamp', PyJsHoisted_bnpClamp_)
@Js
def PyJsHoisted_bnpInvDigit_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['x', 'y'])
    if (var.get(u"this").get('t')<Js(1.0)):
        return Js(0.0)
    var.put('x', var.get(u"this").get('0'))
    if ((var.get('x')&Js(1.0))==Js(0.0)):
        return Js(0.0)
    var.put('y', (var.get('x')&Js(3.0)))
    var.put('y', ((var.get('y')*(Js(2.0)-((var.get('x')&Js(15))*var.get('y'))))&Js(15)))
    var.put('y', ((var.get('y')*(Js(2.0)-((var.get('x')&Js(255))*var.get('y'))))&Js(255)))
    var.put('y', ((var.get('y')*(Js(2.0)-(((var.get('x')&Js(65535))*var.get('y'))&Js(65535))))&Js(65535)))
    var.put('y', ((var.get('y')*(Js(2.0)-((var.get('x')*var.get('y'))%var.get(u"this").get('DV'))))%var.get(u"this").get('DV')))
    return ((var.get(u"this").get('DV')-var.get('y')) if (var.get('y')>Js(0.0)) else (-var.get('y')))
PyJsHoisted_bnpInvDigit_.func_name = 'bnpInvDigit'
var.put('bnpInvDigit', PyJsHoisted_bnpInvDigit_)
@Js
def PyJsHoisted_am2_(i, x, w, j, c, n, this, arguments, var=var):
    var = Scope({'x':x, 'w':w, 'i':i, 'n':n, 'c':c, 'arguments':arguments, 'j':j, 'this':this}, var)
    var.registers(['h', 'l', 'i', 'c', 'm', 'j', 'xl', 'xh', 'x', 'w', 'n'])
    var.put('xl', (var.get('x')&Js(32767)))
    var.put('xh', (var.get('x')>>Js(15.0)))
    while (var.put('n',Js(var.get('n').to_number())-Js(1))>=Js(0.0)):
        var.put('l', (var.get(u"this").get(var.get('i'))&Js(32767)))
        var.put('h', (var.get(u"this").get((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)))>>Js(15.0)))
        var.put('m', ((var.get('xh')*var.get('l'))+(var.get('h')*var.get('xl'))))
        var.put('l', ((((var.get('xl')*var.get('l'))+((var.get('m')&Js(32767))<<Js(15.0)))+var.get('w').get(var.get('j')))+(var.get('c')&Js(1073741823))))
        var.put('c', (((PyJsBshift(var.get('l'),Js(30.0))+PyJsBshift(var.get('m'),Js(15.0)))+(var.get('xh')*var.get('h')))+PyJsBshift(var.get('c'),Js(30.0))))
        var.get('w').put((var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1)), (var.get('l')&Js(1073741823)))
    return var.get('c')
PyJsHoisted_am2_.func_name = 'am2'
var.put('am2', PyJsHoisted_am2_)
@Js
def PyJsHoisted_hex2b64_(h, this, arguments, var=var):
    var = Scope({'h':h, 'arguments':arguments, 'this':this}, var)
    var.registers(['h', 'c', 'i', 'ret'])
    pass
    pass
    var.put('ret', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while ((var.get('i')+Js(3.0))<=var.get('h').get('length')):
        try:
            var.put('c', var.get('parseInt')(var.get('h').callprop('substring', var.get('i'), (var.get('i')+Js(3.0))), Js(16.0)))
            var.put('ret', (var.get('b64map').callprop('charAt', (var.get('c')>>Js(6.0)))+var.get('b64map').callprop('charAt', (var.get('c')&Js(63.0)))), '+')
        finally:
                var.put('i', Js(3.0), '+')
    if ((var.get('i')+Js(1.0))==var.get('h').get('length')):
        var.put('c', var.get('parseInt')(var.get('h').callprop('substring', var.get('i'), (var.get('i')+Js(1.0))), Js(16.0)))
        var.put('ret', var.get('b64map').callprop('charAt', (var.get('c')<<Js(2.0))), '+')
    else:
        if ((var.get('i')+Js(2.0))==var.get('h').get('length')):
            var.put('c', var.get('parseInt')(var.get('h').callprop('substring', var.get('i'), (var.get('i')+Js(2.0))), Js(16.0)))
            var.put('ret', (var.get('b64map').callprop('charAt', (var.get('c')>>Js(2.0)))+var.get('b64map').callprop('charAt', ((var.get('c')&Js(3.0))<<Js(4.0)))), '+')
    while ((var.get('ret').get('length')&Js(3.0))>Js(0.0)):
        var.put('ret', var.get('b64pad'), '+')
    return var.get('ret')
PyJsHoisted_hex2b64_.func_name = 'hex2b64'
var.put('hex2b64', PyJsHoisted_hex2b64_)
@Js
def PyJsHoisted_bnToString_(b, this, arguments, var=var):
    var = Scope({'b':b, 'arguments':arguments, 'this':this}, var)
    var.registers(['i', 'km', 'k', 'm', 'd', 'b', 'r', 'p'])
    if (var.get(u"this").get('s')<Js(0.0)):
        return (Js('-')+var.get(u"this").callprop('negate').callprop('toString', var.get('b')))
    pass
    if (var.get('b')==Js(16.0)):
        var.put('k', Js(4.0))
    else:
        if (var.get('b')==Js(8.0)):
            var.put('k', Js(3.0))
        else:
            if (var.get('b')==Js(2.0)):
                var.put('k', Js(1.0))
            else:
                if (var.get('b')==Js(32.0)):
                    var.put('k', Js(5.0))
                else:
                    if (var.get('b')==Js(4.0)):
                        var.put('k', Js(2.0))
                    else:
                        return var.get(u"this").callprop('toRadix', var.get('b'))
    var.put('km', ((Js(1.0)<<var.get('k'))-Js(1.0)))
    var.put('m', Js(False))
    var.put('r', Js(''))
    var.put('i', var.get(u"this").get('t'))
    var.put('p', (var.get(u"this").get('DB')-((var.get('i')*var.get(u"this").get('DB'))%var.get('k'))))
    if ((var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))>Js(0.0)):
        if ((var.get('p')<var.get(u"this").get('DB')) and (var.put('d', (var.get(u"this").get(var.get('i'))>>var.get('p')))>Js(0.0))):
            var.put('m', Js(True))
            var.put('r', var.get('int2char')(var.get('d')))
        while (var.get('i')>=Js(0.0)):
            if (var.get('p')<var.get('k')):
                var.put('d', ((var.get(u"this").get(var.get('i'))&((Js(1.0)<<var.get('p'))-Js(1.0)))<<(var.get('k')-var.get('p'))))
                var.put('d', (var.get(u"this").get(var.put('i',Js(var.get('i').to_number())-Js(1)))>>var.put('p', (var.get(u"this").get('DB')-var.get('k')), '+')), '|')
            else:
                var.put('d', ((var.get(u"this").get(var.get('i'))>>var.put('p', var.get('k'), '-'))&var.get('km')))
                if (var.get('p')<=Js(0.0)):
                    var.put('p', var.get(u"this").get('DB'), '+')
                    var.put('i',Js(var.get('i').to_number())-Js(1))
            if (var.get('d')>Js(0.0)):
                var.put('m', Js(True))
            if var.get('m'):
                var.put('r', var.get('int2char')(var.get('d')), '+')
    return (var.get('r') if var.get('m') else Js('0'))
PyJsHoisted_bnToString_.func_name = 'bnToString'
var.put('bnToString', PyJsHoisted_bnToString_)
@Js
def PyJsHoisted_bnNegate_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['r'])
    var.put('r', var.get('nbi')())
    var.get('BigInteger').get('ZERO').callprop('subTo', var.get(u"this"), var.get('r'))
    return var.get('r')
PyJsHoisted_bnNegate_.func_name = 'bnNegate'
var.put('bnNegate', PyJsHoisted_bnNegate_)
@Js
def PyJsHoisted_rng_seed_time_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.get('rng_seed_int')(var.get('Date').create().callprop('getTime'))
PyJsHoisted_rng_seed_time_.func_name = 'rng_seed_time'
var.put('rng_seed_time', PyJsHoisted_rng_seed_time_)
@Js
def PyJsHoisted_montRevert_(x, this, arguments, var=var):
    var = Scope({'x':x, 'arguments':arguments, 'this':this}, var)
    var.registers(['r', 'x'])
    var.put('r', var.get('nbi')())
    var.get('x').callprop('copyTo', var.get('r'))
    var.get(u"this").callprop('reduce', var.get('r'))
    return var.get('r')
PyJsHoisted_montRevert_.func_name = 'montRevert'
var.put('montRevert', PyJsHoisted_montRevert_)
@Js
def PyJsHoisted_byte2Hex_(b, this, arguments, var=var):
    var = Scope({'b':b, 'arguments':arguments, 'this':this}, var)
    var.registers(['b'])
    if (var.get('b')<Js(16)):
        return (Js('0')+var.get('b').callprop('toString', Js(16.0)))
    else:
        return var.get('b').callprop('toString', Js(16.0))
PyJsHoisted_byte2Hex_.func_name = 'byte2Hex'
var.put('byte2Hex', PyJsHoisted_byte2Hex_)
@Js
def PyJsHoisted_Classic_(m, this, arguments, var=var):
    var = Scope({'m':m, 'arguments':arguments, 'this':this}, var)
    var.registers(['m'])
    var.get(u"this").put('m', var.get('m'))
PyJsHoisted_Classic_.func_name = 'Classic'
var.put('Classic', PyJsHoisted_Classic_)
@Js
def PyJsHoisted_bnpSquareTo_(r, this, arguments, var=var):
    var = Scope({'r':r, 'arguments':arguments, 'this':this}, var)
    var.registers(['x', 'c', 'i', 'r'])
    var.put('x', var.get(u"this").callprop('abs'))
    var.put('i', var.get('r').put('t', (Js(2.0)*var.get('x').get('t'))))
    while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
        var.get('r').put(var.get('i'), Js(0.0))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<(var.get('x').get('t')-Js(1.0))):
        try:
            var.put('c', var.get('x').callprop('am', var.get('i'), var.get('x').get(var.get('i')), var.get('r'), (Js(2.0)*var.get('i')), Js(0.0), Js(1.0)))
            if (var.get('r').put((var.get('i')+var.get('x').get('t')), var.get('x').callprop('am', (var.get('i')+Js(1.0)), (Js(2.0)*var.get('x').get(var.get('i'))), var.get('r'), ((Js(2.0)*var.get('i'))+Js(1.0)), var.get('c'), ((var.get('x').get('t')-var.get('i'))-Js(1.0))), '+')>=var.get('x').get('DV')):
                var.get('r').put((var.get('i')+var.get('x').get('t')), var.get('x').get('DV'), '-')
                var.get('r').put(((var.get('i')+var.get('x').get('t'))+Js(1.0)), Js(1.0))
        finally:
                var.put('i',Js(var.get('i').to_number())+Js(1))
    if (var.get('r').get('t')>Js(0.0)):
        var.get('r').put((var.get('r').get('t')-Js(1.0)), var.get('x').callprop('am', var.get('i'), var.get('x').get(var.get('i')), var.get('r'), (Js(2.0)*var.get('i')), Js(0.0), Js(1.0)), '+')
    var.get('r').put('s', Js(0.0))
    var.get('r').callprop('clamp')
PyJsHoisted_bnpSquareTo_.func_name = 'bnpSquareTo'
var.put('bnpSquareTo', PyJsHoisted_bnpSquareTo_)
@Js
def PyJsHoisted_RSADoPublic_(x, this, arguments, var=var):
    var = Scope({'x':x, 'arguments':arguments, 'this':this}, var)
    var.registers(['x'])
    return var.get('x').callprop('modPowInt', var.get(u"this").get('e'), var.get(u"this").get('n'))
PyJsHoisted_RSADoPublic_.func_name = 'RSADoPublic'
var.put('RSADoPublic', PyJsHoisted_RSADoPublic_)
@Js
def PyJsHoisted_cSqrTo_(x, r, this, arguments, var=var):
    var = Scope({'x':x, 'r':r, 'arguments':arguments, 'this':this}, var)
    var.registers(['x', 'r'])
    var.get('x').callprop('squareTo', var.get('r'))
    var.get(u"this").callprop('reduce', var.get('r'))
PyJsHoisted_cSqrTo_.func_name = 'cSqrTo'
var.put('cSqrTo', PyJsHoisted_cSqrTo_)
@Js
def PyJsHoisted_nbi_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return var.get('BigInteger').create(var.get(u"null"))
PyJsHoisted_nbi_.func_name = 'nbi'
var.put('nbi', PyJsHoisted_nbi_)
@Js
def PyJsHoisted_nbits_(x, this, arguments, var=var):
    var = Scope({'x':x, 'arguments':arguments, 'this':this}, var)
    var.registers(['r', 't', 'x'])
    var.put('r', Js(1.0))
    if (var.put('t', PyJsBshift(var.get('x'),Js(16.0)))!=Js(0.0)):
        var.put('x', var.get('t'))
        var.put('r', Js(16.0), '+')
    if (var.put('t', (var.get('x')>>Js(8.0)))!=Js(0.0)):
        var.put('x', var.get('t'))
        var.put('r', Js(8.0), '+')
    if (var.put('t', (var.get('x')>>Js(4.0)))!=Js(0.0)):
        var.put('x', var.get('t'))
        var.put('r', Js(4.0), '+')
    if (var.put('t', (var.get('x')>>Js(2.0)))!=Js(0.0)):
        var.put('x', var.get('t'))
        var.put('r', Js(2.0), '+')
    if (var.put('t', (var.get('x')>>Js(1.0)))!=Js(0.0)):
        var.put('x', var.get('t'))
        var.put('r', Js(1.0), '+')
    return var.get('r')
PyJsHoisted_nbits_.func_name = 'nbits'
var.put('nbits', PyJsHoisted_nbits_)
@Js
def PyJsHoisted_bnBitLength_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    if (var.get(u"this").get('t')<=Js(0.0)):
        return Js(0.0)
    return ((var.get(u"this").get('DB')*(var.get(u"this").get('t')-Js(1.0)))+var.get('nbits')((var.get(u"this").get((var.get(u"this").get('t')-Js(1.0)))^(var.get(u"this").get('s')&var.get(u"this").get('DM')))))
PyJsHoisted_bnBitLength_.func_name = 'bnBitLength'
var.put('bnBitLength', PyJsHoisted_bnBitLength_)
@Js
def PyJsHoisted_cConvert_(x, this, arguments, var=var):
    var = Scope({'x':x, 'arguments':arguments, 'this':this}, var)
    var.registers(['x'])
    if ((var.get('x').get('s')<Js(0.0)) or (var.get('x').callprop('compareTo', var.get(u"this").get('m'))>=Js(0.0))):
        return var.get('x').callprop('mod', var.get(u"this").get('m'))
    else:
        return var.get('x')
PyJsHoisted_cConvert_.func_name = 'cConvert'
var.put('cConvert', PyJsHoisted_cConvert_)
@Js
def PyJsHoisted_RSAEncrypt_(text, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'text':text, 'this':this}, var)
    var.registers(['h', 'c', 'm', 'text'])
    var.put('m', var.get('pkcs1pad2')(var.get('text'), ((var.get(u"this").get('n').callprop('bitLength')+Js(7.0))>>Js(3.0))))
    if (var.get('m')==var.get(u"null")):
        return var.get(u"null")
    var.put('c', var.get(u"this").callprop('doPublic', var.get('m')))
    if (var.get('c')==var.get(u"null")):
        return var.get(u"null")
    var.put('h', var.get('c').callprop('toString', Js(16.0)))
    if ((var.get('h').get('length')&Js(1.0))==Js(0.0)):
        return var.get('h')
    else:
        return (Js('0')+var.get('h'))
PyJsHoisted_RSAEncrypt_.func_name = 'RSAEncrypt'
var.put('RSAEncrypt', PyJsHoisted_RSAEncrypt_)
@Js
def PyJsHoisted_am1_(i, x, w, j, c, n, this, arguments, var=var):
    var = Scope({'x':x, 'w':w, 'i':i, 'n':n, 'c':c, 'arguments':arguments, 'j':j, 'this':this}, var)
    var.registers(['i', 'c', 'j', 'x', 'w', 'n', 'v'])
    while (var.put('n',Js(var.get('n').to_number())-Js(1))>=Js(0.0)):
        var.put('v', (((var.get('x')*var.get(u"this").get((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))))+var.get('w').get(var.get('j')))+var.get('c')))
        var.put('c', var.get('Math').callprop('floor', (var.get('v')/Js(67108864))))
        var.get('w').put((var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1)), (var.get('v')&Js(67108863)))
    return var.get('c')
PyJsHoisted_am1_.func_name = 'am1'
var.put('am1', PyJsHoisted_am1_)
@Js
def PyJsHoisted_b64toBA_(s, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 's':s}, var)
    var.registers(['h', 'a', 'i', 's'])
    var.put('h', var.get('b64tohex')(var.get('s')))
    pass
    var.put('a', var.get('Array').create())
    #for JS loop
    var.put('i', Js(0.0))
    while ((Js(2.0)*var.get('i'))<var.get('h').get('length')):
        try:
            var.get('a').put(var.get('i'), var.get('parseInt')(var.get('h').callprop('substring', (Js(2.0)*var.get('i')), ((Js(2.0)*var.get('i'))+Js(2.0))), Js(16.0)))
        finally:
                var.put('i',Js(var.get('i').to_number())+Js(1))
    return var.get('a')
PyJsHoisted_b64toBA_.func_name = 'b64toBA'
var.put('b64toBA', PyJsHoisted_b64toBA_)
@Js
def PyJsHoisted_cReduce_(x, this, arguments, var=var):
    var = Scope({'x':x, 'arguments':arguments, 'this':this}, var)
    var.registers(['x'])
    var.get('x').callprop('divRemTo', var.get(u"this").get('m'), var.get(u"null"), var.get('x'))
PyJsHoisted_cReduce_.func_name = 'cReduce'
var.put('cReduce', PyJsHoisted_cReduce_)
@Js
def PyJsHoisted_bnCompareTo_(a, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'a':a, 'this':this}, var)
    var.registers(['r', 'a', 'i'])
    var.put('r', (var.get(u"this").get('s')-var.get('a').get('s')))
    if (var.get('r')!=Js(0.0)):
        return var.get('r')
    var.put('i', var.get(u"this").get('t'))
    var.put('r', (var.get('i')-var.get('a').get('t')))
    if (var.get('r')!=Js(0.0)):
        return ((-var.get('r')) if (var.get(u"this").get('s')<Js(0.0)) else var.get('r'))
    while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
        if (var.put('r', (var.get(u"this").get(var.get('i'))-var.get('a').get(var.get('i'))))!=Js(0.0)):
            return var.get('r')
    return Js(0.0)
PyJsHoisted_bnCompareTo_.func_name = 'bnCompareTo'
var.put('bnCompareTo', PyJsHoisted_bnCompareTo_)
@Js
def PyJsHoisted_nbv_(i, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'i':i, 'this':this}, var)
    var.registers(['r', 'i'])
    var.put('r', var.get('nbi')())
    var.get('r').callprop('fromInt', var.get('i'))
    return var.get('r')
PyJsHoisted_nbv_.func_name = 'nbv'
var.put('nbv', PyJsHoisted_nbv_)
@Js
def PyJsHoisted_bnpDLShiftTo_(n, r, this, arguments, var=var):
    var = Scope({'r':r, 'n':n, 'arguments':arguments, 'this':this}, var)
    var.registers(['r', 'n', 'i'])
    pass
    #for JS loop
    var.put('i', (var.get(u"this").get('t')-Js(1.0)))
    while (var.get('i')>=Js(0.0)):
        try:
            var.get('r').put((var.get('i')+var.get('n')), var.get(u"this").get(var.get('i')))
        finally:
                var.put('i',Js(var.get('i').to_number())-Js(1))
    #for JS loop
    var.put('i', (var.get('n')-Js(1.0)))
    while (var.get('i')>=Js(0.0)):
        try:
            var.get('r').put(var.get('i'), Js(0.0))
        finally:
                var.put('i',Js(var.get('i').to_number())-Js(1))
    var.get('r').put('t', (var.get(u"this").get('t')+var.get('n')))
    var.get('r').put('s', var.get(u"this").get('s'))
PyJsHoisted_bnpDLShiftTo_.func_name = 'bnpDLShiftTo'
var.put('bnpDLShiftTo', PyJsHoisted_bnpDLShiftTo_)
@Js
def PyJsHoisted_prng_newstate_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return var.get('Arcfour').create()
PyJsHoisted_prng_newstate_.func_name = 'prng_newstate'
var.put('prng_newstate', PyJsHoisted_prng_newstate_)
@Js
def PyJsHoisted_montMulTo_(x, y, r, this, arguments, var=var):
    var = Scope({'x':x, 'y':y, 'r':r, 'arguments':arguments, 'this':this}, var)
    var.registers(['x', 'y', 'r'])
    var.get('x').callprop('multiplyTo', var.get('y'), var.get('r'))
    var.get(u"this").callprop('reduce', var.get('r'))
PyJsHoisted_montMulTo_.func_name = 'montMulTo'
var.put('montMulTo', PyJsHoisted_montMulTo_)
@Js
def PyJsHoisted_linebrk_(s, n, this, arguments, var=var):
    var = Scope({'n':n, 'arguments':arguments, 'this':this, 's':s}, var)
    var.registers(['n', 'i', 'ret', 's'])
    var.put('ret', Js(''))
    var.put('i', Js(0.0))
    while ((var.get('i')+var.get('n'))<var.get('s').get('length')):
        var.put('ret', (var.get('s').callprop('substring', var.get('i'), (var.get('i')+var.get('n')))+Js('\n')), '+')
        var.put('i', var.get('n'), '+')
    return (var.get('ret')+var.get('s').callprop('substring', var.get('i'), var.get('s').get('length')))
PyJsHoisted_linebrk_.func_name = 'linebrk'
var.put('linebrk', PyJsHoisted_linebrk_)
@Js
def PyJsHoisted_bnpIsEven_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return (((var.get(u"this").get('0')&Js(1.0)) if (var.get(u"this").get('t')>Js(0.0)) else var.get(u"this").get('s'))==Js(0.0))
PyJsHoisted_bnpIsEven_.func_name = 'bnpIsEven'
var.put('bnpIsEven', PyJsHoisted_bnpIsEven_)
@Js
def PyJsHoisted_Arcfour_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.get(u"this").put('i', Js(0.0))
    var.get(u"this").put('j', Js(0.0))
    var.get(u"this").put('S', var.get('Array').create())
PyJsHoisted_Arcfour_.func_name = 'Arcfour'
var.put('Arcfour', PyJsHoisted_Arcfour_)
@Js
def PyJsHoisted_bnpFromString_(s, b, this, arguments, var=var):
    var = Scope({'b':b, 'arguments':arguments, 'this':this, 's':s}, var)
    var.registers(['i', 'k', 'b', 'x', 'sh', 'mi', 's'])
    pass
    if (var.get('b')==Js(16.0)):
        var.put('k', Js(4.0))
    else:
        if (var.get('b')==Js(8.0)):
            var.put('k', Js(3.0))
        else:
            if (var.get('b')==Js(256.0)):
                var.put('k', Js(8.0))
            else:
                if (var.get('b')==Js(2.0)):
                    var.put('k', Js(1.0))
                else:
                    if (var.get('b')==Js(32.0)):
                        var.put('k', Js(5.0))
                    else:
                        if (var.get('b')==Js(4.0)):
                            var.put('k', Js(2.0))
                        else:
                            var.get(u"this").callprop('fromRadix', var.get('s'), var.get('b'))
                            return var.get('undefined')
    var.get(u"this").put('t', Js(0.0))
    var.get(u"this").put('s', Js(0.0))
    var.put('i', var.get('s').get('length'))
    var.put('mi', Js(False))
    var.put('sh', Js(0.0))
    while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
        var.put('x', ((var.get('s').get(var.get('i'))&Js(255)) if (var.get('k')==Js(8.0)) else var.get('intAt')(var.get('s'), var.get('i'))))
        if (var.get('x')<Js(0.0)):
            if (var.get('s').callprop('charAt', var.get('i'))==Js('-')):
                var.put('mi', Js(True))
            continue
        var.put('mi', Js(False))
        if (var.get('sh')==Js(0.0)):
            var.get(u"this").put((var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())+Js(1))-Js(1)), var.get('x'))
        else:
            if ((var.get('sh')+var.get('k'))>var.get(u"this").get('DB')):
                var.get(u"this").put((var.get(u"this").get('t')-Js(1.0)), ((var.get('x')&((Js(1.0)<<(var.get(u"this").get('DB')-var.get('sh')))-Js(1.0)))<<var.get('sh')), '|')
                var.get(u"this").put((var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())+Js(1))-Js(1)), (var.get('x')>>(var.get(u"this").get('DB')-var.get('sh'))))
            else:
                var.get(u"this").put((var.get(u"this").get('t')-Js(1.0)), (var.get('x')<<var.get('sh')), '|')
        var.put('sh', var.get('k'), '+')
        if (var.get('sh')>=var.get(u"this").get('DB')):
            var.put('sh', var.get(u"this").get('DB'), '-')
    if ((var.get('k')==Js(8.0)) and ((var.get('s').get('0')&Js(128))!=Js(0.0))):
        var.get(u"this").put('s', (-Js(1.0)))
        if (var.get('sh')>Js(0.0)):
            var.get(u"this").put((var.get(u"this").get('t')-Js(1.0)), (((Js(1.0)<<(var.get(u"this").get('DB')-var.get('sh')))-Js(1.0))<<var.get('sh')), '|')
    var.get(u"this").callprop('clamp')
    if var.get('mi'):
        var.get('BigInteger').get('ZERO').callprop('subTo', var.get(u"this"), var.get(u"this"))
PyJsHoisted_bnpFromString_.func_name = 'bnpFromString'
var.put('bnpFromString', PyJsHoisted_bnpFromString_)
@Js
def PyJsHoisted_rng_get_byte_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    if (var.get('rng_state')==var.get(u"null")):
        var.get('rng_seed_time')()
        var.put('rng_state', var.get('prng_newstate')())
        var.get('rng_state').callprop('init', var.get('rng_pool'))
        #for JS loop
        var.put('rng_pptr', Js(0.0))
        while (var.get('rng_pptr')<var.get('rng_pool').get('length')):
            try:
                var.get('rng_pool').put(var.get('rng_pptr'), Js(0.0))
            finally:
                    var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))
        var.put('rng_pptr', Js(0.0))
    return var.get('rng_state').callprop('next')
PyJsHoisted_rng_get_byte_.func_name = 'rng_get_byte'
var.put('rng_get_byte', PyJsHoisted_rng_get_byte_)
@Js
def PyJsHoisted_bnMod_(a, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'a':a, 'this':this}, var)
    var.registers(['r', 'a'])
    var.put('r', var.get('nbi')())
    var.get(u"this").callprop('abs').callprop('divRemTo', var.get('a'), var.get(u"null"), var.get('r'))
    if ((var.get(u"this").get('s')<Js(0.0)) and (var.get('r').callprop('compareTo', var.get('BigInteger').get('ZERO'))>Js(0.0))):
        var.get('a').callprop('subTo', var.get('r'), var.get('r'))
    return var.get('r')
PyJsHoisted_bnMod_.func_name = 'bnMod'
var.put('bnMod', PyJsHoisted_bnMod_)
@Js
def PyJsHoisted_bnpDivRemTo_(m, q, r, this, arguments, var=var):
    var = Scope({'r':r, 'm':m, 'arguments':arguments, 'this':this, 'q':q}, var)
    var.registers(['ys', 'yt', 'd1', 'i', 'ts', 'r', 'e', 'y0', 'd2', 'ms', 'j', 'm', 'qd', 'q', 'pm', 't', 'nsh', 'pt', 'y'])
    var.put('pm', var.get('m').callprop('abs'))
    if (var.get('pm').get('t')<=Js(0.0)):
        return var.get('undefined')
    var.put('pt', var.get(u"this").callprop('abs'))
    if (var.get('pt').get('t')<var.get('pm').get('t')):
        if (var.get('q')!=var.get(u"null")):
            var.get('q').callprop('fromInt', Js(0.0))
        if (var.get('r')!=var.get(u"null")):
            var.get(u"this").callprop('copyTo', var.get('r'))
        return var.get('undefined')
    if (var.get('r')==var.get(u"null")):
        var.put('r', var.get('nbi')())
    var.put('y', var.get('nbi')())
    var.put('ts', var.get(u"this").get('s'))
    var.put('ms', var.get('m').get('s'))
    var.put('nsh', (var.get(u"this").get('DB')-var.get('nbits')(var.get('pm').get((var.get('pm').get('t')-Js(1.0))))))
    if (var.get('nsh')>Js(0.0)):
        var.get('pm').callprop('lShiftTo', var.get('nsh'), var.get('y'))
        var.get('pt').callprop('lShiftTo', var.get('nsh'), var.get('r'))
    else:
        var.get('pm').callprop('copyTo', var.get('y'))
        var.get('pt').callprop('copyTo', var.get('r'))
    var.put('ys', var.get('y').get('t'))
    var.put('y0', var.get('y').get((var.get('ys')-Js(1.0))))
    if (var.get('y0')==Js(0.0)):
        return var.get('undefined')
    var.put('yt', ((var.get('y0')*(Js(1.0)<<var.get(u"this").get('F1')))+((var.get('y').get((var.get('ys')-Js(2.0)))>>var.get(u"this").get('F2')) if (var.get('ys')>Js(1.0)) else Js(0.0))))
    var.put('d1', (var.get(u"this").get('FV')/var.get('yt')))
    var.put('d2', ((Js(1.0)<<var.get(u"this").get('F1'))/var.get('yt')))
    var.put('e', (Js(1.0)<<var.get(u"this").get('F2')))
    var.put('i', var.get('r').get('t'))
    var.put('j', (var.get('i')-var.get('ys')))
    var.put('t', (var.get('nbi')() if (var.get('q')==var.get(u"null")) else var.get('q')))
    var.get('y').callprop('dlShiftTo', var.get('j'), var.get('t'))
    if (var.get('r').callprop('compareTo', var.get('t'))>=Js(0.0)):
        var.get('r').put((var.get('r').put('t',Js(var.get('r').get('t').to_number())+Js(1))-Js(1)), Js(1.0))
        var.get('r').callprop('subTo', var.get('t'), var.get('r'))
    var.get('BigInteger').get('ONE').callprop('dlShiftTo', var.get('ys'), var.get('t'))
    var.get('t').callprop('subTo', var.get('y'), var.get('y'))
    while (var.get('y').get('t')<var.get('ys')):
        var.get('y').put((var.get('y').put('t',Js(var.get('y').get('t').to_number())+Js(1))-Js(1)), Js(0.0))
    while (var.put('j',Js(var.get('j').to_number())-Js(1))>=Js(0.0)):
        var.put('qd', (var.get(u"this").get('DM') if (var.get('r').get(var.put('i',Js(var.get('i').to_number())-Js(1)))==var.get('y0')) else var.get('Math').callprop('floor', ((var.get('r').get(var.get('i'))*var.get('d1'))+((var.get('r').get((var.get('i')-Js(1.0)))+var.get('e'))*var.get('d2'))))))
        if (var.get('r').put(var.get('i'), var.get('y').callprop('am', Js(0.0), var.get('qd'), var.get('r'), var.get('j'), Js(0.0), var.get('ys')), '+')<var.get('qd')):
            var.get('y').callprop('dlShiftTo', var.get('j'), var.get('t'))
            var.get('r').callprop('subTo', var.get('t'), var.get('r'))
            while (var.get('r').get(var.get('i'))<var.put('qd',Js(var.get('qd').to_number())-Js(1))):
                var.get('r').callprop('subTo', var.get('t'), var.get('r'))
    if (var.get('q')!=var.get(u"null")):
        var.get('r').callprop('drShiftTo', var.get('ys'), var.get('q'))
        if (var.get('ts')!=var.get('ms')):
            var.get('BigInteger').get('ZERO').callprop('subTo', var.get('q'), var.get('q'))
    var.get('r').put('t', var.get('ys'))
    var.get('r').callprop('clamp')
    if (var.get('nsh')>Js(0.0)):
        var.get('r').callprop('rShiftTo', var.get('nsh'), var.get('r'))
    if (var.get('ts')<Js(0.0)):
        var.get('BigInteger').get('ZERO').callprop('subTo', var.get('r'), var.get('r'))
PyJsHoisted_bnpDivRemTo_.func_name = 'bnpDivRemTo'
var.put('bnpDivRemTo', PyJsHoisted_bnpDivRemTo_)
@Js
def PyJsHoisted_RSASetPublic_(N, E, this, arguments, var=var):
    var = Scope({'E':E, 'arguments':arguments, 'this':this, 'N':N}, var)
    var.registers(['E', 'N'])
    if ((((var.get('N')!=var.get(u"null")) and (var.get('E')!=var.get(u"null"))) and (var.get('N').get('length')>Js(0.0))) and (var.get('E').get('length')>Js(0.0))):
        var.get(u"this").put('n', var.get('parseBigInt')(var.get('N'), Js(16.0)))
        var.get(u"this").put('e', var.get('parseInt')(var.get('E'), Js(16.0)))
    else:
        var.get('alert')(Js('Invalid RSA public key'))
PyJsHoisted_RSASetPublic_.func_name = 'RSASetPublic'
var.put('RSASetPublic', PyJsHoisted_RSASetPublic_)
@Js
def PyJsHoisted_bnpFromInt_(x, this, arguments, var=var):
    var = Scope({'x':x, 'arguments':arguments, 'this':this}, var)
    var.registers(['x'])
    var.get(u"this").put('t', Js(1.0))
    var.get(u"this").put('s', ((-Js(1.0)) if (var.get('x')<Js(0.0)) else Js(0.0)))
    if (var.get('x')>Js(0.0)):
        var.get(u"this").put('0', var.get('x'))
    else:
        if (var.get('x')<(-Js(1.0))):
            var.get(u"this").put('0', (var.get('x')+var.get('DV')))
        else:
            var.get(u"this").put('t', Js(0.0))
PyJsHoisted_bnpFromInt_.func_name = 'bnpFromInt'
var.put('bnpFromInt', PyJsHoisted_bnpFromInt_)
@Js
def PyJsHoisted_bnpRShiftTo_(n, r, this, arguments, var=var):
    var = Scope({'r':r, 'n':n, 'arguments':arguments, 'this':this}, var)
    var.registers(['bm', 'i', 'ds', 'cbs', 'n', 'bs', 'r'])
    var.get('r').put('s', var.get(u"this").get('s'))
    var.put('ds', var.get('Math').callprop('floor', (var.get('n')/var.get(u"this").get('DB'))))
    if (var.get('ds')>=var.get(u"this").get('t')):
        var.get('r').put('t', Js(0.0))
        return var.get('undefined')
    var.put('bs', (var.get('n')%var.get(u"this").get('DB')))
    var.put('cbs', (var.get(u"this").get('DB')-var.get('bs')))
    var.put('bm', ((Js(1.0)<<var.get('bs'))-Js(1.0)))
    var.get('r').put('0', (var.get(u"this").get(var.get('ds'))>>var.get('bs')))
    #for JS loop
    var.put('i', (var.get('ds')+Js(1.0)))
    while (var.get('i')<var.get(u"this").get('t')):
        try:
            var.get('r').put(((var.get('i')-var.get('ds'))-Js(1.0)), ((var.get(u"this").get(var.get('i'))&var.get('bm'))<<var.get('cbs')), '|')
            var.get('r').put((var.get('i')-var.get('ds')), (var.get(u"this").get(var.get('i'))>>var.get('bs')))
        finally:
                var.put('i',Js(var.get('i').to_number())+Js(1))
    if (var.get('bs')>Js(0.0)):
        var.get('r').put(((var.get(u"this").get('t')-var.get('ds'))-Js(1.0)), ((var.get(u"this").get('s')&var.get('bm'))<<var.get('cbs')), '|')
    var.get('r').put('t', (var.get(u"this").get('t')-var.get('ds')))
    var.get('r').callprop('clamp')
PyJsHoisted_bnpRShiftTo_.func_name = 'bnpRShiftTo'
var.put('bnpRShiftTo', PyJsHoisted_bnpRShiftTo_)
@Js
def PyJsHoisted_montSqrTo_(x, r, this, arguments, var=var):
    var = Scope({'x':x, 'r':r, 'arguments':arguments, 'this':this}, var)
    var.registers(['x', 'r'])
    var.get('x').callprop('squareTo', var.get('r'))
    var.get(u"this").callprop('reduce', var.get('r'))
PyJsHoisted_montSqrTo_.func_name = 'montSqrTo'
var.put('montSqrTo', PyJsHoisted_montSqrTo_)
@Js
def PyJsHoisted_SecureRandom_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    pass
PyJsHoisted_SecureRandom_.func_name = 'SecureRandom'
var.put('SecureRandom', PyJsHoisted_SecureRandom_)
@Js
def PyJsHoisted_bnpDRShiftTo_(n, r, this, arguments, var=var):
    var = Scope({'r':r, 'n':n, 'arguments':arguments, 'this':this}, var)
    var.registers(['r', 'n', 'i'])
    #for JS loop
    var.put('i', var.get('n'))
    while (var.get('i')<var.get(u"this").get('t')):
        try:
            var.get('r').put((var.get('i')-var.get('n')), var.get(u"this").get(var.get('i')))
        finally:
                var.put('i',Js(var.get('i').to_number())+Js(1))
    var.get('r').put('t', var.get('Math').callprop('max', (var.get(u"this").get('t')-var.get('n')), Js(0.0)))
    var.get('r').put('s', var.get(u"this").get('s'))
PyJsHoisted_bnpDRShiftTo_.func_name = 'bnpDRShiftTo'
var.put('bnpDRShiftTo', PyJsHoisted_bnpDRShiftTo_)
@Js
def PyJsHoisted_rng_seed_int_(x, this, arguments, var=var):
    var = Scope({'x':x, 'arguments':arguments, 'this':this}, var)
    var.registers(['x'])
    var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), (var.get('x')&Js(255.0)), '^')
    var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), ((var.get('x')>>Js(8.0))&Js(255.0)), '^')
    var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), ((var.get('x')>>Js(16.0))&Js(255.0)), '^')
    var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), ((var.get('x')>>Js(24.0))&Js(255.0)), '^')
    if (var.get('rng_pptr')>=var.get('rng_psize')):
        var.put('rng_pptr', var.get('rng_psize'), '-')
PyJsHoisted_rng_seed_int_.func_name = 'rng_seed_int'
var.put('rng_seed_int', PyJsHoisted_rng_seed_int_)
@Js
def PyJsHoisted_ARC4init_(key, this, arguments, var=var):
    var = Scope({'key':key, 'arguments':arguments, 'this':this}, var)
    var.registers(['key', 't', 'j', 'i'])
    pass
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(256.0)):
        try:
            var.get(u"this").get('S').put(var.get('i'), var.get('i'))
        finally:
                var.put('i',Js(var.get('i').to_number())+Js(1))
    var.put('j', Js(0.0))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<Js(256.0)):
        try:
            var.put('j', (((var.get('j')+var.get(u"this").get('S').get(var.get('i')))+var.get('key').get((var.get('i')%var.get('key').get('length'))))&Js(255.0)))
            var.put('t', var.get(u"this").get('S').get(var.get('i')))
            var.get(u"this").get('S').put(var.get('i'), var.get(u"this").get('S').get(var.get('j')))
            var.get(u"this").get('S').put(var.get('j'), var.get('t'))
        finally:
                var.put('i',Js(var.get('i').to_number())+Js(1))
    var.get(u"this").put('i', Js(0.0))
    var.get(u"this").put('j', Js(0.0))
PyJsHoisted_ARC4init_.func_name = 'ARC4init'
var.put('ARC4init', PyJsHoisted_ARC4init_)
@Js
def PyJsHoisted_BigInteger_(a, b, c, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'c':c, 'b':b, 'a':a, 'this':this}, var)
    var.registers(['c', 'b', 'a'])
    if (var.get('a')!=var.get(u"null")):
        if (Js('number')==var.get('a',throw=False).typeof()):
            var.get(u"this").callprop('fromNumber', var.get('a'), var.get('b'), var.get('c'))
        else:
            if ((var.get('b')==var.get(u"null")) and (Js('string')!=var.get('a',throw=False).typeof())):
                var.get(u"this").callprop('fromString', var.get('a'), Js(256.0))
            else:
                var.get(u"this").callprop('fromString', var.get('a'), var.get('b'))
PyJsHoisted_BigInteger_.func_name = 'BigInteger'
var.put('BigInteger', PyJsHoisted_BigInteger_)
@Js
def PyJsHoisted_bnAbs_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    return (var.get(u"this").callprop('negate') if (var.get(u"this").get('s')<Js(0.0)) else var.get(u"this"))
PyJsHoisted_bnAbs_.func_name = 'bnAbs'
var.put('bnAbs', PyJsHoisted_bnAbs_)
@Js
def PyJsHoisted_cRevert_(x, this, arguments, var=var):
    var = Scope({'x':x, 'arguments':arguments, 'this':this}, var)
    var.registers(['x'])
    return var.get('x')
PyJsHoisted_cRevert_.func_name = 'cRevert'
var.put('cRevert', PyJsHoisted_cRevert_)
@Js
def PyJsHoisted_intAt_(s, i, this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments, 'i':i, 's':s}, var)
    var.registers(['c', 'i', 's'])
    var.put('c', var.get('BI_RC').get(var.get('s').callprop('charCodeAt', var.get('i'))))
    return ((-Js(1.0)) if (var.get('c')==var.get(u"null")) else var.get('c'))
PyJsHoisted_intAt_.func_name = 'intAt'
var.put('intAt', PyJsHoisted_intAt_)
@Js
def PyJsHoisted_bnModPowInt_(e, m, this, arguments, var=var):
    var = Scope({'e':e, 'arguments':arguments, 'm':m, 'this':this}, var)
    var.registers(['z', 'e', 'm'])
    pass
    if ((var.get('e')<Js(256.0)) or var.get('m').callprop('isEven')):
        var.put('z', var.get('Classic').create(var.get('m')))
    else:
        var.put('z', var.get('Montgomery').create(var.get('m')))
    return var.get(u"this").callprop('exp', var.get('e'), var.get('z'))
PyJsHoisted_bnModPowInt_.func_name = 'bnModPowInt'
var.put('bnModPowInt', PyJsHoisted_bnModPowInt_)
@Js
def PyJsHoisted_bnpLShiftTo_(n, r, this, arguments, var=var):
    var = Scope({'r':r, 'n':n, 'arguments':arguments, 'this':this}, var)
    var.registers(['bm', 'i', 'ds', 'c', 'cbs', 'bs', 'n', 'r'])
    var.put('bs', (var.get('n')%var.get(u"this").get('DB')))
    var.put('cbs', (var.get(u"this").get('DB')-var.get('bs')))
    var.put('bm', ((Js(1.0)<<var.get('cbs'))-Js(1.0)))
    var.put('ds', var.get('Math').callprop('floor', (var.get('n')/var.get(u"this").get('DB'))))
    var.put('c', ((var.get(u"this").get('s')<<var.get('bs'))&var.get(u"this").get('DM')))
    #for JS loop
    var.put('i', (var.get(u"this").get('t')-Js(1.0)))
    while (var.get('i')>=Js(0.0)):
        try:
            var.get('r').put(((var.get('i')+var.get('ds'))+Js(1.0)), ((var.get(u"this").get(var.get('i'))>>var.get('cbs'))|var.get('c')))
            var.put('c', ((var.get(u"this").get(var.get('i'))&var.get('bm'))<<var.get('bs')))
        finally:
                var.put('i',Js(var.get('i').to_number())-Js(1))
    #for JS loop
    var.put('i', (var.get('ds')-Js(1.0)))
    while (var.get('i')>=Js(0.0)):
        try:
            var.get('r').put(var.get('i'), Js(0.0))
        finally:
                var.put('i',Js(var.get('i').to_number())-Js(1))
    var.get('r').put(var.get('ds'), var.get('c'))
    var.get('r').put('t', ((var.get(u"this").get('t')+var.get('ds'))+Js(1.0)))
    var.get('r').put('s', var.get(u"this").get('s'))
    var.get('r').callprop('clamp')
PyJsHoisted_bnpLShiftTo_.func_name = 'bnpLShiftTo'
var.put('bnpLShiftTo', PyJsHoisted_bnpLShiftTo_)
@Js
def PyJsHoisted_bnpMultiplyTo_(a, r, this, arguments, var=var):
    var = Scope({'r':r, 'arguments':arguments, 'a':a, 'this':this}, var)
    var.registers(['x', 'a', 'y', 'i', 'r'])
    var.put('x', var.get(u"this").callprop('abs'))
    var.put('y', var.get('a').callprop('abs'))
    var.put('i', var.get('x').get('t'))
    var.get('r').put('t', (var.get('i')+var.get('y').get('t')))
    while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
        var.get('r').put(var.get('i'), Js(0.0))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('y').get('t')):
        try:
            var.get('r').put((var.get('i')+var.get('x').get('t')), var.get('x').callprop('am', Js(0.0), var.get('y').get(var.get('i')), var.get('r'), var.get('i'), Js(0.0), var.get('x').get('t')))
        finally:
                var.put('i',Js(var.get('i').to_number())+Js(1))
    var.get('r').put('s', Js(0.0))
    var.get('r').callprop('clamp')
    if (var.get(u"this").get('s')!=var.get('a').get('s')):
        var.get('BigInteger').get('ZERO').callprop('subTo', var.get('r'), var.get('r'))
PyJsHoisted_bnpMultiplyTo_.func_name = 'bnpMultiplyTo'
var.put('bnpMultiplyTo', PyJsHoisted_bnpMultiplyTo_)
@Js
def PyJsHoisted_pkcs1pad2_(s, n, this, arguments, var=var):
    var = Scope({'n':n, 'arguments':arguments, 'this':this, 's':s}, var)
    var.registers(['i', 'c', 'x', 'n', 'ba', 'rng', 's'])
    if (var.get('n')<(var.get('s').get('length')+Js(11.0))):
        var.get('alert')(Js('Message too long for RSA'))
        return var.get(u"null")
    var.put('ba', var.get('Array').create())
    var.put('i', (var.get('s').get('length')-Js(1.0)))
    while ((var.get('i')>=Js(0.0)) and (var.get('n')>Js(0.0))):
        var.put('c', var.get('s').callprop('charCodeAt', (var.put('i',Js(var.get('i').to_number())-Js(1))+Js(1))))
        if (var.get('c')<Js(128.0)):
            var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), var.get('c'))
        else:
            if ((var.get('c')>Js(127.0)) and (var.get('c')<Js(2048.0))):
                var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), ((var.get('c')&Js(63.0))|Js(128.0)))
                var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), ((var.get('c')>>Js(6.0))|Js(192.0)))
            else:
                var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), ((var.get('c')&Js(63.0))|Js(128.0)))
                var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), (((var.get('c')>>Js(6.0))&Js(63.0))|Js(128.0)))
                var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), ((var.get('c')>>Js(12.0))|Js(224.0)))
    var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), Js(0.0))
    var.put('rng', var.get('SecureRandom').create())
    var.put('x', var.get('Array').create())
    while (var.get('n')>Js(2.0)):
        var.get('x').put('0', Js(0.0))
        while (var.get('x').get('0')==Js(0.0)):
            var.get('rng').callprop('nextBytes', var.get('x'))
        var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), var.get('x').get('0'))
    var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), Js(2.0))
    var.get('ba').put(var.put('n',Js(var.get('n').to_number())-Js(1)), Js(0.0))
    return var.get('BigInteger').create(var.get('ba'))
PyJsHoisted_pkcs1pad2_.func_name = 'pkcs1pad2'
var.put('pkcs1pad2', PyJsHoisted_pkcs1pad2_)
@Js
def PyJsHoisted_bnpCopyTo_(r, this, arguments, var=var):
    var = Scope({'r':r, 'arguments':arguments, 'this':this}, var)
    var.registers(['r', 'i'])
    #for JS loop
    var.put('i', (var.get(u"this").get('t')-Js(1.0)))
    while (var.get('i')>=Js(0.0)):
        try:
            var.get('r').put(var.get('i'), var.get(u"this").get(var.get('i')))
        finally:
                var.put('i',Js(var.get('i').to_number())-Js(1))
    var.get('r').put('t', var.get(u"this").get('t'))
    var.get('r').put('s', var.get(u"this").get('s'))
PyJsHoisted_bnpCopyTo_.func_name = 'bnpCopyTo'
var.put('bnpCopyTo', PyJsHoisted_bnpCopyTo_)
@Js
def PyJsHoisted_parseBigInt_(str, r, this, arguments, var=var):
    var = Scope({'r':r, 'str':str, 'arguments':arguments, 'this':this}, var)
    var.registers(['r', 'str'])
    return var.get('BigInteger').create(var.get('str'), var.get('r'))
PyJsHoisted_parseBigInt_.func_name = 'parseBigInt'
var.put('parseBigInt', PyJsHoisted_parseBigInt_)
@Js
def PyJsHoisted_cMulTo_(x, y, r, this, arguments, var=var):
    var = Scope({'x':x, 'y':y, 'r':r, 'arguments':arguments, 'this':this}, var)
    var.registers(['x', 'y', 'r'])
    var.get('x').callprop('multiplyTo', var.get('y'), var.get('r'))
    var.get(u"this").callprop('reduce', var.get('r'))
PyJsHoisted_cMulTo_.func_name = 'cMulTo'
var.put('cMulTo', PyJsHoisted_cMulTo_)
@Js
def PyJsHoisted_RSAKey_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers([])
    var.get(u"this").put('n', var.get(u"null"))
    var.get(u"this").put('e', Js(0.0))
    var.get(u"this").put('d', var.get(u"null"))
    var.get(u"this").put('p', var.get(u"null"))
    var.get(u"this").put('q', var.get(u"null"))
    var.get(u"this").put('dmp1', var.get(u"null"))
    var.get(u"this").put('dmq1', var.get(u"null"))
    var.get(u"this").put('coeff', var.get(u"null"))
PyJsHoisted_RSAKey_.func_name = 'RSAKey'
var.put('RSAKey', PyJsHoisted_RSAKey_)
@Js
def PyJsHoisted_bnpSubTo_(a, r, this, arguments, var=var):
    var = Scope({'r':r, 'arguments':arguments, 'a':a, 'this':this}, var)
    var.registers(['r', 'c', 'm', 'a', 'i'])
    var.put('i', Js(0.0))
    var.put('c', Js(0.0))
    var.put('m', var.get('Math').callprop('min', var.get('a').get('t'), var.get(u"this").get('t')))
    while (var.get('i')<var.get('m')):
        var.put('c', (var.get(u"this").get(var.get('i'))-var.get('a').get(var.get('i'))), '+')
        var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get('c')&var.get(u"this").get('DM')))
        var.put('c', var.get(u"this").get('DB'), '>>')
    if (var.get('a').get('t')<var.get(u"this").get('t')):
        var.put('c', var.get('a').get('s'), '-')
        while (var.get('i')<var.get(u"this").get('t')):
            var.put('c', var.get(u"this").get(var.get('i')), '+')
            var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get('c')&var.get(u"this").get('DM')))
            var.put('c', var.get(u"this").get('DB'), '>>')
        var.put('c', var.get(u"this").get('s'), '+')
    else:
        var.put('c', var.get(u"this").get('s'), '+')
        while (var.get('i')<var.get('a').get('t')):
            var.put('c', var.get('a').get(var.get('i')), '-')
            var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get('c')&var.get(u"this").get('DM')))
            var.put('c', var.get(u"this").get('DB'), '>>')
        var.put('c', var.get('a').get('s'), '-')
    var.get('r').put('s', ((-Js(1.0)) if (var.get('c')<Js(0.0)) else Js(0.0)))
    if (var.get('c')<(-Js(1.0))):
        var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), (var.get(u"this").get('DV')+var.get('c')))
    else:
        if (var.get('c')>Js(0.0)):
            var.get('r').put((var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1)), var.get('c'))
    var.get('r').put('t', var.get('i'))
    var.get('r').callprop('clamp')
PyJsHoisted_bnpSubTo_.func_name = 'bnpSubTo'
var.put('bnpSubTo', PyJsHoisted_bnpSubTo_)
@Js
def PyJsHoisted_int2char_(n, this, arguments, var=var):
    var = Scope({'n':n, 'arguments':arguments, 'this':this}, var)
    var.registers(['n'])
    return var.get('BI_RM').callprop('charAt', var.get('n'))
PyJsHoisted_int2char_.func_name = 'int2char'
var.put('int2char', PyJsHoisted_int2char_)
@Js
def PyJsHoisted_montConvert_(x, this, arguments, var=var):
    var = Scope({'x':x, 'arguments':arguments, 'this':this}, var)
    var.registers(['r', 'x'])
    var.put('r', var.get('nbi')())
    var.get('x').callprop('abs').callprop('dlShiftTo', var.get(u"this").get('m').get('t'), var.get('r'))
    var.get('r').callprop('divRemTo', var.get(u"this").get('m'), var.get(u"null"), var.get('r'))
    if ((var.get('x').get('s')<Js(0.0)) and (var.get('r').callprop('compareTo', var.get('BigInteger').get('ZERO'))>Js(0.0))):
        var.get(u"this").get('m').callprop('subTo', var.get('r'), var.get('r'))
    return var.get('r')
PyJsHoisted_montConvert_.func_name = 'montConvert'
var.put('montConvert', PyJsHoisted_montConvert_)
@Js
def PyJsHoisted_montReduce_(x, this, arguments, var=var):
    var = Scope({'x':x, 'arguments':arguments, 'this':this}, var)
    var.registers(['x', 'j', 'u0', 'i'])
    while (var.get('x').get('t')<=var.get(u"this").get('mt2')):
        var.get('x').put((var.get('x').put('t',Js(var.get('x').get('t').to_number())+Js(1))-Js(1)), Js(0.0))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get(u"this").get('m').get('t')):
        try:
            var.put('j', (var.get('x').get(var.get('i'))&Js(32767)))
            var.put('u0', (((var.get('j')*var.get(u"this").get('mpl'))+((((var.get('j')*var.get(u"this").get('mph'))+((var.get('x').get(var.get('i'))>>Js(15.0))*var.get(u"this").get('mpl')))&var.get(u"this").get('um'))<<Js(15.0)))&var.get('x').get('DM')))
            var.put('j', (var.get('i')+var.get(u"this").get('m').get('t')))
            var.get('x').put(var.get('j'), var.get(u"this").get('m').callprop('am', Js(0.0), var.get('u0'), var.get('x'), var.get('i'), Js(0.0), var.get(u"this").get('m').get('t')), '+')
            while (var.get('x').get(var.get('j'))>=var.get('x').get('DV')):
                var.get('x').put(var.get('j'), var.get('x').get('DV'), '-')
                (var.get('x').put(var.put('j',Js(var.get('j').to_number())+Js(1)),Js(var.get('x').get(var.put('j',Js(var.get('j').to_number())+Js(1))).to_number())+Js(1))-Js(1))
        finally:
                var.put('i',Js(var.get('i').to_number())+Js(1))
    var.get('x').callprop('clamp')
    var.get('x').callprop('drShiftTo', var.get(u"this").get('m').get('t'), var.get('x'))
    if (var.get('x').callprop('compareTo', var.get(u"this").get('m'))>=Js(0.0)):
        var.get('x').callprop('subTo', var.get(u"this").get('m'), var.get('x'))
PyJsHoisted_montReduce_.func_name = 'montReduce'
var.put('montReduce', PyJsHoisted_montReduce_)
@Js
def PyJsHoisted_bnpExp_(e, z, this, arguments, var=var):
    var = Scope({'z':z, 'e':e, 'arguments':arguments, 'this':this}, var)
    var.registers(['i', 'z', 'e', 'g', 't', 'r2', 'r'])
    if ((var.get('e')>Js(4294967295)) or (var.get('e')<Js(1.0))):
        return var.get('BigInteger').get('ONE')
    var.put('r', var.get('nbi')())
    var.put('r2', var.get('nbi')())
    var.put('g', var.get('z').callprop('convert', var.get(u"this")))
    var.put('i', (var.get('nbits')(var.get('e'))-Js(1.0)))
    var.get('g').callprop('copyTo', var.get('r'))
    while (var.put('i',Js(var.get('i').to_number())-Js(1))>=Js(0.0)):
        var.get('z').callprop('sqrTo', var.get('r'), var.get('r2'))
        if ((var.get('e')&(Js(1.0)<<var.get('i')))>Js(0.0)):
            var.get('z').callprop('mulTo', var.get('r2'), var.get('g'), var.get('r'))
        else:
            var.put('t', var.get('r'))
            var.put('r', var.get('r2'))
            var.put('r2', var.get('t'))
    return var.get('z').callprop('revert', var.get('r'))
PyJsHoisted_bnpExp_.func_name = 'bnpExp'
var.put('bnpExp', PyJsHoisted_bnpExp_)
@Js
def PyJsHoisted_Montgomery_(m, this, arguments, var=var):
    var = Scope({'m':m, 'arguments':arguments, 'this':this}, var)
    var.registers(['m'])
    var.get(u"this").put('m', var.get('m'))
    var.get(u"this").put('mp', var.get('m').callprop('invDigit'))
    var.get(u"this").put('mpl', (var.get(u"this").get('mp')&Js(32767)))
    var.get(u"this").put('mph', (var.get(u"this").get('mp')>>Js(15.0)))
    var.get(u"this").put('um', ((Js(1.0)<<(var.get('m').get('DB')-Js(15.0)))-Js(1.0)))
    var.get(u"this").put('mt2', (Js(2.0)*var.get('m').get('t')))
PyJsHoisted_Montgomery_.func_name = 'Montgomery'
var.put('Montgomery', PyJsHoisted_Montgomery_)
@Js
def PyJsHoisted_ARC4next_(this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this}, var)
    var.registers(['t'])
    pass
    var.get(u"this").put('i', ((var.get(u"this").get('i')+Js(1.0))&Js(255.0)))
    var.get(u"this").put('j', ((var.get(u"this").get('j')+var.get(u"this").get('S').get(var.get(u"this").get('i')))&Js(255.0)))
    var.put('t', var.get(u"this").get('S').get(var.get(u"this").get('i')))
    var.get(u"this").get('S').put(var.get(u"this").get('i'), var.get(u"this").get('S').get(var.get(u"this").get('j')))
    var.get(u"this").get('S').put(var.get(u"this").get('j'), var.get('t'))
    return var.get(u"this").get('S').get(((var.get('t')+var.get(u"this").get('S').get(var.get(u"this").get('i')))&Js(255.0)))
PyJsHoisted_ARC4next_.func_name = 'ARC4next'
var.put('ARC4next', PyJsHoisted_ARC4next_)
@Js
def PyJsHoisted_rng_get_bytes_(ba, this, arguments, var=var):
    var = Scope({'arguments':arguments, 'this':this, 'ba':ba}, var)
    var.registers(['i', 'ba'])
    pass
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('ba').get('length')):
        try:
            var.get('ba').put(var.get('i'), var.get('rng_get_byte')())
        finally:
                var.put('i',Js(var.get('i').to_number())+Js(1))
PyJsHoisted_rng_get_bytes_.func_name = 'rng_get_bytes'
var.put('rng_get_bytes', PyJsHoisted_rng_get_bytes_)
pass
pass
pass
pass
pass
pass
pass
pass
var.get('RSAKey').get('prototype').put('doPublic', var.get('RSADoPublic'))
var.get('RSAKey').get('prototype').put('setPublic', var.get('RSASetPublic'))
var.get('RSAKey').get('prototype').put('encrypt', var.get('RSAEncrypt'))
var.put('b64map', Js('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'))
var.put('b64pad', Js('='))
pass
pass
pass
pass
var.put('canary', Js(244837814094590))
var.put('j_lm', ((var.get('canary')&Js(16777215))==Js(15715070)))
pass
pass
pass
pass
pass
if (var.get('j_lm') and (var.get('navigator').get('appName')==Js('Microsoft Internet Explorer'))):
    var.get('BigInteger').get('prototype').put('am', var.get('am2'))
    var.put('dbits', Js(30.0))
else:
    if (var.get('j_lm') and (var.get('navigator').get('appName')!=Js('Netscape'))):
        var.get('BigInteger').get('prototype').put('am', var.get('am1'))
        var.put('dbits', Js(26.0))
    else:
        var.get('BigInteger').get('prototype').put('am', var.get('am3'))
        var.put('dbits', Js(28.0))
var.get('BigInteger').get('prototype').put('DB', var.get('dbits'))
var.get('BigInteger').get('prototype').put('DM', ((Js(1.0)<<var.get('dbits'))-Js(1.0)))
var.get('BigInteger').get('prototype').put('DV', (Js(1.0)<<var.get('dbits')))
var.put('BI_FP', Js(52.0))
var.get('BigInteger').get('prototype').put('FV', var.get('Math').callprop('pow', Js(2.0), var.get('BI_FP')))
var.get('BigInteger').get('prototype').put('F1', (var.get('BI_FP')-var.get('dbits')))
var.get('BigInteger').get('prototype').put('F2', ((Js(2.0)*var.get('dbits'))-var.get('BI_FP')))
var.put('BI_RM', Js('0123456789abcdefghijklmnopqrstuvwxyz'))
var.put('BI_RC', var.get('Array').create())
pass
var.put('rr', Js('0').callprop('charCodeAt', Js(0.0)))
#for JS loop
var.put('vv', Js(0.0))
while (var.get('vv')<=Js(9.0)):
    try:
        var.get('BI_RC').put((var.put('rr',Js(var.get('rr').to_number())+Js(1))-Js(1)), var.get('vv'))
    finally:
            var.put('vv',Js(var.get('vv').to_number())+Js(1))
var.put('rr', Js('a').callprop('charCodeAt', Js(0.0)))
#for JS loop
var.put('vv', Js(10.0))
while (var.get('vv')<Js(36.0)):
    try:
        var.get('BI_RC').put((var.put('rr',Js(var.get('rr').to_number())+Js(1))-Js(1)), var.get('vv'))
    finally:
            var.put('vv',Js(var.get('vv').to_number())+Js(1))
var.put('rr', Js('A').callprop('charCodeAt', Js(0.0)))
#for JS loop
var.put('vv', Js(10.0))
while (var.get('vv')<Js(36.0)):
    try:
        var.get('BI_RC').put((var.put('rr',Js(var.get('rr').to_number())+Js(1))-Js(1)), var.get('vv'))
    finally:
            var.put('vv',Js(var.get('vv').to_number())+Js(1))
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
var.get('Classic').get('prototype').put('convert', var.get('cConvert'))
var.get('Classic').get('prototype').put('revert', var.get('cRevert'))
var.get('Classic').get('prototype').put('reduce', var.get('cReduce'))
var.get('Classic').get('prototype').put('mulTo', var.get('cMulTo'))
var.get('Classic').get('prototype').put('sqrTo', var.get('cSqrTo'))
pass
pass
pass
pass
pass
pass
pass
var.get('Montgomery').get('prototype').put('convert', var.get('montConvert'))
var.get('Montgomery').get('prototype').put('revert', var.get('montRevert'))
var.get('Montgomery').get('prototype').put('reduce', var.get('montReduce'))
var.get('Montgomery').get('prototype').put('mulTo', var.get('montMulTo'))
var.get('Montgomery').get('prototype').put('sqrTo', var.get('montSqrTo'))
pass
pass
pass
var.get('BigInteger').get('prototype').put('copyTo', var.get('bnpCopyTo'))
var.get('BigInteger').get('prototype').put('fromInt', var.get('bnpFromInt'))
var.get('BigInteger').get('prototype').put('fromString', var.get('bnpFromString'))
var.get('BigInteger').get('prototype').put('clamp', var.get('bnpClamp'))
var.get('BigInteger').get('prototype').put('dlShiftTo', var.get('bnpDLShiftTo'))
var.get('BigInteger').get('prototype').put('drShiftTo', var.get('bnpDRShiftTo'))
var.get('BigInteger').get('prototype').put('lShiftTo', var.get('bnpLShiftTo'))
var.get('BigInteger').get('prototype').put('rShiftTo', var.get('bnpRShiftTo'))
var.get('BigInteger').get('prototype').put('subTo', var.get('bnpSubTo'))
var.get('BigInteger').get('prototype').put('multiplyTo', var.get('bnpMultiplyTo'))
var.get('BigInteger').get('prototype').put('squareTo', var.get('bnpSquareTo'))
var.get('BigInteger').get('prototype').put('divRemTo', var.get('bnpDivRemTo'))
var.get('BigInteger').get('prototype').put('invDigit', var.get('bnpInvDigit'))
var.get('BigInteger').get('prototype').put('isEven', var.get('bnpIsEven'))
var.get('BigInteger').get('prototype').put('exp', var.get('bnpExp'))
var.get('BigInteger').get('prototype').put('toString', var.get('bnToString'))
var.get('BigInteger').get('prototype').put('negate', var.get('bnNegate'))
var.get('BigInteger').get('prototype').put('abs', var.get('bnAbs'))
var.get('BigInteger').get('prototype').put('compareTo', var.get('bnCompareTo'))
var.get('BigInteger').get('prototype').put('bitLength', var.get('bnBitLength'))
var.get('BigInteger').get('prototype').put('mod', var.get('bnMod'))
var.get('BigInteger').get('prototype').put('modPowInt', var.get('bnModPowInt'))
var.get('BigInteger').put('ZERO', var.get('nbv')(Js(0.0)))
var.get('BigInteger').put('ONE', var.get('nbv')(Js(1.0)))
pass
pass
pass
var.get('Arcfour').get('prototype').put('init', var.get('ARC4init'))
var.get('Arcfour').get('prototype').put('next', var.get('ARC4next'))
pass
var.put('rng_psize', Js(256.0))
pass
pass
pass
pass
pass
if (var.get('rng_pool')==var.get(u"null")):
    var.put('rng_pool', var.get('Array').create())
    var.put('rng_pptr', Js(0.0))
    pass
    if (((var.get('navigator').get('appName')==Js('Netscape')) and (var.get('navigator').get('appVersion')<Js('5'))) and var.get('window').get('crypto')):
        var.put('z', var.get('window').get('crypto').callprop('random', Js(32.0)))
        #for JS loop
        var.put('t', Js(0.0))
        while (var.get('t')<var.get('z').get('length')):
            try:
                var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), (var.get('z').callprop('charCodeAt', var.get('t'))&Js(255.0)))
            finally:
                    var.put('t',Js(var.get('t').to_number())+Js(1))
    while (var.get('rng_pptr')<var.get('rng_psize')):
        var.put('t', var.get('Math').callprop('floor', (Js(65536.0)*var.get('Math').callprop('random'))))
        var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), PyJsBshift(var.get('t'),Js(8.0)))
        var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), (var.get('t')&Js(255.0)))
    var.put('rng_pptr', Js(0.0))
    var.get('rng_seed_time')()
pass
pass
pass
var.get('SecureRandom').get('prototype').put('nextBytes', var.get('rng_get_bytes'))
pass


# Add lib to the module scope
what = var.to_python()