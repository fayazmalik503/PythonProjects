import pywhatkit as pw

txt =  "Your website is the face of your business. Having the right copy will help your potential customers navigate and understand what your business is and what you sell. Effective Website content allows your followers to easily flow through your content without feeling overwhelmed."

var = pw.text_to_handwriting(txt, "example.png", [0,0,138])


print('Program Executed Successully')