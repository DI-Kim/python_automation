import shutil
import os

os.path.join('folder1', 'folder2', 'file.txt')
# This will create a path that looks like 'folder1/folder2/file.txt' on Unix-like systems
# and 'folder1\folder2\file.txt' on Windows systems.
# It automatically uses the correct path separator for the operating system.

print(os.sep)

# This will return the current working directory of the process.
print(os.getcwd())

# Check if the path exists
print(os.path.exists('c:\\windows\\system32\\calc.exe'))

print(os.listdir('c:\\users\\daein\\documents'))

# Get the size of a file or folder
totalSize = 0
for filename in os.listdir('c:\\users\\daein\\documents\\python'):
    if not os.path.isfile(os.path.join('c:\\users\\daein\\documents\\python', filename)):
        totalSize += os.path.getsize(
            os.path.join('c:\\users\\daein\\documents\\python', filename))
print(totalSize)

# read mode
helloFile = open('c:\\users\\daein\\documents\\python\\hello.txt')
content = helloFile.read()
print(content)
helloFile.close()

# write mode
helloFile = open('c:\\users\\daein\\documents\\python\\hello.txt', 'w')
helloFile.write('Hello!!!!!\n')
helloFile.write('Hello!!!!!')
helloFile.close()

# append mode
helloFile = open('c:\\users\\daein\\documents\\python\\hello.txt', 'a')
helloFile.write('\nHello World\n')
helloFile.close()

if not os.path.exists('c:\\users\\daein\\documents\\python\\test'):
    os.mkdir('c:\\users\\daein\\documents\\python\\test')
    os.makedirs('c:\\users\\daein\\documents\\python\\test\\test2')
    spamFile = open('c:\\users\\daein\\documents\\python\\test\\spam.txt', 'w')
    spamFile.write('Hello World\n')
    spamFile.write('spamspam')
    spamFile.close()

# copy, move
shutil.copy('c:\\users\\daein\\documents\\python\\hello.txt',
            'c:\\users\\daein\\documents\\python\\test\\hello2.txt')
shutil.copytree('c:\\users\\daein\\documents\\python',
                'c:\\users\\daein\\documents\\pythonBackup')
shutil.move('c:\\users\\daein\\documents\\python\\test\\hello2.txt',
            'c:\\users\\daein\\documents\\pythonBackup\\hello3.txt')

# delete
os.remove('c:\\users\\daein\\documents\\pythonBackup\\test\\hello2.txt')
# os.rmdir('c:\\users\\daein\\documents\\python\\test')  # empty folder
# os.unlink('c:\\users\\daein\\documents\\pythonBackup\\hello2.txt')
# shutil.rmtree('c:\\users\\daein\\documents\\pythonBackup') # chmod 777

for folderName, subfolders, filenames in os.walk('c:\\users\\daein\\documents\\python\\test'):
    print('The folder is ' + folderName)
    print('The subfolders in ' + folderName + ' are: ' + str(subfolders))
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()
