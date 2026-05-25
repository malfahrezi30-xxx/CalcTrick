/* ════════════════════════════════════════════════
   CalcPro – main.js
   Dark/Light Mode · History · Copy · Animations
   ════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', function () {

    // ──────────────────────────────────────────────
    //  DARK / LIGHT MODE
    // ──────────────────────────────────────────────
    const html        = document.documentElement;
    const themeToggle = document.getElementById('themeToggle');
    const themeIcon   = document.getElementById('themeIcon');

    const THEME_KEY = 'calcpro-theme';

    function applyTheme(theme) {
        html.setAttribute('data-theme', theme);
        if (themeIcon) {
            themeIcon.className = theme === 'dark'
                ? 'bi bi-moon-stars-fill'
                : 'bi bi-sun-fill';
        }
        localStorage.setItem(THEME_KEY, theme);
    }

    // Load saved theme or default to dark
    const savedTheme = localStorage.getItem(THEME_KEY) || 'dark';
    applyTheme(savedTheme);

    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            const current = html.getAttribute('data-theme');
            applyTheme(current === 'dark' ? 'light' : 'dark');

            // Ripple animation
            this.style.transform = 'rotate(360deg) scale(1.2)';
            setTimeout(() => { this.style.transform = ''; }, 350);
        });
    }

    // ──────────────────────────────────────────────
    //  NAVBAR SCROLL EFFECT
    // ──────────────────────────────────────────────
    const navbar = document.getElementById('mainNavbar');
    if (navbar) {
        window.addEventListener('scroll', function () {
            if (window.scrollY > 10) {
                navbar.style.boxShadow = '0 4px 24px rgba(0,0,0,0.3)';
            } else {
                navbar.style.boxShadow = 'none';
            }
        });
    }

    // ──────────────────────────────────────────────
    //  CLEAR HISTORY
    // ──────────────────────────────────────────────
    const clearBtn = document.getElementById('clearHistoryBtn');
    if (clearBtn) {
        clearBtn.addEventListener('click', function () {
            if (!confirm('Hapus semua riwayat perhitungan?')) return;

            fetch('/clear_history', { method: 'POST' })
                .then(res => res.json())
                .then(() => {
                    // Fade out history items
                    document.querySelectorAll('.history-item').forEach((el, i) => {
                        setTimeout(() => {
                            el.style.opacity = '0';
                            el.style.transform = 'translateY(-10px)';
                            el.style.transition = 'all 0.3s ease';
                        }, i * 50);
                    });
                    setTimeout(() => location.reload(), 400);
                })
                .catch(() => location.reload());
        });
    }

    // ──────────────────────────────────────────────
    //  ANIMATE ON SCROLL (Intersection Observer)
    // ──────────────────────────────────────────────
    const observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.feature-card, .history-item, .stat-item').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        observer.observe(el);
    });

    // ──────────────────────────────────────────────
    //  FORM SUBMIT LOADING STATE
    // ──────────────────────────────────────────────
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function () {
            const btn = this.querySelector('[type="submit"]');
            if (btn) {
                btn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Menghitung...';
                btn.disabled = true;
            }
        });
    });

    // ──────────────────────────────────────────────
    //  STEP ITEMS STAGGER ANIMATION
    // ──────────────────────────────────────────────
    document.querySelectorAll('.step-item').forEach((item, i) => {
        item.style.opacity = '0';
        item.style.transform = 'translateX(-12px)';
        setTimeout(() => {
            item.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
            item.style.opacity = '1';
            item.style.transform = 'translateX(0)';
        }, 100 + i * 60);
    });

    // ──────────────────────────────────────────────
    //  RESULT CARD POP-IN
    // ──────────────────────────────────────────────
    document.querySelectorAll('.result-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'scale(0.96) translateY(10px)';
        card.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'scale(1) translateY(0)';
        }, 50);
    });

    // ──────────────────────────────────────────────
    //  FIBONACCI NUMBER STAGGER
    // ──────────────────────────────────────────────
    document.querySelectorAll('.fib-num').forEach((num, i) => {
        num.style.opacity = '0';
        num.style.transform = 'scale(0.7)';
        num.style.transition = 'opacity 0.3s ease, transform 0.3s ease';
        setTimeout(() => {
            num.style.opacity = '1';
            num.style.transform = 'scale(1)';
        }, 30 * i);
    });

    // ──────────────────────────────────────────────
    //  NUMBER INPUT: prevent non-numeric for integer fields
    // ──────────────────────────────────────────────
    document.querySelectorAll('input[step="1"]').forEach(input => {
        input.addEventListener('input', function () {
            this.value = this.value.replace(/[^0-9-]/g, '');
        });
    });

    // ──────────────────────────────────────────────
    //  AUTO-DISMISS COPY SUCCESS
    // ──────────────────────────────────────────────
    // Handled in copyResult() global function below

});

// ──────────────────────────────────────────────────
//  COPY TO CLIPBOARD (global function)
// ──────────────────────────────────────────────────
function copyResult(value) {
    if (!navigator.clipboard) {
        // Fallback
        const ta = document.createElement('textarea');
        ta.value = value;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        showCopyToast('Hasil disalin!');
        return;
    }
    navigator.clipboard.writeText(String(value)).then(() => {
        showCopyToast('Hasil disalin! ✓');
    }).catch(() => {
        showCopyToast('Gagal menyalin.');
    });
}

function showCopyToast(msg) {
    // Remove existing toast
    const old = document.getElementById('copyToast');
    if (old) old.remove();

    const toast = document.createElement('div');
    toast.id = 'copyToast';
    toast.textContent = msg;
    toast.style.cssText = `
        position: fixed;
        bottom: 30px;
        right: 30px;
        background: linear-gradient(135deg, #d4af37, #f5e6a3, #b8962e);
        color: #0a0a0a;
        padding: 12px 24px;
        border-radius: 12px;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 0.9rem;
        box-shadow: 0 8px 32px rgba(212,175,55,0.45);
        z-index: 9999;
        animation: fadeInUp 0.3s ease;
        transition: opacity 0.3s ease;
    `;
    document.body.appendChild(toast);
    setTimeout(() => {
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 300);
    }, 2000);
}
