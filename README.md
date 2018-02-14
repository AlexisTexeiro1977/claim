# :bookmark_tabs: claim

<p>
    <a href="https://pypi.python.org/pypi/claim/1.0.0b1">
        <img src="https://img.shields.io/badge/v-1.0.0--beta-blue.svg" alt="version">
    </a>
    <a href="https://github.com/bukovyn/claim/blob/master/LICENSE.txt">
        <img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="MIT License">
    </a>
    <a href="https://github.com/bukovyn/claim/pulls">
        <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="pull-requests">
    </a>
</p>

A cli tool that converts file's [line endings](https://en.wikipedia.org/wiki/Newline>) between DOS and Unix-like systems.

### install
  ```pip install claim```

### overview
  ```
usage: claim [-h] [-dos] filename [filename ...]

positional arguments:
  filename    file to be converted

optional arguments:
  -h, --help  show this help message and exit
  -d, -dos        converts file to DOS line endings [\cr\n]
  ```

:grey_exclamation: *Note: The files being converted should use UTF-8 encoding, other encodings are currently not supported.*
