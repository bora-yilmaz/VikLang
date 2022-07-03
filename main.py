#this is the compiler code
#DO NOT EDIT!!

def ctc(command, *param):
	code=[]
	if command=='/var':
		code.append(param[0] + '=' + param[1] + '')
	elif command=='/echo':
		code.append('print("\\033[32m"+str('+param[0]+'))')
	elif command=='/calc':
		code.append('calc= ('+param[0]+');')
	elif command=='/input':
		code.append('inputtaken= input('+ (' '.join(param))+')')
	elif command=='/alert':
		code.append('print("\\033[31m"+str('+param[0]+'))')
	elif command=='/str':
		code.append('stringmade=('+(' '.join(param))+')')
	elif command=='':
		code.append('')
	elif command[0:2]=='//':
		code.append('')
	elif command=='/func':
		with open(param[0]+'.vl','r') as file:
			code.extend(('def '+param[1]+'('+','.join(param[2:])+'):\n\t'+compilew(file.read().split('\n'), '\n\t')).split('\n'))
	elif command=='/if':
		code.extend(['if '+param[0]+':','\t'+param[1]+'('+(','.join(param[2:]))+')'])
	elif command=='/while':
		with open(param[1]+'.vl','r') as file:
			code.extend(('while '+param[0]+':\n\t'+compilew(file.read().split('\n'), '\n\t')).split('\n'))
	elif command=='/json':
		with open(param[0]+'.json', 'r') as file:
			code.append('json = '+file.read().replace('\n', ''))
	elif command[:1]=='/':
		code.append(command[1:]+'('+(','.join(param))+')')
	else:
		print('unknown command')
	return code

with open('main.vl','r') as file:
	codelines = file.read().split('\n')
def compilew(codelines, le='\n'):
	tc = []
	for i, line in enumerate(codelines):
		com = line.split(' ')
		tc.extend(ctc(*com))
	return le.join(tc)
codec = compilew(codelines)
print(codec)
exec(codec)
