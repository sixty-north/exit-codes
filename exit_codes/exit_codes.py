"""Exit status codes.

These mimic those on many unixes (and provided by `os`) but make them
available on all platforms.
"""

# successful termination
OK = 0

# command line usage error
USAGE = 64

# data format error
DATA_ERR = 65

# cannot open input
NO_INPUT = 66

# addressee unknown
NO_USER = 67

# host name unknown
NO_HOST = 68

# service unavailable
UNAVAILABLE = 69

# internal software error
SOFTWARE = 70

# system error (e.g., can't fork)
OS_ERR = 71

# critical OS file missing
OS_FILE = 72

# can't create (user) output file
CANT_CREATE = 73

# input/output error
IO_ERR = 74

# temp failure; user is invited to retry
TEMP_FAIL = 75

# remote error in protocol
PROTOCOL = 76

# permission denied
NO_PERM = 77

# configuration error
CONFIG = 78
