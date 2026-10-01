## Service Discovery

what problem does it solve? 
problem 1: when we are running applications on virtual machines(servers) we can put there ip addresses as target in prometheus config file, but problem starts when servers are not able to handle load and new servers are provisoned as per scaling plan. So challenge is adding and removing targets from prometheus whenever servers are scaled up and scaled down. 

problem 2:
If we put load balancer infront of servers we get new problem, load balancer rutes traffic as per round robin algorithm so everytime prometheus sends request to scrape meterics it will be sent only to single server not all which make metrices inconsitent and unreliable.

problem 3: Serverles compute instances such as azure functions, aws lambda dosen't get ip address or dns name, which is a challenge for prometheus sinceit workon pull based mechenism.

to solve these problems comes service discovery and push gateway(Temporary metric reciver for push based mechanism equipped with internal exporter).

How to condigure Service Discovery?
Service discovery is configured by prometheus.yml file. tags help in configurig service discovery for different kinds of targets, such as ec2_sd_config for aws ec2 instances dns_sd_config for dns based discovery and file_sd_config for file based discovery and more like kubernetes_sd_config, azure_sd_config.  

service discovery automates the  discovery and listing of servers or sources in targets config whch needs to be scraped.

example:
    It uses api calls for cloud provider and credentials to fetchlist of servers based on labels and metadata we provided for matching.
    another example is using file which is filled withlist of servers ip addresses which needs to be scrapped.