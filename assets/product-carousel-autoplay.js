/**
 * Auto-rotating product image carousel
 * Automatically cycles through product images without controls
 */

class ProductCarouselAutoplay {
  constructor() {
    this.carousels = [];
    this.rotationInterval = 4000; // 4 seconds per image
    this.init();
  }

  init() {
    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', () => this.setupCarousels());
    } else {
      this.setupCarousels();
    }
  }

  setupCarousels() {
    // Find all media galleries on product pages
    const mediaGalleries = document.querySelectorAll('media-gallery[data-presentation="carousel"]');

    mediaGalleries.forEach((gallery, index) => {
      this.setupCarousel(gallery, index);
    });
  }

  setupCarousel(gallery, index) {
    const slideshow = gallery.querySelector('[ref="slideshow"]');
    if (!slideshow) return;

    const slides = Array.from(slideshow.querySelectorAll('[ref="slide[]"]'));
    if (slides.length <= 1) return; // No rotation needed for single image

    const carouselData = {
      gallery,
      slideshow,
      slides,
      currentIndex: 0,
      interval: null,
      isPaused: false
    };

    // Hide all controls
    this.hideControls(gallery);

    // Start auto-rotation
    this.startRotation(carouselData);

    // Pause on hover
    gallery.addEventListener('mouseenter', () => this.pauseRotation(carouselData));
    gallery.addEventListener('mouseleave', () => this.resumeRotation(carouselData));

    this.carousels.push(carouselData);
  }

  hideControls(gallery) {
    // Hide all carousel controls
    const controls = gallery.querySelectorAll([
      '.slideshow-controls',
      '.slideshow-arrows',
      '.media-gallery__mobile-controls',
      '[class*="control"]',
      '[class*="pagination"]',
      '[class*="thumbnail"]',
      'button[aria-label*="Next"]',
      'button[aria-label*="Previous"]',
      '.slideshow__button'
    ].join(','));

    controls.forEach(control => {
      control.style.display = 'none';
      control.style.opacity = '0';
      control.style.pointerEvents = 'none';
    });

    // Add custom CSS to ensure controls stay hidden
    const style = document.createElement('style');
    style.textContent = `
      media-gallery[data-presentation="carousel"] .slideshow-controls,
      media-gallery[data-presentation="carousel"] .slideshow-arrows,
      media-gallery[data-presentation="carousel"] .media-gallery__mobile-controls,
      media-gallery[data-presentation="carousel"] [class*="thumbnail"],
      media-gallery[data-presentation="carousel"] button[aria-label*="ext"],
      media-gallery[data-presentation="carousel"] button[aria-label*="revious"] {
        display: none !important;
        opacity: 0 !important;
        pointer-events: none !important;
      }

      /* Smooth transitions for product images */
      media-gallery[data-presentation="carousel"] [ref="slide[]"] {
        transition: opacity 1s ease-in-out, transform 0.5s ease-in-out;
      }

      /* Add subtle fade effect during transitions */
      media-gallery[data-presentation="carousel"] [ref="slide[]"]:not([aria-selected="true"]) {
        opacity: 0;
      }

      media-gallery[data-presentation="carousel"] [ref="slide[]"][aria-selected="true"] {
        opacity: 1;
      }
    `;
    document.head.appendChild(style);
  }

  startRotation(carouselData) {
    if (carouselData.interval) return;

    carouselData.interval = setInterval(() => {
      if (!carouselData.isPaused) {
        this.nextSlide(carouselData);
      }
    }, this.rotationInterval);
  }

  pauseRotation(carouselData) {
    carouselData.isPaused = true;
  }

  resumeRotation(carouselData) {
    carouselData.isPaused = false;
  }

  stopRotation(carouselData) {
    if (carouselData.interval) {
      clearInterval(carouselData.interval);
      carouselData.interval = null;
    }
  }

  nextSlide(carouselData) {
    const { slides, slideshow } = carouselData;

    // Calculate next index
    carouselData.currentIndex = (carouselData.currentIndex + 1) % slides.length;

    // Update slide visibility
    slides.forEach((slide, index) => {
      if (index === carouselData.currentIndex) {
        slide.setAttribute('aria-selected', 'true');
      } else {
        slide.setAttribute('aria-selected', 'false');
      }
    });

    // Trigger slideshow navigation if available
    if (slideshow && typeof slideshow.goToSlide === 'function') {
      slideshow.goToSlide(carouselData.currentIndex);
    } else {
      // Fallback: manually update transform
      const slideWidth = slides[0]?.offsetWidth || 0;
      const track = slideshow.querySelector('[ref="track"]');
      if (track) {
        track.style.transform = `translateX(-${carouselData.currentIndex * slideWidth}px)`;
      }
    }
  }

  destroy() {
    // Clean up all carousels
    this.carousels.forEach(carouselData => {
      this.stopRotation(carouselData);
    });
    this.carousels = [];
  }
}

// Initialize when script loads
const productCarouselAutoplay = new ProductCarouselAutoplay();

// Clean up on page unload
window.addEventListener('beforeunload', () => {
  productCarouselAutoplay.destroy();
});

// Export for potential external use
window.ProductCarouselAutoplay = ProductCarouselAutoplay;
