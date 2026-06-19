import torch

# Task 2: Generate input data
input1 = torch.randn(5)
input2 = torch.randn(5)
target = torch.randint(0, 2, (5,), dtype=torch.long)

# Task 3: Call the API
loss_fn = torch.nn.HingeEmbeddingLoss(margin=1.0, reduction='mean')
loss = loss_fn(input1, input2, target)
print(loss)