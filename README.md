# Ascii-Art
### Converts normal image/gif to ascii art

Using density of characters to produce dark and light pixels replaces each pixel of normal image to a corresponding character.
### Working
The following string contains character in increasing order of light density

**"`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"**

For example, to produce dark pixel " ' " is swapped for original.<br>
Similarly to produce bright pixel " $ " is swapped for original

Uses the following formulas to convert RGB to corresponding levels of brightness(any one can be used)

* **Average**: average the R, G and B values - (R + G + B) / 3
* **Lightness**: average the maximum and minimum values out of R, G and B - max(R, G, B) + min(R, G, B) / 2
* **Luminosity**: take a weighted average of the R, G and B values to account for human perception - 0.21 R + 0.72 G + 0.07 B
<p float="left">
  <img src="https://user-images.githubusercontent.com/94881380/145555661-6663fd57-1aa2-4209-96a6-1d402e1f3a15.png" width="400" />
  <img src="https://user-images.githubusercontent.com/94881380/145556751-650fe24e-c4be-4401-ad38-10e6eb93bdcf.png" width="400" /> 
</p>

<p float="left">
  <img src="https://user-images.githubusercontent.com/94881380/145571664-5df10f97-d1b0-4565-a411-1cf2b8a2fce3.gif" width="400" />
</p>
