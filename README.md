## Img2PDF

**UPDATE 8 July 2019**

Python script to create PDFs from TIFFs for UCLA IDEP newpapers.

Instructions for DL student workstations:

_Note: You will need to create a virtual Python (Anaconda) environment as there is currently an issue with the latest version of the Pillow library (https://github.com/python-pillow/Pillow/issues/1888) as well as an older version of Img2PDF. These steps will need to be executed only the first time you use Anaconda on any new workstation._

0. Open the Anaconda prompt.

1. Determine the latest version of Python on your machine:
conda search "^python$"

2. Create a new Anaconda environment, called img2pdf, with the latest version of Python (the largest/last number from the above list):
conda create --name img2pdf python=3.7.3

3. Enter into the new Anaconda environment created in the previous step. The environment indicator to the left of the directory should change from (base) to (img2pdf):
conda activate img2pdf

4. Install the specific library versions of pillow and img2pdf that work for the conversion process:
pip install Pillow==5.1.0 img2pdf==0.3.1

_At this point, Anaconda is set to run the PdfFromImages.py script. The following instructions assume the above steps are completed._

0. Open the Anaconda prompt. Ensure that you are using the correct virtual environment:
conda activate img2pdf

1. Download the script and extract it on your pc. Navigate to the extracted folder (replace this directory with your folder loaction):
cd Downloads\Img2PDF-master

2. Run the script:
python PdfFromImages.py

3. The script will ask for the path to the TIFFs, - go back to the File Explorer and drag the TIFFs folder onto the Anaconda Prompt to copy the path. It should look something like `\\svm_dlib\Projects\...` - hit Enter

4. The script will now ask for the path where the PDFs should go - drag the PDFs folder onto the Anaconda Prompt to copy the path - hit Enter

5. The Anaconda Prompt terminal will start listing the TIFF files the script found and give you feedback as it creates each PDF. The process takes a while; check the progress periodically to make sure there are no errors.
