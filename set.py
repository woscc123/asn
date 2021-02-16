# 집합
# 순서x,중복x
# 중괄호 or set([])

US_etf = {'vtnr','gme','amc'}
nasdaq = set(['vtnr','apl','tsla'])
# 교집합
print(nasdaq&US_etf)
print(nasdaq.intersection(US_etf))
#합집합 a or b

print(nasdaq | US_etf)
print(US_etf.union(nasdaq))

#차집합( a -b)
print(US_etf-nasdaq)
print(US_etf.difference(nasdaq))

#집합 원소 추가 add
nasdaq.add('nmh')
print(nasdaq)

#집합 원소 삭제 remove
nasdaq.remove('nmh')
print(nasdaq)

upbit = {'xrp','btc','eth'}
bithumb = {'iost','xrp','stp'}
print(upbit&bithumb)
print(upbit.intersection(bithumb))

print(upbit|bithumb)
print(upbit.union(bithumb))

print(upbit-bithumb)
print(upbit.difference(bithumb))

upbit.add("nmh")
print(upbit)

upbit.remove('xrp')
print(upbit)

asn={'kta','fz','kasdn'}
mji={'kasdn','ori','sya'}

print(asn&mji)
print(asn.intersection(mji))

print(asn|mji)
print(asn.union(mji))

print(asn-mji)
print(asn.difference(mji))

asn.add('zd')
print(asn)

asn.remove('kta')
print(asn)