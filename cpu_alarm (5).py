import subprocess
import socket
print (' ')
print 'Host Name          : '+(socket.gethostname())
output_2=subprocess.check_output("echo $(ip a s | grep -w inet | awk '{print $2}' | sed -e \"s/\/.*//\" -e \"/127/d\" | tr \"\n\" \" \")", shell=True).rstrip()
print 'IP Addresss        : '+output_2
output_1=int(subprocess.check_output("echo $(vmstat|tail -1|awk '{print $15}')", shell=True).rstrip())
CPU=100-output_1
print 'CPU utilization is : '+str(CPU)+'%'
print (' ')
output=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 2 | awk '{print $1}' | awk 'NR>1')", shell=True).rstrip()
output1=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 2 | awk '{print $2}' | awk 'NR>1')", shell=True).rstrip()
output2=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 2 | awk '{print $3}' | awk 'NR>1')", shell=True).rstrip()
output3=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 2 | awk '{print $4}' | awk 'NR>1')", shell=True).rstrip()
output4=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 2 | awk '{print $11}' | awk 'NR>1')", shell=True).rstrip()
print 'completed line1'
"""for second highest process"""
out=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 3 | awk '{print $1}' | awk 'NR>2')", shell=True).rstrip()
out1=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 3 | awk '{print $2}' | awk 'NR>2')", shell=True).rstrip()
out2=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 3 | awk '{print $3}' | awk 'NR>2')", shell=True).rstrip()
out3=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 3 | awk '{print $4}' | awk 'NR>2')", shell=True).rstrip()
out4=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 3 | awk '{print $11}' | awk 'NR>2')", shell=True).rstrip()
print 'completed line2'
"""for Third highest process"""
out_1=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 4 | awk '{print $1}' | awk 'NR>3')", shell=True).rstrip()
out1_1=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 4 | awk '{print $2}' | awk 'NR>3')", shell=True).rstrip()
out2_1=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 4 | awk '{print $3}' | awk 'NR>3')", shell=True).rstrip()
out3_1=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 4 | awk '{print $4}' | awk 'NR>3')", shell=True).rstrip()
out4_1=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 4 | awk '{print $11}' | awk 'NR>3')", shell=True).rstrip()
print 'completed line3'
"""for fourth highest process"""
out_2=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 5 | awk '{print $1}' | awk 'NR>4')", shell=True).rstrip()
out1_2=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 5 | awk '{print $2}' | awk 'NR>4')", shell=True).rstrip()
out2_2=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 5 | awk '{print $3}' | awk 'NR>4')", shell=True).rstrip()
out3_2=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 5 | awk '{print $4}' | awk 'NR>4')", shell=True).rstrip()
out4_2=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 5 | awk '{print $11}' | awk 'NR>4')", shell=True).rstrip()
print 'completed line4'
"""for fifth highest process"""
out_3=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 6 | awk '{print $1}' | awk 'NR>5')", shell=True).rstrip()
out1_3=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 6 | awk '{print $2}' | awk 'NR>5')", shell=True).rstrip()
out2_3=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 6 | awk '{print $3}' | awk 'NR>5')", shell=True).rstrip()
out3_3=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 6 | awk '{print $4}' | awk 'NR>5')", shell=True).rstrip()
out4_3=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 6 | awk '{print $11}' | awk 'NR>5')", shell=True).rstrip()
print 'completed line5'
"""for sixth highest process"""
out_4=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 7 | awk '{print $1}' | awk 'NR>6')", shell=True).rstrip()
out1_4=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 7 | awk '{print $2}' | awk 'NR>6')", shell=True).rstrip()
out2_4=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 7 | awk '{print $3}' | awk 'NR>6')", shell=True).rstrip()
out3_4=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 7 | awk '{print $4}' | awk 'NR>6')", shell=True).rstrip()
out4_4=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 7 | awk '{print $11}' | awk 'NR>6')", shell=True).rstrip()
print 'completed line6'
"""for seventh highest process"""
out_5=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 8 | awk '{print $1}' | awk 'NR>7')", shell=True).rstrip()
out1_5=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 8 | awk '{print $2}' | awk 'NR>7')", shell=True).rstrip()
out2_5=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 8 | awk '{print $3}' | awk 'NR>7')", shell=True).rstrip()
out3_5=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 8 | awk '{print $4}' | awk 'NR>7')", shell=True).rstrip()
out4_5=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 8 | awk '{print $11}' | awk 'NR>7')", shell=True).rstrip()
print 'completed line7'
"""for eigth highest process"""
out_6=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 9 | awk '{print $1}' | awk 'NR>8')", shell=True).rstrip()
out1_6=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 9 | awk '{print $2}' | awk 'NR>8')", shell=True).rstrip()
out2_6=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 9 | awk '{print $3}' | awk 'NR>8')", shell=True).rstrip()
out3_6=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 9 | awk '{print $4}' | awk 'NR>8')", shell=True).rstrip()
out4_6=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 9 | awk '{print $11}' | awk 'NR>8')", shell=True).rstrip()
print 'completed line8'
"""for nineth highest process"""
out_7=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 10 | awk '{print $1}' | awk 'NR>9')", shell=True).rstrip()
out1_7=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 10 | awk '{print $2}' | awk 'NR>9')", shell=True).rstrip()
out2_7=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 10 | awk '{print $3}' | awk 'NR>9')", shell=True).rstrip()
out3_7=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 10 | awk '{print $4}' | awk 'NR>9')", shell=True).rstrip()
out4_7=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 10 | awk '{print $11}' | awk 'NR>9')", shell=True).rstrip()
print 'completed line9'
"""for tenth highest process"""
out_8=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 11 | awk '{print $1}' | awk 'NR>10')", shell=True).rstrip()
out1_8=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 11 | awk '{print $2}' | awk 'NR>10')", shell=True).rstrip()
out2_8=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 11 | awk '{print $3}' | awk 'NR>10')", shell=True).rstrip()
out3_8=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 11 | awk '{print $4}' | awk 'NR>10')", shell=True).rstrip()
out4_8=subprocess.check_output("echo $(ps aux | sort -rk 3,3 | head -n 11 | awk '{print $11}' | awk 'NR>10')", shell=True).rstrip()
print 'completed line10'
print '<<<<<<<<<processes consuming High CPU>>>>>>>>'
print (' ')
template = "{0:10} {1:10} {2:12} {3:18} {4:100}"
print template.format("Username", "PID", "CPUUsage(%)", "MemoryUsage(%)", "Process")
print template.format(output, output1, output2, output3, output4)
print template.format(out, out1, out2, out3, out4)
print template.format(out_1, out1_1, out2_1, out3_1, out4_1)
print template.format(out_2, out1_2, out2_2, out3_2, out4_2)
print template.format(out_3, out1_3, out2_3, out3_3, out4_3)
print template.format(out_4, out1_4, out2_4, out3_4, out4_4)
print template.format(out_5, out1_5, out2_5, out3_5, out4_5)
print template.format(out_6, out1_6, out2_6, out3_6, out4_6)
print template.format(out_7, out1_7, out2_7, out3_7, out4_7)
print template.format(out_8, out1_8, out2_8, out3_8, out4_8)
"""print 'username    : '+output
print 'PID         : '+output1
print 'CPU usage   : '+output2
print 'memory usage: '+output3
print 'process     : '+output4
output5=subprocess.check_output("echo $(ps aux --sort -rss | head -n 2 | awk '{print $1}' | awk 'NR>1')", shell=True).rstrip()
output6=subprocess.check_output("echo $(ps aux --sort -rss | head -n 2 | awk '{print $2}' | awk 'NR>1')", shell=True).rstrip()
output7=subprocess.check_output("echo $(ps aux --sort -rss | head -n 2 | awk '{print $4}' | awk 'NR>1')", shell=True).rstrip()
output8=subprocess.check_output("echo $(ps aux --sort -rss | head -n 2 | awk '{print $11}' | awk 'NR>1')", shell=True).rstrip()
print (' ')
print '<<<<<<<<<process consuming High Memory>>>>>>'
print 'username    : '+output5
print 'PID         : '+output6
print 'memory usage: '+output7
print 'process     : '+output8
print (' ')"""
print '<<<<<<<<<<CPU load average>>>>>>>>>'
output9=subprocess.check_output("echo $(uptime | awk '{print $9}')", shell=True).rstrip()
output9_1=subprocess.check_output("echo $(uptime | awk '{print $10}')", shell=True).rstrip()
output9_2=subprocess.check_output("echo $(uptime | awk '{print $11}')", shell=True).rstrip()
print 'load average before 1 minute : '+output9
print 'load average before 5 minute : '+output9_1
print 'load average before 15 minute : '+output9_2
print (' ')
print '<<<<<<<<<<Memory details>>>>>>>>>'
output10=subprocess.check_output("echo $(free -m | head -n 2 | awk 'NR>1' | awk '{print $3}')", shell=True).rstrip()
output11=subprocess.check_output("echo $(free -m | head -n 2 | awk 'NR>1' | awk '{print $4}')", shell=True).rstrip()
print 'Used Memory : '+output10
print 'Free Memory : '+output11
print (' ')
print '<<<<<<<<<<Swap Memory details>>>>>>>>>'
output12=subprocess.check_output("echo $(free -m | head -n 4 | awk 'NR>3' | awk '{print $3}')", shell=True).rstrip()
output13=subprocess.check_output("echo $(free -m | head -n 4 | awk 'NR>3' | awk '{print $4}')", shell=True).rstrip()
print 'Used Memory : '+output12
print 'Free Memory : '+output13


