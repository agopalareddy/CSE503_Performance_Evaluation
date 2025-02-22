import pandas as pd
import matplotlib.pyplot as plt

def plot_comparison():
    py_data = pd.read_csv('python_results.csv')
    js_data = pd.read_csv('nodejs_results.csv')
    
    plt.figure(figsize=(10, 6))
    plt.plot(py_data['Range'], py_data['Duration'], 'b-o', label='Python')
    plt.plot(js_data['Range'], js_data['Duration'], 'r-o', label='Node.js')
    plt.xlabel('Number Range')
    plt.ylabel('Duration (seconds)')
    plt.title('Performance Comparison: Python vs Node.js')
    plt.legend()
    plt.grid(True)
    plt.savefig('performance_comparison.png')

if __name__ == "__main__":
    plot_comparison()


"""
Apache: 


Server Software:        Apache/2.4.62
Server Hostname:        localhost
Server Port:            80

Document Path:          /test.html
Document Length:        45 bytes

Concurrency Level:      10
Time taken for tests:   0.171 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      312000 bytes
HTML transferred:       45000 bytes
Requests per second:    5861.01 [#/sec] (mean)
Time per request:       1.706 [ms] (mean)
Time per request:       0.171 [ms] (mean, across all concurrent requests)
Transfer rate:          1785.78 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     0    2   2.2      1      38
Waiting:        0    1   1.1      1      21
Total:          0    2   2.2      1      38

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      2
  75%      2
  80%      2
  90%      2
  95%      3
  98%      4
  99%     10
 100%     38 (longest request)


Server Software:        Apache/2.4.62
Server Hostname:        localhost
Server Port:            80

Document Path:          /test.html
Document Length:        45 bytes

Concurrency Level:      10
Time taken for tests:   18.384 seconds
Complete requests:      100000
Failed requests:        0
Total transferred:      31200000 bytes
HTML transferred:       4500000 bytes
Requests per second:    5439.65 [#/sec] (mean)
Time per request:       1.838 [ms] (mean)
Time per request:       0.184 [ms] (mean, across all concurrent requests)
Transfer rate:          1657.39 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       2
Processing:     0    2   1.9      2      80
Waiting:        0    2   1.8      2      66
Total:          0    2   1.9      2      80

Percentage of the requests served within a certain time (ms)
  50%      2
  66%      2
  75%      2
  80%      2
  90%      2
  95%      3
  98%      3
  99%      3
 100%     80 (longest request)

Ngix: 



Server Software:        nginx/1.26.2
Server Hostname:        localhost
Server Port:            80

Document Path:          /test.html
Document Length:        45 bytes

Concurrency Level:      10
Time taken for tests:   0.086 seconds
Complete requests:      1000
Failed requests:        0
Total transferred:      276000 bytes
HTML transferred:       45000 bytes
Requests per second:    11686.75 [#/sec] (mean)
Time per request:       0.856 [ms] (mean)
Time per request:       0.086 [ms] (mean, across all concurrent requests)
Transfer rate:          3149.94 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0       2
Processing:     0    0   0.2      0       2
Waiting:        0    0   0.2      0       2
Total:          0    1   0.3      1       2

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      2
  98%      2
  99%      2
 100%      2 (longest request)


Server Software:        nginx/1.26.2
Server Hostname:        localhost
Server Port:            80

Document Path:          /test.html
Document Length:        45 bytes

Concurrency Level:      10
Time taken for tests:   8.242 seconds
Complete requests:      100000
Failed requests:        0
Total transferred:      27600000 bytes
HTML transferred:       4500000 bytes
Requests per second:    12132.79 [#/sec] (mean)
Time per request:       0.824 [ms] (mean)
Time per request:       0.082 [ms] (mean, across all concurrent requests)
Transfer rate:          3270.17 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.3      0       4
Processing:     0    0   0.3      0       5
Waiting:        0    0   0.2      0       3
Total:          0    1   0.3      1       6

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      1
  75%      1
  80%      1
  90%      1
  95%      2
  98%      2
  99%      2
 100%      6 (longest request)

"""
# Create DataFrames for Apache and Nginx results
apache_data = {
    'Test': ['1K Requests', '100K Requests'],
    'Requests_per_second': [5861.01, 5439.65],
    'Time_per_request': [1.706, 1.838],
    'Transfer_rate': [1785.78, 1657.39],
    'Max_response': [38, 80]
}

nginx_data = {
    'Test': ['1K Requests', '100K Requests'],
    'Requests_per_second': [11686.75, 12132.79],
    'Time_per_request': [0.856, 0.824],
    'Transfer_rate': [3149.94, 3270.17],
    'Max_response': [2, 6]
}

df_apache = pd.DataFrame(apache_data)
df_nginx = pd.DataFrame(nginx_data)

# Create comparison plots
metrics = ['Requests_per_second', 'Time_per_request', 'Transfer_rate', 'Max_response']
units = ['req/sec', 'ms', 'KB/sec', 'ms']
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

for idx, (metric, unit) in enumerate(zip(metrics, units)):
    ax = axes[idx//2, idx%2]
    x = range(len(df_apache['Test']))
    
    ax.bar([i-0.2 for i in x], df_apache[metric], width=0.4, label='Apache')
    ax.bar([i+0.2 for i in x], df_nginx[metric], width=0.4, label='Nginx')
    
    ax.set_xticks(x)
    ax.set_xticklabels(df_apache['Test'])
    ax.set_title(metric.replace('_', ' ').title())
    ax.set_ylabel(unit)
    ax.legend()
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('server_comparison.png')