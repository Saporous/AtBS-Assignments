#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;^ is Ctrl key
;# is window
;+ is Shift
;! is Alt key

; GUI
Gui, Add, Text,, Ctrl+1 print('
Gui, Add, Text,, Ctrl+2 print('\n
Gui, Add, Text,, Ctrl+Alt+R reload program
Gui, Add, Text,, Ctrl+q quit program
Gui, Font, norm
Gui, Show, w500 h500, 
return

^1::
Send print('
Return


^2::
Send print('\n
Return


;In case something BAD happens
^q::ExitApp

;when editing, use this to reload
^!r::Reload