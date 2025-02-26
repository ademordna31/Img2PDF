import img2pdf , os
from collections import defaultdict
import time, datetime

# path to the tiffs
# should include the full path, for example '\\svm_dlib\Projects\DEP\Cuba\ihc_lalucha\1928\tiff'
image_directory = input('Enter Path to TIFFs: ')
pdf_directory = input('Enter Path to PDFs: ')

dictTemp = defaultdict(list)
for root, dirs, files in os.walk(image_directory):
    for file in files:
        if file.endswith(".tif"):
            split_names = file.split("_")
            file_key = "_".join((split_names[0],split_names[1],split_names[2]))
            if file_key in dictTemp:
                dictTemp[file_key].append(os.path.join(root,file))
            else:
                dictTemp[file_key].append(os.path.join(root,file))

            print("Discovered this TIF:",os.path.join(root, file))

file_keys = dictTemp.keys()

print("Start time: " + time.strftime('%a %H:%M:%S'))
t1 = time.time()

if file_keys:
    for key in file_keys:
        output_file = key + ".pdf" # The output file name
        print("putting all tifs into ", output_file)
        with open((pdf_directory) + '\{}'.format(output_file), 'wb') as f:
            filelist = dictTemp[key]
            filelist.sort();
            #print("List: ",filelist)
            img2pdf.convert(filelist, outputstream=f)
            print(time.strftime('%a %H:%M:%S'))

else:
    print("Couldnt find any tiffs")

print("End time: " + time.strftime('%a %H:%M:%S'))
t2 = time.time()

delta = t2-t1

print("Total time to complete this operation: " + str(datetime.timedelta(seconds=delta)))

#pdf_bytes = img2pdf.convert([r'C:\Users\parinita ghorpade\Downloads\israeliposters\uclalsc_2147_b1_f01_01.tif'])

#file = open("name.pdf","wb")
#file.write(pdf_bytes)
