import random as rnd
import matplotlib.pyplot as plt

start_atom = 1000

decay_state = 3
allowed_states = 12

decay_count = 0

time = 0

timeData = [0]
atomData = [start_atom]


while start_atom > 0:

	for atom in range(start_atom):
		state = rnd.randint(1,allowed_states)
		if state == decay_state:
			start_atom = start_atom - 1
			if start_atom == 0:
				break
				
	time = time + 1
	timeData.append(time)
	atomData.append(start_atom)
				
print(len(timeData),len(atomData))

plt.plot(timeData,atomData)
plt.show()



				
	
	

