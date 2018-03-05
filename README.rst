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

  import exit_codes

  def main():
      if big_operation():
          # If your program exits normally, return OK
          return exit_codes.OK
      else:
          # Otherwise, return the appropriate error code
          return exit_codes.IO_ERR
