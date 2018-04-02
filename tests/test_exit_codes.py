import os
import exit_codes

import pytest


@pytest.fixture(params=[name[3:]
                        for name in dir(os)
                        if name.startswith('EX')])
def os_code_name(request):
    "All return code names (sans EX_) from `os`."
    return request.param


def test_ok():
    return exit_codes.ExitCode.OK


def test_usage():
    return exit_codes.ExitCode.USAGE


def test_has_same_attributes_as_os(os_code_name):
    assert os_code_name in exit_codes.ExitCode.__members__


def test_has_same_values_as_os(os_code_name):
    assert getattr(exit_codes.ExitCode, os_code_name) == getattr(os, 'EX_' + os_code_name)
