*****
:bookmark_tabs: claim
*****

.. figure:: img/claim.gif
   :alt: Usage example.

A cli tool that converts file's `line endings
<https://en.wikipedia.org/wiki/Newline>`_ between DOS and Unix-like systems.

install:
  :code:`pip install claim`

usage:
  :code:`claim [-h] [-dos] filename [filename ...]`

positional arguments:
  :code:`filename`   the file to be converted

optional arguments:
  -h, --help  prompts help message
  -d, -dos    converts file to DOS line endings [\cr\n]

*Note: The files being converted should use UTF-8 encoding, other encodings are currently not supported.*
