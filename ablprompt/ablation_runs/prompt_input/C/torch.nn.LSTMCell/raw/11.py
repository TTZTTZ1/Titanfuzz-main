import torch

# Define the input size, hidden size, and number of time steps
input_size = 10
hidden_size = 20
num_time_steps = 5
batch_size = 3

# Create a random input tensor and initial hidden/cell states
input_tensor = torch.randn(num_time_steps, batch_size, input_size)
h0 = torch.zeros(batch_size, hidden_size)
c0 = torch.zeros(batch_size, hidden_size)

# Initialize the LSTMCell
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)

# Iterate over time steps and update the hidden and cell states
for t in range(num_time_steps):
    h0, c0 = lstm_cell(input_tensor[t], (h0, c0))

print("Final Hidden State:", h0)
print("Final Cell State:", c0)