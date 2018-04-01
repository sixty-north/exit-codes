# There's not much to test. Verifying the the module imports cleanly is
# pretty good. That plus accessing a few attributes will verify that it's
# cross-platform.

import os
import exit_codes


def test_ok():
    return exit_codes.ExitCode.OK


def test_usage():
    return exit_codes.ExitCode.USAGE


def test_has_same_attributes_as_os():
    os_exit_codes_names = (name[3:] for name in dir(os) if name.startswith('EX'))
    for name in os_exit_codes_names:
        assert name in exit_codes.ExitCode.__members__


def test_has_same_values_as_os():
    os_exit_codes_names = (name[3:] for name in dir(os) if name.startswith('EX'))
    for name in os_exit_codes_names:
        assert getattr(exit_codes.ExitCode, name) == getattr(os, 'EX_' + name)
