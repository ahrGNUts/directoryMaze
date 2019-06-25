# directoryMaze
A Python script that will hide a specified file or folder in a maze of folders and bogus documents.

I tried to manually make one of these when I was a kid and gave up after the first few layers.
Fortunately, computers are much faster and more tenacious than 9 year old me.

## V<=1 Functionality
* Generate a directory tree with n layers and b branches in each layer
* Move specified file or folder to a randomly selected endpoint at the bottom of the tree.
Payload is moved verbatim without being renamed
* Create a "map file" for the user to navigate back to their file

## Planned Features
* Generate bogus binary or text files at various in the tree to further hide the file
(endpoints[!] and intermediate directories[?])
    * OR have endpoint nodes soft or hard link back to root node
* GUI/Terminal versions
    * GUI: startup prompts will be handled with file selection windows and other nice UX stuff 
    using QT, Tkinter, or another framework
    * Terminal: basically just the current version (for those who like typing paths)
* [Terminal] - tab autocomplete paths during opening prompts
* Script will allow user to find their file for them if they lose track of their map file (finder mode)
* Encryption/decryption for payload files and directories
* Cross-platform compatibility (right now has only been tested in a Unix-like env)
* Directory password protection
* Java port? Maybe at least a visualization of the node tree using Processing
* Maybe more as I think of it

## A Note
This probably won't stop a more advanced computer user from finding your files, but it might stop
a less experienced layperson. It might even stop you from finding your files, so **use caution** when using this.