===========
lintjenkins
===========


.. image:: https://img.shields.io/pypi/v/lintjenkins.svg
        :target: https://pypi.python.org/pypi/lintjenkins

.. image:: https://img.shields.io/travis/510908220/lintjenkins.svg
        :target: https://travis-ci.org/510908220/lintjenkins

.. image:: https://readthedocs.org/projects/lintjenkins/badge/?version=latest
        :target: https://lintjenkins.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/510908220/lintjenkins/shield.svg
     :target: https://pyup.io/repos/github/510908220/lintjenkins/
     :alt: Updates


jenkins pylint api.


* Free software: MIT license
* Documentation: https://lintjenkins.readthedocs.io.


Example
--------
.. code-block:: python

   In [2]: from lintjenkins import LintJenkins

   In [3]: lint_jenkins = LintJenkins('http://x.x.x.x:8080', username='username', password='password')

   In [4]: lint_jenkins.add_job(svn = 'svn', username='username', password='password',job_name='aliyun')

   In [7]: lint_jenkins.get_build_numbers('aliyun')
   Out[7]: [2, 1]

   In [8]: lint_jenkins.get_build_info('aliyun',2)
   Out[8]: 
   {
   'commits': [],
   'datetime': '2017-06-16 10:22:33',
   'duration': 47.478,
   'result': 'UNSTABLE',
   'result_url': 'http://x.x.x.x:8080/job/aliyun/2/violations/',
   'revisions': [{'module': 'svn','revision': 18977}],
   'violation_info': {'violation_file_num': 80, 'violation_num': 2027}
   }


对应的在jenkins上的表现是:

.. image:: lintjenkins.png


Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

