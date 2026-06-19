import torch

# Generate input data satisfying the constraints
start = 0
end = 5
step = 1

# Call the API
result = torch.arange(start=start, end=end, step=step)
print(result)