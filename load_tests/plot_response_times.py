"""
Python script using matplotlib to create a bar chart of the response times.
"""

import matplotlib.pyplot as plt
import numpy as np

# Data from your load test
request_types = ['GET /posts', 'POST /posts']

median = [37, 110]
p95 = [67, 340]
max_resp = [170, 395]

x = np.arange(len(request_types))  # label locations
width = 0.25  # bar width

fig, ax = plt.subplots(figsize=(8, 5))

# Bars for each percentile
rects1 = ax.bar(x - width, median, width, label='Median (ms)')
rects2 = ax.bar(x, p95, width, label='95th Percentile (ms)')
rects3 = ax.bar(x + width, max_resp, width, label='Max (ms)')

# Add labels, title, legend
ax.set_ylabel('Response Time (ms)')
ax.set_title('API Response Times by Request Type')
ax.set_xticks(x)
ax.set_xticklabels(request_types)
ax.legend()

# Add value labels on top of bars
def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0,3),  # offset text above bar
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(rects1)
add_labels(rects2)
add_labels(rects3)

plt.tight_layout()
plt.savefig('response_time_chart.png')
plt.show()
