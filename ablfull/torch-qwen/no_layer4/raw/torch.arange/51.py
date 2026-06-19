import torch

# Prepare valid input data
start = 0
end = 10
step = 1

# Call the API
result = torch.arange(start=start, end=end, step=step)
print(result)