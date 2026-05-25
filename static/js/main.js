/* ════════════════════════════════════════════════
   CalcTrick – main.js
   Calculator App Edition
   ════════════════════════════════════════════════ */

document.addEventListener('DOMContentLoaded', function () {

    // ──────────────────────────────────────────────
    //  THEME TOGGLE
    // ──────────────────────────────────────────────
    const themeToggle = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    const htmlElement = document.documentElement;

    function updateThemeIcon(theme) {
        if (!themeIcon) return;
        if (theme === 'light') {
            themeIcon.className = 'bi bi-sun-fill';
        } else {
            themeIcon.className = 'bi bi-moon-stars-fill';
        }
    }
    
    // Set initial icon state based on theme attribute
    updateThemeIcon(htmlElement.getAttribute('data-theme') || 'dark');

    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            const currentTheme = htmlElement.getAttribute('data-theme') || 'dark';
            const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
            
            htmlElement.setAttribute('data-theme', newTheme);
            localStorage.setItem('theme', newTheme);
            updateThemeIcon(newTheme);
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
                    document.querySelectorAll('.history-global-item, .history-row').forEach((el, i) => {
                        setTimeout(() => {
                            el.style.opacity = '0';
                            el.style.transform = 'translateY(-8px)';
                            el.style.transition = 'all 0.25s ease';
                        }, i * 40);
                    });
                    setTimeout(() => location.reload(), 400);
                })
                .catch(() => location.reload());
        });
    }

    // ──────────────────────────────────────────────
    //  FORM SUBMIT LOADING STATE
    // ──────────────────────────────────────────────
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function () {
            const btn = this.querySelector('[type="submit"]:not([style*="display:none"])');
            if (btn) {
                btn.innerHTML = '<span style="display:inline-block;width:12px;height:12px;border:2px solid rgba(255,255,255,0.3);border-top-color:#fff;border-radius:50%;animation:spin 0.6s linear infinite;margin-right:8px;"></span>Menghitung...';
                btn.disabled = true;
            }
        });
    });

    // ──────────────────────────────────────────────
    //  RESULT POP-IN ANIMATION
    // ──────────────────────────────────────────────
    document.querySelectorAll('.result-display').forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'scale(0.95) translateY(8px)';
        el.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
        setTimeout(() => {
            el.style.opacity = '1';
            el.style.transform = 'scale(1) translateY(0)';
        }, 60);
    });

    // ──────────────────────────────────────────────
    //  STEPS STAGGER ANIMATION
    // ──────────────────────────────────────────────
    document.querySelectorAll('.step-row').forEach((item, i) => {
        item.style.opacity = '0';
        item.style.transform = 'translateX(-10px)';
        setTimeout(() => {
            item.style.transition = 'opacity 0.35s ease, transform 0.35s ease';
            item.style.opacity = '1';
            item.style.transform = 'translateX(0)';
        }, 80 + i * 50);
    });

    // ──────────────────────────────────────────────
    //  FIB NUMBERS STAGGER
    // ──────────────────────────────────────────────
    document.querySelectorAll('.fib-num').forEach((num, i) => {
        num.style.opacity = '0';
        num.style.transform = 'scale(0.6)';
        num.style.transition = 'opacity 0.25s ease, transform 0.25s ease';
        setTimeout(() => {
            num.style.opacity = '1';
            num.style.transform = 'scale(1)';
        }, 20 * i);
    });

    // ──────────────────────────────────────────────
    //  BUTTON PRESS RIPPLE
    // ──────────────────────────────────────────────
    document.querySelectorAll('.calc-btn').forEach(btn => {
        btn.addEventListener('mousedown', function (e) {
            const ripple = document.createElement('span');
            const rect = this.getBoundingClientRect();
            const size = Math.max(rect.width, rect.height);
            ripple.style.cssText = `
                position:absolute;
                width:${size}px; height:${size}px;
                left:${e.clientX - rect.left - size/2}px;
                top:${e.clientY - rect.top - size/2}px;
                background:rgba(255,255,255,0.1);
                border-radius:50%;
                transform:scale(0);
                animation:rippleAnim 0.4s ease-out forwards;
                pointer-events:none;
            `;
            this.style.position = 'relative';
            this.style.overflow = 'hidden';
            this.appendChild(ripple);
            setTimeout(() => ripple.remove(), 400);
        });
    });

    // ──────────────────────────────────────────────
    //  DISPLAY COUNTER ANIMATION (home page)
    // ──────────────────────────────────────────────
    const homeDisplay = document.querySelector('.home-display-main');
    if (homeDisplay) {
        const digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '∞', '?'];
        let idx = 0;
        setInterval(() => {
            homeDisplay.textContent = digits[idx % digits.length];
            idx++;
        }, 800);
    }

    // Inject spin keyframe if not present
    if (!document.getElementById('calcKeyframes')) {
        const style = document.createElement('style');
        style.id = 'calcKeyframes';
        style.textContent = `
            @keyframes spin { to { transform: rotate(360deg); } }
            @keyframes rippleAnim { to { transform: scale(2.5); opacity: 0; } }
        `;
        document.head.appendChild(style);
    }

});

// ──────────────────────────────────────────────
//  COPY TO CLIPBOARD
// ──────────────────────────────────────────────
function copyResult(value) {
    const text = String(value);
    if (navigator.clipboard) {
        navigator.clipboard.writeText(text)
            .then(() => showCopyToast('✓ Hasil disalin!'))
            .catch(() => showCopyToast('Gagal menyalin.'));
    } else {
        const ta = document.createElement('textarea');
        ta.value = text;
        document.body.appendChild(ta);
        ta.select();
        document.execCommand('copy');
        document.body.removeChild(ta);
        showCopyToast('✓ Hasil disalin!');
    }
}

function showCopyToast(msg) {
    const old = document.getElementById('copyToast');
    if (old) old.remove();

    const toast = document.createElement('div');
    toast.id = 'copyToast';
    toast.textContent = msg;
    document.body.appendChild(toast);

    setTimeout(() => {
        toast.style.opacity = '0';
        setTimeout(() => toast.remove(), 300);
    }, 2000);
}
