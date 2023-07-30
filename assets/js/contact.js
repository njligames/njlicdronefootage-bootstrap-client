$(document).ready(function () {
  (function ($) {
    "use strict";

    jQuery.validator.addMethod(
      "answercheck",
      function (value, element) {
        return this.optional(element) || /^\bcat\b$/.test(value);
      },
      "type the correct answer -_-"
    );

    // validate contactForm form
    $(function () {
      $("#contactForm").validate({
        rules: {
          name: {
            required: true,
            minlength: 2,
          },
          subject: {
            required: true,
            minlength: 4,
          },
          number: {
            required: true,
            minlength: 5,
          },
          email: {
            required: true,
            email: true,
          },
          message: {
            required: true,
            minlength: 20,
          },
        },
        messages: {
          name: {
            required: "come on, you have a name, don't you?",
            minlength: "your name must consist of at least 2 characters",
          },
          subject: {
            required: "come on, you have a subject, don't you?",
            minlength: "your subject must consist of at least 4 characters",
          },
          number: {
            required: "come on, you have a number, don't you?",
            minlength: "your Number must consist of at least 5 characters",
          },
          email: {
            required: "no email, no message",
          },
          message: {
            required:
              "um...yea, you have to write something to send this form.",
            minlength: "thats all? really?",
          },
        },
        submitHandler: function (form) {
          $(form).ajaxSubmit({
            type: "POST",
            data: $(form).serialize(),
            url: "contact_process.php",
            success: function () {
              $("#contactForm :input").attr("disabled", "disabled");
              $("#contactForm").fadeTo("slow", 1, function () {
                $(this).find(":input").attr("disabled", "disabled");
                $(this).find("label").css("cursor", "default");
                $("#success").fadeIn();
                $(".modal").modal("hide");
                $("#success").modal("show");
              });
            },
            error: function () {
              $("#contactForm").fadeTo("slow", 1, function () {
                $("#error").fadeIn();
                $(".modal").modal("hide");
                $("#error").modal("show");
              });
            },
          });
        },
      });
    });

    // Gets the video src from the data-src on each button

    var $videoSrc;
    $(".video-btn").click(function () {
      $videoSrc = $(this).data("src");
    });
    console.log($videoSrc);

    // when the modal is opened autoplay it
    $("#myModal").on("shown.bs.modal", function (e) {
      // set the video src to autoplay and not to show related video. Youtube related video is like a box of chocolates... you never know what you're gonna get
      $("#video").attr(
        "src",
        $videoSrc + "?muted=0&autoplay=1&amp;modestbranding=1&amp;showinfo=0"
      );
    });

    // stop playing the youtube video when I close the modal
    $("#myModal").on("hide.bs.modal", function (e) {
      // a poor man's stop video
      $("#video").attr("src", "#");
    });
  })(jQuery);
});
