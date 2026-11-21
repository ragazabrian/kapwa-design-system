/**
 * Kapwa Design System - Web Component: <kapwa-tabbar>
 * Floating pill tab bar with animated sliding indicator
 */
class KapwaTabBar extends HTMLElement {
  connectedCallback() {
    this.render();
  }

  render() {
    const tabsData = [
      { id: 'home', icon: 'home', label: 'Home' },
      { id: 'messages', icon: 'message', label: 'Messages' },
      { id: 'schedule', icon: 'table', label: 'Deliveries' },
      { id: 'team', icon: 'users', label: 'Team' }
    ];

    const activeIndex = parseInt(this.getAttribute('active-index') || '0', 10);

    let html = `
      <div class="kw-tabbar-container">
        <div class="kw-tabbar" role="tablist">
          <div class="kw-tabbar__indicator"></div>
    `;

    tabsData.forEach((tab, index) => {
      const iconSvg = window.KapwaIcons ? window.KapwaIcons.get(tab.icon, 32) : '';
      const isActive = index === activeIndex;
      html += `
        <button class="kw-tab ${isActive ? 'kw-tab--active' : ''}" role="tab" aria-selected="${isActive}" data-index="${index}" aria-label="${tab.label}">
          ${iconSvg}
        </button>
      `;
    });

    html += `
        </div>
      </div>
    `;

    this.innerHTML = html;
    this.setupTabs();
  }

  setupTabs() {
    const tabs = this.querySelectorAll('.kw-tab');
    const indicator = this.querySelector('.kw-tabbar__indicator');

    const updateIndicator = (tab) => {
      if (!tab || !indicator) return;
      const left = tab.offsetLeft;
      indicator.style.transform = `translateX(${left - 14}px)`;
    };

    tabs.forEach((tab) => {
      tab.addEventListener('click', () => {
        tabs.forEach(t => {
          t.classList.remove('kw-tab--active');
          t.setAttribute('aria-selected', 'false');
        });
        tab.classList.add('kw-tab--active');
        tab.setAttribute('aria-selected', 'true');
        updateIndicator(tab);
        this.dispatchEvent(new CustomEvent('tab-change', {
          detail: { index: parseInt(tab.dataset.index, 10) }
        }));
      });
    });

    // Initial position
    setTimeout(() => {
      const activeTab = this.querySelector('.kw-tab--active');
      if (activeTab) updateIndicator(activeTab);
    }, 50);
  }
}

if (typeof customElements !== 'undefined' && !customElements.get('kapwa-tabbar')) {
  customElements.define('kapwa-tabbar', KapwaTabBar);
}

export default KapwaTabBar;
