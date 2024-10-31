"""Setup script for packagename."""

import setuptools
import numpy as np


extensions = [
    setuptools.Extension(
        "packagename._extname",
        sources=["packagename/_extname.pyx", "src/extname.c"],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
        include_dirs=["src", np.get_include()],
    )
]
setuptools.setup(ext_modules=extensions)
