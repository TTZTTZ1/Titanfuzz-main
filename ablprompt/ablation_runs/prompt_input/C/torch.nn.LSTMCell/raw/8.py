import torch

# Define model parameters
input_size = 10
hidden_size = 20
batch_size = 5
num_steps = 3

# Initialize LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input and initial states
input_tensor = torch.randn(num_steps, batch_size, input_size)
h0 = torch.zeros(batch_size, hidden_size)
c0 = torch.zeros(batch_size, hidden_size)

# Process each time step
for t in range(num_steps):
    h0, c0 = lstm_cell(input_tensor[t], (h0, c0))

print(h0.shape, c0.shape)  # Output should be (batch_size, hidden_size)