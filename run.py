import itertools
import string

def generate_sequences(length):
    characters = string.ascii_letters + string.digits + string.punctuation  # Letters, numbers, and special characters
    combinations = itertools.product(characters, repeat=length)  # Generate combinations
    
    # Join each combination into a string
    sequences = [''.join(sequence) for sequence in combinations]
    return sequences

# Generate sequences of length 4
sequences_length_4 = generate_sequences(4)

# Print the first 10 sequences
print("First 10 sequences of length 4:")
for sequence in sequences_length_4[:10]:
    print(sequence)
