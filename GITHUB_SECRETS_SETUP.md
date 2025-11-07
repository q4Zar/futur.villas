# GitHub Secrets Setup for futur.villas

This repository is configured to automatically deploy the Shopify theme to **futur.villas** (served by "Ma boutique" - xjtm5x-pp.myshopify.com) when changes are pushed to the `main` branch.

## Required GitHub Secrets

You need to configure the following secrets in your GitHub repository at **github.com:q4Zar/futur.villas.git**:

### Futur Villas Shop (xjtm5x-pp.myshopify.com)

1. **`SHOPIFY_STORE_URL_FUTUR_VILLAS`**
   - Value: `xjtm5x-pp.myshopify.com`
   - Description: The Shopify shop domain (use .myshopify.com, not custom domain)

2. **`SHOPIFY_CLI_THEME_TOKEN_FUTUR_VILLAS`**
   - Value: Theme Access Token from Shopify Admin
   - How to get:
     - Go to Shopify Admin → Apps → Develop apps (or Theme Access)
     - Create a new app or use existing theme access app
     - Generate a new token with `write_themes` and `read_themes` permissions
     - Copy the token (you'll only see it once!)
   - Note: The API key `57d810b500988c65b4253fc122546326` is for API access, but you need a separate Theme Access Token for CLI operations

## How to Add Secrets to GitHub

1. Go to your GitHub repository: **https://github.com/q4Zar/futur.villas**
2. Click on **Settings** tab
3. In the left sidebar, click **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Add each secret one by one:
   - Name: `SHOPIFY_STORE_URL_FUTUR_VILLAS`
   - Value: `xjtm5x-pp.myshopify.com`
   - Click **Add secret**

6. Add the second secret:
   - Name: `SHOPIFY_CLI_THEME_TOKEN_FUTUR_VILLAS`
   - Value: (your Theme Access Token from Shopify)
   - Click **Add secret**

## How to Get Theme Access Token from Shopify

### Method 1: Using Theme Access App (Recommended)

1. Log in to Shopify Admin: **https://xjtm5x-pp.myshopify.com/admin**
2. Go to **Settings** → **Apps and sales channels**
3. Click **Develop apps**
4. If you don't have an app yet:
   - Click **Create an app**
   - Name it "Theme Deployment" or similar
   - Click **Create app**
5. Click on your app
6. Go to **Configuration** tab
7. Under **Theme templates and theme app extensions**, click **Configure**
8. Enable the following scopes:
   - `read_themes`
   - `write_themes`
9. Click **Save**
10. Go to **API credentials** tab
11. Click **Install app** (if not already installed)
12. Copy the **Admin API access token** - this is your `SHOPIFY_CLI_THEME_TOKEN_FUTUR_VILLAS`

### Method 2: Using Shopify CLI (Alternative)

If you have Shopify CLI installed locally:
```bash
shopify theme token --store xjtm5x-pp.myshopify.com
```
This will generate a token you can use.

## Deployment Flow

When you push to `main` branch:

1. **GitHub Action triggers** automatically
2. **Deploys to futur.villas** (xjtm5x-pp.myshopify.com)
   - Checks if theme "futur.villas/main" exists
   - If not, creates a new unpublished theme
   - Pushes all theme files
   - Publishes theme as live (if not already live)
3. **Confirmation** ✅ Theme deployed successfully!

## Manual Deployment

You can also trigger a deployment manually:

1. Go to **Actions** tab in GitHub
2. Select **Deploy Theme to Shopify** workflow
3. Click **Run workflow**
4. Select `main` branch
5. Click **Run workflow**

## Theme Check on Pull Requests

When you create a pull request, the **Theme Check** workflow automatically runs to validate your theme code:

- Checks Liquid syntax
- Validates theme structure
- Identifies potential issues
- Comments results on the PR

This helps catch issues before merging to `main`.

## Troubleshooting

### "Theme Access Token invalid"
- Regenerate the token in Shopify Admin (see steps above)
- Update the `SHOPIFY_CLI_THEME_TOKEN_FUTUR_VILLAS` secret in GitHub
- Re-run the workflow

### "Store URL not found"
- Verify you're using `xjtm5x-pp.myshopify.com` (the .myshopify.com domain)
- Do NOT use the custom domain `futur.villas` in the store URL secret

### "Permission denied" errors
- Ensure the token has both `read_themes` and `write_themes` scopes
- The API key `57d810b500988c65b4253fc122546326` is different from Theme Access Token
- You need to generate a Theme Access Token separately

### Deployment takes a long time
- This is normal for large themes with many assets
- Check the Actions logs for progress
- Each file upload is logged

## Current Configuration

| Shop Name | Shop Domain | Custom Domain | GitHub Secrets |
|-----------|-------------|---------------|----------------|
| Ma boutique | xjtm5x-pp.myshopify.com | futur.villas | `SHOPIFY_STORE_URL_FUTUR_VILLAS` + `SHOPIFY_CLI_THEME_TOKEN_FUTUR_VILLAS` |

## Security Notes

- ⚠️ Never commit tokens or API keys to the repository
- ⚠️ The `.env` file should be in `.gitignore`
- Tokens have write access to themes - keep them secure
- Rotate tokens periodically for security
- Use GitHub Secrets for all sensitive data
- The API key `57d810b500988c65b4253fc122546326` is for API access, not for theme deployment

## Environment Variables (.env file)

For local development, use the `.env` file:

```env
SHOPIFY_SHOP_DOMAIN=xjtm5x-pp.myshopify.com
SHOPIFY_ACCESS_TOKEN=57d810b500988c65b4253fc122546326
SHOPIFY_API_VERSION=2025-07
THEME_NAME=futur.villas/main
```

This API key is for API access (collections, products, etc.), not for theme deployment via GitHub Actions.
