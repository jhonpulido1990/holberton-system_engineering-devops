# 0x08. Networking basics #1
## Details
      By Sylvain Kalache          Weight: 1                Ongoing project - started 02-23-2022, must end by 02-25-2022 (in about 6 hours)          - you're done with 0% of tasks.              Checker will be released at 02-25-2022 12:00 AM              An auto review will be launched at the deadline       ![](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/285/s7kpNYq.png) 

## Resources
Read or watch :
* [What is localhost](https://intranet.hbtn.io/rltoken/7SedZ8ILSQulYf7xzSbraQ) 

* [What is 0.0.0.0](https://intranet.hbtn.io/rltoken/n5IFAt_OWGJtGW33t7Jfag) 

* [What is the hosts file](https://intranet.hbtn.io/rltoken/21l3Uqizr3LpA1ZGrYPg3g) 

* [Netcat examples](https://intranet.hbtn.io/rltoken/uMleIIzkRoR2w8EkwItSEg) 

man or help :
*  ` ifconfig ` 
*  ` telnet ` 
*  ` nc ` 
*  ` cut ` 
## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/BxPpO9moponw8J8TjKpRlg) 
 ,  without the help of Google :
### General
* What is localhost/127.0.0.1
* What is 0.0.0.0
* What is  ` /etc/hosts ` 
* How to display your machine’s active network interfaces
## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted on Ubuntu 20.04 LTS
* All your files should end with a new line
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass  ` Shellcheck `  (version  ` 0.7.0 `  via  ` apt-get ` ) without any errors
* The first line of all your Bash scripts should be exactly  ` #!/usr/bin/env bash ` 
* The second line of all your Bash scripts should be a comment explaining what is the script doing
## Quiz questions
Show
#### 
        
        Question #0
    
 Quiz question Body What is   ` localhost `  ?
 Quiz question Answers * A hostname that means  this IP

* A hostname that means  this computer

* An IP attached to a computer

 Quiz question Tips #### 
        
        Question #1
    
 Quiz question Body What is   ` 0.0.0.0 `  ?
 Quiz question Answers * All IPv4 addresses on the local machine

* All the IPs

* It means null in networking

 Quiz question Tips ## Tasks
### 0. Change your home IP
          mandatory         Progress vs Score  Task Body Write a Bash script that configures an Ubuntu server with the below requirements.
Requirements:
*  ` localhost `  resolves to  ` 127.0.0.2 ` 
*  ` facebook.com `  resolves to  ` 8.8.8.8 ` .
*  The checker is running on Docker, so make sure to read [this](https://intranet.hbtn.io/rltoken/8PP1z09aHTqgTjyvET6-hg) 

Example:
```bash
sylvain@ubuntu$ ping localhost
PING localhost (127.0.0.1) 56(84) bytes of data.
64 bytes from localhost (127.0.0.1): icmp_seq=1 ttl=64 time=0.012 ms
^C
--- localhost ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.012/0.012/0.012/0.000 ms
sylvain@ubuntu$
sylvain@ubuntu$ ping facebook.com
PING facebook.com (157.240.11.35) 56(84) bytes of data.
64 bytes from edge-star-mini-shv-02-lax3.facebook.com (157.240.11.35): icmp_seq=1 ttl=63 time=15.4 ms
^C
--- facebook.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 15.432/15.432/15.432/0.000 ms
sylvain@ubuntu$
sylvain@ubuntu$ sudo ./0-change_your_home_IP
sylvain@ubuntu$
sylvain@ubuntu$ ping localhost
PING localhost (127.0.0.2) 56(84) bytes of data.
64 bytes from localhost (127.0.0.2): icmp_seq=1 ttl=64 time=0.012 ms
64 bytes from localhost (127.0.0.2): icmp_seq=2 ttl=64 time=0.036 ms
^C
--- localhost ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1000ms
rtt min/avg/max/mdev = 0.012/0.024/0.036/0.012 ms
sylvain@ubuntu$
sylvain@ubuntu$ ping facebook.com
PING facebook.com (8.8.8.8) 56(84) bytes of data.
64 bytes from facebook.com (8.8.8.8): icmp_seq=1 ttl=63 time=8.06 ms
^C
--- facebook.com ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 8.065/8.065/8.065/0.000 ms

```
In this example we can see that:
* before running the script,  ` localhost `  resolves to  ` 127.0.0.1 `  and  ` facebook.com `  resolves to  ` 157.240.11.35 ` 
* after running the script,   ` localhost `  resolves to  ` 127.0.0.2 `  and  ` facebook.com `  resolves to  ` 8.8.8.8 ` 
If you’re running this script on a machine that you’ll continue to use, be sure to revert   ` localhost `   to   ` 127.0.0.1 `  . Otherwise, a lot of things will stop working!
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x08-networking_basics_2 ` 
* File:  ` 0-change_your_home_IP ` 
 Self-paced manual review  Panel footer - Controls 
### 1. Show attached IPs
          mandatory         Progress vs Score  Task Body Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.
Example:
 ` sylvain@ubuntu$ ./1-show_attached_IPs | cat -e
10.0.2.15$
127.0.0.1$
sylvain@ubuntu$
 ` Obviously, the IPs displayed may be different depending on which machine you are running the script on.
Note that we can see our   ` localhost `   IP :)
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x08-networking_basics_2 ` 
* File:  ` 1-show_attached_IPs ` 
 Self-paced manual review  Panel footer - Controls 
[Done with the mandatory tasks? Unlock 1 advanced task now!](https://intranet.hbtn.io/projects/285/unlock_optionals) 

×#### Recommended Sandbox
[Running only]() 
### 1 image(1/5 Sandboxes spawned)
### Ubuntu 20.04
Basic Ubuntu 20.04, with vim, emacs, curl, wget and all needed for Holberton Foundations
SSHSFTP[Webterm](https://intranet.hbtn.io/user_containers/17836/webterm) 
[Destroy]() 
#### Credentials
Host4aa76ec2605d.ba0aa7bd.hbtn-cod.ioUsername4aa76ec2605dPassword95896abd009a136e84ba#### Web access
[HTTPS](https://4aa76ec2605d.ba0aa7bd.hbtn-cod.io/) 
[HTTP](http://4aa76ec2605d.ba0aa7bd.hbtn-cod.io/) 
[3000](http://4aa76ec2605d.ba0aa7bd.hbtn-cod.io:3000/) 
[4000](http://4aa76ec2605d.ba0aa7bd.hbtn-cod.io:4000/) 
[5000](http://4aa76ec2605d.ba0aa7bd.hbtn-cod.io:5000/) 
[5001](http://4aa76ec2605d.ba0aa7bd.hbtn-cod.io:5001/) 
[8000](http://4aa76ec2605d.ba0aa7bd.hbtn-cod.io:8000/) 
[8080](http://4aa76ec2605d.ba0aa7bd.hbtn-cod.io:8080/) 
#### Port mapping
SSH49328HTTP49327HTTPS49326300049325MySQL49324400049323500049322500149321800049320808049319