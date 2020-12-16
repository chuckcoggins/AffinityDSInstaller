#! python3
import shutil, os, time, socket
import xml.dom.minidom as md
from pip._vendor.colorama import Fore, Style, init
init()
# Global Variables
source_dir = os.getcwd()
mkdir_ads = 'C:\\Program Files (x86)\\TimeTrak Systems\\TimeTrakCONNECT\\AffinityDS\\'
mkdir_iclock = 'C:\\Program Files (x86)\\TimeTrak Systems\\TimeTrakCONNECT\\AffinityDS\\iclock\\'
mkdir_ess = 'C:\\Program Files (x86)\\TimeTrak Systems\\TimeTrakCONNECT\\AffinityDS\\essInfoTouch\\'
ads_source_dir = source_dir + "\AffinityDS"
ads_target_dir = 'C:\\Program Files (x86)\\TimeTrak Systems\\TimeTrakCONNECT\\AffinityDS\\'


# Coloured Text Function
def colourText(textHere, colour):
    print(getattr(Fore, colour) + textHere + Style.RESET_ALL)

# START
colourText("\n \t \t Welcome to the AffinityDS Clock Server Installer", "RED")
time.sleep(1)
# Make Directories
colourText('\n Creating the necessary directories if they don\'t already exist.\n', 'GREEN')
try:
     os.mkdir(mkdir_ads)
except:
    print('The %s Directory Already Exists! - Continuing On.' % mkdir_ads)
else:
    print('The %s Directory was successfully created.' % mkdir_ads)

try:
    os.mkdir(mkdir_iclock)
except:
    print('The %s Directory Already Exists! - Continuing On.' % mkdir_iclock)
else:
    print('The %s Directory was successfully created.' % mkdir_iclock)

try:
     os.mkdir(mkdir_ess)
except:
    print('The %s Directory Already Exists! - Continuing On.' % mkdir_ess)
else:
    print('The %s Directory was successfully created.' % mkdir_ess)

time.sleep(1)
# Copy AffinityDS to Programs(x86) folder
colourText('\n \t Copying necessary files to the AffinityDS folder.', 'GREEN')
for source_dir, dirs, file_names in os.walk(ads_source_dir):
    target_dir = source_dir.replace(ads_source_dir, ads_target_dir, 1)

    for file in file_names:
        source_file = os.path.join(source_dir, file)
        target_file = os.path.join(target_dir, file)
        if os.path.exists(target_file):
            # in case of the source and target are the same file
            if os.path.samefile(source_file, target_file):
                continue
            os.remove(target_file)
        shutil.copy2(source_file, target_dir)

colourText("\n \t AffinityDS was successfully copied to the (x86) TimeTrak Connect Folder.", "GREEN")

# Open & Close AffinityDS.exe
def start_stop_ads():
    os.startfile('C:\\Program Files (x86)\\TimeTrak Systems\\TimeTrakCONNECT\\AffinityDS\\TTC_AffinityDS.exe')
    time.sleep(2)
    colourText("\n \t Creating the AffinityDS folder + XML file in ProgramData.\n", "GREEN")
    os.chdir('C:\\ProgramData\\TimeTrak Systems\\TimeTrakCONNECT\\AffinityDS\\')
    colourText("\nClosing the AffinityDS Program.", "RED")
    # Checks if the XML file has been created before closing ADS if True ADS Closes if False it re-loops
    for _ in range(0, 5):
        count = 0
        if os.path.isfile('TTC_AffinityDS.xml'):
            os.system("TASKKILL /F /IM TTC_AffinityDS.exe")
            colourText('The AffinityDS Process has been successfully killed.', 'RED')
            break
        else:
            count += 1
            colourText('We cannot kill the AffinityDS Process until the XML is created.', 'RED')
            time.sleep(3)
start_stop_ads()

# Get Server IP and Hostname for user and display it.
def ipInformation():
    os.chdir('C:\\ProgramData\\TimeTrak Systems\\TimeTrakCONNECT\\AffinityDS\\')
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        colourText('\n This is your Computer\Server\'s Host Information:\nPlease Note: This only grabs the top Ethernet Adapter\n', 'GREEN')
        print('\tHostname: ', host_name)
        print('\tIP Address: ', host_ip)
    except:
        colourText('I was unable to obtain Hostname and IP Address for you.', 'RED')

    print('\n'
          '[1] - ', host_ip + '\n'
          '[2] -  Type in your own IP Address: \n')

    action = input('How would you like to add the Server IP Address? (Enter a Number): ')

    if action == '1':
        use_host_ip = host_ip
        # Opening / Parsing the XML File
        xml_file = md.parse('TTC_AffinityDS.xml')

        # modifying the loop back value
        xml_file.getElementsByTagName('ListenerAddress')[0].childNodes[0].nodeValue = use_host_ip + ':3427'

        # writing and saving changes to the xml file
        with open('TTC_AffinityDS.xml', 'w') as xml:
            xml.write(xml_file.toxml())
            xml.close()

    elif action == '2':
        own_host_ip = input('Enter The IP Address: ')
        # Opening / Parsing the XML File
        xml_file = md.parse('TTC_AffinityDS.xml')

        # modifying the loop back value
        xml_file.getElementsByTagName('ListenerAddress')[0].childNodes[0].nodeValue = own_host_ip + ':3427'

        # writing and saving changes to the xml file
        with open('TTC_AffinityDS.xml', 'w') as xml:
            xml.write(xml_file.toxml())
            xml.close()
    else:
        colourText('No valid number was chosen.', 'YELLOW')

ipInformation()
colourText('Modifying the XML File\n', 'RED')

# Create the AffinityDS Service in Windows Services
colourText("\n \t ....Creating the AffinityDS Windows Service....", "GREEN")
os.system('cmd /c "sc create TTC_AffinityDS binPath= "C:\Program Files (x86)\TimeTrak Systems\TimeTrakCONNECT\AffinityDS\TTC_AffinityDSsvc.exe" DisplayName="TimeTrak CONNECT AffinityDS" start=auto"')
time.sleep(1)
# Launch AffinityDS Application so Support can see if clocks are communicating
colourText("\n \t ....Launching the AffinityDS Application....", "GREEN")
os.startfile('C:\\Program Files (x86)\\TimeTrak Systems\\TimeTrakCONNECT\\AffinityDS\\TTC_AffinityDS.exe')
colourText("\n \t ....Good Luck Connecting The Clocks!....", "GREEN")
# END
colourText("\n \t \t TimeTrak AffinityDS has been setup. \n", "RED")

print("\n Made with ", Fore.RED + "<3", Style.RESET_ALL, "by Chuck Coggins \n")
input('Press ENTER to exit')