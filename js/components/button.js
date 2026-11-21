/**
 * Kapwa Design System - Web Component: <kapwa-button>
 */
class KapwaButton extends HTMLElement {
  static get observedAttributes() {
    return ['variant', 'size', 'disabled'];
  }

  connectedCallback() {
    this.render();
  }

  attributeChangedCallback() {
    this.render();
  }

  render() {
    const variant = this.getAttribute('variant') || 'primary';
    const size = this.getAttribute('size') || 'md';
    const disabled = this.hasAttribute('disabled');
    const label = this.innerHTML || 'Button';

    this.className = `kw-btn kw-btn--${variant} ${size !== 'md' ? `kw-btn--${size}` : ''}`;
    if (disabled) {
      this.setAttribute('aria-disabled', 'true');
    } else {
      this.removeAttribute('aria-disabled');
    }
  }
}

if (typeof customElements !== 'undefined' && !customElements.get('kapwa-button')) {
  customElements.define('kapwa-button', KapwaButton);
}

export default KapwaButton;
