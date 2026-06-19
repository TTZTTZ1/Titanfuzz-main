import torch

# Generate a random square matrix with values between -10 and 10
matrix = torch.randint(-10, 11, (5, 5), dtype=torch.float32)

# Call the torch.linalg.det API
result = torch.linalg.det(matrix)