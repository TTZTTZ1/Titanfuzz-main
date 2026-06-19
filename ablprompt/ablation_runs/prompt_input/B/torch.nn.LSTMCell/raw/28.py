import torch

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input and initial hidden/cell states
batch_size = 3
input_tensor = torch.randn(batch_size, input_size)
hx = torch.zeros(batch_size, hidden_size)
cx = torch.zeros(batch_size, hidden_size)

# Process through LSTMCell
for i in range(5):
    hx, cx = lstm_cell(input_tensor[i], (hx, cx))

print(hx)
print(cx)