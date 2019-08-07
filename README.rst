
======================
bobtemplates.migration
======================

``bobtemplates.migration`` provides `mr.bob <http://mrbob.readthedocs.org/en/latest/>`_ templates to generate migration-related packages for Plone projects.


Features
========

Packages created with ``bobtemplates.migration`` use the current best-practices when creating an add-on. It also supports GIT by default, to keep track of changes one is doing with the package.

Provided templates
------------------

Currently, only a `jsonify` template is available.
This will create a Transmogrifier migration that will work with a
`collective.jsonify <https://pypi.org/project/collective.jsonify/>`_ export out of the box.

Pull requests are welcome if you would like a template that will work with other file types.
Examples would be CSV or a Wordpress export.

Compatibility
=============

Add-ons created with ``bobtemplates.migration`` are tested to work in Plone 5.1 and 5.2.
They should also work with older versions but that was not tested (if you are using this to
migrate to a new Plone site, you should be using the latest version of Plone).
It should work on Linux, Mac and Windows.


Documentation
=============

To get started with Transmogrifier, visit the training at https://training.plone.org/5/transmogrifier

For easy usage of mr.bob see: `plonecli <https://pypi.python.org/pypi/plonecli>`_

Installation
============

You can install bobtemplates.migration as every other normal Python package with `pip <https://pypi.python.org/pypi/pip>`_ inside a `virtualenv <https://pypi.python.org/pypi/virtualenv>`_ or better with `pipenv <https://pypi.python.org/pypi/pipenv>`_.


Installion with pipenv
----------------------

.. code-block:: console

    pipenv install bobtemplates.migration


Installation with pip in a virtualenv
-------------------------------------

You can also install ``bobtemplates.migration`` with pip in a virtualenv.
If you don't have an active virtualenv, you can create one inside your project directory.

.. code-block:: bash

    virtualenv .

Then either activate the virtualenv:

.. code-block:: bash

    source ./bin/activate

or just use the binaries directly inside the bin folder as below:

.. code-block:: console

    ./bin/pip install bobtemplates.migration


Use in a buildout
-----------------

.. code-block:: ini

    [buildout]
    parts += mrbob

    [mrbob]
    recipe = zc.recipe.egg
    eggs =
        mr.bob
        bobtemplates.migration

This creates a mrbob-executable in your bin-directory.


Usage
-----

As bobtemplates.migration is a template for mr.bob_, we use mrbob to run the templates.

If you are using `buildout <https://pypi.python.org/pypi/zc.buildout>`_  or an unactivated `virtualenv <https://pypi.python.org/pypi/virtualenv>`_, you can use mrbob like this:

.. code-block:: console

    ./bin/mrbob bobtemplates.migration:jsonify -O src/collective.foo

If you are using pipenv or an activated virtualenv, you can use mrbob like this:

Activate pipenv shell:

.. code-block:: console

    pipenv shell

or activate your virtualenv:

.. code-block:: console

    source bin/activate

.. code-block:: console

    mrbob bobtemplates.migration:jsonify -O src/collective.foo

This will create your Plone package inside the ``src`` directory.

See the documentation of mr.bob_ for further information.

Configuration
=============

You can set all `mr.bob configuration <http://mrbob.readthedocs.io/en/latest/userguide.html#configuration>`_ parameters in your ~/.mrbob file.

Here is an example:

.. code-block:: bash

    [mr.bob]
    verbose = False

    [variables]
    author.name = Maik Derstappen
    author.email = md@derico.de
    author.github.user = MrTango
    plone.version = 5.1.4
    #package.git.init = y
    #package.git.autocommit = n
    #package.git.disabled = n


Contribute
==========

- Issue Tracker: https://github.com/collective/bobtemplates.migration/issues
- Source Code: https://github.com/collective/bobtemplates.migration
- Documentation: https://training.plone.org/5/transmogrifier
