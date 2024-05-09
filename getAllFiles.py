from msilib.schema import Directory
import os


class GetAllFiles():
    
    def __init__(self) -> None:
        self.files = []
        self.directory = []
        self.notKnown = []
    '''sourceFolder and subSource folder have same job is listing the names of the directory '''
    def sourceFolder(self):
        folder_p = input('drag or insert folder:')
        folder_p= folder_p.replace(" '", "")
        folder_p= folder_p.replace('"', "")
        
        folder_p= folder_p.replace("'", "")
        # folder_path= folder_p.replace("&", "")
        folder_path = folder_p
        path_list = os.listdir(folder_path)
        return folder_path, path_list

    def subSourceFolder(self, folder_p):
        folder_path = folder_p
        path_list = os.listdir(folder_path)
        return path_list, folder_path
    
    
    '''cheking if the dir is a folder or file and adding them to a list in __init__'''
    def fileOrDir(self,path_list, folder_path):
        for folder in path_list:
            filepath = folder_path+"/"+folder
            if os.path.isfile(filepath):
                self.files.append(filepath)
            elif os.path.isdir(filepath):
                self.directory.append(filepath)
            else :
                self.notKnown.append(filepath)
        ''' loopDir = looping in folders that is already in list and getting all folders name '''
    def loopDir(self):
        
        ''' the while loop will delete the directory from the array after processing it.
            loop will end if len(directory) == 0                                        
                                                                                        '''
        while len(self.directory)!= 0:
            for dir in self.directory:
                print(str(self.directory)+'\n')
                path_list, folder_path = self.subSourceFolder(dir)
                self.fileOrDir(path_list, folder_path)
                self.directory.remove(dir)
        for file in self.files:
            print(file)
        print('length of files = {}, length of directories = {}, length of not known = {}'.format(
            len(self.files), len(self.directory), len(self.notKnown)))

if __name__ == '__main__':
    '''path list = all files and dir in a path, folder path = the sorce path'''
    GetAllFiles = GetAllFiles()
    folder_path, path_list = GetAllFiles.sourceFolder()
    GetAllFiles.fileOrDir(path_list=path_list,folder_path=folder_path)
    GetAllFiles.loopDir()