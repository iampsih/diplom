window.onload = function () {
  //   appendData();

  var carousel = document.getElementById("myCourses");
  //   var carousel = $jq("#myCourses");
  carousel.trigger("destroy.owl.carousel");
  carousel.find(".owl-stage-outer").children().unwrap();
  carousel.removeClass("owl-center owl-loaded owl-text-select-on");

  // add the new items
  for (var i = 0; i < genres.length; i++) {
    content += '<div class="item">' + genres[i] + "</div>";
  }
  carousel.html(content);

  //reinitialize the carousel (call here your method in which you've set specific carousel properties)
  carousel.owlCarousel();
};

function appendData() {
  data = [
    {
      title: "Python course",
      image: "/assets/images/courses-01.jpg",
      mini_desc: "asdadsasdasdada",
      url: "/courses/1",
    },
    {
      title: "Java course",
      image: "/assets/images/courses-02.jpg",
      mini_desc: "asdadsasdasdada",
      url: "/courses/2",
    },
    {
      title: "Golang course",
      image: "/assets/images/courses-03.jpg",
      mini_desc: "asdadsasdasdada",
      url: "/courses/3",
    },
  ];
  var $owl = $("#owl-stage").owlCarousel({
    navigation: true, // Show next and prev buttons
    slideSpeed: 300,
    paginationSpeed: 400,
    items: 1,
    itemsDesktop: false,
    itemsDesktopSmall: false,
    itemsTablet: false,
    itemsMobile: false,
  });
  //   var mainContainer = document.getElementsByClassName("owl-stage")[0];
  for (var i = 0; i < data.length; i++) {
    var div = document.createElement("div");
    div.className = "owl-item active";
    div.style.width = "233.6px";
    div.style.marginRight = "30px";
    div.innerHTML =
      // <div class="owl-item" style="width: 233.6px; margin-right: 30px;">
      `
              <div class="item">
              <img src="assets/images/courses-05.jpg" alt="">
              <div class="down-content">
                <h4>` +
      data[i].title +
      `</h4>
                <p>
                  Quisque cursus augue ut velit dictum, quis volutpat enim
                  blandit. Maecenas a lectus ac ipsum porta.
                </p>
                <div class="author-image">
                  <img src="assets/images/author-05.png" alt="">
                </div>
                <div class="text-button-free">
                  <a href="#">Free <i class="fa fa-angle-double-right"></i></a>
                </div>
              </div>
            </div>
            `;
    // mainContainer.appendChild(div);
    $owl.append(div);
  }
  //   $owl.trigger("refresh.owl.carousel");
}
