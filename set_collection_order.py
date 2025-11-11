#!/usr/bin/env python3
"""
Set collection sort order using metafields.

This script sets a 'sort_order' metafield on each collection to control
the display order. Lower numbers appear first.

Usage:
    python set_collection_order.py

The script will:
1. Connect to your Shopify store
2. List all collections
3. Allow you to set sort_order for each collection
4. Update metafields via Shopify API
"""

import os
import sys
from typing import Dict, List, Optional
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Shopify API configuration
SHOP_URL = os.getenv('SHOPIFY_STORE_URL_FUTUR_VILLAS', 'xjtm5x-pp.myshopify.com')
ACCESS_TOKEN = os.getenv('SHOPIFY_CLI_THEME_TOKEN_FUTUR_VILLAS')
API_VERSION = '2025-10'

if not ACCESS_TOKEN:
    print("❌ Error: SHOPIFY_CLI_THEME_TOKEN_FUTUR_VILLAS not found in environment")
    print("Please set up your .env file with Shopify credentials")
    sys.exit(1)

# API endpoint base
API_BASE = f"https://{SHOP_URL}/admin/api/{API_VERSION}"

# Headers for API requests
HEADERS = {
    'X-Shopify-Access-Token': ACCESS_TOKEN,
    'Content-Type': 'application/json'
}


def get_all_collections() -> List[Dict]:
    """Fetch all collections from Shopify."""
    collections = []
    url = f"{API_BASE}/collections.json"

    while url:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()

        data = response.json()
        collections.extend(data.get('collections', []))

        # Check for pagination
        link_header = response.headers.get('Link', '')
        url = None
        if 'rel="next"' in link_header:
            # Extract next URL from Link header
            for link in link_header.split(','):
                if 'rel="next"' in link:
                    url = link[link.find('<')+1:link.find('>')]
                    break

    return collections


def get_collection_metafields(collection_id: int) -> List[Dict]:
    """Get metafields for a collection."""
    url = f"{API_BASE}/collections/{collection_id}/metafields.json"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()
    return response.json().get('metafields', [])


def set_collection_sort_order(collection_id: int, sort_order: int) -> bool:
    """Set the sort_order metafield for a collection."""

    # First, check if metafield already exists
    existing_metafields = get_collection_metafields(collection_id)
    existing_metafield = None

    for mf in existing_metafields:
        if (mf.get('namespace') == 'custom' and
            mf.get('key') == 'sort_order'):
            existing_metafield = mf
            break

    metafield_data = {
        "metafield": {
            "namespace": "custom",
            "key": "sort_order",
            "value": str(sort_order),
            "type": "number_integer"
        }
    }

    if existing_metafield:
        # Update existing metafield
        url = f"{API_BASE}/collections/{collection_id}/metafields/{existing_metafield['id']}.json"
        response = requests.put(url, headers=HEADERS, json=metafield_data)
    else:
        # Create new metafield
        url = f"{API_BASE}/collections/{collection_id}/metafields.json"
        response = requests.post(url, headers=HEADERS, json=metafield_data)

    if response.status_code in [200, 201]:
        return True
    else:
        print(f"❌ Error setting metafield: {response.status_code}")
        print(response.text)
        return False


def set_multiple_collections(collection_orders: Dict[str, int]) -> None:
    """
    Set sort order for multiple collections.

    Args:
        collection_orders: Dict mapping collection handle to sort_order
                          e.g., {'dali-oberon': 1, 'dali-opticon': 2}
    """
    print(f"\n📋 Setting sort order for {len(collection_orders)} collections...\n")

    collections = get_all_collections()

    success_count = 0
    for collection in collections:
        handle = collection['handle']
        if handle in collection_orders:
            sort_order = collection_orders[handle]
            print(f"Setting {collection['title']} ({handle}) = {sort_order}...", end=' ')

            if set_collection_sort_order(collection['id'], sort_order):
                print("✅")
                success_count += 1
            else:
                print("❌")

    print(f"\n✅ Successfully updated {success_count}/{len(collection_orders)} collections")


def interactive_mode():
    """Interactive mode to set collection order."""
    print("🏪 Fetching collections from Shopify...\n")
    collections = get_all_collections()

    print(f"Found {len(collections)} collections:\n")

    # Display collections with current sort order
    for i, collection in enumerate(collections, 1):
        metafields = get_collection_metafields(collection['id'])
        current_order = None

        for mf in metafields:
            if mf.get('namespace') == 'custom' and mf.get('key') == 'sort_order':
                current_order = mf.get('value')
                break

        order_display = f"(current: {current_order})" if current_order else "(no order set)"
        print(f"{i:2d}. {collection['title']:40s} {order_display}")

    print("\n" + "="*80)
    print("Set collection order by providing handle:order pairs")
    print("Example: dali-oberon:1 dali-opticon:2 hi-fi-stereo:3")
    print("Or press Enter to use the example below:")
    print("="*80 + "\n")


def main():
    """Main function."""
    print("\n" + "="*80)
    print("  Shopify Collection Sort Order Manager")
    print("="*80)

    # Example: Set your desired collection order here
    # Lower numbers = higher priority (appears first)

    COLLECTION_ORDER = {
        # DALI Series (1-10)
        'dali-oberon': 1,
        'dali-opticon': 2,
        'dali-rubicon': 3,
        'dali-epicon': 4,
        'dali-spektor': 5,

        # Product Types (11-20)
        'enceintes-de-bibliotheque': 11,
        'enceintes-colonnes': 12,
        'enceintes-centrale': 13,
        'enceintes-surround': 14,
        'subwoofers': 15,

        # Use Cases (21-30)
        'hi-fi-stereo': 21,
        'home-cinema': 22,
        'audio-multi-pieces': 23,

        # Marketing (31-40)
        'nouveautes': 31,
        'best-sellers': 32,
        'promotions': 33,
    }

    print("\n📌 Using predefined collection order")
    print("   Edit the COLLECTION_ORDER dict in this script to customize\n")

    response = input("Continue with predefined order? (y/n): ").strip().lower()

    if response == 'y':
        set_multiple_collections(COLLECTION_ORDER)
    else:
        interactive_mode()


if __name__ == '__main__':
    main()
