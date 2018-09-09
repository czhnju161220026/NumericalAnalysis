import mat4py as mpy

def get_vertixs():
    data=mpy.loadmat('path.mat')
    out=open("vertixs.txt",'w+')
    # out.write(str(data))
    vertixs=list(data['path_chan'])
    for vertix in vertixs:
        out.write(str(vertix)+'\n')
    out.close()
    return vertixs




