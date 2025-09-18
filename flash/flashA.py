import time
import random
import sys

class HardwareFlasher:
    def __init__(self):
        self.start_time = time.time()
        self.flash_count = 0
        self.status = "READY"
        
    def simulate_flash(self):
        """Simulate a single flash operation"""
        self.status = "FLASHING"
        
        # Simulate flash preparation (1-2 seconds)
        prep_time = random.uniform(1.0, 2.0)
        print(f"[{time.strftime('%H:%M:%S')}] Preparing flash...")
        time.sleep(prep_time)
        
        # Simulate actual flash writing (0.5-1.5 seconds)
        write_time = random.uniform(0.5, 1.5)
        print(f"[{time.strftime('%H:%M:%S')}] Writing firmware...")
        time.sleep(write_time)
        
        # Simulate verification (0.5-1 second)
        verify_time = random.uniform(0.5, 1.0)
        print(f"[{time.strftime('%H:%M:%S')}] Verifying...")
        time.sleep(verify_time)
        
        # 95% success rate simulation
        success = random.random() > 0.05
        if success:
            self.status = "SUCCESS"
            print(f"[{time.strftime('%H:%M:%S')}] Flash completed successfully!")
        else:
            self.status = "FAILED"
            print(f"[{time.strftime('%H:%M:%S')}] Flash failed! Retrying...")
            
        self.flash_count += 1
        return success
    
    def run_flashing_simulation(self, duration=30):
        """Run the flashing simulation for specified duration"""
        print("=" * 50)
        print("Hardware Flashing Simulation")
        print("=" * 50)
        print(f"Starting simulation for {duration} seconds...")
        print()
        
        end_time = self.start_time + duration
        
        while time.time() < end_time:
            remaining = end_time - time.time()
            
            print(f"\n--- Flash Operation #{self.flash_count + 1} ---")
            print(f"Time remaining: {remaining:.1f}s")
            
            success = self.simulate_flash()
            
            if not success:
                # Wait before retry on failure
                retry_delay = random.uniform(1.0, 3.0)
                print(f"Waiting {retry_delay:.1f}s before retry...")
                time.sleep(retry_delay)
            else:
                # Small delay between successful flashes
                time.sleep(0.5)
        
        self.print_summary()
    
    def print_summary(self):
        """Print simulation summary"""
        print("\n" + "=" * 50)
        print("Simulation Complete!")
        print("=" * 50)
        print(f"Total runtime: {time.time() - self.start_time:.1f}s")
        print(f"Total flash operations: {self.flash_count}")
        print(f"Final status: {self.status}")
        print("=" * 50)

def main():
    """Main function to run the flashing simulation"""
    try:
        flasher = HardwareFlasher()
        flasher.run_flashing_simulation(duration=30)
    except KeyboardInterrupt:
        print("\n\nSimulation interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError during simulation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
