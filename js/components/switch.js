/**
 * Kapwa Design System - Web Component: <kapwa-switch>
 */
class KapwaSwitch extends HTMLElement {
  static get observedAttributes() {
    return ['checked', 'disabled', 'name', 'id'];
  }

  constructor() {
    super();
    this._checked = false;
  }

  connectedCallback() {
    this._checked = this.hasAttribute('checked');
    this.innerHTML = `
      <label class="kw-switch">
        <input type="checkbox" role="switch" ${this._checked ? 'checked' : ''} ${this.hasAttribute('disabled') ? 'disabled' : ''}>
        <div class="kw-switch__track">
          <div class="kw-switch__thumb"></div>
        </div>
      </label>
    `;

    const input = this.querySelector('input');
    input.addEventListener('change', (e) => {
      this._checked = e.target.checked;
      if (this._checked) {
        this.setAttribute('checked', '');
      } else {
        this.removeAttribute('checked');
      }
      this.dispatchEvent(new CustomEvent('change', { detail: { checked: this._checked } }));
    });
  }

  get checked() {
    return this._checked;
  }

  set checked(val) {
    this._checked = Boolean(val);
    const input = this.querySelector('input');
    if (input) input.checked = this._checked;
    if (this._checked) this.setAttribute('checked', '');
    else this.removeAttribute('checked');
  }
}

if (typeof customElements !== 'undefined' && !customElements.get('kapwa-switch')) {
  customElements.define('kapwa-switch', KapwaSwitch);
}

export default KapwaSwitch;
