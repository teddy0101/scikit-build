=============
Release Notes
=============

This is the list of changes to scikit-build between each release. For full
details, see the commit logs at http://github.com/scikit-build/scikit-build

Next Release
============

Bug fixes
---------

* Fixed a regression that caused setuptools to complain about unknown setup option
  (`cmake_process_manifest_hook`).

Documentation
-------------

* Update `Conda: Step-by-step` release guide available in :doc:`/make_a_release` section.
* Update links to CMake documentation pages in :doc:/`generators`.

Tests
-----

* Fix linting error `F522 <https://flake8.pycqa.org/en/latest/user/error-codes.html>`_ reported with flake8 >= 3.8.x. Thanks :user:`benbovy` for the contribution. See :issue:`494`.

Scikit-build 0.11.1
===================

Bug fixes
---------

* Support using scikit-build with conan where ``distro<1.2.0`` is required.
  Thanks :user:`AntoinePrv` and :user:`Chrismarsh` for reporting issue :issue:`472`
  and :issue:`488`.

Documentation
-------------

* Fix link in `Conda: Step-by-step` release guide available in :doc:`/make_a_release` section.

Scikit-build 0.11.0
===================

New Features
------------

* Add a hook to process the cmake install manifest building the wheel. The hook
  function can be specified as an argument to the `setup()` function. This can be used e.g.
  to prevent installing cmake configuration files, headers, or static libraries with the wheel.
  Thanks :user:`SylvainCorlay` for the contribution. See :issue:`473`.

* Add support for passing :ref:`CMake configure options <usage_cmake_configure_options>` like `-DFOO:STRING:bar`
  as global `setuptools` or `pip` options.

* Add support for building project using PyPy or PyPy3. See https://pypy.org
  See :issue:`407`.

* Add support for OS/400 (now known as IBM i).
  Thanks :user:`jwoehr` for the contribution. See :issue:`444`.

* Display CMake command used to configure the project.
  Thanks :user:`native-api` for the contribution. See :issue:`443`.

* CMake modules:

  * Improve CMake module :doc:`/cmake-modules/F2PY` adding `add_f2py_target()` CMake function
    allowing to generate `*-f2pywrappers.f` and `*module.c` files from `*.pyf` files.
    Thanks :user:`xoviat` for the contribution.

  * Update CMake module :doc:`/cmake-modules/PythonExtensions` adding `add_python_library()`
    and `add_python_extension()`.
    Thanks :user:`xoviat` for the contribution.

Bug fixes
---------

* Fix python 2.7 installation ensuring setuptools < 45 is required. See :issue:`478`.

* Fix unclosed file resource in :meth:`skbuild.cmaker.CMaker.check_for_bad_installs`.
  Thanks :user:`Nic30` for the suggestion. See :issue:`429`.

* Update CMake module :doc:`/cmake-modules/PythonExtensions`:

  * Ensure correct suffix is used for compiled python module on windows. See :issue:`383`.

  * Fix warning using `EXT_SUFFIX` config variable instead of deprecated `SO` variable. See :issue:`381`.

* Honor the `MACOSX_DEPLOYMENT_TARGET` environment variable if it is defined on
  macOS. Thanks :user:`certik` for the contribution. See :issue:`441`.

* Fix CMake module :doc:`/cmake-modules/F2PY` to ensure the `f2py` executable specific to
  the python version being used is found. See :issue:`449`. Thanks :user:`bnavigator` for
  the contribution.

* Replace `platform.linux_distribution()` which was removed in Python 3.8 by a call to
  `distro.id()`. This adds the `distro` package as dependency. See :issue:`458`. Thanks
  :user:`bnavigator` for the contribution.

Documentation
-------------

* Add :doc:`/notes` section to the `For maintainers` top-level category that includes a comparison between
  `sysconfig` and `distutils.sysconfig` modules.

* Remove obsolete comment in `cmaker.py`. See :issue:`439`. Thanks :user:`isuruf`

Tests
-----

* Update :func:`initialize_git_repo_and_commit` to prevent signing message on system with commit signing
  enabled globally.

Scikit-build 0.10.0
===================

New Features
------------

* Improve message displayed when discovering a working environment for building projects.
  For example, instead of displaying ``-- Trying "Ninja" generator``, it now displays a message
  like ``-- Trying "Ninja (Visual Studio 15 2017 Win64 v140)" generator``.

Bug fixes
---------

* Checking generator candidates can now handle handle paths and binaries with
  spaces, so that ``setup.py --cmake-executable "C:/Program Files
  (x86)/cmake/cmake.exe"`` works as expected.
  Contributed by :user:`jokva`. See :issue:`400`.

* Fix sdist command to ensure symlinks in original source tree are maintained.
  Contributed by :user:`anibali`. See :issue:`401`.

* Ensure use of `bdist_egg` or `bdist_rpm` commands trigger build using cmake.

* Fix default value returned by :func:`skbuild.constants.skbuild_plat_name()` on macOS.
  See :issue:`417`.

Internal API
------------

* Add :meth:`skbuild.platforms.windows.find_visual_studio`.

Documentation
-------------

* Fix typo in example associated with :doc:`/cmake-modules/PythonExtensions`.
  Thanks :user:`eirrgang` for the contribution.

* Update :doc:`/make_a_release` section to include `Conda: Step-by-step` release guide.

Tests
-----

* Introduce ``check_sdist_content()`` and fix tests that are checking content of sdist to
  account for changes introduced in Python 3.8 and backported to python 2.7, 3.6 and 3.7.
  The changes introduced in `python/cpython#9419 <https://github.com/python/cpython/pull/9419>`_
  adds directory entries to ZIP files created by distutils. Thanks :user:`anibali` for the
  contribution. See :issue:`404`.

* Fix ``check_wheel_content()`` to consider changes in ``0.33.1 < wheel.__version__ < 0.33.4``
  where directory entries are included when building wheel.
  See _`pypa/wheel#294 <https://github.com/pypa/wheel/issues/294>`.

* Fix reporting of ``AssertionError`` raised in ``check_wheel_content()`` function by relocating the
  source code into a dedicated module ``tests.pytest_helpers`` and by adding a ``conftest.py``
  configuration file registering it for pytest assertion rewriting.
  See https://docs.pytest.org/en/latest/writing_plugins.html#assertion-rewriting and :issue:`403`.

* Fix ``test_generator_selection`` when building with "Visual C++ for Python 2.7"
  installed for all users. This addresses failure associated with ``win_c_compilervs2008cxx_compilervs2008python2.7``
  when running test in `scikit-build-feedstock <https://github.com/conda-forge/scikit-build-feedstock>`_ where
  "Visual C++ for Python 2.7" is installed using (`vcpython27 <https://chocolatey.org/packages/vcpython27>`_ chocolatey
  package.

* Continuous Integration

  * Add support for Azure Pipelines for Python 3.7 32-bit and 64-bit

  * AppVeyor: Disable test for Python 3.7 32-bit and 64-bit.

  * CircleCI: Update version of docker images from jessie to stretch. This addresses
    issue `circleci/circleci-images#370 <https://github.com/circleci/circleci-images/issues/370#issuecomment-476611431>`_.

  * TravisCI: Remove obsolete Python 3.4 testing. It reached `end-of-life on March 18 2019 <https://devguide.python.org/devcycle/?highlight=end%20of%20life#end-of-life-branches>`_.


Scikit-build 0.9.0
==================

New Features
------------

* Add support for building distutils based extensions associated with ``ext_modules`` setup keyword along
  side skbuild based extensions. This means using ``build_ext`` command (and associated ``--inplace``
  argument) is supported. Thanks :user:`Erotemic` for the contribution. See :issue:`284`.

Bug fixes
---------

* Fix build of wheels if path includes spaces. See issue :issue:`375`. Thanks :user:`padraic-padraic`
  for the contribution.

* Ensure wheel platform name is correctly set when providing custom ``CMAKE_OSX_DEPLOYMENT_TARGET``
  and ``CMAKE_OSX_ARCHITECTURES`` values are provided. Thanks :user:`nonhermitian` for the contribution.
  See :issue:`377`.

* Fix testing with recent version of pytest by updating the pytest-runner requirements expression in `setup.py`.
  Thanks :user:`mackelab` for the contribution.

Scikit-build 0.8.1
==================

Bug fixes
---------

* Fix ``bdist_wheel`` command to support ``wheel >= 0.32.0``. Thanks :user:`fbudin69500` for reporting
  issue :issue:`360`.

Tests
-----

* Fix ``test_distribution.py`` updating use of ``Path.files()`` and requiring ``path.py>=11.5.0``.


Scikit-build 0.8.0
==================

New Features
------------

* Introduced :const:`skbuild.constants.CMAKE_DEFAULT_EXECUTABLE` to facilitate distribution
  of scikit-build in package manager like `Nixpkgs <https://github.com/NixOS/nixpkgs>`_ where
  all paths to dependencies are hardcoded. Suggested by :user:`FRidh`.

* Setup keywords:

  * If not already set, ``zip_safe`` option is set to ``False``. Suggested by :user:`blowekamp`.

* Add support for ``--skip-generator-test`` when a generator is explicitly selected using
  ``--generator``. This allows to speed up overall build when the build environment is known.

Bug fixes
---------

* Fix support for building project with CMake source directory outside of the
  ``setup.py`` directory. See :issue:`335` fixed by :user:`massich`.

* Fix reading of `.cmake` files having any character not available in
  `CP-1252 <https://en.wikipedia.org/wiki/Windows-1252>`_ (the default code page on
  windows). See :issue:`334` fixed by :user:`bgermann`.

* Fix parsing of macOS specific arguments like ``--plat-name macosx-X.Y-x86_64``
  and ``-DCMAKE_OSX_DEPLOYMENT_TARGET:STRING=X.Y`` and ensure that the ones specified as
  command line arguments override the default values or the one hard-coded in the
  ``cmake_args`` setup keyword. Thanks :user:`yonip` for the help addressing :issue:`342`.

* Support case where relative directory set in `package_dir` has an ending slash.
  For example, specifying ``package_dir={'awesome': 'src/awesome/'},`` is now
  properly handled.

* Fix support for isolated build environment ensuring the CMake project is reconfigured
  when ``pip install -e .`` is called multiple times. See :issue:`352`.

Documentation
-------------

* README: Update overall download count.

* Add logo and update sphinx configuration. Thanks :user:`SteveJordanKW` for the design work.

* Update :ref:`CMake installation <installation_cmake>` section. Thanks :user:`thewtex`.

* Add :ref:`support_isolated_build` section.

* Add :ref:`optimized_incremental_build` section.

* Update :ref:`usage documentation <usage-setuptools_options>` to specify that ``--universal`` and
  ``--python-tags`` have no effect.
  Thanks :user:`bgermann` for the suggestion. See :issue:`353`.

* Simplify documentation merging `Extension Build System` section with the `Advanced Usage` section.
  Thanks :user:`thewtex` for the suggestion.

Tests
-----

* Add ``check_wheel_content`` utility function.

* Skip `test_setup_requires_keyword_include_cmake` if running in conda test environment or
  if https://pypi.org is not reachable. Suggested by :user:`Luthaf`.

* Continuous Integration

  * TravisCI:

    * Remove testing of linux now covered by CircleCI, add testing for Python 3.5, 3.6 and 3.7 on macOS.
    * Ensure system python uses latest version of pip

  * AppVeyor, CircleCI: Add testing for Python 3.7

  * Remove uses of unneeded ``$<RUN_ENV>`` command wrapper. scikit-build should already take care of
    setting up the expected environment.

  * Always install up-to-date `scikit-ci`_ and `scikit-ci-addons`_.

  * Simplify release process managing `versioning` with `python-versioneer <https://github.com/warner/python-versioneer/>`_
    and update :ref:`making_a_release` documentation.


Scikit-build 0.7.1
==================

Documentation
-------------

* Fix description and classifier list in setup.py.
* Fix link in README.

Scikit-build 0.7.0
==================

New Features
------------

* Faster incremental build by re-configuring the project only if needed. This was achieved by (1) adding support
  to retrieve the environment mapping associated with the generator set in the ``CMakeCache.txt`` file, (2) introducing
  a :func:`CMake spec file <skbuild.constants.CMAKE_SPEC_FILE()>` storing the CMake version as well as the
  the CMake arguments and (3) re-configuring only if either the generator or the CMake specs change.
  Thanks :user:`xoviat` for the contribution. See :issue:`301`.

* CMake modules:

  * CMake module :doc:`/cmake-modules/PythonExtensions`: Set symbol visibility to export only the module init function.
    This applies to GNU and MSVC compilers. Thanks :user:`xoviat`. See :issue:`299`.

  * Add CMake module :doc:`/cmake-modules/F2PY` useful to find the ``f2py`` executable for building Python
    extensions with Fortran. Thanks to :user:`xoviat` for moving forward with the integration. Concept for the
    module comes from the work of :user:`scopatz` done in `PyNE <https://github.com/pyne/pyne>`_ project.
    See :issue:`273`.

  * Update CMake module :doc:`/cmake-modules/NumPy` setting variables ``NumPy_CONV_TEMPLATE_EXECUTABLE``
    and ``NumPy_FROM_TEMPLATE_EXECUTABLE``. Thanks :user:`xoviat` for the contribution. See :issue:`278`.

* Setup keywords:

  * Add support for :ref:`cmake_languages <usage-cmake_languages>` setup keyword.

  * Add support for ``include_package_data`` and ``exclude_package_data`` setup keywords as well as parsing of
    ``MANIFEST.in``. See :issue:`315`. Thanks :user:`reiver-dev` for reporting the issue.

  * Add support for ``cmake_minimum_required_version`` setup keyword. See :issue:`312`.
    Suggested by :user:`henryiii`.

  * Install cmake if found in ``setup_requires`` list. See :issue:`313`. Suggested by :user:`henryiii`.

* Add support for ``--cmake-executable`` scikit-build command line option. Thanks :user:`henryborchers` for the suggestion.
  See :issue:`317`.

* Use ``_skbuild/platform-X.Y`` instead of ``_skbuild`` to build package. This allows to have a different build
  directory for each python version. Thanks :user:`isuruf` for the suggestion and :user:`xoviat` for contributing
  the feature. See :issue:`283`.

* Run cmake and ``develop`` command when command ``test`` is executed.


Bug fixes
---------

* Fix support of ``--hide-listing`` when building wheel.

* CMake module :doc:`/cmake-modules/Cython`: Fix escaping of spaces associated with ``CYTHON_FLAGS`` when
  provided as command line arguments to the cython executable through CMake cache entries. See :issue:`265`
  fixed by :user:`neok-m4700`.

* Ensure package data files specified in the ``setup()`` function using ``package_data`` keyword are packaged
  and installed.

* Support specifying a default directory for all packages not already associated with one using syntax like
  ``package_dir={'':'src'}`` in ``setup.py``. Thanks :user:`benjaminjack` for reporting the issue.
  See :issue:`274`.

* Improve ``--skip-cmake`` command line option support so that it can re-generate a source distribution or a python
  wheel without having to run cmake executable to re-configure and build. Thanks to :user:`jonwoodring` for reporting
  the issue on the `mailing list <https://groups.google.com/forum/?utm_medium=email&utm_source=footer#!topic/scikit-build/-ManO0dhIV4>`_.

* Set ``skbuild <version>`` as wheel generator.
  See `PEP-0427 <https://www.python.org/dev/peps/pep-0427/#file-contents>`_ and :issue:`191`.

* Ensure ``MANIFEST.in`` is considered when generating source distribution. Thanks :user:`seanlis` for reporting
  the problem and providing an initial patch, and thanks :user:`henryiii` for implementing the corresponding test.
  See :issue:`260`.

* Support generation of source distribution for git repository having submodules. This works only for version
  of git >= 2.11 supporting the ``--recurse-submodules`` option with ``ls-files`` command.

Internal API
------------

* Add :meth:`skbuild.cmaker.get_cmake_version`.

Python Support
--------------

* Tests using Python 3.3.x were removed and support for this version of python is not guaranteed anymore. Support was
  removed following the deprecation warnings reported by version 0.31.0 of wheel package, these were causing the tests
  ``test_source_distribution`` and ``test_wheel`` to fail.

Tests
-----

* Speedup execution of tests that do not require any CMake language enabled. This is achieved by (1) introducing the
  test project ``hello-no-language``, (2) updating test utility functions ``execute_setup_py`` and ``project_setup_py_test``
  to accept the optional parameter ``disable_languages_test`` allowing to skip unneeded compiler detection in test project
  used to verify that the selected CMake generator works as expected, and (3) updating relevant tests to use the new test
  project and parameters.

  Overall testing time on all continuous integration services was reduced:

  * AppVeyor:

    * from **~16 to ~7** minutes for 64 and 32-bit Python 2.7 tests done using Visual Studio Express 2008
    * from more than **2 hours to ~50 minutes** for 64 and 32-bit Python 3.5 tests done using Visual Studio 2015. Improvement specific
      to Python 3.x were obtained by caching the results of slow calls to ``distutils.msvc9compiler.query_vcvarsall`` (for Python 3.3 and 3.4) and
      ``distutils._msvccompiler._get_vc_env`` (for Python 3.5 and above).
      These functions were called multiple times to create the list of :class:`skbuild.platform_specifics.windows.CMakeVisualStudioCommandLineGenerator`
      used in :class:`skbuild.platform_specifics.windows.WindowsPlatform`.


  * CircleCI: from **~7 to ~5** minutes.

  * TravisCI: from **~21 to ~10** minutes.

* Update maximum line length specified in flake8 settings from 80 to 120 characters.

* Add ``prepend_sys_path`` utility function.

* Ensure that the project directory is prepended to ``sys.path`` when executing test building sample project
  with the help of ``execute_setup_py`` function.

* Add codecov config file for better defaults and prevent associated Pull Request checks from reporting failure
  when coverage only slightly changes.

Documentation
-------------

* Improve internal API documentation:

  * :mod:`skbuild.platform_specifics.windows`
  * :mod:`skbuild.command`
  * :mod:`skbuild.command.generate_source_manifest`
  * :mod:`skbuild.utils`

* Split usage documentation into a `Basic Usage` and `Advanced Usage` sections.

Cleanups
--------

* Fix miscellaneous pylint warnings.

Scikit-build 0.6.1
==================

Bug fixes
---------

* Ensure CMake arguments passed to scikit-build and starting with ``-DCMAKE_*``
  are passed to the test project allowing to determine which generator to use.
  For example, this ensures that arguments like ``-DCMAKE_MAKE_PROGRAM:FILEPATH=/path/to/program``
  are passed. See :issue:`256`.

Documentation
-------------

* Update :doc:`/make_a_release` section including instructions to update ``README.rst``
  with up-to-date pypi download statistics based on Google big table.


Scikit-build 0.6.0
==================

New features
------------

* Improve ``py_modules`` support: Python modules generated by CMake are now
  properly included in binary distribution.

* Improve developer mode support for ``py_modules`` generated by CMake.


Bug fixes
---------

* Do not implicitly install python modules when the beginning of their name
  match a package explicitly listed. For example, if a project has a package
  ``foo/__init__.py`` and a module ``fooConfig.py``, and only package ``foo``
  was listed in ``setup.py``, ``fooConfig.py`` is not installed anymore.

* CMake module :doc:`/cmake-modules/targetLinkLibrariesWithDynamicLookup`: Fix the
  caching of *dynamic lookup* variables. See :issue:`240` fixed by :user:`blowekamp`.

Requirements
------------

* wheel:  As suggested by :user:`thewtex`, unpinning version of the package
  by requiring ``>=0.29.0`` instead of ``==0.29.0`` will avoid uninstalling a newer
  version of wheel package on up-to-date system.

Documentation
-------------

* Add a command line :ref:`CMake Options <usage_cmake_options>` section to :doc:`Usage <\usage>`.

* Fix :ref:`table <Visual Studio>` listing *Visual Studio IDE* version and
  corresponding with *CPython version* in :doc:`/generators`.

* Improve :doc:`/make_a_release` section.

Tests
-----

* Extend ``test_hello``, ``test_setup``, and ``test_sdist_hide_listing`` to
  (1) check if python modules are packaged into source and wheel distributions
  and (2) check if python modules are copied into the source tree when developer
  mode is enabled.

Internal API
------------

* Fix :meth:`skbuild.setuptools_wrap.strip_package` to handle empty package.

* Teach :meth:`skbuild.command.build_py.build_py.find_modules` function to look
  for `py_module` file in ``CMAKE_INSTALL_DIR``.

* Teach :class:`skbuild.utils.PythonModuleFinder` to search for `python module`
  in the CMake install tree.

* Update :meth:`skbuild.setuptools_wrap._consolidate` to copy file into the CMake
  tree only if it exists.

* Update :meth:`skbuild.setuptools_wrap._copy_file` to create directory only if
  there is one associated with the destination file.

Scikit-build 0.5.1
==================

Bug fixes
---------

* Ensure file copied in "develop" mode have "mode bits" maintained.


Scikit-build 0.5.0
==================

New features
------------

* Improve user experience by running CMake only if needed. See :issue:`207`

* Add support for :ref:`cmake_with_sdist <usage-cmake_with_sdist>` setup keyword argument.

* Add support for ``--force-cmake`` and ``--skip-cmake`` global :ref:`setup command-line options <usage-setuptools_options>`.

* scikit-build conda-forge recipe added by :user:`isuruf`.
  See `conda-forge/staged-recipes#1989 <https://github.com/conda-forge/staged-recipes/pull/1989>`_

* Add support for `development mode <https://packaging.python.org/distributing/#working-in-development-mode>`_. (:issue:`187`).

* Improved :doc:`/generators` selection:

 * If available, uses :ref:`Ninja` build system generator on all platforms. An
   advantages is that ninja automatically parallelizes the build based on the number
   of CPUs.

 * Automatically set the expected `Visual Studio` environment when
   ``Ninja`` or ``NMake Makefiles`` generators are used.

 * Support `Microsoft Visual C++ Compiler for Python 2.7 <http://aka.ms/vcpython27>`_.
   See :issue:`216`.

* Prompt for user to install the required compiler if it is not available. See :issue:`27`.

* Improve :doc:`/cmake-modules/targetLinkLibrariesWithDynamicLookup`  CMake Module extending
  the API of ``check_dynamic_lookup`` function:

 * Update long signature: ``<LinkFlagsVar>`` is now optional
 * Add support for short signature: ``check_dynamic_lookup(<ResultVar>)``.
   See `SimpleITK/SimpleITK#80 <https://github.com/SimpleITK/SimpleITK/pull/80#issuecomment-267617180>`_.

Bug fixes
---------

* Fix scikit-build source distribution and add test. See :issue:`214`
  Thanks :user:`isuruf` for reporting the issue.

* Support building extension within a virtualenv on windows. See :issue:`119`.

Documentation
-------------

* add :doc:`/generators` section

* add :doc:`/changes` section

* allow github issues and users to easily be referenced using ``:issue:`XY```
  and ``:user:`username``` markups.
  This functionality is enabled by the `sphinx-issue <https://github.com/sloria/sphinx-issues>`_ sphinx extension

* make_a_release: Ensure uploaded distributions are signed

* usage:

 * Add empty cross-compilation / wheels building sections
 * Add :ref:`Why should I use scikit-build ? <why>`
 * Add :ref:`Setup options <usage-setup_options>` section

* hacking:

 * Add :ref:`internal_api` section generated using `sphinx-apidoc`.

 * Add :ref:`internal_cmake_modules` to document :doc:`/cmake-modules/targetLinkLibrariesWithDynamicLookup`
   CMake module.

Requirements
------------

* setuptools: As suggested by :user:`mivade` in :issue:`212`, remove the
  hard requirement for ``==28.8.0`` and require version ``>= 28.0.0``. This allows
  to "play" nicely with conda where it is problematic to update the version
  of setuptools. See `pypa/pip#2751 <https://github.com/pypa/pip/issues/2751>`_
  and `ContinuumIO/anaconda-issues#542 <https://github.com/ContinuumIO/anaconda-issues/issues/542>`_.

Tests
-----

* Improve "push_dir" tests to not rely on build directory name.
  Thanks :user:`isuruf` for reporting the issue.

* travis/install_pyenv: Improve MacOSX build time updating `scikit-ci-addons`_

* Add ``get_cmakecache_variables`` utility function.

.. _scikit-ci-addons: http://scikit-ci-addons.readthedocs.io

Internal API
------------

* :meth:`skbuild.cmaker.CMaker.configure`: Change parameter name from ``generator_id``
  to ``generator_name``. This is consistent with how generator are identified
  in `CMake documentation <https://cmake.org/cmake/help/v3.7/manual/cmake-generators.7.html>`_.
  This change breaks backward compatibility.

* :meth:`skbuild.platform_specifics.abstract.CMakePlatform.get_best_generator`: Change parameter name
  from ``generator`` to ``generator_name``. Note that this function is also directly importable
  from :mod:`skbuild.platform_specifics`.
  This change breaks backward compatibility.

* :class:`skbuild.platform_specifics.abstract.CMakeGenerator`: This class allows to
  handle generators as sophisticated object instead of simple string. This is done
  anticipating the support for `CMAKE_GENERATOR_PLATFORM <https://cmake.org/cmake/help/v3.7/variable/CMAKE_GENERATOR_PLATFORM.html>`_
  and `CMAKE_GENERATOR_TOOLSET <https://cmake.org/cmake/help/v3.7/variable/CMAKE_GENERATOR_TOOLSET.html>`_. Note also that the
  class is directly importable from :mod:`skbuild.platform_specifics` and is now returned
  by :meth:`skbuild.platform_specifics.get_best_generator`. This change breaks backward compatibility.


Cleanups
--------

* appveyor.yml:

 * Remove unused "on_failure: event logging" and "notifications: GitHubPullRequest"
 * Remove unused SKIP env variable


Scikit-build 0.4.0
==================

New features
------------

* Add support for ``--hide-listing`` option

 * allow to build distributions without displaying files being included

 * useful when building large project on Continuous Integration service limiting
   the amount of log produced by the build

* CMake module: ``skbuild/resources/cmake/FindPythonExtensions.cmake``

 * Function ``python_extension_module``: add support for `module suffix <https://github.com/scikit-build/scikit-build/commit/0a9b7ef>`_

Bug fixes
---------

* Do not package python modules under "purelib" dir in non-pure wheel

* CMake module: ``skbuild/resources/cmake/targetLinkLibrariesWithDynamicLookup.cmake``:

 * Fix the logic checking for cross-compilation (the regression
   was introduced by :issue:`51` and :issue:`47`

 * It configure the text project setting `CMAKE_ENABLE_EXPORTS <https://cmake.org/cmake/help/v3.6/prop_tgt/ENABLE_EXPORTS.html?highlight=enable_export>`_ to ON. Doing
   so ensure the executable compiled in the test exports symbols (if supported
   by the underlying platform)

Docs
----

* Add `short note <http://scikit-build.readthedocs.io/en/latest/cmake-modules.html>`_
  explaining how to include scikit-build CMake module
* Move "Controlling CMake using scikit-build" into a "hacking" section
* Add initial version of `"extension_build_system" documentation <http://scikit-build.readthedocs.io/en/latest/extension_build_system.html>`_

Tests
-----

* tests/samples: Simplify project removing unneeded install rules and file copy

* Simplify continuous integration

 * use `scikit-ci <http://scikit-ci.readthedocs.io/en/latest/>`_ and
   `scikit-ci-addons`_
 * speed up build setting up caching

* Makefile:

 * Fix `coverage` target
 * Add `docs-only` target allowing to regenerate the Sphinx documentation
   without opening a new page in the browser.

Scikit-build 0.3.0
==================

New features
------------

* Improve support for "pure", "CMake" and "hybrid" python package

 * a "pure" package is a python package that have all files living
   in the project source tree

 * an "hybrid" package is a python package that have some files living
   in the project source tree and some files installed by CMake

 * a "CMake" package is a python package that is fully generated and
   installed by CMake without any of his files existing in the source
   tree

* Add support for source distribution. See :issue:`84`

* Add support for setup arguments specific to scikit-build:

 * ``cmake_args``: additional option passed to CMake
 * ``cmake_install_dir``: relative directory where the CMake project being
   built should be installed
 * ``cmake_source_dir``: location of the CMake project

* Add CMake module ``FindNumPy.cmake``

* Automatically set ``package_dir`` to reasonable defaults

* Support building project without CMakeLists.txt



Bug fixes
---------

* Fix dispatch of arguments to setuptools, CMake and build tool. See :issue:`118`

* Force binary wheel generation. See :issue:`106`

* Fix support for ``py_modules`` (`6716723 <https://github.com/scikit-build/scikit-build/commit/6716723>`_)

* Do not raise error if calling "clean" command twice

Documentation
-------------

* Improvement of documentation published
  on http://scikit-build.readthedocs.io/en/latest/

* Add docstrings for most of the modules, classes and functions

Tests
-----

* Ensure each test run in a dedicated temporary directory

* Add tests to raise coverage from 70% to 91%

* Refactor CI testing infrastructure introducing CI drivers written in python
  for AppVeyor, CircleCI and TravisCI

* Switch from ``nose`` to ``py.test``

* Relocate sample projects into a dedicated
  home: https://github.com/scikit-build/scikit-build-sample-projects

Cleanups
--------

* Refactor commands introducing ``set_build_base_mixin`` and ``new_style``

* Remove unused code
