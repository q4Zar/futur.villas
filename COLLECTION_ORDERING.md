# Collection Ordering System

This system allows you to control the display order of collections using a weight-based priority system.

## How It Works

### 1. Metafield System

Collections are sorted using a custom metafield:
- **Namespace**: `custom`
- **Key**: `sort_order`
- **Type**: `number_integer`
- **Value**: Lower numbers = higher priority (appears first)

### 2. Theme Integration

The theme (`sections/main-collection-list.liquid`) automatically:
- Reads the `sort_order` metafield from each collection
- Sorts collections by this value (ascending order)
- Collections without a weight are assigned 9999 (appear last)

### 3. Setting Collection Order

Use the Python script to set collection order:

```bash
# Install dependencies
pip install requests python-dotenv

# Set up your .env file with Shopify credentials
# SHOPIFY_STORE_URL_FUTUR_VILLAS=xjtm5x-pp.myshopify.com
# SHOPIFY_CLI_THEME_TOKEN_FUTUR_VILLAS=your_token_here

# Run the script
python set_collection_order.py
```

## Example Order

The script includes a predefined order:

```python
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
```

## Manual Setup (Shopify Admin)

You can also set collection order manually:

1. Go to Shopify Admin > Collections
2. Click on a collection
3. Scroll to "Metafields"
4. Add a new metafield:
   - **Namespace**: `custom`
   - **Key**: `sort_order`
   - **Type**: Integer
   - **Value**: Your desired order (e.g., 1, 2, 3...)

## Order Guidelines

- **1-10**: Featured/premium collections (DALI series)
- **11-20**: Product type collections
- **21-30**: Use case collections
- **31-40**: Marketing collections
- **41+**: Secondary collections
- **9999**: Default (no order set)

## Benefits

✅ **Flexible**: Change order anytime via script or Shopify admin
✅ **Persistent**: Order survives theme updates
✅ **No Manual Sorting**: Automatic sorting in theme
✅ **Granular Control**: Set exact position for each collection

## Technical Details

### Liquid Template Logic

```liquid
# For each collection, get metafield value
assign weight = collection.metafields.custom.sort_order.value

# Collections without weight get 9999 (appear last)
if weight == blank
  assign weight = 9999
endif

# Sort by weight (ascending)
# Result: Collections appear in order: 1, 2, 3... 9999
```

### API Metafield Structure

```json
{
  "metafield": {
    "namespace": "custom",
    "key": "sort_order",
    "value": "1",
    "type": "number_integer"
  }
}
```

## Troubleshooting

**Collections not sorting?**
- Check metafield namespace is `custom` and key is `sort_order`
- Verify metafield type is `number_integer`
- Clear cache and refresh the page

**Script errors?**
- Ensure `.env` file has correct credentials
- Check Shopify API token has `read_products` and `write_products` scopes
- Verify internet connection

## Future Enhancements

Potential improvements:
- Web UI for drag-and-drop ordering
- Bulk reordering via CSV import
- Collection groups/categories
- Scheduled rotation of featured collections
