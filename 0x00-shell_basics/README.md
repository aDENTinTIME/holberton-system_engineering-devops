# Holberton System-Engineering Devops / 0x00-shell_basics

0. Where am I? [0-current_working_directory](https://github.com/aDENTinTIME/holberton-system_engineering-devops/blob/master/0x00-shell_basics/0-current_working_directory)  
   Write a script that prints the absolute path name of the current working directory.
```bash
#!/bin/bash
pwd
```
---
1. What’s in there? [1-listit](https://github.com/aDENTinTIME/holberton-system_engineering-devops/blob/master/0x00-shell_basics/1-listit)  
   Display the contents list of your current directory.
```bash
#!/bin/bash
ls
```
---
2. There is no place like home [2-bring_me_home](https://github.com/aDENTinTIME/holberton-system_engineering-devops/blob/master/0x00-shell_basics/2-bring_me_home)  
   Write a script that changes the working directory to the user’s home directory.
```bash
#!/bin/bash
cd
```
---
3. The long format [3-listfiles](https://github.com/aDENTinTIME/holberton-system_engineering-devops/blob/master/0x00-shell_basics/3-listfiles)  
   Display current directory contents in a long format
```bash
#!/bin/bash
ls -l
```

4. Hidden files [4-listmorefiles](https://github.com/aDENTinTIME/holberton-system_engineering-devops/blob/master/0x00-shell_basics/4-listmorefiles)  
   Display current directory contents, including hidden files (starting with .). Use the long format.
```bash
#!/bin/bash
ls -la
```
---
5. I love numbers [5-listfilesdigitonly](https://github.com/aDENTinTIME/holberton-system_engineering-devops/blob/master/0x00-shell_basics/5-listfilesdigitonly)  
   Display current directory contents.  
   • Long format  
   • with user and group IDs displayed numerically  
   • And hidden files (starting with .)
```bash
#!/bin/bash
ls -lan
```
---
6. Welcome holberton [6-firstdirectory](https://github.com/aDENTinTIME/holberton-system_engineering-devops/blob/master/0x00-shell_basics/6-firstdirectory)

   Create a script that creates a directory named `holberton` in the `/tmp/` directory.
```bash
#!/bin/bash
mkdir /tmp/holberton/
```

7. Betty in Holberton [7-movethatfile](https://github.com/aDENTinTIME/holberton-system_engineering-devops/blob/master/0x00-shell_basics/7-movethatfile)

   Move the file `betty` from `/tmp/` to `/tmp/holberton`.
```bash
#!/bin/bash
mv /tmp/betty /tmp/holberton/
```

8. Bye bye Betty [8-firstdelete](https://github.com/aDENTinTIME/holberton-system_engineering-devops/blob/master/0x00-shell_basics/8-firstdelete)

   Delete the file betty.
   
   • The file `betty` is in `/tmp/holberton`
```bash
#!/bin/bash
rm /tmp/holberton/betty
```

9. Bye bye Holberton [9-firstdirdeletion](https://github.com/aDENTinTIME/holberton-system_engineering-devops/blob/master/0x00-shell_basics/9-firstdirdeletion)

   Delete the directory `holberton` that is in the `/tmp` directory.
```bash
#!/bin/bash
rmdir /tmp/holberton/
```

XXXXXXXX []()

   XXXXXXXXXX
```bash
#!/bin/bash

```

•••
