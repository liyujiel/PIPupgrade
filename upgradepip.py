import pip
from subprocess import call

for dist in pip.getinstalled_distributions():
	call('pip install --upgrade ' + dist.project_name, shell=True)