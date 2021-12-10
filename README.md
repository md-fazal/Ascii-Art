# Ascii-Art
### Converts normal image to ascii art

Using density of characters to produce dark and light pixels replaces each pixel of normal image to a corresponding character.
### Working
The following string contains character in incresing order of light density

**"`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"**

For example, to produce dark pixel " ' " is swapped for original.<br>
Similarly to produce bright pixel " $ " is swapped for original

Uses the following formulas to convert RGB to corresponding levels of brightness(any one can be used)

* **Average**: average the R, G and B values - (R + G + B) / 3
* **Lightness**: average the maximum and minimum values out of R, G and B - max(R, G, B) + min(R, G, B) / 2
* **Luminosity**: take a weighted average of the R, G and B values to account for human perception - 0.21 R + 0.72 G + 0.07 B
