from pprint import pprint
def substringDiff(k, A, B):
    """ F[i][j][k] =k_tmp """
    F = [[[None]*len(A) for _ in range(len(B))] for _ in range(len(B))]
    F[0][0][0] = 0
    if (A[0] == B[0]):
        F[0][0][1] = 0
    else:
        F[0][0][1] = 1
    max_val =float("-inf")
    for i in range(len(A)):
        for j in range(len(B)):
            tt = 0
            if (A[i] != B[j]):
                tt=1
            F[i][j][0] = tt
            for len_tmp in range(1,len(A)-max(i,j)):
                tmp = 0
                if (i+len_tmp < len(A) and j + len_tmp < len(B) and A[i+len_tmp] != B[j + len_tmp]):
                    tmp = 1
                F[i][j][len_tmp] = F[i][j][len_tmp-1] + tmp
                if (F[i][j][len_tmp] <=k ):
                    if (len_tmp>max_val):
                        max_val = max(max_val,len_tmp)
                else:
                    break
    return max_val+1

print(substringDiff(10, "gatezejttddpkmndtauvjcffiiafgzhkqgzliirdldbmqkdfpeadgjxcirgkmkcfxorthhpujbnenxansboejjrqfxoohuolsxgohukxmpzfukzvkduurvajrodlpxojzsihiqftrbkixbcxraqpiyadbkzqihmigunrzfzcgzfkeszcpkdotulkktfduekyqzkymqpeidhpyuhotynqaxknnsheiogrhobrajzkrekexvorlvlyhtgstjrtdgjzahvmjnprcumulnvftgoiyctjgtthleeunkgbemapsntmfdnuaydkrbyngbrbpsznfdftonfmbjahqrpgddbkokvdxfflzysneapnqvsqhilxabbjamkdhpktscxsczpoontmliozurkrvagnidnmcayiradtbacltouzacvseayrdzkkkqgbfrrnfydbnnxvctffgtfpbmfzsqjnclcnttztcvvpbmkovahvpdnjqghcafzcxhrxumhxxkdtyjqypljzsbidfpoydlumdrhokvmstydlmymldvimdduvzzcmiyxapbrrrndhjnhncpibdmiryjteyvcydxkthxcbgxshffuzevvfrcrpzaotcpbefqqppehgdlbfstralgzbtdfervuvejyvvocrabkiohjxjnnrshvyijyonzzioeakpbkgxybtlcbybgzvvvvhhkdfvpupxnlecqizvzhgigliotybprnnntqdsiquxvdxojripdlmzsyorhjandaqtjfptgebxbjmnokevncfxkkadrsqjvxuttokcabefxehmnhkcbgrdmnmmycflifrrkriggeplcfafpxsbfchbdzbvdgsbrcebgkgsdbdntfdbaltnsdzraafhobrsygkvetomeqvkrntyzeqimcaktnvfcehaeexqjnjfyvomfqlbdjxhhjojvytaovvprpfrdpgurzfhknsimnmhctbkzxfxjrzfjvjsigivmlxcgiginjitarxettzzcpceonufetlpdxupmpfmhzanufjxrkaapaaalaulebxizfjshbjsagmxmuesvecuoobuctngykkzsztzauquxxdgmjxuybkzvxsftzpqhmarlsbaeriaahlrcdgjadhbrizmnabcfadtnfdzobdhayhrxmdddycenimblnrlicasqhttekqyiafijoiykcmutzbjupsbqxbzeyqxbsshelvzieoiozylenrlaelpykdpvzhvpttmsyxsjbrfqchgrxcuvkgqinluzjrqlnzitvhlofjiznsxvbbhscsuoufodozsrmjecfdrkcslgmmrcletuvxcdfitpmgocjdcurrbfqpefxtndzkuuzxpaxfanxdxnteiapkzouvqiykxntmltdpmyzjveivnfuhzlrkseyhpbgrtcvnqmpqcgubjyourdrizixmoflmyzsskvfagtdopgthcdmmqhkmksxgeckagmjgauvz" ,"gltezejtfdehkmndtauvicffiiafozhkqmzlieedldbmqjdfpeadgjxcirbkmkcfxorthhpujbnekzansboejjrqfxoohuozsxgohukxmpzbukzvkduurvajrodlpxojzsvhiqftrbgixbcxmaqpiyadbkzqnhmigunrzfzugzfkeszcpbdotulketftuekfqzkymqpeidhpyuhotynqqxknnsheitgrhobrajzkrekexvorlvlyhtmstjrldhjzahvmjnprgtgulhvftgoiyctjgtthleeunkgbemapsntmfdnuaydkrbyigbrbpsknfdftonfmbtahqrpgddbkokvdxfflzysneapnqvsqhilnabbjamkdhpktsxxsczpoontmliozurkrvagnidnmcayiradtbacltouzacvseayrdzkkkqgbfrrnfydbnnxuctfegtfpbmfzsqjnclcnttftcvvpbmkovahvpdnjqghcafzcxhrgumhoxkityjqypljzsbidfcoynlumdrhokvmstydlmymldvimrduvzzcmiyxapbrrrndhjnhncpjbdmiryjteyvcydxkthxcbgxshffyzevvfrcrpzaotcpbefqqppehgdlbfstaalgzbtdfervuvehyvvocrabkioojxjnnrshvyijymnnzioeakpbkgxdbtlobybgzvpvvhhkdcvplpvnlecqizvzhgiglsotobprnnntqdsiquxvdxojripdlmzsyorhjandaqtjfptgegxbjmnokevncfxkladrsqjvxugtokcabeqxehmnhkcbgrdmnmmyfsmifrrkriggeplcfbfpxsbfcxbdzbvdgsbrcebmkpsdbdntfdbaltnsdzrfafhobrsygktetomeqvkrztyzeqimcaktnvfcehaeexqjnjfyvomfqsbdjxhhjojvytaovvirpfrdpgurzfhknsimnmhctbkixfcjrzfjvjsigilmoxcuiginjitarxettzzcpcesnufbtlpdxupmpfmhzqnufjxrkaapaaalaulebxizfjshbjsagmxmueshecuoobzctngykkzsftzatquxxdgmjxuybkzvxsftzpqhmarlsbayriaahlrcdgjadhbrizmnaycfaftnfdzobdhhyhrxvddsycenimblnrcicasqhttekqyiafijoiykcmstzbjupsbqxbzeyqxbsshelvzxekiozylenrlaelpykdpvzhvpttmsyxsjbrfqchgrxcubkgqinluzjrqltzitvhlofjizxsxvbbqbcsuoufodozsrmjecfdricsljmmrcletuvxcxfitpmgocjdcurzbfqpefxtndzkuuzxpaxfanxdxntuiapkzoufqiykxntmlyepmyzjneyvnfuqzlrkseyhpbgrtcpnqmpqcgubjuourdriziimoflmyzsskvfagldopgthcdmmqhrmksxgeckarmjgauvj"))
