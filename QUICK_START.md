# Quick Start Guide - Detailed Phone Number Analysis

## 🔑 Your API Key Configuration

Your OpenCage API key is already configured:
```
07946bd7491c482885aa52325c0400f0
```

**API Limits:**
- Free tier: 2,500 requests/day
- Rate limit: 1 request/second
- No credit card required

## 🚀 How to Use

### Method 1: Run the Detailed Analyzer (Recommended)

```bash
python detailed_phone_analyzer.py
```

Then enter any phone number with country code when prompted.

### Method 2: Quick Analysis in Python

```python
from detailed_phone_analyzer import analyze_phone_number_detailed

# Analyze any number
analyze_phone_number_detailed("+447700900123", "07946bd7491c482885aa52325c0400f0")
```

## 📊 What Information You'll Get

The analyzer provides **10 comprehensive sections**:

### Section 1: Validation & Basic Info
- ✅ Is the number valid?
- ✅ Is it possible?
- Country code
- National number
- Extension (if any)
- Leading zeros

### Section 2: Number Type & Classification
- Mobile, Fixed Line, VoIP, Toll-Free, etc.
- Detailed description
- Type code

### Section 3: Number Formatting
- E164 format
- International format
- National format
- RFC3966 format
- How to dial from USA, UK, India

### Section 4: Geographical Information
- Location in English
- Location in 8+ other languages
- ISO region code
- All possible regions

### Section 5: Carrier Information
- Service provider name
- Operator details
- Local carrier name

### Section 6: Timezone & Time
- All applicable timezones
- Current local time
- UTC offset
- Daylight Saving Time status

### Section 7: Detailed Geocoding
- Exact coordinates (latitude/longitude)
- Full formatted address
- Country, state, city, postal code
- Confidence score
- What3Words address
- DMS coordinates
- MGRS, Maidenhead, Geohash
- Currency information
- Sunrise/sunset times

### Section 8: Advanced Validation
- International dialing capability
- Length validation
- Emergency number check
- Detailed validation status

### Section 9: Interactive Map
- HTML map with marker
- 50km coverage radius
- Detailed popup information
- Coordinates display

### Section 10: Data Export
- Complete JSON export
- UTF-8 encoding
- All data preserved

## 🌍 Example Phone Numbers to Test

### United States
```
+14155552671  (San Francisco)
+12125551234  (New York)
+13105551234  (Los Angeles)
```

### United Kingdom
```
+447700900123  (Mobile)
+442071838750  (London)
+441632960123  (Fictional)
```

### India
```
+919876543210  (Mobile)
+912266000123  (Mumbai)
+911140000123  (Delhi)
```

### France
```
+33123456789  (Paris)
+33612345678  (Mobile)
```

### Germany
```
+493012345678  (Berlin)
+491512345678  (Mobile)
```

### Australia
```
+61291234567  (Sydney)
+61412345678  (Mobile)
```

### Japan
```
+81312345678  (Tokyo)
+819012345678  (Mobile)
```

## 📁 Output Files Generated

After analysis, you'll get:

1. **phone_map_[number].html** - Interactive map
2. **phone_analysis_[number].json** - Complete data export

## 🔍 Sample Output Structure

```
================================================================================
COMPREHENSIVE PHONE NUMBER ANALYSIS
================================================================================
Analyzing Number: +447700900123
Analysis Time: 2024-02-09 15:30:45
================================================================================

┌─ SECTION 1: VALIDATION & BASIC INFORMATION
├──────────────────────────────────────────────────────────────────────────────
│ Valid Number: True
│ Possible Number: True
│ Country Code: +44
│ National Number: 7700900123
│ Number of Leading Zeros: 0
│ Raw Input: N/A

┌─ SECTION 2: NUMBER TYPE & CLASSIFICATION
├──────────────────────────────────────────────────────────────────────────────
│ Number Type: MOBILE
│ Description: Mobile/cellular phone
│ Type Code: 1

... [8 more detailed sections]
```

## 💡 Pro Tips

1. **Always include the country code** (+ prefix)
   - ✅ Correct: `+447700900123`
   - ❌ Wrong: `447700900123` or `7700900123`

2. **No spaces or formatting needed**
   - Both work: `+44 7700 900123` or `+447700900123`

3. **Check the JSON export** for programmatic access to data

4. **View the HTML map** in any browser for visual location

5. **API rate limits**: Wait 1 second between requests

## 🛠️ Troubleshooting

### "Invalid API Key"
- Your key is already configured correctly
- Check your internet connection
- Verify you haven't exceeded 2,500 requests/day

### "Cannot parse phone number"
- Make sure to include the + and country code
- Example: `+1` for USA, `+44` for UK

### "Location data unavailable"
- Some numbers don't have precise location data
- Virtual/VoIP numbers may have limited info

### "Geocoding Error"
- API might be temporarily unavailable
- Check your daily request limit

## 📞 Need More Help?

- OpenCage Documentation: https://opencagedata.com/api
- Phone number formats: https://en.wikipedia.org/wiki/E.164
- Country codes: https://countrycode.org/

## ⚠️ Privacy & Legal Notice

This tool is for:
✅ Educational purposes
✅ Personal phone number analysis
✅ Verification of your own numbers
✅ Development and testing

NOT for:
❌ Stalking or harassment
❌ Unauthorized tracking
❌ Violation of privacy laws
❌ Commercial use without proper consent

Always respect privacy laws and obtain proper authorization before analyzing phone numbers.

---

**Enjoy analyzing phone numbers with maximum detail! 🎉**
