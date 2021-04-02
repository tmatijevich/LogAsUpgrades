# File: LogAsUpgrades.py
# Author: Tyler Matijevich
# Created: 2020-03-06
# Description: List all installed upgrades for each version of Automation Studio

# Get time functions
from time import localtime, strftime

# Binary mode disables the conversion of line endings
logFile = open("AsUpgradesLog_" + strftime("%Y-%m-%d_%H.%M.%S", localtime()) + ".txt", "w")

# Write header
logFile.write("=" * 80 + "\n")
logFile.write("List of installed upgrades for each version of Automation Studio\n")
logFile.write("Time generated: " + strftime("%Y-%m-%d %H:%M:%S", localtime()) + "\n")
logFile.write("Created by: Tyler Matijevich (2020-03-06)\n")
logFile.write("=" * 80 + "\n")
logFile.write("\n")

# Begin file operations

# Copy over all upgrade files to a temporary location
import os
tempDir = ".\\Temp\\AsUpgrades"
os.system("md " + tempDir)
# For development only
# os.system("del /q ")
# os.system("rmdir .\\Temp\\AsUpgrades")

# Create a list of file names
fileNames = []
fileNames.append("ASAR-UpgradeIndex.xml")

# Copy over the AS version independent upgrades index file
os.system("echo AR && copy %homedrive%\\BrAutomation\\AS\\Upgrades\\UpgradeIndex.xml  .\\Temp\\AsUpgrades\\" + fileNames[0]) # > nul

# Copy over AS version dependent upgrades index files
for i in range(1,12+1):
    sourceFile = "%homedrive%\\BrAutomation\\AS4" + str(i) + "\\Upgrades\\UpgradeIndex.xml"
    fileName = "AS4" + str(i) + "-UpgradeIndex.xml"
    fileNames.append(fileName)
    os.system("echo AS4." + str(i) + "&& copy " + sourceFile + " " + tempDir + "\\" + fileName)

# Create tables listing upgrades
columnWidths = [8, 24, 12, 12, 36, 24]
headers = ["Type", "Name", "Version", "AS Version", "File", "Date Installed"]
headerMatches = ["Type", "Name", "Version", "AsVersion", "FileName", "InstalledAt"]
import xml.etree.ElementTree as ET

for CurrentFile in fileNames:
    if not os.path.isfile(tempDir + "\\" + CurrentFile): continue
    
    # Get xml element tree root
    tree = ET.parse(tempDir + "\\" + CurrentFile)
    root = tree.getroot()
    
    # Create the section header
    sectionHeader = "=" * 80 + "\n"
    if CurrentFile == fileNames[0]:
        sectionHeader += "B&R Automation Runtime Upgrades\n"
    else:
        sectionHeader += "B&R Automation Studio 4." + CurrentFile[3] + " Upgrades\n"
    sectionHeader += "=" * 80 + "\n\n"
    logFile.write(sectionHeader)
    
    # Create the first two rows of the table
    row1 = ""
    row2 = ""
    for i in range(len(headers)):
        row1 += headers[i].ljust(columnWidths[i])
        row2 += "-" * columnWidths[i]
        if i < (len(headers) - 1): 
            row1 += "|"
            row2 += "+"
    logFile.write(row1 + "\n" + row2 + "\n")
    
    # Loop through all elements in the root
    for i in range(len(list(root))):
        matchIndex = 0
        childIndex = 0
        loopCount = 0
        row = ""
        # Loop through all children of each element
        while matchIndex < len(headerMatches):
            # Check each child against each match (in order)
            if root[i][childIndex].tag == headerMatches[matchIndex]:
                # Reformat the date installed entry
                if headerMatches[matchIndex] == "InstalledAt":
                    row += root[i][childIndex].text[:10] + " at " + root[i][childIndex].text[-8:]
                else:
                    row += root[i][childIndex].text.ljust(columnWidths[matchIndex])
                if matchIndex < (len(headerMatches) - 1): row += "|"
                # Next header, reset the child index
                childIndex = 0
                matchIndex += 1
            elif childIndex < (len(list(root[i])) - 1):
                childIndex += 1
            else:
                break
        logFile.write(row + "\n")
    
    # Create space between tables
    logFile.write("\n\n\n")

# Remove the temporary files and directory
os.system("del /q " + tempDir + "\\*")
os.system("rmdir " + tempDir)
os.system("rmdir .\\Temp")

# Close the log file
logFile.close()
