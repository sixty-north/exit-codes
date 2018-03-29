|Python version| |Build Status|

============
 exit_codes
============

Platform-independent exit codes.

Python provides standard exit status codes for some platforms, but not all. This
is technically, pedantically correct, but it makes it awkward to provide
practical cross-platform exit statuses. This package takes the exit status codes
defined in ``os`` for Unixes and make them available to the unwashed masses.

It's simple to use:

.. code-block:: python

  from exit_codes import ExitCode

  def main():
      if big_operation():
          # If your program exits normally, return OK
          return ExitCode.OK
      else:
          # Otherwise, return the appropriate error code
          return ExitCode.IO_ERR

.. |Python version| image:: https://img.shields.io/badge/Python_version-2.6+-blue.svg
   :target: https://www.python.org/
.. |Build Status| image:: https://travis-ci.org/sixty-north/exit-codes.png?branch=master
   :target: https://travis-ci.org/sixty-north/exit-codes
