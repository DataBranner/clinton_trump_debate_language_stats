## Measuring the reading grade-level of the language at the first Trump-Clinton debate, 20160926

This little script runs as Python 2, and reports the Flesch-Kincaid Grade Level and other formal measures of "readability", using [code by Shivam Bansal and Chaitanya Aggarwal](https://github.com/shivam5992/textstat). To run:

 1. Install and activate a Python 2 virtual environment:

    ```python
    virtualenv v_env2
    . v_env2/bin/activate
    pip install -U requirements_py2.txt
    ```

 1. Run at the command line
    
    ```bash
    python report_stats.py
    ```

The `text_samples` directory contains debate-transcript text taken from [the National Public Radio site](http://www.npr.org/2016/09/26/495115346/fact-check-first-presidential-debate) (accessed 20160927) and separated by speaker.

[end]
