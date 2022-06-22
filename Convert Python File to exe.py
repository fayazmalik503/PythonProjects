"""""1. pyinstaller, 2. auto-py-to-exe

I tried this on last project we created with name
Internet Speed Test Using Python with GUI.py

To convert into .exe file these steps are need to follow


two methods

1 method which is short

2 Method which is configuration

pip install pyinstaller                # for old version python
           or                               
python -m PyInstaller App.py          # support with 3.10 version of python

# This will create extra files as well

To resolve this issue: we can write: 
pyinstaller --onefile digital.py     # for old version python

I have tried this for storing in single file
in CMD:
> python -m PyInstaller --onefile App.py      # support with 3.10 version of python
"""""

"""
Second Method : 

pip install auto-py-to-exe   # support with 3.10 version of python
***Installing your module -----

I tried old way that is:
auto-py-to-exe

then I tried
python -m auto_py_to_exe   # This worked



"""