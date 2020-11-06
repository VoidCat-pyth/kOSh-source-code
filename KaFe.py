def runprog(file):
	mnf = open(file)
	compilebas(mnf)
	mnf.close()

def compilebas(mainf):
	prog = {}
	code = list(mainf.readlines())#.split())
	for i in range(len(code)):
		curstr = code[i].split()
		prog[i] = {curstr:type(code[i])}	
	print(prog)
runprog('.\\applications\\file.kaf')