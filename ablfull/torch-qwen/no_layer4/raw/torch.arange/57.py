import torch

# Generate input data
start = 0
end = 5
step = 1

# Call the API
output = torch.arange(start=start, end=end, step=step)
print(output)