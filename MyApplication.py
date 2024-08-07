"""
this is your APPLICATION layer. it contains logic specific to deploying the logic in its core LIBRARY as a PROGRAM.
"""

import my_application

def parse_args():
	pass
	# use argparse to create args:list and kwargs:dict
	# you can add this as a library component instead if it gets complicated

def  main(args, kwargs):
	my_application.run(*args, **kwargs)


if __name__ == "__main__":
	args, kwargs = parse_args()
	main(args, kwargs)
