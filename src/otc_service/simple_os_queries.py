# import needed modules  
import shade  
import re  
  
# Initialize and turn on debug logging  
shade.simple_logging(debug=True)  
  
# Initialize cloud  
# Cloud configs are read with os-client-config  
cloud = shade.openstack_cloud(cloud='otc-alexa')  
  
def vm_count():  
    counttotal = []  
    countactive = []  
    countstopped = []  
    for i in cloud.list_servers(bare=True):  
        counttotal.append(i.name)  
        if i.status == 'ACTIVE':  
            countactive.append(i.name)  
        elif i.status == 'SHUTOFF':  
            countstopped.append(i.name)  
    t = len(counttotal)  
    a = len(countactive)  
    s = len(countstopped)  
    #print "Total: " + str(t)  
    #print "Active: " + str(a)  
    #print "Stopped: " + str(s)  
    return (t,a,s) 

def total_volume_size():
    volumes    = cloud.list_volumes()
    # total_size = reduce(lambda a,b: a.size + b.size, volumes).size 
    total_size = 0
    unused = 0
    for v in volumes:  
        total_size += v.size  
        if v.status != 'in-use':  
           unused += 1   
    return ( len(volumes), total_size, unused )

#def cce_clusters()
#
#    clusters   =
