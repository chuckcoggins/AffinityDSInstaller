# AffinityDSInstaller
This Python Program installs a piece of work software automatically for us.

I am unable to provide the files that get copied out to their destination folders due to the files belonging to the company I work for.

This is the second tool I have created for my Support and Implementation Team for the company I work for.

We have a program called AffinityDS and this is what needs to happen to manually install this.
First you have to copy the files out to their respective locations.
Next you have to launch the AffinityDS program.
When this program is launched/executed it creates a folder in ProgramData and it also creates an XML file in which the AffinityDS program uses.
Then from there you need to go to the ProgramData folder. Open the XML file and change the loopback 127.0.0.1 address to the address of the server/computer.
Once all that is done you need to then create a service for the AffinityDSSvc application so the program can run all the time in the background as a service once it is setup.
Finally you would normally launch AffinityDS to watch all of the clocks connect in and make sure everything is setup and working as normal before shutting off the application and turning on the service.

The program I made automates all of this for us.

I think one of the cool things I added was I have the program return your hostname and IP address.
Then I let you choose (Press 1 or Press 2) to either use that IP address or Specify your own IP address to use.

The Code:

Lines 7-12
Specify the current source working directory.
Then I have a bunch of variables I created that will make directories if they need to be there.

Line 16+17
This is a function I created to make printing in colour easier.
I can just call colourText() and add in what I want to print out to the screen and then the colour I want that text to be.

Lines 24 - 43
These are try and except conditions.
I had never used the try and except before in any of my code so I wanted to give that a shot and I used it here.
What we end up doing is checking to see if those directories in the variables of lines 7-12 exist or not. It tries to create the directories, but if the directory already exists it falls on except and tells the user that the directory (path) already exists and that it is continuing on to the next step.

Lines 48 - 59
This is the copy code which uses os.walk() and is a truple.
This part of the code just goes through and copies all of the source file data to the same spot in the new location.

Lines 64 - 81
This is a function called start and stop affinity ds.
This one was kind of cool and I had another first for me in this function.
Lines 64 - 66
I use os.startfile to open up AffinityDS. 
I am doing this because the application needs to open to create the programdata XML and directories.
I added a sleep timer so things don't happen too quick.

Then the cool part
Lines 68 - 81
I change the directory using os.chdir to the programdata folder
I spin up a for loop in range of 0,5.
On line 73 I am checking to make sure that the AffinityDS application created the XML file by using os.path.isfile
If the file exists it then runs os.system TASKKILL and kills the AffinityDS application.
However, if the file does not exist it will loop through 5 times with a sleep timer of 3 seconds and wait for the file to exist.
If it never exists the program would stop and tell us it cannot kill ADS because the XML was never created.

Lines 84 - 127
I created another function which grabs the hostname and IP information and displays it on screen.
Then allows you to choose the IP address by pressing 1 or specify your own IP by pressing 2.
It will then open the XML file and modify the loopback address to the new IP you wanted.

Lines 86 - 93
This is another try and except condition. I realize I probably did not need to use this, but I wanted try and use some code I had never used before.
So we created some variables that get the hostname and get the IP address and stores those in the variables we made.
Then we print those out for the user to see.
There is an except statement that if for some reason the program was unable to get the hostname and IP it would tell you that it could not obtain them.

Lines 95 - 127
The first few lines above this are print statements that just say press 1 to use the IP: xxx.xxx.xxx.xxx or press 2 to enter your own.
Then line 101 is an if statement that says if 1 is pressed read the xml file
The modification of the XML happens in line 107.
Line 110 - 112 actually opens the xml to write mode and adds in our modified line and then closes the file.

Line 114 is the second if/elif statement that says if == "2" create an input so the user can add in their own IP address.
Lines 117 - 127 ends up doing the same thing as the above lines 95-112

Line 134 is an os.system line where we launch command prompt and do an sc create to create a windows service. We then create our windows service for AffnityDS.

Line 138 is the real final line of code and it is another os.startfile command where we are just starting the AffinityDS application again so our user can setup clocks.

That is it.





