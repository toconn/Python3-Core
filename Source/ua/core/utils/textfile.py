from .isfirst import IsFirst

class TextFile:
    
    def __init__(self, file_path):
        
        self.file_path = file_path
        
    def read(self):
        
        with open(self.file_path, 'r') as file_handle:
            content_text = file_handle.read()

        return content_text
        
    def read_lines(self):
        
        content_text = self.read()
        content_lines = content_text.split('\n')
        
        return content_lines
        
    def write_lines(self, content_lines):
        
        with open(self.file_path, 'w') as file_handle:
            
            first = IsFirst()
            
            for line in content_lines:
                if first.is_first():
                    file_handle.write('%s' % line)
                else:
                    file_handle.write('\n%s' % line)

