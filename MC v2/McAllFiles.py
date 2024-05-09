'''
fix the printing it print each file twice
'''

import os


def allFiles(source_folder: str):
    '''
    returens all files path and files name
    '''
    file_names = []
    files = []

    file_id = []
    directory = []
    notKnown = []
    def loopDir(source_folder):
        ''' the while loop will delete the directory from the array after processing it.
            loop will end if len(directory) == 0                                        
                                                                                        '''
        folder_path, path_listdir =  sourceFolder(source_folder)
        fileOrDir(path_listdir, folder_path)
        while len(directory)!= 0:
            for dir in directory:
                print(str(directory)+'\n')
                path_listdir, folder_path = subSourceFolder(dir)
                fileOrDir(path_listdir, folder_path)
                directory.remove(dir)
        print("\nfiles name:")
        for file in file_names:
            print(file)
        print('length of files = {}, length of directories = {}, length of not known = {}'.format(
            len(files), len(directory), len(notKnown)))

    def fileOrDir(path_list, folder_path):
        for folder in path_list:
            filepath = folder_path+"/"+folder
            if os.path.isfile(filepath):
                files.append(filepath)
                file_id_name = filepath.split("Test{}".format(chr(92)))
                print(file_id_name)
                file_names.append(folder)
                file_id.append(file_id_name)
            elif os.path.isdir(filepath):
                directory.append(filepath)
            else :
                notKnown.append(filepath)
    
    def subSourceFolder(dir):
        folder_path = dir
        path_listdir = os.listdir(folder_path)
        return path_listdir, folder_path
    
    def sourceFolder(source_folder):
        folder_p = source_folder
        folder_p= folder_p.replace(" '", "")
        folder_p= folder_p.replace('"', "")
        folder_p= folder_p.replace("'", "")
        folder_p= folder_p.replace("&", "")
        folder_path = folder_p
        path_listdir = os.listdir(folder_path)
        return folder_path, path_listdir
    loopDir(source_folder)
    return files, file_names