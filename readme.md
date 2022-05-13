# Hue Bulb Control
I wanted more control over my hue bulbs and practice some new skills.

This project is a playground for me to experiment with threads in lighting control. Not sure where it's going but ultimately I'd like to get to a point where I can spawn a thread for each bulb and control them independently. Every lighting control app I've written has been single threaded, hopefully this will allow me to run more complicated patterns concurrently on different light fixtures while allowing an audio sampling thread to keep serving up data for the patterns.

One drawback I've noticed working with the Hue API is latency. Some testing should reveal where the latency is coming from because it seems very responsive from the first party control app.

## Goals & To-Dos
- More robust API token authentication, my key is just hard-coded
- The `Bulb` class should have methods not only for HSV control, but also include animations that spawn a thread to run the animation and not block the main thread
- Sampling thread to send FFT data to animation methods that are currently running
- See if there's a way around latency issues. It could be that I'm sending requests too quickly; I'm not used to 16-bit hue values.
- Ultimately, move to C++
- GUI or CLI
