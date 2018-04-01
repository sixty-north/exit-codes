try:
    from enum import IntEnum as Base
except ImportError:
    Base = object


class ExitCode(Base):
    """Exit status codes.

    These mimic those on many unixes (and provided by `os`) but make them
    available on all platforms.

        OK           Successful termination
        USAGE        Command-line usage error
        DATA_ERR     Invalid data
        NO_INPUT     No input provided
        NO_USER      User unknown
        NO_HOST      Hostname unknown
        UNAVAILABLE  Service unavailable
        SOFTWARE     Internal software error
        OS_ERR       System error (e.g., can't fork)
        OS_FILE      File missing
        CANT_CREATE  Can't create (user) output file
        IO_ERR       Input/output error
        TEMP_FAIL    A temporary failure; the user is invited to retry
        PROTOCOL     A protocol error
        NO_PERM      Permission denied
        CONFIG       Configuration error

    """

    """Successful termination"""
    OK = 0

    """Command-line usage error"""
    USAGE = 64

    """Invalid data"""
    DATA_ERR = 65

    """No input provided"""
    NO_INPUT = 66

    """User unknown"""
    NO_USER = 67

    """Hostname unknown"""
    NO_HOST = 68

    """Service unavailable"""
    UNAVAILABLE = 69

    """Internal software error"""
    SOFTWARE = 70

    """System error (e.g., can't fork)"""
    OS_ERR = 71

    """File missing"""
    OS_FILE = 72

    """Can't create (user) output file"""
    CANT_CREATE = 73

    """Input/output error"""
    IO_ERR = 74

    """A temporary failure; the user is invited to retry"""
    TEMP_FAIL = 75

    """A protocol error"""
    PROTOCOL = 76

    """Permission denied"""
    NO_PERM = 77

    """Configuration error"""
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
