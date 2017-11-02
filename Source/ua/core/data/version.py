from ua.core.utils import listutils

class Version(object):

    def __init__ (self, *args):
        
        self._reset()
        
        args_count = listutils.count(args)

        if args_count == 1:

            self.version_string = args[0]
            
        elif args_count == 3:
            self.major = args[0]
            self.minor = args[1]
            self.revision = args[2]

    def __repr__(self):
        
        return self.version_string()

    def incr_major(self):
        
        self.major += 1
        self.minor = 0
        self.revision = 0
       
    def incr_minor(self):
        
        self.minor += 1
        self.revision = 0
       
    def incr_revision(self):
        
        self.revision += 1
       
    @property
    def version_string(self):
        
        return str(self.major) + '.' + str(self.minor) + '.' + str(self.revision)
    
    @version_string.setter
    def version_string (self, value):
              
        self._reset()
        
        if value is not None:
            
            ver_nums = value.split('.')
            ver_num_count = len(ver_nums)
            
            if ver_num_count >= 1:
                self.major = int(ver_nums[0])
                
            if ver_num_count >= 2:
                self.minor = int(ver_nums[1])
                
            if ver_num_count >= 3:
                self.revision = int(ver_nums[2])
    
    def _reset(self):
        
        self.major = 0
        self.minor = 0
        self.revision = 0

        

