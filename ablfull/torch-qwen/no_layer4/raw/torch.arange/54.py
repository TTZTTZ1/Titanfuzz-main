import torch

# Prepare valid input data
start = 0
end = 10
step = 2

# Call the target API
result = torch.arange(start, end, step)

print(result)