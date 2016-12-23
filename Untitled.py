
   try:
      response = urllib2.urlopen('https://raw.githubusercontent.com/ZZcat/Update-numbers/master/1')
      html = response.read()
      web_vesion = html[:5]
      f = open('version.txt', 'r')
      vesion = f.read()
      print "Your vesion is ",vesion,"\nThe newest vesion is ", web_vesion
      if vesion == web_vesion:
         print "You have the newest vesion!"
      else:
         print "###You need to update this program"
         print "###Updating..."
         print "\n###Reading lines"
         folder_dir = os.popen("pwd").readlines()
         print "###Done!!!"
         print "\n###Cuting varuibal"
         folder_dir = folder_dir[:-10]
         print "###Done!!!\n\n###Cloning dicrectory"
         com = "git clone https://github.com/ZZcat/C-code.git"
         os.system(com)
         print "###Done\n\n###Moving directory"
         com = "mv C-code " , folder_dir
         print "###Done!!!"
         print "\n###Removing copy folder"
         com = "rm C-code"
         print "###Done!!!"
   except:
         print "###You need to update this program"
         print "###Updating..."
         print "\n###Reading lines"
         folder_dir = os.popen("pwd").readlines()
         print "###Done!!!"
         print "\n###Cuting varuibal"
         folder_dir = folder_dir[:-10]
         print "###Done!!!\n\n###Cloning dicrectory"
         com = "git clone https://github.com/ZZcat/C-code.git"
         os.system(com)
         print "###Done\n\n###Moving directory"
         com = "mv C-code " , folder_dir
         print "###Done!!!"
         print "\n###Removing copy folder"
         com = "rm C-code"
         print "###Done!!!"
