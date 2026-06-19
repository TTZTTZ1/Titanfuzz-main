import torch

# Generate input data
input1 = torch.randn(5)
input2 = torch.randn(5)
target = torch.randint(0, 2, (5,))

# Call the API
loss_fn = torch.nn.HingeEmbeddingLoss()
loss = loss_fn(input1, input2, target)

print(loss)