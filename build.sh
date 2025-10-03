#!/bin/bash

# Random System Monitor Script
# Logs system information and simulated activities

SCRIPT_NAME="sys_monitor_$(date +%Y%m%d_%H%M%S)"
DURATION=$((RANDOM % 120 + 60))  # Random duration between 60-180 seconds
INTERVAL=$((RANDOM % 5 + 2))     # Random interval between 2-7 seconds

echo "=== Starting System Monitor Script ==="
echo "Script: $SCRIPT_NAME"
echo "Duration: $DURATION seconds"
echo "Interval: $INTERVAL seconds"
echo "======================================"

start_time=$(date +%s)
end_time=$((start_time + DURATION))
iteration=1

# Array of random activities
activities=(
    "Checking disk usage"
    "Monitoring CPU load"
    "Scanning network connections"
    "Verifying system processes"
    "Analyzing memory usage"
    "Testing disk I/O performance"
    "Checking system temperature"
    "Monitoring user activity"
    "Scanning for security updates"
    "Testing network bandwidth"
)

# Array of status messages
statuses=("OK" "WARNING" "CRITICAL" "INFO" "DEBUG")

while [ $(date +%s) -lt $end_time ]; do
    current_time=$(date '+%Y-%m-%d %H:%M:%S')
    random_activity=${activities[$RANDOM % ${#activities[@]}]}
    random_status=${statuses[$RANDOM % ${#statuses[@]}]}
    
    # Generate some random metrics
    cpu_load=$(awk -v min=1 -v max=100 'BEGIN{srand(); print int(min+rand()*(max-min+1))}')
    mem_usage=$(awk -v min=20 -v max=95 'BEGIN{srand(); print int(min+rand()*(max-min+1))}')
    disk_usage=$(awk -v min=5 -v max=90 'BEGIN{srand(); print int(min+rand()*(max-min+1))}')
    
    # Log the information
    echo "[$current_time] Iteration $iteration - $random_activity [$random_status]"
    echo "  CPU Load: ${cpu_load}% | Memory Usage: ${mem_usage}% | Disk Usage: ${disk_usage}%"
    
    # Occasionally add some special events
    if [ $((iteration % 3)) -eq 0 ]; then
        special_events=(
            "Performing routine maintenance"
            "Cleaning temporary files"
            "Rotating log files"
            "Updating system cache"
            "Optimizing database"
        )
        random_event=${special_events[$RANDOM % ${#special_events[@]}]}
        echo "  ⚡ SPECIAL EVENT: $random_event"
    fi
    
    # Add some random errors occasionally
    if [ $((RANDOM % 10)) -eq 0 ]; then
        error_messages=(
            "Failed to connect to remote server"
            "Disk write error on /dev/sda1"
            "High memory consumption detected"
            "Network latency above threshold"
            "Service restart required"
        )
        random_error=${error_messages[$RANDOM % ${#error_messages[@]}]}
        echo "  ❌ ERROR: $random_error"
    fi
    
    echo "----------------------------------------"
    
    iteration=$((iteration + 1))
    sleep $INTERVAL
done

# Final summary
end_time_formatted=$(date '+%Y-%m-%d %H:%M:%S')
total_iterations=$((iteration - 1))
echo "========================================"
echo "=== Script Completed ==="
echo "End Time: $end_time_formatted"
echo "Total Iterations: $total_iterations"
echo "Total Duration: $DURATION seconds"
echo "Average Interval: $INTERVAL seconds"
echo "========================================"
