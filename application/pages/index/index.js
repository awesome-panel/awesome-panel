let isDark = localStorage.getItem('theme') === 'sl-theme-dark';
const toggle = document.getElementById('theme-toggler')
// Set initial theme
if (isDark) {
    document.body.classList.add('sl-theme-dark');
}
const noTransitions = Object.assign(document.createElement('style'), {
    textContent: '* { transition: none !important; }'
    });

// Toggle theme
toggle.addEventListener('click', () => {
    isDark = !isDark;
    isDark ? localStorage.setItem('theme', 'sl-theme-dark') : localStorage.removeItem('theme');
    toggle.name = isDark ? 'sun' : 'moon';

    // Disable transitions as the theme changes
    document.body.appendChild(noTransitions);
    requestAnimationFrame(() => {
    document.body.classList.toggle('sl-theme-dark', isDark);
    requestAnimationFrame(() => document.body.removeChild(noTransitions));
    });
});

function openSelectedApp() {
  console.log("hello world3")
  var x = document.getElementById("application-selector").value;
  window.open(x);
}

const select = document.querySelector('sl-select');
console.log(select);
select.addEventListener('sl-change', event => {
  url = select.value;
  window.open(url);
});