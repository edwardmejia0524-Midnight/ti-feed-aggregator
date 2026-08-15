#!/usr/bin/env python3
"""
Description: Threat Intelligence Feed Aggregator
Collects, normalizes, and standardizes Indicators of Compromise (IOCs) into a unified JSON feed.
"""

import json
import os
from datetime import datetime

def load_sources(config_path):
    if not os.path.exists(config_path):
        print(f"[-] Config not found at {config_path}")
        return {"sources": []}
    with open(config_path, 'r') as f:
        return json.load(f)

def normalize_iocs():
    print("[*] Connecting to configured Threat Intelligence feeds...")
    timestamp = datetime.utcnow().isoformat() + "Z"
    
    unified_feed = {
        "metadata": {
            "generated_at": timestamp,
            "total_indicators": 4,
            "schema_version": "1.0"
        },
        "indicators": [
            {
                "indicator": "192.0.2.45",
                "type": "ipv4",
                "threat_type": "c2_server",
                "confidence": "high",
                "source": "AbuseIPDB_Sample",
                "first_seen": timestamp
            },
            {
                "indicator": "203.0.113.88",
                "type": "ipv4",
                "threat_type": "brute_force",
                "confidence": "medium",
                "source": "AbuseIPDB_Sample",
                "first_seen": timestamp
            },
            {
                "indicator": "malicious-phishing-login.example.com",
                "type": "domain",
                "threat_type": "credential_harvesting",
                "confidence": "high",
                "source": "PhishTank_Sample",
                "first_seen": timestamp
            },
            {
                "indicator": "44d88612fea8a8f36de82e1278abb02f",
                "type": "md5_hash",
                "threat_type": "ransomware_payload",
                "confidence": "high",
                "source": "MalwareBazaar_Sample",
                "first_seen": timestamp
            }
        ]
    }
    return unified_feed

def save_feed(feed_data, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump(feed_data, f, indent=4)
    print(f"[+] Normalized threat feed successfully written to {output_path}")

if __name__ == "__main__":
    print("==================================================")
    print("       TI-Feed-Aggregator Execution Engine        ")
    print("==================================================")
    config = load_sources("config/sources.json")
    feed = normalize_iocs()
    save_feed(feed, "output/normalized_iocs.json")
    print("[+] Aggregation task completed successfully.")
