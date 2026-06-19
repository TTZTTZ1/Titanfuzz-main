import torch

# Generate valid input data
dtype = 'float'
low = 1.0
high = 5.0
generator = torch.Generator().manual_seed(42)

# Call the API
result = torch.tensor(0.).random_(from_=low, to=high, generator=generator)
print(result)