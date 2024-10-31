==============
${packagename}
==============

.. badges

|PyPI Status| |GHA Status| |Documentation Status|

.. |PyPI Status| image:: https://img.shields.io/pypi/v/${packagename}.svg
    :target: https://pypi.org/project/${packagename}
    :alt: PyPI Status
.. |GHA Status| image:: https://github.com/${organization}/${packagename}/actions/workflows/ci.yml/badge.svg
    :target: https://github.com/${organization}/${packagename}/actions
    :alt: GitHub Actions Status
.. |Documentation Status| image:: https://readthedocs.org/projects/${packagename}/badge/?version=latest
    :target: https://${packagename}.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. description

Long description


Download
--------

The ``${packagename}`` source code can be downloaded from the Git_
repository on GitHub_: https://github.com/${organization}/${packagename}.


.. _Git: https://git-scm.com
.. _GitHub: https://github.com


Installation
------------

The pip_ tool can be used to install the package::

  $ python3 -m pip install ${packagename}


.. _Pip: https://pip.pypa.io


Testing
-------

stbx includes a quite complete test suite.
It is recommended to use the pytest_ tool to run the tests::

  $ python3 -m pytest ${packagename}


.. _pytest: https://docs.pytest.org


License
-------

:copyright: 2024 Antonio Valentino

The ``${packagename}`` package is distributed under the ${license_name} License
(see the `LICENSE` file).
