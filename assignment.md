Assignment Description
Now that you have a solid foundation of Linux, it's time to create your own Linux VM instead of relying on pre-built distributions. Why would you do such a thing? Well... there are lots (hundreds) of different Linux distros for a reason - different people want different things. Being able to tailor your Linux OS to exactly what you want in there, and nothing else, is a feature that neither Windows or macOS provide. More importantly, for this course, creating your own Linux VM will provide you a tangible artifact that proves you can use the baseline Linux skills you have learned to do something potentially useful. This assignment will greatly enhance your understanding of how Linux works at a deeper level - a great asset to have if things break!

Installation
In this assignment, you will create your own Arch Linux VM byt following the Arch Linux Installation Wiki.

You will also make the following modifications:

1) The Arch Linux installation wiki ends without a GUI-based desktop environment (DE). You will choose and install a compatible DE. At very least, you should install LXQT, which is a very light-weight desktop that uses less hard drive space. BUT... this is not a requirement. Choose a DE that you like.

2) Create a user account for yourself, justin, and codi with sudo permissions. The passwords for the instructor users shall be "GraceHopper1906" and be set to be changed after login.

3) Install a different shell other than bash, such as zsh or fish.

4) Install ssh.

5) Add color coding to the terminal (like you see in the archiso during installation).

6) Set the system to boot into the GUI desktop environment.

7) Add a few aliases to your shell configuration file (surch as .zshrc for zsh or .bashrc for bash). Need some ideas for good Linux aliases? Check here.



What will you turn in for your assignment? There are two deliverables for this task:

Process Documentation
Walkthrough video
See the next two posts below for guidance on your installation process documentation and walkthrough video.

Deliverable #1: Installation Documentation
Using the Arch installation wiki, your newfound knowledge of Linux, and the almighty power of wisely-crafted DuckDuckGo searches, you will be able to build your own customized Arch Linux VM. You are required to create an installation document that shows what you did, if you encountered any issues during a step of the installation and what you did to overcome the issues, and any other comments or required or optional choices you made during the installation.

Some comments on this deliverable:

This is not a recreation of the Arch Install wiki. This is a shortened, useful, document that you can use to quickly recreate your Arch VM. When Codi & Justin sat down together to do this assignment, they did what you will likely do one or more times - they skimmed / skipped over some important recommended or required steps in the installation process. But, because they documented their process used up to the point where they realized they made an error, they were able to quickly recover (in only a few minutes compared to 1+ hours). You will create a document for yourself that covers the installation process and all the modifications identified in the assignment description.
You will individually turn in your installation documentation link on Harvey. While you can work with others during the install process, each student needs to create their own documentation and not just copy each others' work and submit the same documentation. You will use your documentation for the second deliverable (Walkthrough Video) so you need to understand your documentation not only while creating the video but for possible future use.
You will create and share your Arch Linux VM installation documentation using Github Pages. If you have never used Github Pages, the link provided walks you through the process. You can make your documentation as plain or pretty as you want, but it must be formatted so that others can easily follow the flow of your process. It is highly recommended to make your documentation using Markdown to make the transition to GitHub Pages seamless.
You are STRONGLY RECOMMENDED to start your installation documentation at the beginning of your initial install process from the Arch Wiki.  

Add comments as you think of them during the install. Focus on comments that might help you recreate your process if you are called upon to do so. Which may happen...
Have a question during the install that you found the answer for - document it.
It is especially important to document any errors you make and how your recovered. This can be as simple as missing a step or making a choice you did not like. If you made this error once, you could make it again so let your documentation help you prevent future mistakes.
Document every command you use and provide a comment on what it does.
Markdown Resources
https://www.markdownguide.org/getting-started/ 
https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet


Recommended Markdown Editors:

Visual Studio Code (has Markdown to PDF and linting extensions)

Obsidian (amazing for notes and documentation)

Deliverable #2: Walkthrough Video
You will submit a walkthrough video showcasing your Arch Linux VM. Specifics / comments:

The video will be created / uploated to Panopto on Harvey.
The video will be bookmarked to allow easy navigation to different sections of the video.
There is no length minimum as long as it meets the below requirements. The average is around 5-9 minutes. However, the video should only be as long as necessary to complete the required tasks. I will not watch a video that is over 15 minutes.
The following tasks are required, in order, for your walkthrough video and each requirement shall be bookmarked in Panopto.

1: Installation Process Summary: Briefly introduce yourself and then briefly summarize the installation process you used for your Arch VM. It would be good to use the Installation Documentation you created during this part. You should not read each command you used aloud but instead briefly summarize the main steps in the process. This is not an install guide video - the VM should be completed before you start recording.

2: VM operation and configuration: Show the following in your video:

Log into the desktop environment (GUI)
Launch a shell and show the IP address of your VM
Show the user list
Show the sudoers
Demonstrate some of your aliases
Launch a browser (which means you need to install one) and navigate to your Github-Pages hosted installation documentation to show that you have Internet connectivity
Show any cool customizations (if any) you did
Pick some package to install from the Arch User Repository (AUR)
3: Problems: Provide a short list of any problems you encountered during the installation and how you overcame them. Again, this can be as simple as missing a step in the Arch install wiki or something else that required you to do some extra troubleshooting. If you missed a step in the install process, when did you figure it out and how did you get back on track?