Contributor's Guide
===================

Contributions are always welcome and greatly appreciated!

Code contributions
------------------

We love pull requests from everyone! Here's a quick guide to improve the code:

1. Fork `the repository <https://github.com/affo/affo-ce>`_ and clone the fork.
2. Create a virtual environment using your tool of choice (e.g. ``virtualenv``, ``conda``, etc).
3. Change the current directory to the one of:

    * backend
    * services/deeplinks
    * services/events
    * services/postbacks

4. Install development dependencies:

::

    pip install -r requirements.txt
    pip install -r requirements-test.txt

5. Make sure all tests pass:

::

    pytest

6. Start making your changes to the **master** branch (or branch off of it).
7. Make sure all tests still pass:

::

    pytest

8. Add yourself to ``AUTHORS.rst``.
9. Commit your changes and push your branch to GitHub.
10. Create a `pull request <https://help.github.com/articles/about-pull-requests/>`_ through the GitHub website.

Bug reports
-----------

When `reporting a bug <https://github.com/affo/affo-ce/issues>`_
please include:

    * Operating system name and version.
    * `affo-ce` version.
    * Any details about your local setup that might be helpful in troubleshooting.
    * Detailed steps to reproduce the bug.

Feature requests and feedback
-----------------------------

The best way to send feedback is to file an issue on
`Github <https://github.com/affo/affo-ce/issues>`_. If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
