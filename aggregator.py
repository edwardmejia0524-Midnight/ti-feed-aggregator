import requests
import json
from datetime import datetime, timezone

# Defined threat intelligence sources for aggregation
FEED_SOURCES = [
    {
        "name": "Internal Honeypot Telemetry",
        "type": "IP",
        "sample_indicators": ["203.0.113.45", "198.51.100.23"]
    },
    {
        "name": "Simulated OSINT Feed",
        "type": "Domain",
        "sample_indicators": ["malicious-phishing-domain.test", "c2-callback-server.test"]
    }
]

def normalize_indicators():
    """Aggregates and normalizes indicators into a unified schema."""
    normalized_feed = []
    current_time = datetime.now(timezone.utc).isoformat()

    print("[*] Starting threat intelligence aggregation...")

    for source in FEED_SOURCES:
        print(f"[+] Processing source: {source['name']}")
        for item in source["sample_indicators"]:
            indicator_record = {
                "indicator": item,
                "indicator_type": source["type"],
                "source": source["name"],
                "confidence_score": 85 if "Honeypot" in source["name"] else 70,
                "first_seen": current_time,
                "status": "Active"
            }
            normalized_feed.append(indicator_record)

    return normalized_feed

def main():
    print("=" * 60)
    print(" Threat-Intelligence Feed Aggregator")
    print("=" * 60)

    indicators = normalize_indicators()

    print(f"[+] Total indicators normalized: {len(indicators)}")

    # Save to a unified JSON file
    output_filename = "unified_threat_feed.json"
    with open(output_filename, "w") as f:
        json.dump(indicators, f, indent=4)

    print(f"[+] Unified feed successfully exported to {output_filename}")
    print("=" * 60)

if __name__ == "__main__":
    main()
