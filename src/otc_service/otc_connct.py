import shade  
from munch import *  
from pprint import *  
  
# Initialize and turn on debug logging  
shade.simple_logging(debug=True)  
  
# Initialize cloud  
# Cloud configs are read with os-client-config  
cloud = shade.openstack_cloud(cloud='otc-alexa')  
  
# read all flavors, unmunchify and print out human readable  
flavors =  cloud.list_flavors()  
for flavor in flavors:  
    pprint(unmunchify(flavor))  
    print "#########################"  
