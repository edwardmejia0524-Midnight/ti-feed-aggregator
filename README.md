# TI Feed Aggregator

## 1. Executive Summary

The `ti-feed-aggregator` is a Python-based security automation utility engineered to collect, normalize, and standardize Indicators of Compromise (IOCs) from disparate threat intelligence sources into a unified, structured JSON feed. This utility streamlines indicator ingestion for Security Information and Event Management (SIEM) platforms, firewalls, and security orchestration tools.

## 2. Environment & Architecture

- **Programming Language**: Python 3.x
- **Configuration Source**: Multi-source JSON mapping 
- **Output Format**: Standardized JSON schema containing IPv4 addresses, domains, and cryptographic file hashes with metadata scoring and timestamps.

### Repository Directory Structure

```text
ti-feed-aggregator/
├── assets/
│   └── execution.png         # CLI execution & output verification screenshot
├── config/
│   └── sources.json          # Threat intelligence source definitions
├── output/
│   └── normalized_iocs.json  # Standardized output feed
├── src/
│   └── aggregator.py         # Core execution and normalization script
├── .gitignore                # Git ignore exclusions
├── requirements.txt          # Python package dependencies
└── README.md                 # Technical project documentation
```

## 3. Implementation Details

### Configuration Management 

Defines external ingestion endpoints, data types (IP, domain, hash), refresh cadences, and source enablement flags to govern data collection streams.

### Normalization Engine 

The core Python script executes the following modular workflow:

1. **Source Ingestion**: Loads active intelligence feeds from the JSON configuration directory.
2. **Data Transformation**: Parses raw telemetry across multiple threat vectors.
3. **Standardization**: Normalizes disparate data structures into a unified dictionary model featuring standardized confidence ratings (`high`, `medium`) and UTC timestamps.
4. **Export**: Compiles the unified payload and outputs it to `output/normalized_iocs.json` for downstream consumption.

## 4. Execution & Verification

To run the aggregation script locally:

```bash
python3 src/aggregator.py
```

**Execution Output & Verification**

![Execution Output & Verification]
