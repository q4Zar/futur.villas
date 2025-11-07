# Futur Villas - Shopify GitHub Actions Deployment Templates

This directory contains all the necessary files to set up automated Shopify theme deployment for the **futur.villas** repository using GitHub Actions.

## 📁 Files Included

```
futur-villas-templates/
├── .github/
│   └── workflows/
│       ├── shopify-theme-deploy.yml    # Main deployment workflow
│       └── shopify-theme-check.yml     # PR theme validation workflow
├── .env                                 # Local development environment variables
├── GITHUB_SECRETS_SETUP.md             # Detailed secrets configuration guide
└── README.md                            # This file
```

## 🚀 Quick Setup

### Step 1: Copy Files to futur.villas Repository

Copy all files from this template to the root of your futur.villas repository:

```bash
# Navigate to your futur.villas repository
cd /path/to/futur.villas

# Copy the GitHub workflows
mkdir -p .github/workflows
cp /path/to/this/template/.github/workflows/*.yml .github/workflows/

# Copy .env for local development (make sure it's in .gitignore!)
cp /path/to/this/template/.env .env

# Copy documentation
cp /path/to/this/template/GITHUB_SECRETS_SETUP.md .github/
```

### Step 2: Configure GitHub Secrets

Follow the instructions in `GITHUB_SECRETS_SETUP.md` to set up the required secrets in your GitHub repository.

**Required secrets:**
- `SHOPIFY_STORE_URL_FUTUR_VILLAS` = `xjtm5x-pp.myshopify.com`
- `SHOPIFY_CLI_THEME_TOKEN_FUTUR_VILLAS` = Your Theme Access Token

### Step 3: Push to Main Branch

Once secrets are configured, push your code to the `main` branch to trigger automatic deployment:

```bash
git add .
git commit -m "Add GitHub Actions deployment workflow"
git push origin main
```

## 🔄 How It Works

### Automatic Deployment (on push to main)

1. Push changes to `main` branch
2. GitHub Actions automatically triggers
3. Theme is deployed to futur.villas (xjtm5x-pp.myshopify.com)
4. Theme is published as live
5. You receive a confirmation ✅

### Theme Check (on pull requests)

1. Create a pull request
2. GitHub Actions runs theme validation
3. Results are commented on the PR
4. Identifies issues before merging

### Manual Deployment

You can also deploy manually from GitHub Actions UI:
- Go to Actions → Deploy Theme to Shopify → Run workflow

## 🏪 Shop Configuration

| Property | Value |
|----------|-------|
| **Shop Name** | Ma boutique |
| **Admin Domain** | xjtm5x-pp.myshopify.com |
| **Public Domain** | futur.villas |
| **Theme Name** | futur.villas/main |
| **API Key** | 57d810b500988c65b4253fc122546326 (for API access, not theme deployment) |

## 🔐 Security

- ⚠️ Never commit the `.env` file to the repository
- ⚠️ Never commit tokens or API keys
- ✅ Use GitHub Secrets for all sensitive data
- ✅ Add `.env` to your `.gitignore`

## 📝 Theme Structure Expected

The workflows expect a standard Shopify theme structure:

```
futur.villas/
├── assets/
├── config/
├── layout/
├── locales/
├── sections/
├── snippets/
└── templates/
```

## 🆘 Support

If you encounter issues:

1. Check the GitHub Actions logs for detailed error messages
2. Verify all secrets are correctly configured
3. Ensure the Theme Access Token has the right permissions (`read_themes` and `write_themes`)
4. Refer to `GITHUB_SECRETS_SETUP.md` for troubleshooting steps

## 🔗 Related Repositories

This template is based on the deployment setup from:
- **lrt-garage.fr** - Similar dual-shop deployment configuration

## 📚 Additional Resources

- [Shopify CLI Theme Commands](https://shopify.dev/docs/themes/tools/cli/theme-commands)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Shopify Theme Development](https://shopify.dev/docs/themes)

## ⚙️ Customization

### Change Theme Name

Edit `.github/workflows/shopify-theme-deploy.yml`:

```yaml
theme_name: "futur.villas/main"  # Change this to your preferred name
```

### Add Multiple Environments

You can extend the matrix strategy to deploy to multiple shops (dev, staging, production):

```yaml
matrix:
  shop:
    - name: "Dev Shop"
      store_url: SHOPIFY_STORE_URL_DEV
      theme_token: SHOPIFY_CLI_THEME_TOKEN_DEV
      theme_name: "futur.villas/dev"
    - name: "Production"
      store_url: SHOPIFY_STORE_URL_FUTUR_VILLAS
      theme_token: SHOPIFY_CLI_THEME_TOKEN_FUTUR_VILLAS
      theme_name: "futur.villas/main"
```

## 🎯 Next Steps

1. ✅ Copy all template files to futur.villas repository
2. ✅ Add `.env` to `.gitignore`
3. ✅ Configure GitHub secrets
4. ✅ Push to `main` branch to test deployment
5. ✅ Create a test PR to verify theme check workflow

---

**Repository:** github.com:q4Zar/futur.villas.git
**Template Created:** 2025-11-07
**Based on:** lrt-garage.fr deployment configuration
