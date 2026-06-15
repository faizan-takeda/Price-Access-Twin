@echo off
setlocal enableextensions
rem ============================================================
rem  AccessTwin - Forced Autoplay Launcher
rem  Opens the prototype with audible autoplay ENABLED, so the
rem  welcome narration starts with NO click and NO keypress.
rem
rem  >>> Double-click THIS file instead of the .html <<<
rem
rem  Why this is needed: every modern browser blocks audible
rem  autoplay until the user interacts. Page JavaScript cannot
rem  override that. Launching the browser with the flag below
rem  is the supported way to allow it for a trusted local page.
rem ============================================================

rem Page to open (this launcher sits in the same folder as the HTML).
set "PAGE=%~dp0index_2_Autoplay_Fixed.html"

rem A dedicated profile guarantees a fresh browser PROCESS, so the
rem autoplay flag always takes effect even if Edge/Chrome is already
rem running (otherwise a new tab would join the existing process and
rem silently ignore the flag).
set "PROFILE=%TEMP%\AccessTwinKiosk"

set "ARGS=--autoplay-policy=no-user-gesture-required --user-data-dir=%PROFILE% --no-first-run --no-default-browser-check --new-window --start-maximized"

rem ---- Prefer Microsoft Edge ----
set "BROWSER=%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe"
if not exist "%BROWSER%" set "BROWSER=%ProgramFiles%\Microsoft\Edge\Application\msedge.exe"
if exist "%BROWSER%" goto launch

rem ---- Fall back to Google Chrome ----
set "BROWSER=%ProgramFiles%\Google\Chrome\Application\chrome.exe"
if not exist "%BROWSER%" set "BROWSER=%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"
if exist "%BROWSER%" goto launch

echo.
echo   Could not find Microsoft Edge or Google Chrome.
echo   Install either browser, or set Edge media autoplay to Allow:
echo   edge://settings/content/mediaAutoplay
echo.
pause
exit /b 1

:launch
start "" "%BROWSER%" %ARGS% "%PAGE%"
exit /b 0
