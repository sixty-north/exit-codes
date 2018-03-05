# There's not much to test. Verifying the the module imports cleanly is
# pretty good. That plus accessing a few attributes will verify that it's
# cross-platform.

import exit_codes


def test_ok():
    exit_codes.OK


def test_usage():
    exit_codes.USAGE
