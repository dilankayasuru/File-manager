import os

root_path = "C:\\Users\\Dilanka\\Desktop\\Projects\\Documents"

file_paths = []

for root, directories, files in os.walk(root_path):
    for filename in files:
        file_path = os.path.join(root, filename)
        file_paths.append(file_path)

for files in file_paths:
    if os.path.splitext(files)[1][1:] == 'pptx':
        powerpointDir = os.path.join(root_path, "PowerPoint")
        try:
            os.makedirs(powerpointDir)
        except FileExistsError:
            pass
        newPath = os.path.join(powerpointDir, os.path.basename(files))
        os.replace(files, newPath)
    elif os.path.splitext(files)[1][1:] == 'jpeg' or os.path.splitext(files)[1][1:] == 'jpg':
        imageDir = os.path.join(root_path, "Images")
        try:
            os.makedirs(imageDir)
        except FileExistsError:
            pass  
        newPath = os.path.join(imageDir, os.path.basename(files))
        os.replace(files, newPath)
    elif os.path.splitext(files)[1][1:] == 'pdf':
        pdfDir = os.path.join(root_path, "PDF Docs")
        try:
            os.makedirs(pdfDir)
        except FileExistsError:
            pass
        newPath = os.path.join(pdfDir, os.path.basename(files))
        os.replace(files, newPath)
    elif os.path.splitext(files)[1][1:] == 'txt':
        txtDir = os.path.join(root_path, "Text Docs")
        try:
            os.makedirs(txtDir)
        except FileExistsError:
            pass
        newPath = os.path.join(txtDir, os.path.basename(files))
        os.replace(files, newPath)
    else:
        otherDir = os.path.join(root_path, "Other")
        try:
            os.makedirs(otherDir)
        except FileExistsError:
            pass
        newPath = os.path.join(otherDir, os.path.basename(files))
        os.replace(files, newPath)

print("Files mannaged!!!")