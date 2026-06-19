import torch

# Task 2: Generate input data
input1 = torch.tensor([1.0, -1.0], dtype=torch.float32)
input2 = torch.tensor([-1.0, 1.0], dtype=torch.float32)
target = torch.tensor([1, -1], dtype=torch.int64)

# Task 3: Call the API
loss_fn = torch.nn.HingeEmbeddingLoss()
loss = loss_fn(input1, input2, target)

print(loss)