import torch

# Generate input data
start = 0
end = 5
step = 1

# Call the API
result = torch.arange(start, end, step)
print(result)