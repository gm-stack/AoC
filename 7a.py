import sys
i = open("input-7.txt").readlines()

commands = [line.strip().split(" ") for line in i]
wires = {}

def wire(w):
	if w.isalpha():
		return int(wires[w])
	else:
		return int(w)

while commands:
	print len(commands)
	cmd = commands.pop(0)

	try:
		dst = cmd[-1]
		wires["b"] = 956
		if len(cmd) == 3:
				wires[dst] = wire(cmd[0])
		elif len(cmd) == 4:
			subcmd = cmd[0]
			arg0 = cmd[1]
			if subcmd == "NOT":
				wires[dst] = ~wire(arg0) & 0xFFFF
			else:
				print cmd, len(cmd)
		elif len(cmd) == 5:
			subcmd = cmd[1]
			arg0 = cmd[0]
			arg1 = cmd[2]
			if subcmd == "AND":
				wires[dst] = int(wire(arg0)) & int(wire(arg1))
			elif subcmd == "OR":
				wires[dst] = int(wire(arg0)) | int(wire(arg1))
			elif subcmd == "LSHIFT":
				wires[dst] = int(wire(arg0)) << int(wire(arg1))
			elif subcmd == "RSHIFT":
				wires[dst] = int(wire(arg0)) >> int(wire(arg1))
			else:
				print cmd, len(cmd)
		else:
			print cmd, len(cmd)
		wires["b"] = 956
	except KeyError:
		print sys.exc_info()
		print cmd
		commands.append(cmd)


#for wire in sorted(wires):
#	print wire + ": " + str(wires[wire])

print wires["a"]

#	