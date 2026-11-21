/**
 * Kapwa Design System - Theme Manager
 * Supports Light & Dark themes with system synchronization and localStorage persistence
 */
const KapwaTheme = {
  STORAGE_KEY: 'kapwa-theme',

  init() {
    const saved = localStorage.getItem(this.STORAGE_KEY);
    if (saved) {
      this.setTheme(saved);
    } else {
      const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
      this.setTheme(prefersDark ? 'dark' : 'light');
    }

    if (window.matchMedia) {
      window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem(this.STORAGE_KEY)) {
          this.setTheme(e.matches ? 'dark' : 'light');
        }
      });
    }
  },

  getTheme() {
    return document.documentElement.getAttribute('data-theme') || 'light';
  },

  setTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem(this.STORAGE_KEY, theme);
    window.dispatchEvent(new CustomEvent('kapwa:theme-change', { detail: { theme } }));
  },

  toggle() {
    const current = this.getTheme();
    const next = current === 'dark' ? 'light' : 'dark';
    this.setTheme(next);
    return next;
  }
};

if (typeof window !== 'undefined') {
  window.KapwaTheme = KapwaTheme;
  document.addEventListener('DOMContentLoaded', () => KapwaTheme.init());
}

export default KapwaTheme;
