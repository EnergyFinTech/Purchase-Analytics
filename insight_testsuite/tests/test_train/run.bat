@ECHO OFF

REM Windows

ECHO %DATE% %TIME%

ECHO Working folder is %PWD%

SET rptFile=".\output\report.csv"
SET timStamp="YYYYMMDDhhmmss.bak"
REM SET bakFile = ".\output\" and timStamp

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

cd ".\src"
python "rptDeptOrder.py"
cd ..
 
IF EXIST %rptFile% (
	ECHO "Good: Output File created " %rptFile%
) ELSE (
	ECHO "FAIL: Output File not created " %rptFile%
)
