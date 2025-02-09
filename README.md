# unitest-Feb-9-25
unite testing in python
## simple tests 
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
    * Assert actual== expected expression=True, "<message for **False**>"
* to run 2 options:
  * to run all tests: terminal -> pytest . - will run with colors.
  * run "play" and select what to test

## testing for receive errors:
* false possible test: if there was an error that was **not** caught, the test passed 
* for example: division by zero:
  * trick 1 for solution is to add to the test try and except and assert true in the except
  ```
  try:
      assert False "should raise the error and didn't" -  will fail the test
  except:
    assert True
  ```
  * the right pretty way to test it:
  ```
  with pytest.raises(<errorType>..) as ex:
      calc.div(a,b)
  
  ```
    meaning if in this section there will be error from type < errorType > like in the () the test will pass
    we expect for error from type <errorType> 
    *   to general the errorType , write raises(Exception) 
  