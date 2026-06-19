import torch

# Choose a valid backend and operation based on constraints
reduce_op = torch.distributed.ReduceOp.SUM
backend = 'gloo'
tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.float32)

# Ensure MAX is not used with complex tensors
if reduce_op == torch.distributed.ReduceOp.MAX:
    tensor = torch.tensor([1.0, 2.0, 3.0], dtype=torch.complex64)

# Call the API
result = torch.distributed.all_reduce(tensor, op=reduce_op, async_op=False)
print(result)