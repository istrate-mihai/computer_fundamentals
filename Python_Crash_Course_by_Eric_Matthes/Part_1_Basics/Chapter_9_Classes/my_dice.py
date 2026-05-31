from die import Die

die_6_sided  = Die()
die_10_sided = Die(10)
die_20_sided = Die(20)

for i in range(0, 10):
	die_6_sided.roll_die()
	die_10_sided.roll_die()
	die_20_sided.roll_die()
