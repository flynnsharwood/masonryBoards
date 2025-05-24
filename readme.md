# masonryBoard

## what this does

it takes directories filled with pics and sub directories filled with pics, and converts it into html files linking to those images. 
The images are arranged in a masonry format (looks like pinterest).
Click on the image to copy the image path.
You can change the number of columns shown.


## how to 

input your masterDir in the config.yml, the dir in which you want to store the created html files. 

Then create a csv file in the fileLists Folder.
Fill the first column with the absolute path of the directory with the images, and fill the second one with the name you want to give the directory in the created folders. 

You can change the csv filenames as you wish, add more or remove existing.

use --csvs flag to provide a list of csv files. If this isn't used, it will fallback to the directories mentioned in the config.yml.

That should be it. 


## Future to-dos

- [ ] make it so that it can push to a github pages site.
- [ ] Make the bash file better, make the bash file do the above task.
- [x] Clean the code, organise it and put it on github
- [x] Fix nested folders not being links issue.
- [x] Get the list of target and destination folders from a csv file or a txt file.
- [ ] hide image option
- [ ] Long press to open image in new tab
- [ ] start image option
- [ ] Bookmark location so that we can come to that part later
- [ ] Randomise button. Randomisation should be temporary, only till the tab is open. 
- [ ] sort by option
- [ ] add an option to copy a list of images to clipboard