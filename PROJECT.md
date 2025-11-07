# Futur Villas - Shopify Theme Project

## Overview

This is the Shopify theme for **Futur Villas** (futur.villas), a Shopify-based e-commerce platform. The theme "Savor" was exported on November 7, 2025, and is now ready for development and deployment.

## Shop Information

| Property | Value |
|----------|-------|
| **Shop Name** | Ma boutique |
| **Admin Domain** | xjtm5x-pp.myshopify.com |
| **Public Domain** | futur.villas |
| **Theme Name** | Savor (futur.villas/main) |
| **Export Date** | November 7, 2025 11:27 AM |

## Theme Structure

The theme follows standard Shopify theme architecture:

```
├── assets/          # CSS, JavaScript, and static assets
├── blocks/          # Reusable theme blocks
├── config/          # Theme configuration and settings
├── layout/          # Base layout templates
├── locales/         # Translation files
├── sections/        # Theme sections (modular components)
├── snippets/        # Reusable code snippets
└── templates/       # Page templates
```

## Key Features

- **Modern JavaScript Components**: Includes custom components for cart, product display, announcements, etc.
- **Responsive Design**: Mobile-first approach with adaptive layouts
- **Modular Sections**: Highly customizable sections for flexible page building
- **GitHub Actions Integration**: Automated deployment pipeline configured

## Development Workflow

### GitHub Actions Deployment

This theme includes automated deployment workflows:

1. **Auto-deploy on Push to Main** (`.github/workflows/shopify-theme-deploy.yml`)
   - Automatically deploys theme when changes are pushed to `main` branch
   - Publishes theme as live on the store

2. **Theme Check on Pull Requests** (`.github/workflows/shopify-theme-check.yml`)
   - Validates theme code on PR creation
   - Identifies issues before merging

### Required GitHub Secrets

To enable automated deployment, configure these secrets in the GitHub repository:

- `SHOPIFY_STORE_URL_FUTUR_VILLAS` = `xjtm5x-pp.myshopify.com`
- `SHOPIFY_CLI_THEME_TOKEN_FUTUR_VILLAS` = Theme Access Token (with `read_themes` and `write_themes` permissions)

See `GITHUB_SECRETS_SETUP.md` for detailed configuration instructions.

## Local Development

### Prerequisites

- Shopify CLI installed
- Theme Access Token configured in `.env` file

### Environment Variables

Copy `.env` file and configure:

```bash
SHOPIFY_CLI_THEME_TOKEN=your-theme-access-token
SHOPIFY_STORE=xjtm5x-pp.myshopify.com
```

**⚠️ Security**: Never commit `.env` to version control. Ensure it's in `.gitignore`.

### Development Commands

```bash
# Start local development server
shopify theme dev

# Push theme to Shopify
shopify theme push

# Pull latest theme from Shopify
shopify theme pull

# Run theme check
shopify theme check
```

## Assets Overview

The theme includes various custom JavaScript components:

- `cart-drawer.js` - Shopping cart drawer functionality
- `product-*.js` - Product display and interaction components
- `collection-*.js` - Collection page components
- `announcement-bar.js` - Promotional announcements
- `dialog.js` - Modal and popup functionality
- And many more...

## Sections Overview

Key theme sections include:

- `featured-product.liquid` - Featured product display
- `featured-blog-posts.liquid` - Blog post showcase
- `collection-list.liquid` - Collection grid/list
- `footer.liquid` - Site footer
- `custom-liquid.liquid` - Custom code sections
- And many more modular sections for page building

## Related Documentation

- `README.md` - Quick setup and deployment guide
- `GITHUB_SECRETS_SETUP.md` - Detailed GitHub secrets configuration
- `DEPLOYMENT_SUMMARY.md` - Deployment process overview
- `WORKFLOW.md` - Current workflow and task tracking

## Repository

- **Git Repository**: github.com:q4Zar/futur.villas.git
- **Current Branch**: shopify-savor-theme
- **Main Branch**: main

## Next Steps

1. Review and test theme functionality locally
2. Configure GitHub secrets for automated deployment
3. Customize theme settings as needed
4. Deploy to production via GitHub Actions

---

*Last Updated: 2025-11-07*
*Theme Version: Savor Export (November 7, 2025)*
