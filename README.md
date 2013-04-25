This is the readme


System Simulation Life Support 
SSLS. Better names are encouraged.

This project is intended to provide a framework for system design.
Many of the high level decisions will be made, meaning that most of the developers time can be spent developing and optimizing solutions. 
Not reinventing the wheel.


Everything in python can be end to end solution, 
going to C/C++ where needed for speed.
First cut of any feature could be done in python. 


Modules:

pySync: Adaptor to sync repo.
pyBuild: Builds if needed
pyScenGen: generates scenarios
pyMail: email client



Features:
	
	repo control: (git 'cus we're using github)
		-check out
		-sync
		-labelling
	build control:
		-make
		-ncsim
	scenario control:
		-generate
		-default/overrides
		-override vectors without massive filenames
		-override pass/fail criteria
	build status:
		-sanity
		-feature results
	results status:
		-email
		-web page
		-visual display
		-automated documentation
		-method for evaluating results
	configuration control:
	
	vector matching support:

	debug dumping support:

Thoughts:
	how about using this whole concept to test itself.	
