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








// ------------secciones wizard-------------
$(document).ready(function () {
    $('.web-nav-tabs > li a[title]').tooltip();
    
    //Wizard botones next
    $('a[data-toggle="tab"]').on('shown.bs.tab', function (e) {

        var target = $(e.target);
    
        if (target.parent().hasClass('disabled')) {
            return false;
        }
    });

    $(".next-step").click(function (e) {

        var active = $('.web-wizard .web-nav-tabs li.active');
        active.next().removeClass('disabled');
        nextTab(active);

    });
    
});

function nextTab(elem) {
    $(elem).next().find('a[data-toggle="tab"]').click();
}
function prevTab(elem) {
    $(elem).prev().find('a[data-toggle="tab"]').click();
}


$('.web-nav-tabs').on('click', 'li', function() {
    $('.web-nav-tabs li.active').removeClass('active');
    $(this).addClass('active');
});




