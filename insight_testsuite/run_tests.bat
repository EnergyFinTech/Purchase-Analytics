@ECHO OFF

REM Windows

ECHO %DATE% %TIME%

SET rptFile=".\output\report.csv"
SET timStamp="YYYYMMDDhhmmss.bak"
REM SET bakFile = ".\output\" and timStamp

ECHO ################   TEST 1  Begin ################
cd ".\test_1\src"
ECHO Operating folder is %PWD%
ECHO Looking for %rptFile%

IF EXIST %rptFile% (
	ECHO "File exists " %rptFile%
	ECHO "Create Backup"
	REN %rptFile% "report.bak"
	DEL %rptFile% /f
	ECHO "Deleted File " %rptFile%
)

IF NOT EXIST %rptFile% ECHO "Fair: File does not exist " %rptFile%
	
ECHO "Execute script rptDeptOrder.py"
python "rptDeptOrder.py"
 
cd ..
cd ..

IF EXIST %rptFile% (
	ECHO "Good: Output File created " %rptFile%
) ELSE (
	ECHO "FAIL: Output File not created " %rptFile%
)

ECHO ################   TEST 1  end ################

ECHO ################   TEST train  Begin ################
cd ".\test_train\src"
ECHO Operating folder is %PWD%

ECHO Looking for %rptFile%

IF EXIST %rptFile% (
	ECHO "File exists " %rptFile%
	ECHO "Create Backup"
	REN %rptFile% "report.bak"
	DEL %rptFile% /f
	ECHO "Deleted File " %rptFile%
)

IF NOT EXIST %rptFile% ECHO "Fair: File does not exist " %rptFile%
	
ECHO "Execute script rptDeptOrder.py"
python "rptDeptOrder.py"
 
cd ..
cd ..

IF EXIST %rptFile% (
	ECHO "Good: Output File created " %rptFile%
) ELSE (
	ECHO "FAIL: Output File not created " %rptFile%
)

ECHO ################   TEST train  end ################

ECHO ################   TEST prior  Begin ################
cd ".\test_prior\src"
ECHO Operating folder is %PWD%

ECHO Looking for %rptFile%

IF EXIST %rptFile% (
	ECHO "File exists " %rptFile%
	ECHO "Create Backup"
	REN %rptFile% "report.bak"
	DEL %rptFile% /f
	ECHO "Deleted File " %rptFile%
)

IF NOT EXIST %rptFile% ECHO "Fair: File does not exist " %rptFile%
	
ECHO "Execute script rptDeptOrder.py"
python "rptDeptOrder.py"
 
cd ..
cd ..

IF EXIST %rptFile% (
	ECHO "Good: Output File created " %rptFile%
) ELSE (
	ECHO "FAIL: Output File not created " %rptFile%
)

ECHO ################   TEST prior  end ################

