(function () {
  var STORAGE_KEY = 'budgetwise-theme';
  var root = document.documentElement;

  function applyTheme(theme) {
    root.setAttribute('data-theme', theme);

    var textNodes = document.querySelectorAll('[data-theme-text]');
    for (var i = 0; i < textNodes.length; i++) {
      textNodes[i].textContent = theme === 'dark' ? '🌙' : '☀';
    }

    var toggles = document.querySelectorAll('[data-theme-toggle]');
    for (var j = 0; j < toggles.length; j++) {
      toggles[j].checked = theme === 'dark';
    }
  }

  function getInitialTheme() {
    var saved = localStorage.getItem(STORAGE_KEY);
    if (saved === 'dark' || saved === 'light') {
      return saved;
    }

    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      return 'dark';
    }

    return 'light';
  }

  function bindToggleHandlers() {
    var toggles = document.querySelectorAll('[data-theme-toggle]');

    for (var i = 0; i < toggles.length; i++) {
      toggles[i].addEventListener('change', function (event) {
        var nextTheme = event.target.checked ? 'dark' : 'light';
        localStorage.setItem(STORAGE_KEY, nextTheme);
        applyTheme(nextTheme);
      });
    }
  }

  document.addEventListener('DOMContentLoaded', function () {
    var initialTheme = getInitialTheme();
    applyTheme(initialTheme);
    bindToggleHandlers();
  });
})();
