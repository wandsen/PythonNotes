import subprocess

#Spawning
# subprocess.call('dir' , shell = True)

# subprocess.run('dir', shell = True)

'''
subprocess.check_output(['echo', 'hello world'], shell=True)

p= subprocess.Popen(['echo', 'helloworld'] , stdout=subprocess.PIPE, shell=True)
p.communicate()
(b'helloworld\r\n', None)


proc=subprocess.Popen(['echo', 'to stdout'], stdout=subprocess.PIPE, shell=True)
stdout_v=proc.communicate()[0]
repr(stdout_v)
'b\'"to stdout"\\r\\n\''

'''