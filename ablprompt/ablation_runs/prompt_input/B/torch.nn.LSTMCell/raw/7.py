import torch

# Define model parameters
input_size = 10
hidden_size = 20

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create dummy input and initial states
batch_size = 5
input_data = torch.randn(batch_size, input_size)
hx = torch.zeros(batch_size, hidden_size)
cx = torch.zeros(batch_size, hidden_size)

# Process multiple time steps
for i in range(3):
    hx, cx = lstm_cell(input_data, (hx, cx))

print(hx.shape, cx.shape)