# unitest-Feb-9-25
unite testing in python
* engine name selenium : a tool that can simulate testing for web actions
* need to use and import a library name pytest:
  * if doesn't exist: in terminal window run: pip install pytest or 
  * this will install on the environment you're working on
* create a separate file for testing: test_<file_you test>.py
* create a test function per function you want to test:
  * according to 3 As:Arrange Act Assert:
    * Arrange: define parameters
      * a=2,b=5, expected=7
    * Act: call the tested functions
      * actual=add(a,b)
    * Assert actual== expected expression=True, "<message for true>"
* to run 2 options:
  * to run all tests: terminal -> pytest . - will run with colors.
  * run "play" and select what to test
  