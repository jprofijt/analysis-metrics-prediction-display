class Files(object):
    u"""
    Class that contains input and output file locations
    """
    def __init__(self, input, output):
        self.input = input
        self.output = output

    def getInput(self):
        u"""
        gets input file location

        :returns: input file path
        :rtype: str
        """
        return self.input
    
    def getOutput(self):
        u"""
        gets output file location

        :returns: output file path
        :rtype: str
        """
        return self.output
