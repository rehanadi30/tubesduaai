from clips import Environment, Symbol

env = Environment()

env.load('miner.clp')

env.assert_string('(kotak)')
env.assert_string('(akan-buka-kotak 0 0 6)')

for i in env.facts():
    print(i)

env.run()

print()
for i in env.facts():
    print(i)