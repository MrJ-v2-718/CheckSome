class Results:
    def __init__(self):
        self.dev_checksum = ""
        self.filename = ""
        self.algorithm = ""
        self.checksum = ""
        self.match = ""

    def set_dev_checksum(self, dev_checksum):
        self.dev_checksum = dev_checksum

    def set_filename(self, filename):
        self.filename = filename

    def set_algorithm(self, algorithm):
        self.algorithm = algorithm

    def set_checksum(self, checksum):
        self.checksum = checksum

    def set_match(self, match):
        self.match = match

    def save(self):
        filename = "CheckSome Results.txt"
        with open(filename, "a") as outfile:
            outfile.write(f"         Filename: {self.filename}\n")
            outfile.write(f"        Algorithm: {self.algorithm}\n")
            outfile.write(f"Provided checksum: {self.dev_checksum}\n")
            outfile.write(f"  Actual checksum: {self.checksum}\n")
            outfile.write(f"            Match: {self.match}\n\n")
