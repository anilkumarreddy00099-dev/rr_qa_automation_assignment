import os
import time

def capture_screenshot(driver, name):
    os.makedirs("reports/screenshots", exist_ok=True)
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    path = f"reports/screenshots/{name}_{timestamp}.png"
    driver.save_screenshot(path)
    return path
