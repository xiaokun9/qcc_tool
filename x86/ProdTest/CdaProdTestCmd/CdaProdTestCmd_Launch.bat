C:
REM Update the path in the line below as appropriate for the BlueSuite installation being used.
cd "\Program Files (x86)\QTIL\BlueSuite 3.3.7"

set Arg1=-setup
set Arg2=-sernum
set Exec=CdaProdTestCmd.exe
REM In the line below provide the path to the setup file in place of "<path_to_setup_file>".
set FilePath=<path_to_setup_file>

:START

cls

@echo.
@echo.
@set /p SerialNum=SCAN NEXT BARCODE...
@echo.
@echo.

%Exec% %Arg1% %FilePath% %Arg2% %SerialNum%

pause

goto START
