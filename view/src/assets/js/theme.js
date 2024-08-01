(function ($) {
    'use strict';

     //Header Search
    if($('.search-box-outer').length) {
        $('.search-box-outer').on('click', function() {
            $('body').addClass('search-active');
        });
        $('.close-search').on('click', function() {
            $('body').removeClass('search-active');
        });
    }

    // Mobile Menu
    $('.mobile-menu nav').meanmenu({
        meanScreenWidth: "991",
        meanMenuContainer: ".mobile-menu",
        meanMenuOpen: "<span></span> <span></span> <span></span>",
        onePage: false,
    });

        // =======< accordion js >========
        $(".accordion > li:eq(0) a").addClass("active").next().slideDown();
        $('.accordion a').on('click', function (j) {
            var dropDown = $(this).closest("li").find("p");
    
            $(this).closest(".accordion").find("p").not(dropDown).slideUp();
    
            if ($(this).hasClass("active")) {
                $(this).removeClass("active");
            } else {
                $(this).closest(".accordion").find("a.active").removeClass("active");
                $(this).addClass("active");
            }
    
            dropDown.stop(false, true).slideToggle();
    
            j.preventDefault();
        });

           
    // sticky
    var wind = $(window);
    var sticky = $('#sticky-header');
    wind.on('scroll', function () {
        var scroll = wind.scrollTop();
        if (scroll < 100) {
            sticky.removeClass('sticky');
        } else {
            sticky.addClass('sticky');
        }
    });

    // Loder  //
    $(function () {
        $('body').addClass('loaded');
    });

    
    // counterUp
    $('.counter').counterUp({
        delay: 5,
        time: 3000
    });

   

    // Case Study Active
    $('.service-slider').owlCarousel({
        loop: true,
        autoplay: true,
        smartSpeed: 1500,
        autoplayTimeout: 1500,
        dots: true,
        nav: false,
        margin: 30,
        navText: ["<i class='bi bi-arrow-left''></i>", "<i class='bi bi-arrow-right''></i>"],
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 3
            },
            1200: {
                items: 3
            },
            1920: {
                items: 3
            }
        }
    })


    // testimonial Active
    $('.testimonial-list').owlCarousel({
        loop: true,
        autoplay: true,
        autoplayTimeout: 10000,
        dots: true,
        nav: false,
        margin:20,
        navText: ["<i class='bi bi-arrow-left''></i>", "<i class='bi bi-arrow-right''></i>"],
        responsive: {
            0: {
                items: 1
            },
            768: {
                items: 2
            },
            992: {
                items: 1
            },
            1200: {
                items: 1
            },
            1920: {
                items: 1
            }
        }
    })

    
        // brand Active
        $('.brand-list').owlCarousel({
            loop: true,
            autoplay: true,
            autoplayTimeout: 10000,
            dots: false,
            nav: false,
            margin:20,
            navText: ["<i class='bi bi-arrow-left''></i>", "<i class='bi bi-arrow-right''></i>"],
            responsive: {
                0: {
                    items: 0
                },
                320: {
                    items: 1
                },
                480: {
                    items: 1
                }
                ,600: {
                    items: 2
                },
                768: {
                    items: 3
                },
                992: {
                    items: 4
                },
                1200: {
                    items: 4
                },
                1920: {
                    items: 5
                }
            }
        })

        

        // scroll up

        if($('.prgoress_indicator path').length){
            var progressPath = document.querySelector('.prgoress_indicator path');
            var pathLength = progressPath.getTotalLength();
            progressPath.style.transition = progressPath.style.WebkitTransition = 'none';
            progressPath.style.strokeDasharray = pathLength + ' ' + pathLength;
            progressPath.style.strokeDashoffset = pathLength;
            progressPath.getBoundingClientRect();
            progressPath.style.transition = progressPath.style.WebkitTransition = 'stroke-dashoffset 10ms linear';
            var updateProgress = function () {
              var scroll = $(window).scrollTop();
              var height = $(document).height() - $(window).height();
              var progress = pathLength - (scroll * pathLength / height);
              progressPath.style.strokeDashoffset = progress;
            }
            updateProgress();
            $(window).on('scroll', updateProgress);
            var offset = 250;
            var duration = 550;
            jQuery(window).on('scroll', function () {
              if (jQuery(this).scrollTop() > offset) {
                jQuery('.prgoress_indicator').addClass('active-progress');
              } else {
                jQuery('.prgoress_indicator').removeClass('active-progress');
              }
            });
            jQuery('.prgoress_indicator').on('click', function (event) {
              event.preventDefault();
              jQuery('html, body').animate({ scrollTop: 0 }, duration);
              return false;
            });
        }

        
     //======< scrollcue js >======
    //  $(function(){
    //     scrollCue.init({
    //     duration : 2500,
    //     interval : -0.7,
    //     percentage : 0.90,
    //     smartSpeed: 5000 
        
    //     })
    // });


    /*---------------------
    WOW active js 
    --------------------- */

    // new WOW().init();


    // Venubox

    $('.venobox').venobox({

        numeratio: true,

        infinigall: true

    });
    /*--------------------------
     scrollUp
    ---------------------------- */
    $.scrollUp({
        scrollText: '<i class="fa fa-angle-up"></i>',
        easingType: 'linear',
        scrollSpeed: 900,
        animation: 'fade'
    })

    jQuery(document).ready(function ($) {
        "use strict";

    //=====< barfiller script >====
    $('#bar1').barfiller({
        duration: 7000
    });
    $('#bar2').barfiller({
        duration: 7000
    });
    $('#bar3').barfiller({
        duration: 7000
    });


        
    //======< Custom Tab >======
    $('.tab ul.tabs').addClass('active').find('> li:eq(0)').addClass('current');

    $(".tab ul.tabs li a").on("click", function (g) {
        var tab = $(this).closest('.tab'),
            index = $(this).closest('li').index();

        tab.find('ul.tabs > li').removeClass('current');
        $(this).closest('li').addClass('current');

        tab.find('.tab_content').find('div.tabs_item').not('div.tabs_item:eq(' + index + ')').slideUp();
        tab.find('.tab_content').find('div.tabs_item:eq(' + index + ')').slideDown();

        g.preventDefault();
    });

});


    // // Sidebar
    
    // "use strict";
    //     jQuery(document).ready(function (o) {
    //         0 < o(".offset-side-bar").length &&
    //             o(".offset-side-bar").on("click", function (e) {
    //                 e.preventDefault(), e.stopPropagation(), o(".cart-group").addClass("isActive");
    //             }),
    //             0 < o(".close-side-widget").length &&
    //                 o(".close-side-widget").on("click", function (e) {
    //                     e.preventDefault(), o(".cart-group").removeClass("isActive");
    //                 }),
    //             0 < o(".navSidebar-button").length &&
    //                 o(".navSidebar-button").on("click", function (e) {
    //                     e.preventDefault(), e.stopPropagation(), o(".info-group").addClass("isActive");
    //                 }),
    //             0 < o(".close-side-widget").length &&
    //                 o(".close-side-widget").on("click", function (e) {
    //                     e.preventDefault(), o(".info-group").removeClass("isActive");
    //                 }),
    //             o("body").on("click", function (e) {
    //                 o(".info-group").removeClass("isActive"), o(".cart-group").removeClass("isActive");
    //             }),
    //             o(".xs-sidebar-widget").on("click", function (e) {
    //                 e.stopPropagation();
    //             }),
    //             0 < o(".xs-modal-popup").length &&
    //                 o(".xs-modal-popup").magnificPopup({
    //                     type: "inline",
    //                     fixedContentPos: !2,
    //                     fixedBgPos: !0,
    //                     overflowY: "auto",
    //                     closeBtnInside: !2,
    //                     callbacks: {
    //                         beforeOpen: function () {
    //                             this.st.mainClass = "my-mfp-slide-bottom xs-promo-popup";
    //                         },
    //                     },
    //                 });
    //         });

    // Pricing Tab
         $(document).ready(function() {
            const tabs= document.querySelectorAll('.pricing-tab-button button');
            const all_content= document.querySelectorAll('.tab-content')
    
            tabs.forEach((tab, index)=>{
                tab.addEventListener('click', ()=>{
                    tabs.forEach(tab=>{tab.classList.remove('active')});
                    tab.classList.add('active');
    
                    all_content.forEach(content=>{content.classList.remove('active')});
                    all_content[index].classList.add('active');
                });
            });
        });


    // Pricing Tab
        $(document).ready(function() {
            const tabs= document.querySelectorAll('.Price-tab-btn');
            const all_content= document.querySelectorAll('.tab-contents')
    
            tabs.forEach((tab, index)=>{
                tab.addEventListener('click', ()=>{
                    tabs.forEach(tab=>{tab.classList.remove('active')});
                    tab.classList.add('active');
    
                    all_content.forEach(content=>{content.classList.remove('active')});
                    all_content[index].classList.add('active');
                });
            });
        });



        
})(jQuery);