# File-Splitter-and-Merger
Splitter splits the attached file into 2 equal parts. The splitted parts can be splitted again.  
Merger merges the splitted files in the current directory back together into a single file and removes the splitted files.   

Generally used to reduce the size of big files.

## How To Use
Splitting:  
- (Optional, Recommended) Compress the file(s) or the folder(s) into a zip file (or any other compressed file) (this helps reducing the overall size and can be used to turn a folder or multiple files into a single file)  
- Run the Splitter while the file you would like to split attached (can be easily done by dragging and dropping the file onto the .exe or .py files), or you can run the program without attaching a file and typing the file name when prompted.
This will create the splitted files with a prefix in their names (splitted binary files might seem corrupted, this is normal).  
- (Optional) Repeat the last step with the splitted files with the prefix to achieve smaller files. (You can remove each main file after you split them. Or they will be remved once merged anyway.)

Merging:  
- Have all the splitted files with the prefix inside the same directory as the Merger and run the Merger.  
This will merge all the splitted files back into the ultimate main file and get rid of all the splitted files.  
Note: Merger does not open any windows or a console when working.
