import chainedrandom

start_seed = '0.598549237622'

c1 = chainedrandom.ChainedRandom(seed=start_seed)
c2 = chainedrandom.ChainedRandom(seed=start_seed)

passed = True
for i in range(100):
    v1 = c1.randint(0,1000).values[0]
    v2 = c2.randint(0,1000).values[0]
    passed = passed and v1 == v2

for i in range(100):
    v1 = c1.rand_n(1000)
    v2 = c2.rand_n(1000)
    passed = passed and v1 == v2

if passed:
    print "PASS"
else:
    print "FAIL"
