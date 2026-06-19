import torch

# Define the input size, hidden size, and other parameters
input_size = 10
hidden_size = 20
batch_size = 5
num_steps = 3

# Initialize the LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Create random input and initial hidden/cell states
input_data = torch.randn(num_steps, batch_size, input_size)
h0 = torch.zeros(batch_size, hidden_size)
c0 = torch.zeros(batch_size, hidden_size)

# Forward pass through the LSTMCell
for i in range(num_steps):
    h0, c0 = lstm_cell(input_data[i], (h0, c0))

print("Final Hidden State:", h0)
print("Final Cell State:", c0)