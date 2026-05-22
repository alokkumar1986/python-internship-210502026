num=int(input ("enter a number"))
ones=["zero","one","two","three","four","five","six","seven","eight","nine"]


teens=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
tens=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
if 10<=num<=19:
    print(teens[num-10])
else:
    print(tens[num//10],ones[num%10])