<b>Monitoring System Health with Disk and CPU Usage Checks</b>

In this code, the check_disk_usage function checks the available free space on the specified disk (in this case, the root directory) and returns True if there is more than 20% free space. The check_cpu_usage function checks the current CPU usage and returns True if it is less than 75%.

If either of these checks fail (i.e., there is not enough free disk space or the CPU usage is too high), an error message is printed. If both checks pass, the program then checks the localhost and connectivity using the check_localhost and check_connectivity functions from the network module. If these checks pass, a message indicating that everything is okay is printed. If either of these checks fail, a message indicating that the network checks have failed is printed.
