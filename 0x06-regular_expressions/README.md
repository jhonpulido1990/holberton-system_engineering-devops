# 0x06. Regular expression
## Details
      By Sylvain Kalache          Weight: 1                Ongoing project - started 02-23-2022, must end by 02-24-2022 (in about 13 hours)          - you're done with 0% of tasks.              Checker will be released at 02-23-2022 06:00 PM      Manual QA review must be done          (request it when you are done with the project)              An auto review will be launched at the deadline      ## Concepts
For this project, students are expected to look at this concept:
* [Regular Expression](https://intranet.hbtn.io/concepts/29) 

## Background Context
For this project, you have to build your regular expression using Oniguruma, a regular expression library that which is used by Ruby by default. Note that other regular expression libraries sometimes have different properties.
Because the focus of this exercise is to play with regular expressions (regex), here is the Ruby code that you should use, just replace the regexp part, meaning the code in between the   ` // `  :
```bash
sylvain@ubuntu$ cat example.rb
#!/usr/bin/env ruby
puts ARGV[0].scan(/127.0.0.[0-9]/).join
sylvain@ubuntu$
sylvain@ubuntu$ ./example.rb 127.0.0.2
127.0.0.2
sylvain@ubuntu$ ./example.rb 127.0.0.1
127.0.0.1
sylvain@ubuntu$ ./example.rb 127.0.0.a

```
## Resources
Read or watch :
* [Regular expressions - basics](https://intranet.hbtn.io/rltoken/SJ2eQ7V2iQlCgLc-L96zWg) 

* [Regular expressions - advanced](https://intranet.hbtn.io/rltoken/qyjWL-J1_qUaZGR690gH1Q) 

* [Rubular is your best friend](https://intranet.hbtn.io/rltoken/WCjn8NgohbQ5NGXEObWZvQ) 

* [Use a regular expression against a problem: now you have 2 problems](https://intranet.hbtn.io/rltoken/Zfvv_ydOCvJ_YaBB6eDqVw) 

* [Learn Regular Expressions with simple, interactive exercises](https://intranet.hbtn.io/rltoken/Y-OVGcJ5cskdXWIBowiE_A) 

## Requirements
### General
* Allowed editors:  ` vi ` ,  ` vim ` ,  ` emacs ` 
* All your files will be interpreted on Ubuntu 20.04 LTS
* All your files should end with a new line
* A  ` README.md `  file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* The first line of all your Bash scripts should be exactly  ` #!/usr/bin/env ruby ` 
* All your regex must be built for the Oniguruma library
## Quiz questions
Show
#### 
        
        Question #0
    
 Quiz question Body What is the   ` /school/ `   regexp matching?
 Quiz question Answers * sch00l

* School

* school

 Quiz question Tips #### 
        
        Question #1
    
 Quiz question Body What is the   ` /scho.l/ `   regexp matching?
 Quiz question Answers * scho.l

* school

* sch0ol

 Quiz question Tips #### 
        
        Question #2
    
 Quiz question Body What is the   ` /Scho*l/ `   regexp matching?
 Quiz question Answers * Scholl

* Schol

 Quiz question Tips ## Tasks
### 0. Simply matching School
          mandatory         Progress vs Score  Task Body  ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/ec65557f0da1fbfbff6659413885e4d4822f5b1d.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220223%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220223T153517Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=2d4074c6d4af42b7d986dbc50114ec06785cd0108efd79bc6521cb92e895394b) 

Requirements:
* The regular expression must match  ` School ` 
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
Example:
```bash
sylvain@ubuntu$ ./0-simply_match_holberton.rb School | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Best School" | cat -e
School$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "School Best School" | cat -e
SchoolSchool$
sylvain@ubuntu$ ./0-simply_match_holberton.rb "Grace Hopper" | cat -e
$

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x06-regular_expressions ` 
* File:  ` 0-simply_match_school.rb ` 
 Self-paced manual review  Panel footer - Controls 
### 1. Repetition Token #0
          mandatory         Progress vs Score  Task Body  ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/e7db3c377d46453588fc84f3a975661d142fee91.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220223%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220223T153517Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=d5c16715edf3b9ca59e4af56b56b6b6439e40c8de3c4012484b312c618e0091e) 

Requirements:
* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x06-regular_expressions ` 
* File:  ` 1-repetition_token_0.rb ` 
 Self-paced manual review  Panel footer - Controls 
### 2. Repetition Token #1
          mandatory         Progress vs Score  Task Body  ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/c59ff11db195d5cf17d1790a5141ae2f234786d2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220223%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220223T153517Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=32af6e1be20740abde30e02c8a294ba60203a705f998eef5dd8a1fbe83962921) 

Requirements:
* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x06-regular_expressions ` 
* File:  ` 2-repetition_token_1.rb ` 
 Self-paced manual review  Panel footer - Controls 
### 3. Repetition Token #2
          mandatory         Progress vs Score  Task Body  ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/3b6bf4aeca6a0c2de584e7f5d68d11eef57ce205.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220223%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220223T153517Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=f76cd3b074e8e48ad91e36c9d9ac07573b8a467088804d21af8ef73c42c2e36d) 

Requirements:
* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x06-regular_expressions ` 
* File:  ` 3-repetition_token_2.rb ` 
 Self-paced manual review  Panel footer - Controls 
### 4. Repetition Token #3
          mandatory         Progress vs Score  Task Body  ![](https://holbertonintranet.s3.amazonaws.com/uploads/medias/2020/9/f8dbcb9cf5ae569a8645027dc46e81cb372ce28e.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOU5BHMTQX4%2F20220223%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220223T153517Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=9b82ef43a8e00b3614bfb1d268c6455ec0564a35d1d969b88f8141f2e838e6d7) 

Requirements:
* Find the regular expression that will match the above cases
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
* Your regex should not contain square brackets
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x06-regular_expressions ` 
* File:  ` 4-repetition_token_3.rb ` 
 Self-paced manual review  Panel footer - Controls 
### 5. Not quite HBTN yet
          mandatory         Progress vs Score  Task Body Requirements:
* The regular expression must be exactly matching a string that starts with  ` h `  ends with  ` n `  and can have any single character in between
* Using the project instructions, create a Ruby script that accepts one argument and pass it to a regular expression matching method
Example:
```bash
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbn' | cat -e
hbn$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'hbtn' | cat -e
$
sylvain@ubuntu$ ./5-beginning_and_end.rb 'h8n' | cat -e
h8n$
sylvain@ubuntu$
$

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x06-regular_expressions ` 
* File:  ` 5-beginning_and_end.rb ` 
 Self-paced manual review  Panel footer - Controls 
### 6. Call me maybe
          mandatory         Progress vs Score  Task Body This task is brought to you by a professional advisor  [Neha Jain](https://intranet.hbtn.io/rltoken/V4rEpseJEPRMMnfaZPbkgw) 
 , Senior Software Engineer at LinkedIn.
Requirement:
* The regular expression must match a 10 digit phone number
Example:
```bash
sylvain@ubuntu$ ./6-phone_number.rb 4155049898 | cat -e
4155049898$
sylvain@ubuntu$ ./6-phone_number.rb " 4155049898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415 504 9898" | cat -e
$
sylvain@ubuntu$ ./6-phone_number.rb "415-504-9898" | cat -e
$
sylvain@ubuntu$

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x06-regular_expressions ` 
* File:  ` 6-phone_number.rb ` 
 Self-paced manual review  Panel footer - Controls 
### 7. OMG WHY ARE YOU SHOUTING?
          mandatory         Progress vs Score  Task Body  ![](https://intranet.hbtn.io/images/contents/sysadmin/projects/78/shouting.jpg) 

Requirement:
* The regular expression must be only matching: capital letters
Example:
```bash
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "I realLy hOpe VancouvEr posseSs Yummy Soft vAnilla Dupper Mint Ice Nutella cream" | cat -e
ILOVESYSADMIN$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "WHAT do you SAY?" | cat -e
WHATSAY$
sylvain@ubuntu$ ./7-OMG_WHY_ARE_YOU_SHOUTING.rb "cannot read you" | cat -e
$
sylvain@ubuntu$

```
 Task URLs  Github information Repo:
* GitHub repository:  ` holberton-system_engineering-devops ` 
* Directory:  ` 0x06-regular_expressions ` 
* File:  ` 7-OMG_WHY_ARE_YOU_SHOUTING.rb ` 
 Self-paced manual review  Panel footer - Controls 
[Done with the mandatory tasks? Unlock 2 advanced tasks now!](https://intranet.hbtn.io/projects/78/unlock_optionals) 

Ready for a manualreview×#### Recommended Sandbox
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