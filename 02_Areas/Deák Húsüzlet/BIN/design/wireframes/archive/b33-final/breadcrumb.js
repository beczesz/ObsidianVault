/* Breadcrumb reference system for DH wireframes */
(function() {
  // Don't run on index.html
  var filename = location.pathname.split('/').pop();
  if (filename === 'index.html' || filename === '') return;

  // Inject CSS
  var style = document.createElement('style');
  style.textContent = `
    .breadcrumb-bar {
      margin: 10px 24px 0; display: flex; align-items: center; gap: 8px;
      background: #F5F0EB; border: 1px solid #E8E2DB; border-radius: 8px;
      padding: 8px 12px; font-size: 12px; font-weight: 500; color: #8A8078;
      font-family: ui-monospace, 'SF Mono', Monaco, Consolas, monospace;
      cursor: pointer; transition: border-color 0.15s; user-select: all;
      max-width: 1500px;
    }
    .breadcrumb-bar:hover { border-color: #9B2335; }
    .breadcrumb-bar .bc-text { flex: 1; min-width: 0; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
    .breadcrumb-bar .bc-copy {
      display: inline-flex; align-items: center; justify-content: center;
      width: 28px; height: 28px; border-radius: 6px; border: 1px solid #E8E2DB;
      background: white; cursor: pointer; flex-shrink: 0; font-size: 13px;
      transition: all 0.15s;
    }
    .breadcrumb-bar .bc-copy:hover { background: #F9E0E3; border-color: #9B2335; }
    .breadcrumb-bar .bc-copy.copied { background: #D4EDDA; border-color: #2D7A4F; }
  `;
  document.head.appendChild(style);

  function insertBar() {
    var bar = document.createElement('div');
    bar.className = 'breadcrumb-bar';
    bar.id = 'breadcrumb';
    bar.onclick = copyBreadcrumb;
    bar.innerHTML = '<span class="bc-text" id="bcText"></span><span class="bc-copy" id="bcCopy" title="Hivatkozás másolása">📋</span>';

    var header = document.querySelector('.header');
    if (header) {
      header.appendChild(bar);
      bar.style.margin = '10px 0 0';
      bar.style.maxWidth = 'none';
    } else {
      var tabsNav = document.querySelector('.tabs-nav');
      var h1 = document.querySelector('h1');
      var target = tabsNav || (h1 && h1.parentElement);
      if (target) {
        target.parentElement.insertBefore(bar, target.nextSibling);
      } else {
        document.body.insertBefore(bar, document.body.firstChild);
      }
    }
    updateBreadcrumb();
  }

  function isVisible(el) {
    if (!el) return false;
    var style = window.getComputedStyle(el);
    return style.display !== 'none' && style.visibility !== 'hidden' && style.opacity !== '0';
  }

  function getVisibleActive(selector) {
    var els = document.querySelectorAll(selector);
    for (var i = 0; i < els.length; i++) {
      if (isVisible(els[i]) && isVisible(els[i].closest('.feature, .tab-panel, [class]'))) {
        return els[i];
      }
    }
    return null;
  }

  function getBreadcrumbRef() {
    // Active tab
    var activeTab = getVisibleActive('.tab.active, .tab-btn.active');
    var tabLabel = activeTab ? activeTab.textContent.trim() : '';
    // If no visible tab, try active feature h2
    if (!tabLabel) {
      var features = document.querySelectorAll('.feature');
      for (var i = 0; i < features.length; i++) {
        if (isVisible(features[i])) {
          var h2 = features[i].querySelector('h2');
          if (h2) { tabLabel = h2.textContent.trim(); break; }
        }
      }
    }
    // Active scenario — only visible ones
    var activeScenario = getVisibleActive('.scenario-btn.active');
    var scenarioLabel = activeScenario ? activeScenario.textContent.trim() : '';
    var parts = [filename];
    if (tabLabel) parts.push(tabLabel);
    if (scenarioLabel) parts.push(scenarioLabel);
    return '@screen[' + parts.join(' > ') + ']';
  }

  window.updateBreadcrumb = function() {
    var el = document.getElementById('bcText');
    if (el) el.textContent = getBreadcrumbRef();
  };

  window.copyBreadcrumb = function() {
    var text = document.getElementById('bcText').textContent;
    var bcCopy = document.getElementById('bcCopy');
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.style.cssText = 'position:fixed;left:-9999px';
    document.body.appendChild(ta);
    ta.select();
    document.execCommand('copy');
    document.body.removeChild(ta);
    bcCopy.classList.add('copied');
    bcCopy.textContent = '\u2713';
    setTimeout(function() { bcCopy.classList.remove('copied'); bcCopy.textContent = '\uD83D\uDCCB'; }, 1500);
  };

  // Use MutationObserver to watch for class changes on tabs/scenarios
  var observer = new MutationObserver(function() {
    setTimeout(updateBreadcrumb, 50);
  });
  
  function observeButtons() {
    document.querySelectorAll('.tab, .tab-btn, .scenario-btn').forEach(function(el) {
      observer.observe(el, { attributes: true, attributeFilter: ['class'] });
    });
  }

  // Re-observe when DOM changes (dynamically rendered scenarios)
  var bodyObserver = new MutationObserver(function() {
    observeButtons();
    setTimeout(updateBreadcrumb, 100);
  });
  bodyObserver.observe(document.body, { childList: true, subtree: true });

  // Direct click interception on scenario/tab buttons — most reliable
  document.body.addEventListener('click', function(e) {
    var btn = e.target.closest('.tab, .tab-btn, .scenario-btn');
    if (btn) {
      // Wait for the click handler to toggle .active
      setTimeout(updateBreadcrumb, 50);
      setTimeout(updateBreadcrumb, 200);
    }
  }, true);

  // Also re-observe after full load (catches late-rendered elements)
  window.addEventListener('load', function() {
    observeButtons();
    updateBreadcrumb();
  });

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', insertBar);
  } else {
    insertBar();
  }
})();
