!(function (e) {
    "use strict";
    jQuery(document).on("ready", function () {
        e.fn.classyNav && e("#EduStudyNav").classyNav({ theme: "light" }),
            e(function () {
                e('a[href="#search"]').on("click", function (o) {
                    o.preventDefault(), e("#search-area").addClass("open"), e('#search-area > form > input[type="search"]').focus();
                }),
                    e("#search-area, #search-area button.close").on("click keyup", function (o) {
                        (o.target != this && "close" != o.target.className && 27 != o.keyCode) || e(this).removeClass("open");
                    })
            }),
            e(".home-slides").owlCarousel({
                items: 1,
                loop: !0,
                autoplay: !0,
                nav: !0,
                animateOut: "fadeOut",
                animateIn: "fadeInUp",
                responsiveClass: !0,
                dots: !1,
                autoplayHoverPause: !0,
                mouseDrag: !0,
                navText: ["<i class='icofont-rounded-left'></i>", "<i class='icofont-rounded-right'></i>"],
            }),
            e(".home-slides-two").owlCarousel({
                items: 1,
                loop: !0,
                autoplay: !0,
                nav: !0,
                animateOut: "fadeOut",
                responsiveClass: !0,
                dots: !1,
                autoplayHoverPause: !0,
                mouseDrag: !0,
                navText: ["<i class='icofont-rounded-left'></i>", "<i class='icofont-rounded-right'></i>"],
            }),
            e(".popup-video").magnificPopup({ disableOn: 320, type: "iframe", mainClass: "mfp-fade", removalDelay: 160, preloader: !1, fixedContentPos: !1 }),
            e(".count").counterUp({ delay: 20, time: 1500 }),
            e(".news-slider").owlCarousel({
                nav: !0,
                dots: !1,
                center: !1,
                touchDrag: !1,
                mouseDrag: !0,
                autoplay: !0,
                smartSpeed: 750,
                autoplayHoverPause: !0,
                loop: !0,
                navText: ["<i class='icofont-thin-left'></i>", "<i class='icofont-thin-right'></i>"],
                responsive: { 0: { items: 1 }, 768: { items: 2 }, 1200: { items: 3 } },
            }),
            e(".partner-slider").owlCarousel({ nav: !1, dots: !1, mouseDrag: !0, autoplay: !0, smartSpeed: 750, autoplayHoverPause: !0, loop: !0, responsive: { 0: { items: 1 }, 768: { items: 3 }, 1200: { items: 6 } } }),
            e(".testimonials-slider").owlCarousel({
                nav: !0,
                dots: !1,
                center: !0,
                touchDrag: !1,
                items: 4,
                mouseDrag: !0,
                autoplay: !0,
                smartSpeed: 750,
                autoplayHoverPause: !0,
                loop: !0,
                navText: ["<i class='icofont-rounded-left'></i>", "<i class='icofont-rounded-right'></i>"],
                responsive: { 0: { items: 1 }, 768: { items: 2 } },
            }),
            e(".about-slider").owlCarousel({
                items: 1,
                loop: !0,
                autoplay: !0,
                nav: !0,
                responsiveClass: !0,
                dots: !1,
                autoplayHoverPause: !0,
                mouseDrag: !0,
                navText: ["<i class='icofont-rounded-left'></i>", "<i class='icofont-rounded-right'></i>"],
            }),
            e(function () {
                e('[data-toggle="tooltip"]').tooltip();
            }),
            e("#tabs li").on("click", function () {
                var o = e(this).attr("id");
                e(this).hasClass("inactive") &&
                    (e(this).removeClass("inactive"),
                    e(this).addClass("active"),
                    e(this).siblings().removeClass("active").addClass("inactive"),
                    e("#" + o + "_content").addClass("show"),
                    e("#" + o + "_content")
                        .siblings("div")
                        .removeClass("show"));
            }),
            e(window).on("scroll", function () {
                e(this).scrollTop() > 300 ? e(".scrolltop").fadeIn() : e(".scrolltop").fadeOut();
            }),
            e(".scrolltop").on("click", function () {
                return e("html, body").animate({ scrollTop: 0 }, 1e3), !1;
            }),
            e(".scroll-down a, .slide-inner-content a, .cta-area a").on("click", function (o) {
                var a = e(this);
                e("html, body")
                    .stop()
                    .animate({ scrollTop: e(a.attr("href")).offset().top - 70 }, 1500),
                    o.preventDefault();
            });
    }),
        jQuery(window).on("load", function () {
            e(".preloader-area").fadeOut();
        });

        // jQuery(document).on('click', '.alert', function (e) {
        
        //     console.log('heyhey')
        // });

        
        jQuery(document).ready(function() {
            setTimeout(function() {
                
                
                $(".alert").removeClass('lightSpeedIn').addClass('lightSpeedOut ');


              }, 2000);
            });





})(jQuery);



jQuery(document).ready(function() {


    $('.myButtons').on('click', function () {
        $('#loader1').show();
        console.log("ok");
    });

    // $('#ch').on('click', function () { 
    //     // $('#video-content').toggle(); //hide the button
    //     $('#video-content').hide();
    //     $('#text-content').show() //hide the button
    //     var val = $('input[id^="myText"]', this).val();
    //     $('#text-content').html(val);
      
    //     });
    $('.myButtons').on('click', function () { 
        // $('#video-content').toggle(); //hide the button
        $('#text-content').hide(1000)
        $('#iframe1').on('load', function () {
            $('#loader1').hide();
            
        });

        $('#video-content').show(); //hide the button
        });


});


jQuery(document).ready(function(){
    var productForm = $(".course-ajax") // #form-product-ajax
    
    function toster_option(msg){
        toastr.options = {
            "closeButton": true,
            "debug": false,
            "newestOnTop": true,
            "progressBar": true,
            // "positionClass": "toast-bottom-center",
            "preventDuplicates": false,
            "onclick": null,
            "showDuration": "300",
            "hideDuration": "1000",
            "timeOut": "5000",
            "extendedTimeOut": "1000",
            "showEasing": "swing",
            "hideEasing": "linear",
            "showMethod": "fadeIn",
            "hideMethod": "fadeOut",
            "hideMethod": "fadeOut"

          }

          toastr.success(msg);
    }

productForm.submit(function(event){
        event.preventDefault();
        var thisForm = $(this)
        var actionEndpoint = thisForm.attr("action");
        var httpMethod = thisForm.attr("method");
        var formData = thisForm.serialize();

        $.ajax({
          url: actionEndpoint,
          method: httpMethod,
          data: formData,
          success: function(data){
            var submitSpan = thisForm.find(".button-ajax")
            if (data.added){
              submitSpan.html('<a href="" class=""><button class="btn btn-danger">Remove From cart</button></a>')
            //   toastr.success('Item Was Added On Cart');
                toster_option('Item Was Added On Cart.');
            } else {
              submitSpan.html('<a href="" class=""><button class="btn btn-danger">Add to cart</button></a>')
                toster_option('Item Was Removed From Cart.');


                
            }
            var cartCount = $(".count-ajax")
            cartCount.text(data.CartItemCount)
          },
          error: function(errorData){
            toster_option('Somthing Went wrong !!');
          }
        })

    })



function refreshCart(){
    console.log("in current cart")
    var cartTable = $(".cart-table")
    var cartBody = cartTable.find(".cart-body")
    //cartBody.html("<h1>Changed</h1>")
    var productRows = cartBody.find(".cart-product")
    var currentUrl = window.location.href

    var refreshCartUrl = '/api/cart/'
    var refreshCartMethod = "GET";
    var data = {};
    $.ajax({
      url: refreshCartUrl,
      method: refreshCartMethod,
      data: data,
      success: function(data){
        
        var hiddenCartItemRemoveForm = $(".cart-item-remove-form")
        if (data.products.length > 0){
            productRows.html(" ")
            i = data.products.length
            $.each(data.products, function(index, value){
              console.log(value)
              var newCartItemRemove = hiddenCartItemRemoveForm.clone()
              newCartItemRemove.css("display", "block")
              // newCartItemRemove.removeClass("hidden-class")
              newCartItemRemove.find(".cart-item-product-id").val(value.id)
                cartBody.prepend("<tr><th scope=\"row\">" + i + "</th><td><a href='" + value.url + "'>" + value.name + "</a>" + newCartItemRemove.html() + "</td><td>" + value.price + "</td></tr>")
                i --
            })
            
            cartBody.find(".cart-subtotal").text(data.subtotal)
            cartBody.find(".cart-total").text(data.total)
        } else {
          window.location.href = currentUrl
        }
        
      },
      error: function(errorData){
        $.alert({
            title: "Oops!",
            content: "An error occurred",
            theme: "modern",
          })
      }
    })


  }


})



