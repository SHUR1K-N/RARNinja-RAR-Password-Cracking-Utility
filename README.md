# RARNinja: RAR Password Cracking Utility

## Description & Usage
A high-speed & unique multithreaded dictionary attack implementation that attacks a password-protected RAR file with a "chunkified" user-defined dictionary file to find the correct password within the candidates.

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/RARNinja-RAR-Password-Cracking-Utility/master/Images/Example.png" >
<p>Example Execution</p>
</div>

Upon the discovery of the correct password, the supplied RAR is automatically unlocked and extracted into the "Extracted" folder in the current working directory; so RARNinja can easily be left to crack a RAR file in the background as well.

This project was created in Python, for experimental/observational purposes; and can also be aided with my own super fast number dictionary generator [**NumNinja**](https://github.com/SHUR1K-N/NumNinja-Number-Dictionary-Generator) (up to 2M+ lines per second) for numeric attacks.

## Optimization
The high password-matching speed is owed to the approach of "chunkifying" the dictionary file (creating multiple "chunks" of the dictionary) and then operating on all those simplified chunks concurrently (multithreading) in different directions (forward and backward) for significantly higher overall balance, efficiency and performance.

<div align="center">
<img src="https://raw.githubusercontent.com/SHUR1K-N/RARNinja-RAR-Password-Cracking-Utility/master/Images/Multithreading%20Presentation.png" >
<p>Approaches: Regular Vs. Multithreaded</p>
</div>

## Dependencies to PIP-Install
- **rarfile** (for working with RAR files)
- **colorama** (for colors)
- **termcolor** (for colors)

------------

My website: https://TheComputerNoob.com
