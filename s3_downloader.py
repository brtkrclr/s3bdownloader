import boto3
import pyfiglet
from colorama import Fore, Back, Style

#Banner 
banner = pyfiglet.figlet_format("S3B Downloader")
print(Fore.RED+banner+Style.RESET_ALL)

client = boto3.client(
    's3',
    aws_access_key_id= 'ACCESS KEY ID',
    aws_secret_access_key= 'ACCESS KEY'
)

print(Fore.YELLOW + "\nWelcome to Amazon S3 Backup Downloader.\nIn order to exit please type 3" +Style.RESET_ALL)

while True:

  cluster=int(input("\nPlease select a cluster:\nPOC2 ("+Fore.YELLOW+"type 1"+Style.RESET_ALL+")\nCUSTOMER2 ("+Fore.YELLOW+"type 2"+Style.RESET_ALL+")\nEXIT ("+Fore.YELLOW+"type 3"+Style.RESET_ALL+")\n"))
  if cluster == 1:
    print("Selected cluster is: "+Fore.GREEN+"POC2\n"+Style.RESET_ALL)
    FILE_NAME=input("Please enter the name of the backup file:\n")
    BUCKET_NAME='ENTER THE BUCKET NAME'
    OBJECT_NAME= 'ENTER THE OBJECT NAME'+FILE_NAME
    client.download_file(BUCKET_NAME, OBJECT_NAME, FILE_NAME)
    print(FILE_NAME+Fore.GREEN+" successfully downloaded!"+Style.RESET_ALL+"\n Bye!")
    break
  elif cluster == 2:
    print("Selected cluster is: "+Fore.GREEN+"CUSTOMER2\n"+Style.RESET_ALL)
    FILE_NAME=input("Please enter the name of the backup file:\n")
    BUCKET_NAME='ENTER THE BUCKET NAME'
    OBJECT_NAME= 'ENTER THE OBJECT NAME'+FILE_NAME
    client.download_file(BUCKET_NAME, OBJECT_NAME, FILE_NAME)
    print(FILE_NAME+Fore.GREEN+" successfully downloaded!"+Style.RESET_ALL+"Bye!")
    break
  elif cluster==3:
    print("Bye!")
    break
  else:
    print(Fore.RED+"Please enter a valid number"+Style.RESET_ALL)
