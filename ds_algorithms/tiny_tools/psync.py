import os
import subprocess
import sys

def sync(local):
    hosts=['hadoop100','hadoop101','hadoop102','hadoop103']
    if os.path.exists(local):
        for host in hosts:
                tem=os.path.split(local)[0]
                cmd = "rsync -av {local_file} {ip}:{remote_file}".format(local_file=local,ip=host,remote_file=tem)
                subprocess.call(cmd, shell=True)
                #print(cmd)
    else:
        print ("文件不存在")
    
def excute(*args):
    inp=''
    for i in args:
        inp=i[1]
    sync(inp)

if __name__ == "__main__":
    args = sys.argv
    excute(args)