## Measuring the reading grade-level of the language at the Trump-Clinton debates, 2016

This little script runs as Python 2, and reports the Flesch-Kincaid Grade Level and other formal measures of "readability", using [code by Shivam Bansal and Chaitanya Aggarwal](https://github.com/shivam5992/textstat). To run:

 1. Install and activate a Python 2 virtual environment:

    ```python
    virtualenv v_env2
    . v_env2/bin/activate
    pip install -Ur requirements_py2.txt
    ```

 1. Run at the command line
    
    ```bash
    python report_stats.py
    ```

The `text_samples` directory contains debate-transcript text taken from the National Public Radio site:

 * [Debate 1](http://www.npr.org/2016/09/26/495115346/fact-check-first-presidential-debate) (accessed 20160927)
 * [Debate 2](http://www.npr.org/2016/10/09/497056227/fact-check-clinton-and-trump-debate-for-the-second-time) (accessed 20161021)
 * [Debate 3](http://www.npr.org/2016/10/19/498293478/fact-check-trump-and-clinton-s-final-presidential-debate) (accessed 20161021)
 
I separated the content by speaker and used CSS classes to eliminated commentary.

[end]
