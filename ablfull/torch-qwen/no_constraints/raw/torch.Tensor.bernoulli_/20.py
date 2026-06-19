import torch

# Generate a tensor of shape (5,) filled with random integers from 0 to 1
input_data = torch.randint(0, 2, (5,))

# Call the API
result = input_data.bernoulli_()

print(result)