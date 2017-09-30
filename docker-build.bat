@echo off

SET DOCKER_EXTERNAL_PORT=6080
cd %~dp0

net session >nul 2>&1
 if %errorLevel% == 0 (
          ECHO Beginning build.
          docker build . -t "reddit-notifier:RNOTIFIER"
          ECHO Docker build complete.
          docker run -i -d -p %DOCKER_EXTERNAL_PORT%:80 -t reddit-notifier:RNOTIFIER
          GOTO End
 ) else (
          ECHO Error! Run me with admin rights.
          GOTO End
 )


:End
ECHO End of script.
pause >nul
