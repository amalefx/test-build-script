import time
import random
import sys
from enum import Enum

class TestStatus(Enum):
    PASS = "PASS"
    FAIL = "FAIL"
    RUNNING = "RUNNING"
    PENDING = "PENDING"

class HardwareTester:
    def __init__(self):
        self.start_time = time.time()
        self.tests_completed = 0
        self.tests_passed = 0
        self.tests_failed = 0
        self.current_test = None
        
    def simulate_memory_test(self):
        """Simulate memory testing"""
        test_time = random.uniform(1.5, 3.0)
        print(f"  Testing RAM modules...")
        time.sleep(test_time * 0.3)
        print(f"  Verifying memory addresses...")
        time.sleep(test_time * 0.4)
        print(f"  Running memory stress test...")
        time.sleep(test_time * 0.3)
        
        # 90% success rate for memory test
        return random.random() > 0.1, test_time
    
    def simulate_cpu_test(self):
        """Simulate CPU testing"""
        test_time = random.uniform(2.0, 4.0)
        print(f"  Testing processor cores...")
        time.sleep(test_time * 0.2)
        print(f"  Running floating point operations...")
        time.sleep(test_time * 0.3)
        print(f"  Testing cache performance...")
        time.sleep(test_time * 0.3)
        print(f"  Checking thermal management...")
        time.sleep(test_time * 0.2)
        
        # 95% success rate for CPU test
        return random.random() > 0.05, test_time
    
    def simulate_storage_test(self):
        """Simulate storage device testing"""
        test_time = random.uniform(2.5, 5.0)
        print(f"  Testing read/write speeds...")
        time.sleep(test_time * 0.4)
        print(f"  Checking disk integrity...")
        time.sleep(test_time * 0.3)
        print(f"  Verifying storage capacity...")
        time.sleep(test_time * 0.3)
        
        # 85% success rate for storage test
        return random.random() > 0.15, test_time
    
    def simulate_network_test(self):
        """Simulate network interface testing"""
        test_time = random.uniform(1.0, 2.5)
        print(f"  Testing network connectivity...")
        time.sleep(test_time * 0.3)
        print(f"  Checking packet transmission...")
        time.sleep(test_time * 0.4)
        print(f"  Verifying network speed...")
        time.sleep(test_time * 0.3)
        
        # 80% success rate for network test (more prone to issues)
        return random.random() > 0.2, test_time
    
    def simulate_gpu_test(self):
        """Simulate graphics card testing"""
        test_time = random.uniform(2.0, 3.5)
        print(f"  Testing graphics rendering...")
        time.sleep(test_time * 0.3)
        print(f"  Checking video output...")
        time.sleep(test_time * 0.3)
        print(f"  Running 3D performance test...")
        time.sleep(test_time * 0.4)
        
        # 88% success rate for GPU test
        return random.random() > 0.12, test_time
    
    def run_test(self, test_name):
        """Run a specific hardware test"""
        print(f"\n[{time.strftime('%H:%M:%S')}] Starting {test_name}...")
        self.current_test = test_name
        
        test_functions = {
            "Memory Test": self.simulate_memory_test,
            "CPU Test": self.simulate_cpu_test,
            "Storage Test": self.simulate_storage_test,
            "Network Test": self.simulate_network_test,
            "GPU Test": self.simulate_gpu_test
        }
        
        if test_name in test_functions:
            success, duration = test_functions[test_name]()
            status = TestStatus.PASS if success else TestStatus.FAIL
            
            print(f"[{time.strftime('%H:%M:%S')}] {test_name}: {status.value} ({duration:.1f}s)")
            return success, duration
        
        return False, 0
    
    def run_test_suite(self, duration=30):
        """Run the complete hardware test suite"""
        print("=" * 60)
        print("HARDWARE TESTING SIMULATION")
        print("=" * 60)
        print(f"Starting comprehensive hardware test suite...")
        print(f"Test duration: {duration} seconds")
        print("=" * 60)
        
        test_cases = [
            "Memory Test",
            "CPU Test", 
            "Storage Test",
            "Network Test",
            "GPU Test"
        ]
        
        end_time = self.start_time + duration
        test_cycle = 0
        
        while time.time() < end_time:
            test_cycle += 1
            print(f"\n{'#' * 30}")
            print(f"TEST CYCLE {test_cycle}")
            print(f"{'#' * 30}")
            
            # Shuffle test order for variety
            random.shuffle(test_cases)
            
            for test in test_cases:
                if time.time() >= end_time:
                    break
                    
                success, test_duration = self.run_test(test)
                self.tests_completed += 1
                
                if success:
                    self.tests_passed += 1
                else:
                    self.tests_failed += 1
                    print(f"  !!! {test} FAILED - will retry in next cycle !!!")
        
        self.print_summary()
    
    def print_summary(self):
        """Print detailed test summary"""
        total_time = time.time() - self.start_time
        pass_rate = (self.tests_passed / self.tests_completed * 100) if self.tests_completed > 0 else 0
        
        print("\n" + "=" * 60)
        print("HARDWARE TEST SUMMARY")
        print("=" * 60)
        print(f"Total test time: {total_time:.1f}s")
        print(f"Test cycles completed: {self.tests_completed // 5}")
        print(f"Total tests run: {self.tests_completed}")
        print(f"Tests passed: {self.tests_passed} ({pass_rate:.1f}%)")
        print(f"Tests failed: {self.tests_failed}")
        print("=" * 60)
        
        if pass_rate >= 95:
            print("OVERALL STATUS: EXCELLENT - All systems nominal")
        elif pass_rate >= 85:
            print("OVERALL STATUS: GOOD - Minor issues detected")
        elif pass_rate >= 70:
            print("OVERALL STATUS: FAIR - Several issues need attention")
        else:
            print("OVERALL STATUS: POOR - Significant hardware problems")
        print("=" * 60)

def main():
    """Main function to run the hardware testing simulation"""
    try:
        print("Initializing hardware testing environment...")
        time.sleep(1)
        
        tester = HardwareTester()
        tester.run_test_suite(duration=30)
        
    except KeyboardInterrupt:
        print("\n\nTesting interrupted by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\nError during testing: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
