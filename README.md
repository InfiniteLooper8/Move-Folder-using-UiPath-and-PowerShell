# Move-Folder-using-UiPath-and-PowerShell

## Project Overview
This project automates the process of checking folder size, zipping, and moving folders using UiPath workflows and PowerShell scripts. It includes both a **Flowchart-based UiPath workflow** and a **Sequence-based UiPath workflow** that invokes Python files for size checking. 

The `GeneratedFiles` folder contains example files and scripts used to create a folder with random data and a Python script that retrieves folder sizes (used in the Sequence-based workflow).

## Project Structure
- **File_Size_Check_Using_PowerShell_Flowchart/**: Flowchart-based UiPath workflow.
- **File_Size_Check_Using_PowerShell_Python/**: Python scripts for file size check.
- **GeneratedFiles/**: Example files and generated random data.
  - **Files/**: Random test files for file size check.
  - **Scripts/**: PowerShell and Python scripts.
    
---

## Workflow Descriptions
1. **Flowchart-based UiPath Workflow**:
- This workflow uses a visual flowchart to check the folder size and invoke PowerShell scripts to automate the folder zipping and moving process.
2. **Sequence-based UiPath Workflow**:
- This workflow is structured as a sequence and utilizes a Python script for calculating folder size before proceeding with the rest of the automation steps.

---

## How to Use
### Running the Flowchart-based Workflow
1. Open the File_Size_Check_Using_PowerShell_Flowchart in UiPath Studio.
2. Create a "C:\Temp\Removedata" folder (or edit newLocation settings)
3. Set up "GeneratedFiles" folder in you C drive (or edit settings in UiPath to your chosen location path).
4. Run the workflow, and it will automatically check the folder size, zip it if needed, and move the folder.

### Running the Sequence-based Workflow with Python Script
1. Open the File_Size_Check_Using_PowerShell_Python in UiPath Studio.
2. Ensure the Python script (folder_size.py) is set up correctly.
3. Create a "C:\Temp\Removedata" folder (or edit newLocation settings)
4. Set up "GeneratedFiles" folder in you C drive (or edit settings in UiPath to your chosen location path).
5. Run the workflow, and it will calculate the folder size using Python and proceed with folder operations.

## Generated Files
- **Files** - used to store randomly generated files to further use in process;
- **Scripts**:
   - **create_files** = run this script to generate random files for Files folder
   - **folder_size**  = this scrip is used in Sequence-based process to calculate size of folder

## Requirements
- **UiPath Studio** (for running workflows)
- **PowerShell(5.1)** (for folder operations)
  
