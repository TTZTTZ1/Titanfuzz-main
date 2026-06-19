import torch

# Prepare valid input data
reduce_op = torch.distributed.ReduceOp.SUM
tensor = torch.tensor([1.0], dtype=torch.float32)

# Call the target API
result = reduce_op(tensor)