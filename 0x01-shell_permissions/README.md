# 0x01. Shell, permissions
## Details
      By Julien Barbier          Weight: 1              Project over - took place from 09-23-2021 to 09-24-2021          - you're done with 200% of tasks.              An auto review will be launched at the deadline      #### In a nutshell…
* Auto QA review:          68.25/70 mandatory            &            13.0/20 optional      
* Altogether:         160.88%* Mandatory: 97.5%
* Optional: 65.0%
*               Calculation:                   97.5%                    + (97.5% * 65.0%)               == 160.88%

## About Bash projects

Unless stated, all your projects will be auto-corrected with Ubuntu 20.04 LTS.

## Resources
Read or watch :
* [Permissions](https://intranet.hbtn.io/rltoken/5uUsOHrMbVBOpZFteNyBLg) 

man or help :
*  ` chmod ` 
*  ` sudo ` 
*  ` su ` 
*  ` chown ` 
*  ` chgrp ` 
*  ` id ` 
*  ` groups ` 
*  ` whoami ` 
*  ` adduser ` 
*  ` useradd ` 
*  ` addgroup ` 
## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/Y35d0Jims8dedreTJJiaAw) 
 ,  without the help of Google :
### Permissions
* What do the commands  ` chmod ` ,  ` sudo ` ,  ` su ` ,  ` chown ` ,  ` chgrp `  do
* Linux file permissions
* How to represent each of the three sets of permissions (owner, group, and other) as a single digit
* How to change permissions, owner and group of a file
* Why can’t a normal user  ` chown `  a file
* How to run a command with root privileges
* How to change user ID or become superuser
### Other Man Pages
* How to create a user
* How to create a group
* How to print real and effective user and group IDs
* How to print the groups a user is in
* How to print the effective userid
## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your scripts will be tested on Ubuntu 20.04 LTS
* All your scripts should be exactly two lines long ( ` $ wc -l file `  should print 2)
* All your files should end with a new line ([why?](http://unix.stackexchange.com/questions/18743/whats-the-point-in-adding-a-new-line-to-the-end-of-a-file/18789) 
)
* The first line of all your files should be exactly  ` #!/bin/bash ` 
* A  ` README.md `  file, at the root of the folder of the project, describing what each script is doing
* You are not allowed to use backticks,  ` && ` ,  ` || `  or  ` ; ` 
* All your files must be executable
## Quiz questions
Show
#### 
        
        Question #0
    
 Quiz question Body Which command should I use for changing a file permission?
 Quiz question Answers * su

* chmod

* chown

* chgrp

 Quiz question Tips #### 
        
        Question #1
    
 Quiz question Body Which command should I use for changing a file owner?
 Quiz question Answers * su

* chmod

* chown

* chgrp

 Quiz question Tips #### 
        
        Question #2
    
 Quiz question Body What is the permission value for a file without any restriction?
 Quiz question Answers * 600

* 644

* 777

 Quiz question Tips #### 
        
        Question #3
    
 Quiz question Body What is the permission value for a file read only for the group owner?
 Quiz question Answers * 040

* 050

* 060

* 070

 Quiz question Tips #### 
        
        Question #4
    
 Quiz question Body What is the numerical value for the   ` rwx------ `   permission?
 Quiz question Answers * 600

* 621

* 704

* 700

 Quiz question Tips #### 
        
        Question #5
    
 Quiz question Body What is the numerical value for the   ` r-xr--r-- `   permission?
 Quiz question Answers * 522

* 544

* 644

* 411

 Quiz question Tips #### 
        
        Question #6
    
 Quiz question Body What is the numerical value for the   ` ----w---x `   permission?
 Quiz question Answers * 123

* 121

* 221

* 021

 Quiz question Tips ## Tasks
### 0. My name is Betty
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body Create a script that switches the current user to the user   ` betty `  .
* You should use exactly 8 characters for your command (+1 character for the new line)
* You can assume that the user  ` betty `  will exist when we will run your script
 ` julien@ubuntu:/tmp/h$ tail -1 0-iam_betty | wc -c
9
julien@ubuntu:/tmp/h$
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x01-shell_permissions ` 
* File:  ` 0-iam_betty ` 
 Self-paced manual review  Panel footer - Controls 
### 1. Who am I
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body Write a script that prints the effective username of the current user.
 ` julien@ubuntu:/tmp/h$ ./1-who_am_i
julien
julien@ubuntu:/tmp/h$ 
 `  Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x01-shell_permissions ` 
* File:  ` 1-who_am_i ` 
 Self-paced manual review  Panel footer - Controls 
### 2. Groups
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body Write a script that prints all the groups the current user is part of.
```bash
julien@ubuntu:/tmp/h$ ./2-groups
julien adm cdrom sudo dip plugdev lpadmin sambashare
julien@ubuntu:/tmp/h$ 

```
Note: depending on the user, you will get a different output.
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x01-shell_permissions ` 
* File:  ` 2-groups ` 
 Self-paced manual review  Panel footer - Controls 
### 3. New owner
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body Write a script that changes the owner of the file   ` hello `   to the user   ` betty `  .
```bash
julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 30 Sep 20 14:23 3-new_owner
-rw-rw-r-- 1 julien julien  0 Sep 20 14:18 hello
julien@ubuntu:/tmp/h$ sudo ./3-new_owner 
julien@ubuntu:/tmp/h$ ls -l
total 4
-rwxrw-r-- 1 julien julien 30 Sep 20 14:23 3-new_owner
-rw-rw-r-- 1 betty  julien  0 Sep 20 14:18 hello
julien@ubuntu:/tmp/h$

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x01-shell_permissions ` 
* File:  ` 3-new_owner ` 
 Self-paced manual review  Panel footer - Controls 
### 4. Empty!
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body Write a script that creates an empty file called   ` hello `  .
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x01-shell_permissions ` 
* File:  ` 4-empty ` 
 Self-paced manual review  Panel footer - Controls 
### 5. Execute
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body Write a script that adds execute permission to the owner of the file   ` hello `  .
* The file  ` hello `  will be in the working directory
```bash
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:26 5-execute
-rw-rw-r-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./hello
bash: ./hello: Permission denied
julien@ubuntu:/tmp/h$ ./5-execute 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:26 5-execute
-rwxrw-r-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x01-shell_permissions ` 
* File:  ` 5-execute ` 
 Self-paced manual review  Panel footer - Controls 
### 6. Multiple permissions
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body Write a script that adds execute permission to the owner and the group owner, and read permission to other users, to the file   ` hello `  .
* The file  ` hello `  will be in the working directory
```bash
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 36 Sep 20 14:31 6-multiple_permissions
-r--r----- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./6-multiple_permissions 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 36 Sep 20 14:31 6-multiple_permissions
-r-xr-xr-- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x01-shell_permissions ` 
* File:  ` 6-multiple_permissions ` 
 Self-paced manual review  Panel footer - Controls 
### 7. Everybody!
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body Write a script that adds execution permission to the owner, the group owner and the other users, to the file   ` hello ` 
* The file  ` hello `  will be in the working directory
* You are not allowed to use commas for this script
```bash
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:35 7-everybody
-rw-r----- 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./7-everybody 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:35 7-everybody
-rwxr-x--x 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x01-shell_permissions ` 
* File:  ` 7-everybody ` 
 Self-paced manual review  Panel footer - Controls 
### 8. James Bond
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body Write a script that sets the permission to the file   ` hello `   as follows:
* Owner: no permission at all
* Group: no permission at all
* Other users: all the permissions
The file   ` hello `   will be in the working directoryYou are not allowed to use commas for this script
```bash
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:40 8-James_Bond
-rwxr-x--x 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./8-James_Bond 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 28 Sep 20 14:40 8-James_Bond
-------rwx 1 julien julien 23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x01-shell_permissions ` 
* File:  ` 8-James_Bond ` 
 Self-paced manual review  Panel footer - Controls 
### 9. John Doe
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body Write a script that sets the mode of the file   ` hello `   to this:
 ` -rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
 ` * The file  ` hello `  will be in the working directory
* You are not allowed to use commas for this script
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x01-shell_permissions ` 
* File:  ` 9-John_Doe ` 
 Self-paced manual review  Panel footer - Controls 
### 10. Look in the mirror
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body Write a script that sets the mode of the file   ` hello `   the same as   ` olleh `  ’s mode.
* The file  ` hello `  will be in the working directory
* The file  ` olleh `  will be in the working directory
```bash
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 42 Sep 20 14:45 10-mirror_permissions
-rwxr-x-wx 1 julien julien 23 Sep 20 14:25 hello
-rw-rw-r-- 1 julien julien  0 Sep 20 14:43 olleh
julien@ubuntu:/tmp/h$ ./10-mirror_permissions 
julien@ubuntu:/tmp/h$ ls -l
total 8
-rwxrw-r-- 1 julien julien 42 Sep 20 14:45 10-mirror_permissions
-rw-rw-r-- 1 julien julien 23 Sep 20 14:25 hello
-rw-rw-r-- 1 julien julien  0 Sep 20 14:43 olleh
julien@ubuntu:/tmp/h$ 

```
Note: the mode of   ` olleh `   will not always be 664. Make sure your script works for any mode.
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x01-shell_permissions ` 
* File:  ` 10-mirror_permissions ` 
 Self-paced manual review  Panel footer - Controls 
### 11. Directories
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body Create a script that adds execute permission to all subdirectories of the current directory for  the owner, the group owner and all other users. Regular files should not be changed.
```bash
julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   24 Sep 20 14:53 11-directories_permissions
drwx------ 2 julien julien 4096 Sep 20 14:49 dir0
drwx------ 2 julien julien 4096 Sep 20 14:49 dir1
drwx------ 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./11-directories_permissions 
julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   24 Sep 20 14:53 11-directories_permissions
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x01-shell_permissions ` 
* File:  ` 11-directories_permissions ` 
 Self-paced manual review  Panel footer - Controls 
### 12. More directories
          mandatory         Progress vs Score           Score: 100.00% (Checks completed: 100.00%)         Task Body Create a script that creates a directory called   ` my_dir `   with permissions 751 in the working directory.
```bash
julien@ubuntu:/tmp/h$ ls -l
total 20
-rwxrwxr-x 1 julien julien   39 Sep 20 14:59 12-directory_permissions
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ ./12-directory_permission s
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   39 Sep 20 14:59 12-directory_permissions
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien 4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x01-shell_permissions ` 
* File:  ` 12-directory_permissions ` 
 Self-paced manual review  Panel footer - Controls 
### 13. Change group
          mandatory         Progress vs Score           Score: 65.00% (Checks completed: 100.00%)         Task Body Write a script that changes the group owner to   ` school `   for the file   ` hello ` 
* The file  ` hello `  will be in the working directory
```bash
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   34 Sep 20 15:03 13-change_group
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien 4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ sudo ./13-change_group 
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      34 Sep 20 15:03 13-change_group
drwx--x--x 2 julien julien    4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien    4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien    4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien    4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 julien school   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x01-shell_permissions ` 
* File:  ` 13-change_group ` 
 Self-paced manual review  Panel footer - Controls 
### 14. Owner and group
          #advanced         Progress vs Score           Score: 65.00% (Checks completed: 100.00%)         Task Body Write a script that changes the owner to   ` vincent `   and the group owner to   ` staff `   for all the files and directories in the working directory.
```bash
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   36 Sep 20 15:06 100-change_owner_and_group
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir0
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir1
drwx--x--x 2 julien julien 4096 Sep 20 14:49 dir2
drwxr-x--x 2 julien julien 4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ sudo ./100-change_owner_and_group 
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 vincent staff   36 Sep 20 15:06 100-change_owner_and_group
drwx--x--x 2 vincent staff 4096 Sep 20 14:49 dir0
drwx--x--x 2 vincent staff 4096 Sep 20 14:49 dir1
drwx--x--x 2 vincent staff 4096 Sep 20 14:49 dir2
drwxr-x--x 2 vincent staff 4096 Sep 20 14:59 my_dir
-rw-rw-r-- 1 vincent staff   23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x01-shell_permissions ` 
* File:  ` 100-change_owner_and_group ` 
 Self-paced manual review  Panel footer - Controls 
### 15. Symbolic links
          #advanced         Progress vs Score           Score: 65.00% (Checks completed: 100.00%)         Task Body Write a script that changes the owner and the group owner of   ` _hello `   to   ` vincent `   and   ` staff `   respectively.
* The file  ` _hello `  is in the working directory
* The file  ` _hello `  is a symbolic link
```bash
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien   44 Sep 20 15:12 101-symbolic_link_permissions
-rw-rw-r-- 1 julien julien   23 Sep 20 14:25 hello
lrwxrwxrwx 1 julien julien    5 Sep 20 15:10 _hello -> hello
julien@ubuntu:/tmp/h$ sudo ./101-symbolic_link_permissions 
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      44 Sep 20 15:12 101-symbolic_link_permissions
-rw-rw-r-- 1 julien julien      23 Sep 20 14:25 hello
lrwxrwxrwx 1 vincent  staff    5 Sep 20 15:10 _hello -> hello
julien@ubuntu:/tmp/h$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x01-shell_permissions ` 
* File:  ` 101-symbolic_link_permissions ` 
 Self-paced manual review  Panel footer - Controls 
### 16. If only
          #advanced         Progress vs Score           Score: 65.00% (Checks completed: 100.00%)         Task Body Write a script that changes the owner of the file   ` hello `   to   ` vincent `   only if it is owned by the user   ` guillaume `  .
* The file  ` hello `  will be in the working directory
```bash
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien    julien      47 Sep 20 15:18 102-if_only 
-rw-rw-r-- 1 guillaume julien      23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ sudo ./102-if_only 
julien@ubuntu:/tmp/h$ ls -l
total 24
-rwxrwxr-x 1 julien julien      47 Sep 20 15:18 102-if_only 
-rw-rw-r-- 1 vincent  julien      23 Sep 20 14:25 hello
julien@ubuntu:/tmp/h$ 

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x01-shell_permissions ` 
* File:  ` 102-if_only ` 
 Self-paced manual review  Panel footer - Controls 
### 17. Star Wars
          #advanced         Progress vs Score           Score: 65.00% (Checks completed: 100.00%)         Task Body Write a script that will play the StarWars IV episode in the terminal.
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x01-shell_permissions ` 
* File:  ` 103-Star_Wars ` 
 Self-paced manual review  Panel footer - Controls 
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