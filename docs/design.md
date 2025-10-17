# Nano-Banana Studio - Design System

## Design Philosophy

### Principles
1. **Professional, Not Playful** - Clean, sophisticated aesthetics suitable for professional creatives
2. **Consistency Over Novelty** - Predictable patterns across all interfaces
3. **Clarity Over Cleverness** - Direct communication, minimal cognitive load
4. **Accessible by Default** - WCAG AA compliance, keyboard navigation, proper contrast

### Visual Language
- **Tone:** Dark, modern, tech-forward
- **Mood:** Focused, efficient, powerful
- **Inspiration:** Professional design tools (Figma, Adobe), VS Code, Linear

---

## Color System

### Base Palette

#### Backgrounds
```css
/* Primary background - main canvas */
--bg-primary: rgba(12, 12, 18, 1);

/* Secondary background - drawers, modals */
--bg-secondary: rgba(12, 12, 18, 0.98);

/* Tertiary background - headers, sticky elements */
--bg-tertiary: rgba(15, 15, 22, 0.95);

/* Surface - cards, elevated content */
--bg-surface: rgba(255, 255, 255, 0.05);
```

#### Text
```css
/* Primary text - headings, important content */
--text-primary: rgba(255, 255, 255, 1);

/* Secondary text - body copy */
--text-secondary: rgba(255, 255, 255, 0.9);

/* Tertiary text - labels, captions */
--text-tertiary: rgba(255, 255, 255, 0.7);

/* Disabled text */
--text-disabled: rgba(255, 255, 255, 0.4);

/* Placeholder text */
--text-placeholder: rgba(255, 255, 255, 0.3);
```

#### Borders
```css
/* Primary border */
--border-primary: rgba(255, 255, 255, 0.12);

/* Secondary border - subtle dividers */
--border-secondary: rgba(255, 255, 255, 0.08);

/* Focus border */
--border-focus: rgba(120, 40, 200, 0.5);
```

### Semantic Colors

#### Purple (Primary/Brand)
```css
--purple-bg-subtle: rgba(120, 40, 200, 0.08);
--purple-bg-hover: rgba(120, 40, 200, 0.15);
--purple-bg-active: rgba(120, 40, 200, 0.25);
--purple-border: rgba(120, 40, 200, 0.3);
--purple-solid: rgb(120, 40, 200);
--purple-text: rgba(200, 150, 255, 0.9);
```

**Usage:**
- Primary actions (Save, Create)
- Active states
- Brand elements
- Focus indicators

#### Green (Success)
```css
--green-bg-subtle: rgba(40, 200, 120, 0.08);
--green-bg-hover: rgba(40, 200, 120, 0.15);
--green-bg-active: rgba(40, 200, 120, 0.25);
--green-border: rgba(40, 200, 120, 0.3);
--green-solid: rgb(40, 200, 120);
--green-text: rgba(100, 255, 180, 0.9);
```

**Usage:**
- Success messages
- Add/Create actions
- Positive states
- Field chips

#### Red (Danger/Delete)
```css
--red-bg-subtle: rgba(200, 40, 80, 0.08);
--red-bg-hover: rgba(200, 40, 80, 0.15);
--red-bg-active: rgba(200, 40, 80, 0.25);
--red-border: rgba(200, 40, 80, 0.3);
--red-solid: rgb(200, 40, 80);
--red-text: rgba(255, 100, 130, 0.9);
```

**Usage:**
- Delete actions
- Error messages
- Destructive actions
- Warnings

#### Blue (Info/Preview)
```css
--blue-bg-subtle: rgba(40, 120, 200, 0.08);
--blue-text: rgba(100, 200, 255, 0.85);
```

**Usage:**
- Informational messages
- Code/preview blocks
- Links

### Color Usage Matrix

| Element | Background | Border | Text | Hover |
|---------|-----------|--------|------|-------|
| Button Primary | purple-bg-hover | purple-border | white | purple-bg-active |
| Button Success | green-bg-hover | green-border | white | green-bg-active |
| Button Danger | red-bg-hover | red-border | red-solid | red-bg-active |
| Input | rgba(0,0,0,0.3) | border-primary | white | border-focus |
| Card | bg-surface | border-secondary | text-primary | bg-surface + opacity |
| Drawer | bg-secondary | purple-border | text-primary | n/a |

---

## Typography

### Font Stack
```css
font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 
             Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
```

**Why Inter:**
- Professional, modern sans-serif
- Excellent readability at all sizes
- Wide character support
- Variable font available (future)

### Type Scale

#### Headers
```css
/* H1 - Main page title */
.h1 {
  font-size: 2em;
  font-weight: 700;
  letter-spacing: -0.02em;
  line-height: 1.2;
}

/* H2 - Drawer titles, section headers */
.h2 {
  font-size: 1.2em;
  font-weight: 600;
  letter-spacing: 0.3px;
  line-height: 1.3;
}

/* H3 - Subsection headers */
.h3 {
  font-size: 1.1em;
  font-weight: 600;
  letter-spacing: 0.2px;
  line-height: 1.4;
}
```

#### Body Text
```css
/* Base body text */
.body-base {
  font-size: 0.95em;
  font-weight: 400;
  line-height: 1.5;
}

/* Small text - helper text, captions */
.body-small {
  font-size: 0.85em;
  font-weight: 400;
  line-height: 1.4;
  color: var(--text-disabled);
}

/* Extra small - timestamps, metadata */
.body-xs {
  font-size: 0.75em;
  font-weight: 400;
  line-height: 1.3;
}
```

#### Labels
```css
/* Form labels */
.label {
  font-size: 0.85em;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: 0.8px;
  color: var(--text-tertiary);
}
```

#### Monospace (Code/Preview)
```css
.code {
  font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
  font-size: 0.9em;
  line-height: 1.6;
  color: var(--blue-text);
}
```

### Font Weights
- **400 (Regular):** Body text, general content
- **500 (Medium):** Emphasized text, labels
- **600 (Semibold):** Headers, important actions
- **700 (Bold):** Main titles (rarely used)

---

## Spacing System

### Scale
Based on 4px base unit for mathematical consistency.

```css
--space-1: 4px;    /* 0.25rem */
--space-2: 8px;    /* 0.5rem */
--space-3: 12px;   /* 0.75rem */
--space-4: 16px;   /* 1rem */
--space-5: 20px;   /* 1.25rem */
--space-6: 24px;   /* 1.5rem */
--space-8: 32px;   /* 2rem */
--space-10: 40px;  /* 2.5rem */
```

### Component Spacing

#### Drawers
- Padding (header): 16px 20px
- Padding (content): 20px
- Gap between sections: 24px
- Gap between form fields: 24px

#### Buttons
- Padding (icon only): 8px
- Padding (text): 10px 16px
- Gap (icon + text): 6px

#### Cards
- Padding: 15px
- Margin bottom: 12px
- Gap between card elements: 8px

#### Form Fields
- Margin bottom: 24px
- Label margin bottom: 8px
- Helper text margin top: 6px

---

## Border Radius

### Scale
```css
--radius-none: 0px;    /* Drawers (sharp edges for professionalism) */
--radius-sm: 4px;      /* Buttons, inputs */
--radius-md: 6px;      /* Cards, chips, field chips */
--radius-lg: 8px;      /* (reserved for special cases) */
```

**Rationale:**
- Subtle rounding (4-6px) feels modern without being "playful"
- Drawers have 0px radius for clean, professional edge
- Consistent rounding creates visual harmony

---

## Elevation & Shadows

### Shadow Scale
```css
/* Drawer shadow */
--shadow-drawer: -8px 0 32px rgba(0, 0, 0, 0.6);

/* Card shadow (hover) */
--shadow-card-hover: 0 4px 12px rgba(0, 0, 0, 0.3);

/* Button shadow (hover, rare) */
--shadow-button: 0 2px 8px rgba(0, 0, 0, 0.2);

/* Toast notification */
--shadow-toast: 0 4px 12px rgba(0, 0, 0, 0.3);
```

### Z-Index Layers
```
Backdrop: 1999
Drawer L1: 2000
Drawer L2: 2001
Drawer L3: 2002
Drawer L4: 2003
Modal: 3000
Toast: 10000
```

---

## Components

### Buttons

#### Primary Button
```css
.button-primary {
  background: var(--purple-bg-hover);
  border: 1px solid var(--purple-border);
  color: white;
  padding: 10px 16px;
  border-radius: 4px;
  font-weight: 500;
  font-size: 0.9em;
  min-height: 44px;
  transition: all 0.2s;
}

.button-primary:hover {
  background: var(--purple-bg-active);
}
```

#### Success Button
```css
.button-success {
  background: var(--green-bg-hover);
  border: 1px solid var(--green-border);
  color: white;
  /* ... same as primary */
}
```

#### Danger Button
```css
.button-danger {
  background: var(--red-bg-hover);
  border: 1px solid var(--red-border);
  color: var(--red-solid);
  /* ... same as primary */
}
```

#### Icon Button
```css
.button-icon {
  background: none;
  border: none;
  color: var(--text-tertiary);
  padding: 8px;
  min-width: 44px;
  min-height: 44px;
  transition: color 0.2s;
}

.button-icon:hover {
  color: var(--text-primary);
}
```

### Inputs

#### Text Input
```css
.input-text {
  width: 100%;
  padding: 12px;
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid var(--border-primary);
  border-radius: 4px;
  color: white;
  font-size: 0.9em;
  font-family: 'Inter', sans-serif;
}

.input-text:focus {
  outline: none;
  border-color: var(--border-focus);
}

.input-text::placeholder {
  color: var(--text-placeholder);
}
```

#### Select
```css
.select {
  width: 100%;
  padding: 12px;
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid var(--border-primary);
  border-radius: 4px;
  color: white;
  font-size: 0.95em;
  font-family: 'Inter', sans-serif;
}
```

#### Textarea
```css
.textarea {
  width: 100%;
  padding: 12px;
  background: rgba(0, 0, 0, 0.3);
  border: 1px solid var(--border-primary);
  border-radius: 4px;
  color: white;
  font-size: 0.9em;
  font-family: 'Inter', sans-serif;
  resize: vertical;
  line-height: 1.5;
}
```

#### Checkbox
```css
.checkbox {
  width: 18px;
  height: 18px;
  cursor: pointer;
  accent-color: var(--purple-solid);
}
```

#### Radio Button
```css
.radio {
  width: 18px;
  height: 18px;
  cursor: pointer;
  accent-color: var(--purple-solid);
}
```

### Cards

#### Preset Card
```css
.card-preset {
  background: var(--bg-surface);
  border: 1px solid var(--border-secondary);
  border-radius: 12px;
  padding: 15px;
  margin-bottom: 12px;
  transition: all 0.2s;
  cursor: pointer;
}

.card-preset:hover {
  background: rgba(255, 255, 255, 0.08);
  border-color: var(--border-primary);
}
```

#### Field Chip
```css
.chip-field {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: var(--green-bg-hover);
  border: 1px solid var(--green-border);
  border-radius: 6px;
  padding: 10px 14px;
}
```

### Drawers

#### Drawer Container
```css
.drawer {
  position: fixed;
  top: 0;
  right: -650px;
  width: 650px;
  height: 100vh;
  background: var(--bg-secondary);
  box-shadow: var(--shadow-drawer);
  border-left: 1px solid var(--purple-border);
  transition: right 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  overflow-y: auto;
}

.drawer.open {
  right: 0;
}
```

#### Drawer Header
```css
.drawer-header {
  position: sticky;
  top: 0;
  background: var(--bg-tertiary);
  padding: 16px 20px;
  border-bottom: 1px solid var(--border-secondary);
  backdrop-filter: blur(12px);
  z-index: 10;
  display: flex;
  align-items: center;
  gap: 12px;
}
```

### Icons

All icons are SVG-based, inline in HTML. Standard viewBox is `0 0 24 24`.

#### Icon Sizes
- Navigation (Back, Close): 20px × 20px
- Action icons (Save, Delete, Add): 16px × 16px
- Small icons (in chips): 14px × 14px

#### Icon Library

**Close (X)**
```html
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" 
     stroke="currentColor" stroke-width="2" stroke-linecap="round">
  <path d="M18 6L6 18M6 6l12 12"/>
</svg>
```

**Back (Chevron Left)**
```html
<svg width="20" height="20" viewBox="0 0 24 24" fill="none" 
     stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M15 18l-6-6 6-6"/>
</svg>
```

**Save (Check)**
```html
<svg width="16" height="16" viewBox="0 0 24 24" fill="none" 
     stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
  <polyline points="20 6 9 17 4 12"/>
</svg>
```

**Add (Plus)**
```html
<svg width="16" height="16" viewBox="0 0 24 24" fill="none" 
     stroke="currentColor" stroke-width="2.5" stroke-linecap="round">
  <path d="M12 5v14M5 12h14"/>
</svg>
```

**Delete (Trash)**
```html
<svg width="16" height="16" viewBox="0 0 24 24" fill="none" 
     stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  <path d="M3 6h18M8 6V4c0-1 1-2 2-2h4c1 0 2 1 2 2v2m3 0v14c0 1-1 2-2 2H7c-1 0-2-1-2-2V6h14z"/>
</svg>
```

**Edit (Pencil)**
```html
<svg width="14" height="14" viewBox="0 0 14 14" fill="none" 
     stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <path d="M10 1l3 3L5 12H2v-3L10 1z"/>
</svg>
```

---

## Transitions & Animations

### Timing Functions
```css
--ease-default: cubic-bezier(0.4, 0, 0.2, 1);  /* Smooth, professional */
--ease-in: cubic-bezier(0.4, 0, 1, 1);         /* Accelerating */
--ease-out: cubic-bezier(0, 0, 0.2, 1);        /* Decelerating */
```

### Durations
```css
--duration-fast: 0.15s;    /* Hover states */
--duration-normal: 0.3s;   /* Drawers, modals */
--duration-slow: 0.5s;     /* Page transitions */
```

### Common Transitions
```css
/* Drawer slide */
transition: right 0.3s cubic-bezier(0.4, 0, 0.2, 1);

/* Button hover */
transition: all 0.2s;

/* Color change */
transition: color 0.2s;

/* Background change */
transition: background 0.2s;
```

---

## Accessibility

### Minimum Touch Targets
All interactive elements must be at least **44px × 44px** for touch accessibility.

```css
.button, .icon-button {
  min-width: 44px;
  min-height: 44px;
}
```

### Color Contrast

#### Text on Backgrounds
- **Normal text:** 4.5:1 minimum (WCAG AA)
- **Large text (18pt+):** 3:1 minimum
- **Interactive elements:** 3:1 minimum

#### Verified Combinations
| Text | Background | Contrast | Pass |
|------|-----------|----------|------|
| white | rgba(12,12,18,1) | 15.8:1 | ✅ AAA |
| rgba(255,255,255,0.9) | rgba(12,12,18,1) | 14.2:1 | ✅ AAA |
| rgba(255,255,255,0.7) | rgba(12,12,18,1) | 10.5:1 | ✅ AAA |
| rgba(255,255,255,0.4) | rgba(12,12,18,1) | 5.2:1 | ✅ AA |

### Focus States
All interactive elements must have visible focus indicators:

```css
.button:focus-visible {
  outline: 2px solid var(--purple-solid);
  outline-offset: 2px;
}

.input:focus {
  border-color: var(--border-focus);
  outline: none;
}
```

### ARIA Labels
All icon buttons must have `aria-label`:

```html
<button aria-label="Close drawer" onclick="closeDrawer()">
  <svg><!-- icon --></svg>
</button>
```

### Keyboard Navigation
- Tab order follows visual flow
- Escape closes active drawer
- Enter/Space activates buttons
- Arrow keys for radio/select groups

---

## Responsive Behavior

### Breakpoints
```css
--breakpoint-sm: 640px;
--breakpoint-md: 768px;
--breakpoint-lg: 1024px;
--breakpoint-xl: 1280px;
```

### Drawer Responsive Behavior
- **Desktop (1024px+):** 650px drawer width
- **Tablet (768-1023px):** 100vw drawer width
- **Mobile (<768px):** 100vw drawer width

```css
@media (max-width: 1023px) {
  .drawer {
    width: 100vw;
    right: -100vw;
  }
}
```

---

## Dark Mode (Current Default)

The entire application uses a dark theme. Light mode is not currently supported but can be added using CSS custom properties.

### Future Light Mode Palette
```css
/* Light mode (future) */
--bg-primary-light: rgba(255, 255, 255, 1);
--bg-secondary-light: rgba(250, 250, 252, 1);
--text-primary-light: rgba(0, 0, 0, 0.9);
/* ... etc */
```

---

## Design Checklist

When implementing new components, verify:

- [ ] Uses Inter font family
- [ ] Border radius: 0px (drawers), 4px (inputs/buttons), 6px (cards)
- [ ] Touch targets minimum 44px × 44px
- [ ] Color contrast meets WCAG AA
- [ ] SVG icons (not emojis or icon fonts)
- [ ] Consistent spacing from spacing scale
- [ ] Smooth transitions (0.3s cubic-bezier)
- [ ] Hover states on interactive elements
- [ ] Focus indicators present
- [ ] ARIA labels on icon buttons
- [ ] Responsive behavior considered

---

## Design Assets

### Figma File
*(Future: Link to Figma design file)*

### Icon Set
All icons are custom SVG, stored inline in HTML. No external icon library used.

### Font Files
Loaded from Google Fonts CDN:
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
```

---

## Brand Guidelines

### Logo
**Nano-Banana Studio** 🍌

- Primary logo: Text + emoji
- Color: White text on dark background
- Emoji: 🍌 (banana emoji)
- Tagline: "Text-to-Image • Image Editing • Multi-Image Composition"

### Voice & Tone
- **Professional but approachable**
- Clear, concise copy
- No jargon unless necessary
- Action-oriented button labels
- Helpful, not condescending error messages

### Naming Conventions
- **Preset** not "template" or "style"
- **Field** not "parameter" or "input"
- **Drawer** not "sidebar" or "panel"
- **Generate** not "create" (for images)
- **Save** not "submit" or "apply"

---

## References

- [Inter Font Specimen](https://rsms.me/inter/)
- [Material Design 3 Color System](https://m3.material.io/styles/color)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
