from zipfile import ZipFile
from zipfile import ZIP_STORED

class UaZipFile(ZipFile):
    ''' Extends standard ZipFile by adding the ability to set the route source directory.
        When the root source directory is set, the zipped file path will be truncated
        to after the root.
    '''

    def __init__(self, zip_file_path, root_dir=None, mode="r", compression=ZIP_STORED, allowZip64=True):
        
        super().__init__(file = zip_file_path, mode = mode, compression = compression, allowZip64 = allowZip64)    
        self.root_dir = root_dir
    
    def get_zipped_file_path(self, file_path):
        
        if self._root_dir_len > 0 and file_path is not None:
            file_path = file_path[self._root_dir_len:]
        # else
            # return as is.
            
        return file_path

    def has_file(self, zipped_file_path):

        try:
            info = super().getinfo (zipped_file_path)
        except:
            info = None
             
        return info is not None

    def has_not_file (self, zipped_file_path):
        
        return not self.has_file(zipped_file_path)

    @property
    def root_dir(self):
        
        return self._root_dir

    @root_dir.setter
    def root_dir(self, root_dir):
        
        self._root_dir = root_dir
        
        if root_dir is not None:
            self._root_dir_len = len(root_dir) + 1
        else:
            self._root_dir_len = 0
    
    def write(self, file_path, zipped_file_path = None, overwrite = False):
        
        if zipped_file_path is None:
            zipped_file_path = self.get_zipped_file_path(file_path)
    
        if overwrite or self.has_not_file(zipped_file_path):
            super().write (file_path, zipped_file_path)
        #else:
            # overwrite is not allowed and
            # the file exists.
