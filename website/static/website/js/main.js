document.addEventListener('DOMContentLoaded', () => {

// Image Swiper
// JS
    new Swiper(".beforeAfterSwiper", {
      loop: true,
      slidesPerView: 1,
      spaceBetween: 16,
      navigation: {
        nextEl: ".swiper-button-next",
        prevEl: ".swiper-button-prev",
      },
      breakpoints: {
        992: {
          slidesPerView: 3,
        },
      },
      autoplay: {
    delay: 2000, 
    disableOnInteraction: true
  },
    });
// Navbar
  handleNavbarCollapse()
  handleDropdowns()

// Travel page
 const tabButtons = document.querySelectorAll('[data-toggle="pill"]')

  tabButtons.forEach(button => {
    button.addEventListener('click', () => {
      const targetSelector = button.getAttribute('data-target')
      const targetPane = document.querySelector(targetSelector)

      if (!targetPane) return

      // Deactivate all buttons
      tabButtons.forEach(btn => {
        btn.classList.remove('active')
        btn.setAttribute('aria-selected', 'false')
      })

      // Hide all panes
      document.querySelectorAll('.tab-pane').forEach(pane => {
        pane.classList.remove('show', 'active')
      })

      // Activate clicked button
      button.classList.add('active')
      button.setAttribute('aria-selected', 'true')

      // Show target pane
      targetPane.classList.add('active', 'show')
    })
  })

  // Treatment pages
   const cards = document.querySelectorAll('.animate-on-scroll')

  const observer = new IntersectionObserver(
    entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible')
        }
      })
    },
    { threshold: 0.15 }
  )

  cards.forEach(card => observer.observe(card))

  // Image Carousel 
    let items = document.querySelectorAll("#smartCarousel .carousel-item");
        items.forEach((el) => {
          const minPerSlide = 3;
          let next = el.nextElementSibling;
          for (let i = 1; i < minPerSlide; i++) {
            if (!next) {
              next = items[0];
            }
            let cloneChild = next.firstElementChild.cloneNode(true);
            el.appendChild(cloneChild);
            next = next.nextElementSibling;
          }
        });
})

function handleNavbarCollapse() {
  const toggler = document.querySelector('.navbar-toggler')
  if (!toggler) return

  const targetSelector = toggler.getAttribute('data-target')
  const target = document.querySelector(targetSelector)

  toggler.addEventListener('click', () => {
    const isOpen = target.classList.toggle('show')
    toggler.setAttribute('aria-expanded', isOpen)
  })
}

function handleDropdowns() {
  const toggles = document.querySelectorAll('.dropdown-toggle')

  toggles.forEach(toggle => {
    const menu = toggle.nextElementSibling

    toggle.addEventListener('click', e => {
      e.preventDefault()
      e.stopPropagation()

      closeAllDropdowns(menu)
      menu.classList.toggle('show')
    })
  })

  // Close on outside click
  document.addEventListener('click', () => {
    closeAllDropdowns()
  })

  // Close on ESC
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeAllDropdowns()
  })
}

function closeAllDropdowns(except = null) {
  document.querySelectorAll('.dropdown-menu.show').forEach(menu => {
    if (menu !== except) {
      menu.classList.remove('show')
    }
  })
}

// Enable tooltips
  document.addEventListener('DOMContentLoaded', function () {
    var tooltipTriggerList = [].slice.call(
      document.querySelectorAll('[data-bs-toggle="tooltip"]'),
    );

    tooltipTriggerList.map(function (tooltipTriggerEl) {
      return new bootstrap.Tooltip(tooltipTriggerEl);
    });
  });

