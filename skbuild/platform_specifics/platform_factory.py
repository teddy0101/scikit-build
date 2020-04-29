"""This modules implements the logic allowing to instantiate the expected
:class:`.abstract.CMakePlatform`."""

import platform
import sys

from . import bsd
from . import cygwin
from . import linux
from . import osx
from . import windows


def get_platform():
    """Return an instance of :class:`.abstract.CMakePlatform` corresponding
    to the current platform."""
    this_platform = platform.system().lower()

    if this_platform == "windows":
        return windows.WindowsPlatform()
    elif sys.platform == "cygwin":
        return cygwin.CygwinPlatform()
    elif this_platform == "linux":
        return linux.LinuxPlatform()
    elif this_platform == "freebsd":
        return bsd.BSDPlatform()
    elif this_platform == "darwin":
        return osx.OSXPlatform()
    elif this_platform == "os400":
        return bsd.BSDPlatform()
    else:
        raise RuntimeError("Unsupported platform: {:s}. Please contact "
                           "the scikit-build team.".format(this_platform))
