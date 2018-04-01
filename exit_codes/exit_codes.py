try:
    from enum import IntEnum as Base
except ImportError:
    Base = object


class ExitCode(Base):
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


    # Aliases which have the same name as those in the standard
    # library os module, without the leading EX_. These are to
    # allow for easier porting as EX_FOO may be globally replaced
    # with ExitCode.FOO.  For new code, prefer the easier to read
    # names above.

    DATAERR = 65
    NOINPUT = 66
    NOUSER = 67
    NOHOST = 68
    OSERR = 71
    OSFILE = 72
    CANTCREAT = 73
    IOERR = 74
    TEMPFAIL = 75
    NOPERM = 77
