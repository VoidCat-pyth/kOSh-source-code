import os
import keyboard
#import zipfile
#import KaFe
#direct = [os.path.split(os.getcwd())[1]]
#print(direct) - Это была проверка
try:
	class commands: #Все комманды
		def chd(dire):
			if dire != '..': 
			#try:
				os.chdir(dire[0])
			#direct.append(dire[0])
			
			elif dire == '..': 
			
			#direct.pop(len(direct)-1)
				os.system('cd ..')
		
		def lsd(pust):
			cdirfiles = os.listdir()
			for n in cdirfiles:
				if len(cdirfiles) == 1:
					print(n)
				else:
					if n != cdirfiles[-1::]:
						print(n+', ',end='')
					else:
						print(n, end='')
			print()
	
		def rdfl(file):
			try:
				f = open(file[0])
				fil = f.readlines()
				for o in fil:
					print(o, end='')
				print()

				f.close()
			except FileNotFoundError:
				print('FILE NOT FOUND')

		def mkd(name):
			try:
				os.mkdir((os.getcwd()+'\\'+name[0]))
				print('FOLDER SUCCEFULLY CREATED')
			except OSError:
				print('ERROR, FOLDER IS CURRENTLY EXIST')

		def rmd(name):
			try:
				os.rmdir((os.getcwd()+'\\'+name[0]))
				print('FILE SUCCEFULLY REMOVED')
			except FileNotFoundError:
				print('FILE NOT FOUND')

		def clr(pust):
			if os.name == 'nt':
				os.system('cls')
			else:
				os.system('clear')

	#def lnc(name):
	#	if zipfile.is_zipfile(name[0]):
	#		p = zipfile.ZipFile(name[0])
	#		p.extractall()
	#		p.close()
	#	else:
	#		print('THIS FILE IS NOT ZIP FILE')

		def exit(pust):
			keyboard.press_and_release('ctrl + c')

		def hpme(pust):
			print('hpme - Show help(this) menu\nchd - Change directory\nlsd - Show list of files in current directory\nrdfl - Reads file\nmkd - Create folder\nrmd - Remove folder\nclr - Clear the command line\nexit - Exit the kOSh')
	commands.hpme(None)
	print('kOSh V0.1(alpha)')
	while 1:
	#for j in direct: #вывод расположения относительно ОС
		#if len(direct) == 1:
		#	print(j + '#',end='')
		#else:
			#if j != direct[-1::]:
			#	print(j +'\\', end='')
		
			#else:
				#print(j + '#',end='')
		
	#print(direct[i] for i in direct+'#',end='')
		print('#',end='')
	
		command = str(input()).lower() #Ввод комманд
		if command == '':
			pass
		else:
	#print(command)
			cmd = list(command.split()) #разбор комманды по частям
	#print(cmd)

	#try: #запуск и проверка комманды на существование
			try:
				exec('commands.'+str(cmd[0])+'( '+ str(cmd[1::]) +' )')
			except AttributeError:
				print('COMMAND NOT FOUND')
			except IndexError:
				pass
except KeyboardInterrupt:
	print('GOODBYE')