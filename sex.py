import platform
bit = platform.architecture()[0]
if bit == '64bit':
    import sex64_enc 
