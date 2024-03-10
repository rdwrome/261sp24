# min/midi/bpm

1. Create a file named `min.py`.
- Write a Python program to convert a given number of seconds into minutes and seconds.
- For example, 225 seconds should be converted to 3 minutes and 45 seconds.
- Use `duration_in_seconds // 60` to calculate the number of minutes in the given duration.
- Use `duration_in_seconds % 60` to find the remaining seconds.
- Print the duration in minutes and seconds using the `print()` function.
- For example, if the user enters 225 seconds, the printout must look as below:

```
The duration is 3 minutes and 45 seconds.
```

2. Create a file named `midi.py`.
- In music, note names, MIDI numbers, and frequencies are related concepts.
- Use the MIDI to frequency conversion equation found [here](https://en.wikipedia.org/wiki/MIDI_tuning_standard) to convert a MIDI number to a corresponding frequency.
- Ask the user to enter a MIDI number between 0 and 127.
- You can use the [exponentiation](https://www.w3schools.com/python/python_operators.asp) operator (`**`) to implement this equation.
- Print the original MIDI note number and the converted frequency value using a single `print()` function.
- If the user enters 60 for a MIDI number, the printout must look like the following:

```bash
The frequency of the MIDI note number 60 is 261.6255653005986 Hz.
```

3. Create a file named `bpm.py`.
- Write a Python program that converts BPM (beats-per-minute) to a millisecond interval representation. (You can find the equation from [this website](https://studioslave.com/tempo-bpm-to-millisecond-ms-conversion-calculator-studio-slave-tools/).)
- Ask the user to enter BPM using the `input()` function.
- Print the initial BPM value and the converted millisecond interval representation using `print()` and f-string.
- For example, if the user types in 120 as the BPM, the printout must look as below:

```
A quarter note delay in milliseconds for 120 BPM is 500 ms.
```
4. SUBMIT (as a link canvas to an assignment folder called "min/midi/bpm" in *your* GitHub repository):
	- Your three (3) .py files
	- A documentation file (in Markdown as an .md file!) of the .py files as outlined in the syllabus.
