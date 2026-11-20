# SED1515 – Lab 7: Pen Plotter

This project uses a Raspberry Pi Pico to control a robotic pen plotter using G-code commands.

The program reads a G-code file and controls three servomotors to move the arm and raise or lower the pen.

## Files
- `main.py` – Main program
- `analyseur_gcode.py` – Reads G-code commands
- `interpreteur_gcode.py` – Controls the servos
- `traducteur_servo.py` – Converts angles to PWM values
- `ligne.gcode` – Example drawing instructions
- `test_analyseur.py` – Tests the G-code parser
- `test_traducteur.py` – Tests angle conversion

## Testing
I added two test files to check the G-code parser and servo angle conversion. These tests can be run separately using Python.

The main program runs on the Raspberry Pi Pico using MicroPython.
