"""
Machines are good at crunching numbers - faster and more accurately than most 
humans! Create a small program that calculates something useful to you 
(making you smile is useful). It should take user input, at use at least one of the 
number operators we saw in class: + / * . You may modify one of your previous 
exercises to include calculations, if you wish.

Remember to design your algorithm in English first, then translate it to Python 
code. Test as you go!
"""
print("Hello, I am a calculator")

firstNum= input("Please input your first number:    ")
operation = input("Please input the operation ex.(*+/-):    ").strip()
secondNum = input("Input your second number:   ")

match operation:
    case "+":
        answer = float(firstNum) + float(secondNum)
    case "-":
        answer = float(firstNum) - float(secondNum)
    case "*":
        answer = float(firstNum) * float(secondNum)
    case "/":
        answer = float(firstNum) / float(secondNum)

print(answer)