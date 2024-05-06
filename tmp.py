import random


# Generate a random sequence of 'A', 'U', 'C', 'G'
def generate_sequence(length):
    bases = ["A", "U", "C", "G"]
    return "".join(random.choices(bases, k=length))


# Open a file in write mode
with open("output.txt", "w") as file:
    for i in range(2, 22):  # From gene_2 to gene_21
        length = random.randint(1000, 3000)
        sequence = generate_sequence(length)
        file.write(">gene_" + str(i) + "\n")  # Writing gene number
        file.write(sequence + "\n")
