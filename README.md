Here is a clean **README.txt** version of your project, properly structured and ready to use:

---

# DETAILED PHONE NUMBER ANALYZER

A comprehensive Python tool for analyzing phone numbers with deep insights including validation, carrier info, geolocation, timezone, and interactive map generation.

---

## 🔑 API CONFIGURATION

OpenCage API Key:
07946bd7491c482885aa52325c0400f0

Free Tier Limits:

* 2,500 requests per day
* 1 request per second
* No credit card required

---

## 🚀 HOW TO USE

## Method 1: Run the Analyzer Script

Run the script directly:

```
python detailed_phone_analyzer.py
```

Then enter a phone number with country code when prompted.

## Method 2: Use in Python Code

Import and call the function:

```
from detailed_phone_analyzer import analyze_phone_number_detailed

analyze_phone_number_detailed("+447700900123", "YOUR_API_KEY")
```

---

## 📊 FEATURES (10 ANALYSIS SECTIONS)

1. VALIDATION & BASIC INFO

   * Valid / Possible number
   * Country code
   * National number
   * Extensions & leading zeros

2. NUMBER TYPE & CLASSIFICATION

   * Mobile, Landline, VoIP, Toll-Free, etc.
   * Type description and code

3. NUMBER FORMATTING

   * E164
   * International
   * National
   * RFC3966
   * Dialing formats (USA, UK, India)

4. GEOGRAPHICAL INFORMATION

   * Location (multi-language support)
   * Region code
   * Possible regions

5. CARRIER INFORMATION

   * Network provider
   * Local carrier details

6. TIMEZONE INFORMATION

   * Timezones associated with number
   * Current local time
   * UTC offset
   * DST status

7. DETAILED GEOCODING

   * Latitude / Longitude
   * Full address
   * Country, city, postal code
   * Confidence score
   * What3Words address
   * Geohash, MGRS, Maidenhead
   * Currency details
   * Sunrise / Sunset data

8. ADVANCED VALIDATION

   * International dialing support
   * Length validation
   * Emergency number detection

9. INTERACTIVE MAP

   * HTML map output
   * Marker with phone details
   * 50 km coverage radius

10. DATA EXPORT

* Full JSON export
* UTF-8 encoding
* Structured dataset

---

## 🌍 SAMPLE PHONE NUMBERS

USA:
+14155552671
+12125551234

UK:
+447700900123
+442071838750

India:
+919876543210
+912266000123

France:
+33123456789

Germany:
+493012345678

Australia:
+61291234567

Japan:
+81312345678

---

## 📁 OUTPUT FILES

After analysis, the following files are generated:

1. phone_map_<number>.html

   * Interactive map with marker and details

2. phone_analysis_<number>.json

   * Complete structured data export

---

## 💡 USAGE TIPS

* Always include country code with '+' prefix
  Example: +447700900123

* Spaces and formatting are optional

* Check JSON output for programmatic usage

* Open HTML map in browser for visualization

* Respect API rate limit (1 request/second)

---

## 🛠️ TROUBLESHOOTING

Invalid API Key:

* Ensure API key is correct
* Check internet connection
* Verify daily quota

Cannot Parse Number:

* Ensure correct format with country code

Location Not Available:

* Some numbers (VoIP/virtual) lack precise data

Geocoding Error:

* API may be temporarily unavailable

---

## 📚 REFERENCES

OpenCage API:
[https://opencagedata.com/api](https://opencagedata.com/api)

Phone Number Format (E.164):
[https://en.wikipedia.org/wiki/E.164](https://en.wikipedia.org/wiki/E.164)

Country Codes:
[https://countrycode.org/](https://countrycode.org/)

---

## ⚠️ PRIVACY & LEGAL NOTICE

This tool is intended for:

* Educational use
* Personal number analysis
* Development and testing

Not intended for:

* Unauthorized tracking
* Stalking or harassment
* Privacy law violations
* Commercial misuse without consent

Always comply with local laws and obtain proper authorization.

---

## ✅ END OF README

If you want, I can also convert this into a **GitHub README.md (with badges, formatting, and visuals)** or generate a **project structure with requirements.txt**.
