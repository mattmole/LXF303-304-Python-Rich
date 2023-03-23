from rich import print
from rich.prompt import Prompt
from rich.progress import track

# Print a title
print("𝛑[red underline] Let's generate Pi [/red underline]𝛑")

# Request the number of iterations from the user
iterations = None
while iterations == None:
    try:
        iterations = Prompt.ask(
            "Enter number of iterations", default="1000000")
        iterations = int(iterations)
    except:
        iterations = None

# Iteratively calculate Pi using the number of iterations captured from the user
quarterPi = float(1)
for i in track(range(1, iterations, 1), description='Generating pi...'):
    divisor = i*2+1
    if i % 2 == 1:
        quarterPi -= 1 / divisor
    else:
        quarterPi += 1 / divisor

print(f"Pi has been estimated as: {4*quarterPi}")
