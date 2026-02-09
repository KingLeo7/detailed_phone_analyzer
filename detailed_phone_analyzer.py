import phonenumbers
from phonenumbers import geocoder, carrier, timezone
from phonenumbers.phonenumberutil import NumberParseException
from opencage.geocoder import OpenCageGeocode
import folium
from datetime import datetime
import pytz
import json


def analyze_phone_number_detailed(number: str, api_key: str):
    """
    Comprehensive analysis of a phone number with maximum detail extraction
    """
    
    print("\n" + "="*80)
    print("COMPREHENSIVE PHONE NUMBER ANALYSIS")
    print("="*80)
    print(f"Analyzing Number: {number}")
    print(f"Analysis Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80)
    
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(number)
        
        # ============================================================
        # SECTION 1: VALIDATION & BASIC INFO
        # ============================================================
        print("\n┌─ SECTION 1: VALIDATION & BASIC INFORMATION")
        print("├" + "─"*78)
        
        is_valid = phonenumbers.is_valid_number(parsed_number)
        is_possible = phonenumbers.is_possible_number(parsed_number)
        
        print(f"│ Valid Number: {is_valid}")
        print(f"│ Possible Number: {is_possible}")
        print(f"│ Country Code: +{parsed_number.country_code}")
        print(f"│ National Number: {parsed_number.national_number}")
        
        if parsed_number.extension:
            print(f"│ Extension: {parsed_number.extension}")
        
        if parsed_number.italian_leading_zero:
            print(f"│ Italian Leading Zero: Yes")
        
        print(f"│ Number of Leading Zeros: {parsed_number.number_of_leading_zeros}")
        print(f"│ Raw Input: {parsed_number.raw_input if hasattr(parsed_number, 'raw_input') else 'N/A'}")
        
        # ============================================================
        # SECTION 2: NUMBER TYPE & CLASSIFICATION
        # ============================================================
        print("\n├─ SECTION 2: NUMBER TYPE & CLASSIFICATION")
        print("├" + "─"*78)
        
        number_type = phonenumbers.number_type(parsed_number)
        type_mapping = {
            0: "FIXED_LINE",
            1: "MOBILE",
            2: "FIXED_LINE_OR_MOBILE",
            3: "TOLL_FREE",
            4: "PREMIUM_RATE",
            5: "SHARED_COST",
            6: "VOIP",
            7: "PERSONAL_NUMBER",
            8: "PAGER",
            9: "UAN",
            10: "VOICEMAIL",
            99: "UNKNOWN"
        }
        
        type_descriptions = {
            0: "Traditional landline phone",
            1: "Mobile/cellular phone",
            2: "Could be either fixed line or mobile",
            3: "Free to call for the caller",
            4: "Premium rate service (costly)",
            5: "Shared cost between caller and receiver",
            6: "Voice over IP service",
            7: "Personal number service",
            8: "Paging device",
            9: "Universal Access Number",
            10: "Voicemail access number",
            99: "Type cannot be determined"
        }
        
        print(f"│ Number Type: {type_mapping.get(number_type, 'UNKNOWN')}")
        print(f"│ Description: {type_descriptions.get(number_type, 'Unknown type')}")
        print(f"│ Type Code: {number_type}")
        
        # ============================================================
        # SECTION 3: FORMATTING OPTIONS
        # ============================================================
        print("\n├─ SECTION 3: NUMBER FORMATTING")
        print("├" + "─"*78)
        
        formats = {
            "E164": phonenumbers.PhoneNumberFormat.E164,
            "INTERNATIONAL": phonenumbers.PhoneNumberFormat.INTERNATIONAL,
            "NATIONAL": phonenumbers.PhoneNumberFormat.NATIONAL,
            "RFC3966": phonenumbers.PhoneNumberFormat.RFC3966
        }
        
        for format_name, format_type in formats.items():
            formatted = phonenumbers.format_number(parsed_number, format_type)
            print(f"│ {format_name:20s}: {formatted}")
        
        # Out of country format examples
        print(f"│ {'From USA':20s}: {phonenumbers.format_out_of_country_calling_number(parsed_number, 'US')}")
        print(f"│ {'From UK':20s}: {phonenumbers.format_out_of_country_calling_number(parsed_number, 'GB')}")
        print(f"│ {'From India':20s}: {phonenumbers.format_out_of_country_calling_number(parsed_number, 'IN')}")
        
        # ============================================================
        # SECTION 4: GEOGRAPHICAL INFORMATION
        # ============================================================
        print("\n├─ SECTION 4: GEOGRAPHICAL INFORMATION")
        print("├" + "─"*78)
        
        # Get location in different languages
        location_en = geocoder.description_for_number(parsed_number, "en")
        
        print(f"│ Location (English): {location_en}")
        
        # Try other languages
        languages = {
            'de': 'German',
            'fr': 'French',
            'es': 'Spanish',
            'it': 'Italian',
            'zh': 'Chinese',
            'ja': 'Japanese',
            'ar': 'Arabic',
            'ru': 'Russian'
        }
        
        print("│")
        print("│ Location in Other Languages:")
        for lang_code, lang_name in languages.items():
            try:
                loc = geocoder.description_for_number(parsed_number, lang_code)
                if loc and loc != location_en:
                    print(f"│   {lang_name:15s}: {loc}")
            except:
                pass
        
        # Get region code
        region_code = phonenumbers.region_code_for_number(parsed_number)
        print(f"│")
        print(f"│ Region Code (ISO): {region_code}")
        
        # Get region from country code
        regions = phonenumbers.region_codes_for_country_code(parsed_number.country_code)
        print(f"│ Possible Regions: {', '.join(regions)}")
        
        # ============================================================
        # SECTION 5: CARRIER INFORMATION
        # ============================================================
        print("\n├─ SECTION 5: CARRIER & SERVICE PROVIDER")
        print("├" + "─"*78)
        
        carrier_name = carrier.name_for_number(parsed_number, "en")
        print(f"│ Carrier/Operator: {carrier_name if carrier_name else 'Unknown'}")
        
        # Try to get carrier in original language
        if region_code:
            carrier_local = carrier.name_for_number(parsed_number, region_code.lower())
            if carrier_local and carrier_local != carrier_name:
                print(f"│ Carrier (Local): {carrier_local}")
        
        # ============================================================
        # SECTION 6: TIMEZONE INFORMATION
        # ============================================================
        print("\n├─ SECTION 6: TIMEZONE & TIME INFORMATION")
        print("├" + "─"*78)
        
        timezones = timezone.time_zones_for_number(parsed_number)
        
        if timezones:
            print(f"│ Number of Timezones: {len(timezones)}")
            print(f"│ Timezone(s): {', '.join(timezones)}")
            print("│")
            
            for i, tz_name in enumerate(timezones, 1):
                try:
                    tz = pytz.timezone(tz_name)
                    current_time = datetime.now(tz)
                    utc_offset = current_time.strftime('%z')
                    
                    print(f"│ Timezone {i}: {tz_name}")
                    print(f"│   Current Time: {current_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
                    print(f"│   UTC Offset: {utc_offset}")
                    print(f"│   DST Active: {bool(current_time.dst())}")
                    
                    if i < len(timezones):
                        print("│")
                except Exception as e:
                    print(f"│   Error getting time: {e}")
        else:
            print("│ Timezone: Unknown")
        
        # ============================================================
        # SECTION 7: DETAILED GEOCODING
        # ============================================================
        print("\n├─ SECTION 7: DETAILED GEOCODING DATA")
        print("├" + "─"*78)
        
        geocoder_api = OpenCageGeocode(api_key)
        
        try:
            result = geocoder_api.geocode(location_en)
            
            if result and len(result) > 0:
                geo_data = result[0]
                
                # Coordinates
                print(f"│ Latitude: {geo_data['geometry']['lat']}")
                print(f"│ Longitude: {geo_data['geometry']['lng']}")
                print(f"│ Formatted Address: {geo_data['formatted']}")
                
                # Components
                components = geo_data['components']
                print("│")
                print("│ Address Components:")
                
                component_labels = {
                    'continent': 'Continent',
                    'country': 'Country',
                    'country_code': 'Country Code',
                    'state': 'State/Province',
                    'state_code': 'State Code',
                    'county': 'County',
                    'city': 'City',
                    'town': 'Town',
                    'village': 'Village',
                    'suburb': 'Suburb',
                    'postcode': 'Postal Code',
                    'road': 'Road',
                    'region': 'Region',
                    'ISO_3166-1_alpha-2': 'ISO Code (Alpha-2)',
                    'ISO_3166-1_alpha-3': 'ISO Code (Alpha-3)',
                }
                
                for key, label in component_labels.items():
                    if key in components:
                        print(f"│   {label:20s}: {components[key]}")
                
                # Additional metadata
                print("│")
                print("│ Geocoding Metadata:")
                print(f"│   Confidence: {geo_data.get('confidence', 'N/A')}/10")
                print(f"│   What3Words: {geo_data.get('annotations', {}).get('what3words', {}).get('words', 'N/A')}")
                
                annotations = geo_data.get('annotations', {})
                
                if 'DMS' in annotations:
                    dms = annotations['DMS']
                    print(f"│   DMS Coordinates: {dms.get('lat', 'N/A')}, {dms.get('lng', 'N/A')}")
                
                if 'MGRS' in annotations:
                    print(f"│   MGRS: {annotations['MGRS']}")
                
                if 'Maidenhead' in annotations:
                    print(f"│   Maidenhead: {annotations['Maidenhead']}")
                
                if 'geohash' in annotations:
                    print(f"│   Geohash: {annotations['geohash']}")
                
                if 'currency' in annotations:
                    curr = annotations['currency']
                    print(f"│   Currency: {curr.get('name', 'N/A')} ({curr.get('iso_code', 'N/A')})")
                    print(f"│   Currency Symbol: {curr.get('symbol', 'N/A')}")
                
                if 'callingcode' in annotations:
                    print(f"│   Calling Code: +{annotations['callingcode']}")
                
                if 'timezone' in annotations:
                    tz_info = annotations['timezone']
                    print(f"│   Timezone Name: {tz_info.get('name', 'N/A')}")
                    print(f"│   Timezone Offset: {tz_info.get('offset_string', 'N/A')}")
                
                if 'sun' in annotations:
                    sun = annotations['sun']
                    print(f"│   Sunrise: {sun.get('rise', {}).get('apparent', 'N/A')}")
                    print(f"│   Sunset: {sun.get('set', {}).get('apparent', 'N/A')}")
                
        except Exception as e:
            print(f"│ Geocoding Error: {e}")
        
        # ============================================================
        # SECTION 8: VALIDATION CHECKS
        # ============================================================
        print("\n├─ SECTION 8: ADVANCED VALIDATION CHECKS")
        print("├" + "─"*78)
        
        # Check if number can be internationally dialled
        print(f"│ Can be Dialled Internationally: {is_valid}")
        
        # Check length
        validation_result = phonenumbers.is_possible_number_with_reason(parsed_number)
        validation_reasons = {
            0: "IS_POSSIBLE",
            1: "INVALID_COUNTRY_CODE",
            2: "TOO_SHORT",
            3: "TOO_LONG",
            4: "IS_POSSIBLE_LOCAL_ONLY",
            5: "INVALID_LENGTH"
        }
        print(f"│ Possibility Status: {validation_reasons.get(validation_result, 'UNKNOWN')}")
        
        # Check if it's an emergency number
        try:
            is_emergency = phonenumbers.is_emergency_number(number, region_code)
            print(f"│ Emergency Number: {is_emergency}")
        except:
            print(f"│ Emergency Number: Cannot determine")
        
        # ============================================================
        # SECTION 9: GENERATE MAP
        # ============================================================
        print("\n├─ SECTION 9: GENERATING INTERACTIVE MAP")
        print("├" + "─"*78)
        
        try:
            if result and len(result) > 0:
                lat = result[0]['geometry']['lat']
                lng = result[0]['geometry']['lng']
                
                # Create detailed map
                phone_map = folium.Map(
                    location=[lat, lng],
                    zoom_start=10,
                    tiles='OpenStreetMap'
                )
                
                # Create popup HTML
                popup_html = f"""
                <div style="font-family: Arial, sans-serif; width: 350px;">
                    <h3 style="color: #2c3e50; margin-bottom: 10px;">📱 Phone Number Details</h3>
                    <hr style="border: 1px solid #3498db;">
                    
                    <h4 style="color: #34495e;">Number Information</h4>
                    <table style="width: 100%; font-size: 12px;">
                        <tr><td><b>Number:</b></td><td>{phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}</td></tr>
                        <tr><td><b>Type:</b></td><td>{type_mapping.get(number_type, 'UNKNOWN')}</td></tr>
                        <tr><td><b>Valid:</b></td><td>{'✅ Yes' if is_valid else '❌ No'}</td></tr>
                    </table>
                    
                    <h4 style="color: #34495e; margin-top: 10px;">Location</h4>
                    <table style="width: 100%; font-size: 12px;">
                        <tr><td><b>Country:</b></td><td>{components.get('country', 'Unknown')}</td></tr>
                        <tr><td><b>City:</b></td><td>{components.get('city', components.get('town', 'Unknown'))}</td></tr>
                        <tr><td><b>Coordinates:</b></td><td>{lat:.4f}, {lng:.4f}</td></tr>
                    </table>
                    
                    <h4 style="color: #34495e; margin-top: 10px;">Service</h4>
                    <table style="width: 100%; font-size: 12px;">
                        <tr><td><b>Carrier:</b></td><td>{carrier_name if carrier_name else 'Unknown'}</td></tr>
                        <tr><td><b>Timezone:</b></td><td>{', '.join(timezones) if timezones else 'Unknown'}</td></tr>
                    </table>
                </div>
                """
                
                # Add marker
                folium.Marker(
                    [lat, lng],
                    popup=folium.Popup(popup_html, max_width=400),
                    tooltip=f"{number} - {location_en}",
                    icon=folium.Icon(color='red', icon='phone', prefix='fa')
                ).add_to(phone_map)
                
                # Add circle
                folium.Circle(
                    [lat, lng],
                    radius=50000,  # 50km
                    color='red',
                    fill=True,
                    fillColor='red',
                    fillOpacity=0.2,
                    popup=f'Approximate coverage area (50km radius)'
                ).add_to(phone_map)
                
                # Save map
                map_filename = f"phone_map_{parsed_number.national_number}.html"
                phone_map.save(map_filename)
                print(f"│ Map Generated: {map_filename}")
                print(f"│ Map Center: {lat}, {lng}")
                print(f"│ Coverage Radius: 50km")
            else:
                print("│ Cannot generate map: Location data unavailable")
        except Exception as e:
            print(f"│ Map Generation Error: {e}")
        
        # ============================================================
        # SECTION 10: EXPORT DATA
        # ============================================================
        print("\n├─ SECTION 10: DATA EXPORT")
        print("├" + "─"*78)
        
        # Create comprehensive data dictionary
        export_data = {
            "analysis_timestamp": datetime.now().isoformat(),
            "input_number": number,
            "parsed_data": {
                "country_code": parsed_number.country_code,
                "national_number": str(parsed_number.national_number),
                "extension": parsed_number.extension,
                "number_of_leading_zeros": parsed_number.number_of_leading_zeros
            },
            "validation": {
                "is_valid": is_valid,
                "is_possible": is_possible,
                "validation_result": validation_reasons.get(validation_result, 'UNKNOWN')
            },
            "classification": {
                "number_type": type_mapping.get(number_type, 'UNKNOWN'),
                "type_code": number_type,
                "description": type_descriptions.get(number_type, 'Unknown')
            },
            "formatting": {
                "e164": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164),
                "international": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL),
                "national": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL),
                "rfc3966": phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.RFC3966)
            },
            "geography": {
                "location": location_en,
                "region_code": region_code,
                "possible_regions": regions
            },
            "carrier": {
                "name": carrier_name if carrier_name else "Unknown"
            },
            "timezone": {
                "zones": list(timezones) if timezones else [],
                "count": len(timezones) if timezones else 0
            }
        }
        
        # Add geocoding data if available
        if result and len(result) > 0:
            export_data["geocoding"] = {
                "latitude": result[0]['geometry']['lat'],
                "longitude": result[0]['geometry']['lng'],
                "formatted_address": result[0]['formatted'],
                "components": result[0]['components'],
                "confidence": result[0].get('confidence', None)
            }
        
        # Save to JSON
        json_filename = f"phone_analysis_{parsed_number.national_number}.json"
        with open(json_filename, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=4, ensure_ascii=False)
        
        print(f"│ JSON Export: {json_filename}")
        print(f"│ Data Size: {len(json.dumps(export_data))} bytes")
        print(f"│ Encoding: UTF-8")
        
        print("\n└" + "─"*78)
        print("\n✅ ANALYSIS COMPLETED SUCCESSFULLY")
        print("="*80)
        
    except NumberParseException as e:
        print(f"\n❌ ERROR: Unable to parse phone number")
        print(f"Reason: {e}")
        print("="*80)
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        print("="*80)


if __name__ == "__main__":
    # Your API key
    API_KEY = "07946bd7491c482885aa52325c0400f0"
    
    # Get phone number from user
    print("="*80)
    print("DETAILED PHONE NUMBER ANALYZER")
    print("="*80)
    print("\nEnter phone number with country code (e.g., +1234567890, +447700900123)")
    print("Examples:")
    print("  USA: +14155552671")
    print("  UK: +447700900123")
    print("  India: +919876543210")
    print("  France: +33123456789")
    print("\n" + "="*80)
    
    phone_number = input("\n📱 Enter phone number: ").strip()
    
    if phone_number:
        analyze_phone_number_detailed(phone_number, API_KEY)
    else:
        print("❌ No phone number provided!")
