# FastAPI

curl -X POST "http://localhost:8000/query" \
     -H "Content-Type: application/json" \
     -d '{"text": "What are the key features of the NextGen Smartwatch?", "n_results": 3}'

{
  "query": "What are the key features of the NextGen Smartwatch?",
  "results": [
    {
      "text": "User Guide: NextGen Smartwatch  1. Getting Started    - Charging your device    - Pairing with your smartphone    - Initial setup and customization  2. Basic Operations    - Navigating the interface    - Customizing watch faces    - Managing notifications  3. Health and Fitness Features    - Setting up health monitoring    - Using the workout modes    - Viewing and interpreting health data  4. Smart Assistant    - Activating voice commands    - Setting reminders and alarms    - Using the AI-powered suggestions  5. Troubleshooting    - Common issues and solutions    - Updating firmware    - Contacting support",
      "metadata": {
        "chunk": 0,
        "source": "./data/user_guide.txt"
      },
      "distance": 0.4619564414024353
    },
    {
      "text": "Product Launch: NextGen Smartwatch  Key Features: 1. Advanced Health Monitoring: Tracks heart rate, blood oxygen, and stress levels. 2. Extended Battery Life: Up to 7 days on a single charge. 3. AI-Powered Personal Assistant: Contextual reminders and suggestions. 4. Customizable Watch Faces: Over 1000 designs available. 5. Water Resistant: Up to 50 meters.  Target Market: - Health-conscious individuals - Tech enthusiasts - Fitness enthusiasts  Launch Date: October 15, 2024 Retail Price: $299.99",
      "metadata": {
        "chunk": 0,
        "source": "./data/product_launch.txt"
      },
      "distance": 0.6149939894676208
    },
    {
      "text": "Technical Specifications - NextGen Smartwatch  Display: 1.4\" AMOLED, 454 x 454 pixels Processor: Dual-core 1.2 GHz Memory: 1GB RAM, 8GB Storage Sensors: Heart rate, SpO2, Accelerometer, Gyroscope, Altimeter Connectivity: Bluetooth 5.0, Wi-Fi, NFC, GPS Battery: 420mAh, up to 7 days typical use Water Resistance: 5 ATM (up to 50 meters) Compatibility: iOS 12+ and Android 8.0+ Dimensions: 44 x 44 x 10.7 mm Weight: 36g (without strap)",
      "metadata": {
        "chunk": 0,
        "source": "./data/technical_specifications.txt"
      },
      "distance": 0.6327174305915833
    }
  ]
}
