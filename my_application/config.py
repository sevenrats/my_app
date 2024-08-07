import os

A_GLOBAL_CONSTANT = os.getenv("var_name", "foo-default-value")
# etc...
# parse args can import this if you want, but business logic can use it directly too
