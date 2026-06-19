import torch

# Generate input data
input_data = [torch.tensor(42), torch.tensor([1, 2, 3]), torch.tensor([[1, 2], [3, 4]])]

# Call the API
result = torch.atleast_1d(*input_data)