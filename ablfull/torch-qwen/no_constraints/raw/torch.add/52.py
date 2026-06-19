import torch

# Generate input data
input1 = torch.tensor([1.0, 2.0])
input2 = torch.tensor([3.0, 4.0])

# Call the API
result = torch.add(input1, input2)
print(result)