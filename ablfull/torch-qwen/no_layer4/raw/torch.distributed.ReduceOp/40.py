import torch

# Task 2: Generate input data
tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)

# Task 3: Call the API with valid parameters
result = torch.distributed.reduce(tensor, op=torch.distributed.ReduceOp.SUM)
print(result)