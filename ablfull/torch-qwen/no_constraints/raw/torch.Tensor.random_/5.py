import torch

# Generate a random tensor of shape (3, 4) with values between 0 and 9
input_data = torch.zeros(3, 4)
input_data.random_(0, 10)

# Call the API
result = input_data.random_(0, 10)
print(result)