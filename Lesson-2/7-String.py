# 6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475";
eot = text.find(':')
num_s = text[eot+1:].strip()
num = float(num_s)
print(num_s)
