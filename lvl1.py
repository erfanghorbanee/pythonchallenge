# Cracking Caesar Cipher Code

plainText = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

shift = 2
lowerAlpha = "abcdefghijklmnopqrstuvwxyz"
upperAlpha = lowerAlpha.upper()
numbers = "0123456789"
before = lowerAlpha + upperAlpha + numbers
after = (
    lowerAlpha[shift:]
    + lowerAlpha[:shift]
    + upperAlpha[shift:]
    + upperAlpha[:shift]
    + numbers[shift:]
    + numbers[:shift]
)
translation = str.maketrans(before, after)
Message = plainText.translate(translation)
print("\nFrom:  {}".format(before))
print("  To:  {}\n".format(after))
print("Message:  {}".format(Message))

# The result suggests to change the URL from map.html to ocr.jvon, but since there is no such thing as a .jvon file, try ocr.html.
