import torch

# Task 2: Generate input data
input1 = torch.randn(5)
input2 = torch.randn(5)
target = torch.randint(0, 2, (5,)).float()

# Task 3: Call the API
criterion = torch.nn.HingeEmbeddingLoss()
loss = criterion(input1, input2, target)

print(loss)