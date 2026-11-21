/**
 * Kapwa Design System - Main JS Library Entry
 * No build tools required! Works natively in modern browsers.
 */
import KapwaIcons from './utils/icons.js';
import KapwaTheme from './utils/theme.js';
import KapwaButton from './components/button.js';
import KapwaSwitch from './components/switch.js';
import KapwaTabBar from './components/tabbar.js';

const Kapwa = {
  version: '1.0.0',
  theme: KapwaTheme,
  icons: KapwaIcons,

  openSheet(sheetId = 'confirm-delivery-sheet') {
    const sheet = document.getElementById(sheetId);
    if (sheet) {
      sheet.classList.add('kw-sheet-backdrop--open');
      document.body.style.overflow = 'hidden';
    }
  },

  closeSheet(sheetId = 'confirm-delivery-sheet') {
    const sheet = document.getElementById(sheetId);
    if (sheet) {
      sheet.classList.remove('kw-sheet-backdrop--open');
      document.body.style.overflow = '';
    }
  },

  init() {
    console.log(`[Kapwa Design System] Initialized v${this.version}`);
    // Setup backdrop dismissals
    document.querySelectorAll('.kw-sheet-backdrop').forEach(backdrop => {
      backdrop.addEventListener('click', (e) => {
        if (e.target === backdrop) {
          backdrop.classList.remove('kw-sheet-backdrop--open');
          document.body.style.overflow = '';
        }
      });
    });
  }
};

if (typeof window !== 'undefined') {
  window.Kapwa = Kapwa;
  document.addEventListener('DOMContentLoaded', () => Kapwa.init());
}

export default Kapwa;
