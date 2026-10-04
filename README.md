# Maya Watson's Personal Website

A visually attractive personal website for Maya Watson, a fictional/creative online personality based in London.

## Project Structure

```
maya-site/
├── index.html              # Home page
├── about.html              # About Maya page
├── gallery.html            # Photo gallery
├── videos.html             # Video section
├── journal.html            # Journal/posts section
├── assets/
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   ├── js/
│   │   └── main.js         # JavaScript for mobile menu and interactions
│   ├── images/             # Place for Maya's photographs
│   │   ├── placeholder-album-1.jpg
│   │   ├── placeholder-album-2.jpg
│   │   ├── placeholder-album-3.jpg
│   │   ├── placeholder-album-4.jpg
│   │   ├── placeholder-photo-1.jpg
│   │   ├── placeholder-photo-2.jpg
│   │   ├── placeholder-photo-3.jpg
│   │   ├── placeholder-photo-4.jpg
│   │   ├── placeholder-photo-5.jpg
│   │   └── placeholder-photo-6.jpg
│   └── videos/             # Place for Maya's video files (MP4 recommended)
```

## Getting Started

1. **Clone or download this repository**
2. **Replace placeholder media**:
   - Add your own photographs to the `assets/images/` folder
   - Add your own video files (MP4 format recommended) to the `assets/videos/` folder
   - Update the HTML files to reference your actual media files instead of placeholders
3. **Test locally**:
   - Open any HTML file in a web browser, or
   - Use a local server (see below)

## Running Locally

For the best experience (especially if you plan to add more features later), use a local server:

### Option 1: Python (built-in)
```bash
# From the project directory
python -m http.server 8000
```
Then visit `http://localhost:8000` in your browser.

### Option 2: Node.js (if you have it installed)
```bash
# Install serve globally if needed
npm install -g serve
# Then run
serve
```
Then visit the provided local URL (usually `http://localhost:3000`).

### Option 3: Simple double-click
You can open the HTML files directly in your browser, but some features (like future AJAX calls) may not work due to browser security restrictions.

## Adding Content

### Photographs
- Place image files in `assets/images/`
- Supported formats: JPG, PNG, WebP
- For optimal web performance, consider compressing images to reasonable file sizes
- Update the `src` attributes in `gallery.html` to point to your actual images

### Videos
- Place video files in `assets/videos/`
- Recommended format: MP4 with H.264 encoding
- Keep individual files under 10-15MB for faster loading
- Update the video sections in `videos.html` to reference your actual video files

### Journal Entries
- Copy an existing `<div class="post">` block in `journal.html`
- Update the date, heading, and content
- Maintain Maya's voice: personal, observational, warm with a touch of wit
- Refer to the "Maya's Voice & Personality Guide" section on the About page for consistency

## Design Philosophy

This site aims to feel like a genuine personal corner of the internet rather than a corporate or influencer profile. Key aspects:

- **Authentic voice**: Maya speaks like a real 52-year-old London woman—confident, warm, witty, and slightly cheeky
- **Visual focus**: Designed around strong photography and video content
- **London lifestyle**: Subtle references to tennis, markets, cafes, and London life throughout
- **Timeless aesthetic**: Modern but not trend-focused, with emphasis on readability and ease of navigation
- **Mobile-first**: Fully responsive design that works well on all devices

## Future Expansion

The site is structured to easily accommodate:
- More photo albums and galleries
- Expanded video library
- AI-generated journal entries (maintaining Maya's voice)
- Interactive features (comments, likes, etc.)
- Social media integration
- Tennis and London recommendation sections
- Automated content updates

## Maintenance

This site uses only HTML, CSS, and vanilla JavaScript—no frameworks or build tools required. This makes it easy to maintain and host anywhere.

For questions or updates to Maya's character/profile, refer to the voice guide in the About page.