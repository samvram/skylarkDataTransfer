echo "Press 'u' for Updating Dataset or 'c' for Creating one"
set /p REPLY = Enter your choice

if [ %REPLY% == "u" ]
(
	echo  Downloading...
	python Workingv1.py 
	echo Downloaded_Deals
	python Workingv2.py 
	echo Downloaded_organizations
	python Workingv3.py 
	echo Downloaded_people
	python Workingv4.py
 	echo Mixed_Table_formed
	call powerBI2_1.exe;
	call powerBI2_2.exe;
	echo Success;
)
else (if [ %REPLY% == "c" ]
	(
		echo Downloading...
		python Workingv1.py
		echo Downloaded_Deals
		python Workingv2.py
		echo Downloaded_organizations
		python Workingv3.py
		echo Downloaded_people
		python Workingv4.py
		echo Mixed_Table_formed
		call powerBI_1.exe;
		call powerBI_2.exe;
	))

