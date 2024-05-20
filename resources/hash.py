import hashlib


def hashfile(filename, algorithm):
    filename = filename
    algorithm = algorithm

    # How much data to read at a time in bytes. 65536 bytes = 64 kilobytes
    BUFFER_SIZE = 65536

    # Initialize hashing algorithms ("md5", "sha1", "sha224", "sha256", "sha384", "sha512")
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha224 = hashlib.sha224()
    sha256 = hashlib.sha256()
    sha384 = hashlib.sha384()
    sha512 = hashlib.sha512()

    # Open the file as the 1st commandline argument
    with open(filename, 'rb') as f:
        while True:
            # reading data = BUFFER_SIZE from the file and saving it in a variable
            data = f.read(BUFFER_SIZE)

            # True if eof = 1
            if not data:
                break

            # Passing data to hash function and updating function with data
            if algorithm == "md5":
                md5.update(data)
            elif algorithm == "sha1":
                sha1.update(data)
            elif algorithm == "sha224":
                sha224.update(data)
            elif algorithm == "sha256":
                sha256.update(data)
            elif algorithm == "sha384":
                sha384.update(data)
            elif algorithm == "sha512":
                sha512.update(data)
            else:
                print("Not a valid algorithm")

    if algorithm == "md5":
        return md5.hexdigest()
    elif algorithm == "sha1":
        return sha1.hexdigest()
    elif algorithm == "sha224":
        return sha224.hexdigest()
    elif algorithm == "sha256":
        return sha256.hexdigest()
    elif algorithm == "sha384":
        return sha384.hexdigest()
    elif algorithm == "sha512":
        return sha512.hexdigest()
    else:
        print("Not a valid algorithm")
